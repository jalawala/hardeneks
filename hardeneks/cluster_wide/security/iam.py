import boto3
from kubernetes import client
import kubernetes
from hardeneks.rules import Rule, Result
from ...resources import Resources
import pprint
import requests

class disable_anonymous_access_for_cluster_roles(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Review and revoke unnecessary anonymous access"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#review-and-revoke-unnecessary-anonymous-access"

    def check(self, resources: Resources):
        offenders = []

        ignored = ["system:public-info-viewer"]

        for cluster_role_binding in resources.cluster_role_bindings:
            if (
                cluster_role_binding.subjects
                and cluster_role_binding.metadata.name not in ignored
            ):
                for subject in cluster_role_binding.subjects:
                    if (
                        subject.name == "system:unauthenticated"
                        or subject.name == "system:anonymous"
                    ):
                        offenders.append(cluster_role_binding)

        if offenders:
            self.result = Result(
                status=False,
                resource_type="ClusterRoleBinding",
                resources=[i.metadata.name for i in offenders],
            )
        else:
            self.result = Result(status=True, resource_type="ClusterRoleBinding")
            

class cluster_endpoint_public_and_private_mode(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Make the EKS Cluster Endpoint private"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#make-the-eks-cluster-endpoint-private"

    def check(self, resources: Resources):
        Status = True
        
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        cluster_endpoint = cluster_metadata["cluster"]["endpoint"]
        endpoint_public_access  = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
        endpoint_private_access = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"]
        Info = "public: " + str(endpoint_public_access) + ", " + "private: " + str(endpoint_private_access)
        
        if endpoint_public_access == True and endpoint_private_access == True:
            public_access_cidr_list  = cluster_metadata["cluster"]["resourcesVpcConfig"]["publicAccessCidrs"]
            if '0.0.0.0/0' in public_access_cidr_list :
                Info = "EKS Cluster Endpoint is Public and Open to Internet Access ['0.0.0.0/0']"
                Status = False
        else:
            Status = False
        
        self.result = Result(status=Status, resource_type="EKS Cluster Endpoint Mode",info=Info)    

class restrict_wildcard_for_cluster_roles(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Employ least privileged access when creating RoleBindings and ClusterRoleBindings"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#employ-least-privileged-access-when-creating-rolebindings-and-clusterrolebindings"

    def check(self, resources: Resources):

        offenders = []
        allow_list = [
            "aws-node",
            "cluster-admin",
            "eks:addon-manager",
            "eks:cloud-controller-manager",
        ]

        #print("cluster_roles={}".format(resources.cluster_roles))
        for role in resources.cluster_roles:
            role_name = role.metadata.name
            if not (role_name.startswith("system") or role_name in allow_list):
                for rule in role.rules:
                    if "*" in rule.verbs:
                        offenders.append(role_name)
                    if rule.resources and "*" in rule.resources:
                        offenders.append(role_name)

        if offenders:
            self.result = Result(
                status=False,
                resources=offenders,
                resource_type="Cluster Role",
            )
        else:
            self.result = Result(status=True, resource_type="Cluster Role")


class check_aws_node_daemonset_service_account(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Update the aws-node daemonset to use IRSA."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#update-the-aws-node-daemonset-to-use-irsa"


    def check(self, resources: Resources):

        daemonset = kubernetes.client.AppsV1Api().read_namespaced_daemon_set(name="aws-node", namespace="kube-system")
        sa = daemonset.spec.template.spec.service_account_name
        sa_data = kubernetes.client.CoreV1Api().read_namespaced_service_account(sa, 'kube-system', pretty="true")
        #print(sa_data.metadata.annotations.keys())
        
        if 'eks.amazonaws.com/role-arn' in sa_data.metadata.annotations.keys():
            Status = True
            Info = "VPC CNI uses separate IAM Role (IRSA)"
        else:
            Status = False
            Info = "VPC CNI doesn't use separate IAM Role (IRSA)"            
        
        self.result = Result(status=Status, resource_type="IRSA for VPC CNI",info=Info)    
    

class use_imds_v2(Rule):
    
    
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "When your application needs access to IMDS, use IMDSv2 and increase the hop limit on EC2 instances to 2"
    url = "\https://aws.github.io/aws-eks-best-practices/security/docs/iam/#when-your-application-needs-access-to-imds-use-imdsv2-and-increase-the-hop-limit-on-ec2-instances-to-2"

    def check(self, resources: Resources):
        client = boto3.client("ec2", region_name=resources.region)
        offenders = []
        Status = False

        instance_metadata = client.describe_instances(
            Filters=[
                {
                    "Name": "tag:aws:eks:cluster-name",
                    "Values": [
                        resources.cluster,
                    ],
                },
            ]
        )

        for instance in instance_metadata["Reservations"]:
            
            #print("MetadataOptions={}".format(instance["Instances"][0]["MetadataOptions"]))
            HttpPutResponseHopLimit =  instance["Instances"][0]["MetadataOptions"]["HttpPutResponseHopLimit"]
            HttpEndpoint = instance["Instances"][0]["MetadataOptions"]["HttpEndpoint"]
            HttpTokens = instance["Instances"][0]["MetadataOptions"]["HttpTokens"]
            Info = "HttpPutResponseHopLimit : {} HttpEndpoint : {} HttpTokens : {}".format(HttpPutResponseHopLimit, HttpEndpoint, HttpTokens)
            
            if HttpPutResponseHopLimit != 2 or HttpEndpoint != 'enabled' or HttpTokens != 'required':
                offenders.append(instance["Instances"][0]["InstanceId"])
                

        if offenders:
            self.result = Result(
                status=False,
                resource_type="Node",
                resources=offenders,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="Node",info=Info)
            
class use_iam_role_for_multiple_iam_users(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Use IAM Roles when multiple users need identical access to the cluster¶"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#use-iam-roles-when-multiple-users-need-identical-access-to-the-cluster"


    def check(self, resources: Resources):

        Status = True
        Info = "mapUsers does not exist in aws-auth config map"
        
        cm = kubernetes.client.CoreV1Api().read_namespaced_config_map(name="aws-auth", namespace="kube-system")
        #print(pprint.pformat(cm, indent=4))

        if 'mapUsers' in cm.data.keys():
            Status = False
            Info = "mapUsers exist in aws-auth config map"
        
        self.result = Result(status=Status, resource_type="iam users",info=Info)    
    


class use_imds_v2(Rule):
    
    
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "When your application needs access to IMDS, use IMDSv2 and increase the hop limit on EC2 instances to 2"
    url = "\https://aws.github.io/aws-eks-best-practices/security/docs/iam/#when-your-application-needs-access-to-imds-use-imdsv2-and-increase-the-hop-limit-on-ec2-instances-to-2"

    def check(self, resources: Resources):
        client = boto3.client("ec2", region_name=resources.region)
        offenders = []
        Status = False

        instance_metadata = client.describe_instances(
            Filters=[
                {
                    "Name": "tag:aws:eks:cluster-name",
                    "Values": [
                        resources.cluster,
                    ],
                },
           ]
        )

        for instance in instance_metadata["Reservations"]:
            
            #print("MetadataOptions={}".format(instance["Instances"][0]["MetadataOptions"]))
            HttpPutResponseHopLimit =  instance["Instances"][0]["MetadataOptions"]["HttpPutResponseHopLimit"]
            HttpEndpoint = instance["Instances"][0]["MetadataOptions"]["HttpEndpoint"]
            HttpTokens = instance["Instances"][0]["MetadataOptions"]["HttpTokens"]
            Info = "HttpPutResponseHopLimit : {} HttpEndpoint : {} HttpTokens : {}".format(HttpPutResponseHopLimit, HttpEndpoint, HttpTokens)
            
            if HttpPutResponseHopLimit != 2 or HttpEndpoint != 'enabled' or HttpTokens != 'required':
                offenders.append(instance["Instances"][0]["InstanceId"])
                

        if offenders:
            self.result = Result(
                status=False,
                resource_type="Node",
                resources=offenders,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="Node",info=Info)
    
    
    
class restrict_access_to_instance_profile(Rule):


    
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Restrict access to the instance profile assigned to the worker node"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#restrict-access-to-the-instance-profile-assigned-to-the-worker-node"

    def check(self, resources: Resources):
        client = boto3.client("ec2", region_name=resources.region)
        offenders = []
        Status = False

        instance_metadata = client.describe_instances(
            Filters=[
                {
                    "Name": "tag:aws:eks:cluster-name",
                    "Values": [
                        resources.cluster,
                    ],
                },
          ]
        )

        for instance in instance_metadata["Reservations"]:
            
            #print("MetadataOptions={}".format(instance["Instances"][0]["MetadataOptions"]))
            HttpPutResponseHopLimit =  instance["Instances"][0]["MetadataOptions"]["HttpPutResponseHopLimit"]
            HttpEndpoint = instance["Instances"][0]["MetadataOptions"]["HttpEndpoint"]
            HttpTokens = instance["Instances"][0]["MetadataOptions"]["HttpTokens"]
            Info = "HttpPutResponseHopLimit : {} HttpEndpoint : {} HttpTokens : {}".format(HttpPutResponseHopLimit, HttpEndpoint, HttpTokens)
            
            if HttpPutResponseHopLimit != 1 and HttpTokens != 'required':
                offenders.append(instance["Instances"][0]["InstanceId"])
                

        if offenders:
            self.result = Result(
                status=False,
                resource_type="Node",
                resources=offenders,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="Node",info=Info)
    
    
    
    
class do_not_assign_system_masters_for_normal_users(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Do not assign system:masters group to normal users"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#employ-least-privileged-access-when-creating-rolebindings-and-clusterrolebindings"


    def check(self, resources: Resources):

        Status = True
        Info = "system:masters does not exist in aws-auth config map"
        
        cm = kubernetes.client.CoreV1Api().read_namespaced_config_map(name="aws-auth", namespace="kube-system")
        #print(pprint.pformat(cm, indent=4))
        #map_roles = cm['data']['mapRoles']
        map_roles = cm.data['mapRoles']
        map_users = cm.data['mapUsers']
        if "system:masters" in map_roles or "system:masters" in map_users:
            Status = False
            Info = "system:masters exist in aws-auth config map"
        #print(type(map_roles))
        #print(pprint.pformat(map_roles, indent=4))
        
        
        self.result = Result(status=Status, resource_type="least privileged rbac role",info=Info)    
    
    
    
    
    
class create_cluster_with_dedicated_iam_role(Rule):
    
    _type = "cluster_wide"
    pillar = "security"
    section = "iam"
    message = "Create the cluster with a dedicated IAM role"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#create-the-cluster-with-a-dedicated-iam-role"


    def check(self, resources: Resources):

        Status = True
        
        
        
        url = "http://169.254.169.254/latest/meta-data/instance-id"
        response = requests.get(url)
        instance_id = response.text
        #print(pprint.pformat(response.text, indent=4))

        ec2client = boto3.client("ec2", region_name=resources.region)                
        response = ec2client.describe_instances(InstanceIds=[instance_id,])
        instance = response["Reservations"][0]["Instances"][0]
        instance_profile_arn = instance["IamInstanceProfile"]["Arn"]
        
        iamclient = boto3.client("iam")
        
        
        
        response = iamclient.get_instance_profile(InstanceProfileName='eksworkshop-admin')
        #response = iamclient.get_instance_profile(InstanceProfileName=instance_profile_arn)
    
        role_name = response["InstanceProfile"]["Roles"][0]["RoleName"]
        role_arn = response["InstanceProfile"]["Roles"][0]["Arn"]
        #print(role_arn)
        
        Info = "IAM Role {} does not have AdministratorAccess policy".format(role_arn)
        
        attached_policies = iamclient.list_attached_role_policies(
            RoleName=role_name)["AttachedPolicies"]
            
        inline_policies = iamclient.list_role_policies(RoleName=role_name)["PolicyNames" ]
        
        #print(pprint.pformat(attached_policies, indent=4))
        #print(pprint.pformat(inline_policies, indent=4))
        
        for policy in attached_policies:
            if policy['PolicyName'] == 'AdministratorAccess':
                Status = False
                Info = "IAM Role {} has AdministratorAccess policy".format(role_arn)
        
        
        #print("attached_policies={} inline_policies={}".format(attached_policies, inline_policies))
        

        #print(pprint.pformat(instance_profile_arn, indent=4))
        
        self.result = Result(status=Status, resource_type="dedicated cluster role",info=Info)    
    
    
    
        