import boto3
import kubernetes

from hardeneks.rules import Rule, Result
from ...resources import Resources
from hardeneks import helpers


def _get_policy_documents_for_role(role_name, iam_client):
    attached_policies = iam_client.list_attached_role_policies(
        RoleName=role_name
    )["AttachedPolicies"]
    inline_policies = iam_client.list_role_policies(RoleName=role_name)[
        "PolicyNames"
    ]
    actions = []
    for policy_arn in [x["PolicyArn"] for x in attached_policies]:
        version_id = iam_client.get_policy(PolicyArn=policy_arn)["Policy"][
            "DefaultVersionId"
        ]
        response = iam_client.get_policy_version(
            PolicyArn=policy_arn, VersionId=version_id
        )["PolicyVersion"]["Document"]["Statement"]
        for statement in response:
            if type(statement["Action"]) == str:
                actions.append(statement["Action"])
            elif type(statement["Action"]) == list:
                actions.extend(statement["Action"])
    for policy_name in inline_policies:
        response = iam_client.get_role_policy(
            RoleName=role_name, PolicyName=policy_name
        )["PolicyDocument"]["Statement"]
        for statement in response:
            if type(statement["Action"]) == str:
                actions.append(statement["Action"])
            elif type(statement["Action"]) == list:
                actions.extend(statement["Action"])
    return actions



class check_any_cluster_autoscaler_exists(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Deploy either K8s Cluster Autoscaler or Karpenter"
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/"

    def check(self, resources: Resources):
        
        Status = False
        
        (isCADeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("cluster-autoscaler", "kube-system")
        (isKarpenterDeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("karpenter", "karpenter")
        
        Info = "Deployment Status for CA : {} and Karpenter : {}".format(isCADeployed, isKarpenterDeployed)
        
        if isCADeployed or isKarpenterDeployed:          
            Status = True            
        
        self.result = Result(status=Status, resource_type="Deployment", info=Info)
        
        
class ensure_cluster_autoscaler_and_cluster_versions_match(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Ensure K8s and CA Versions match"
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#operating-the-cluster-autoscaler"

    def check(self, resources):
        
        Status = True
        
        eks_client = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eks_client.describe_cluster(name=resources.cluster)
        cluster_version = cluster_metadata["cluster"]["version"]

        (isCADeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("cluster-autoscaler", "kube-system")
        
        if isCADeployed:
            ca_containers = deploymentData.spec.template.spec.containers
            ca_image = ca_containers[0].image
            ca_image_version = ca_image.split(":")[-1]
            Info = "K8s Version : {} CA Version : {}".format(cluster_version,ca_image_version)
            if cluster_version not in ca_image_version:
                Status = False
        else:    
            Info = "Kubernetes Cluster Autoscaler is not deployed in the cluster"
            Status = False
            

        self.result = Result(status=Status, resource_type="Deployment", info=Info)



class ensure_cluster_autoscaler_has_autodiscovery_mode(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Ensure Auto discovery of Node groups enabled for K8s CA"
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#operating-the-cluster-autoscaler"

    def check(self, resources):
        
        Status = False
        Info = "K8s CA is not configured with Auto Discovery of Node groups"
        (isCADeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("cluster-autoscaler", "kube-system")
        
        if isCADeployed:
            ca_containers = deploymentData.spec.template.spec.containers
            ca_command = ca_containers[0].command
            #print("ca_command={}".format(ca_command))
            if any("node-group-auto-discovery" in item for item in ca_command):
                Status = True
                Info = "K8s CA is configured with Auto Discovery of Node groups"
        else:
            Info = "Kubernetes Cluster Autoscaler is not deployed in the cluster"
            
        self.result = Result(status=Status, resource_type="Deployment", info=Info)

class use_separate_iam_role_for_cluster_autoscaler(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Ensure K8s CA Uses dedicated IAM Role (IRSA)."
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#employ-least-privileged-access-to-the-iam-role"

    def check(self, resources):
        Status = False
        (isCADeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("cluster-autoscaler", "kube-system")
        
        if isCADeployed:
            sa = deploymentData.spec.template.spec.service_account_name
            sa_data = kubernetes.client.CoreV1Api().read_namespaced_service_account(sa, 'kube-system', pretty="true")
            if 'eks.amazonaws.com/role-arn' in sa_data.metadata.annotations.keys():
                Status = True
                Info = "K8s CA uses separate IAM Role (IRSA)"
            else:
                Info = "K8s CA doesn't use separate IAM Role (IRSA)" 
        else:
            Info = "Kubernetes Cluster Autoscaler is not deployed in the cluster"

        self.result = Result(status=Status, resource_type="IRSA for K8s CA",info=Info) 

class employ_least_privileged_access_cluster_autoscaler_role(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Cluster autoscaler role has unnecessary actions assigned."
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#employ-least-privileged-access-to-the-iam-role"

    def check(self, resources):

        iam_client = boto3.client("iam", region_name=resources.region)
        ACTIONS = {
            "autoscaling:DescribeAutoScalingGroups",
            "autoscaling:DescribeAutoScalingInstances",
            "autoscaling:DescribeLaunchConfigurations",
            "autoscaling:DescribeScalingActivities",
            "autoscaling:DescribeTags",
            "ec2:DescribeImages",
            "ec2:DescribeInstanceTypes",
            "ec2:DescribeLaunchTemplateVersions",
            "ec2:GetInstanceTypesFromInstanceRequirements",
            "eks:DescribeNodegroup",
            "autoscaling:SetDesiredCapacity",
            "autoscaling:TerminateInstanceInAutoScalingGroup",
        }
        
        Status = False
        (isCADeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("cluster-autoscaler", "kube-system")
        
        if isCADeployed:
            sa = deploymentData.spec.template.spec.service_account_name
            sa_data = kubernetes.client.CoreV1Api().read_namespaced_service_account(sa, 'kube-system', pretty="true")
            if 'eks.amazonaws.com/role-arn' in sa_data.metadata.annotations.keys():
                sa_iam_role_arn = sa_data.metadata.annotations["eks.amazonaws.com/role-arn"]
                sa_iam_role = sa_iam_role_arn.split("/")[-1]
                print("sa_iam_role={}".format(sa_iam_role))
                
                actions = _get_policy_documents_for_role(sa_iam_role, iam_client)

                if len(set(actions) - ACTIONS) > 0:
                    Info = "K8s CA IAM Role has more IAM permissions than needed"
                    self.result = Result(
                        status=False,
                        resource_type="IAM Role Action",
                        resources=(set(actions) - ACTIONS),
                    )           
                else:
                    Status = True
                    Info = "K8s CA IAM Role has least privileged access"
            else:
                Info = "K8s CA doesn't use separate IAM Role (IRSA)" 
        else:
            Info = "Kubernetes Cluster Autoscaler is not deployed in the cluster"

        self.result = Result(status=Status, resource_type="K8s CA IAM Role least privileged access",info=Info) 


class use_managed_nodegroups(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Nodes are recommended to be part of a managed noge group."
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#configuring-your-node-groups"

    def check(self, resources):
        offenders = []
        nodes = kubernetes.client.CoreV1Api().list_node().items

        for node in nodes:
            labels = node.metadata.labels
            if "eks.amazonaws.com/nodegroup" in labels.keys():
                pass
            elif "alpha.eksctl.io/nodegroup-name" in labels.keys():
                offenders.append(node)
            elif "karpenter.sh/provisioner-name" in labels.keys():
                pass
            else:
                offenders.append(node)

        self.result = Result(status=True, resource_type="Node")

        if offenders:
            self.result = Result(
                status=False,
                resource_type="Node",
                resources=[i.metadata.name for i in offenders],
            )


class ensure_cluster_autoscaler_has_three_replicas(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Ensure Cluster Autoscaler has 3 replicas for HA"
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#configuring-your-node-groups"

    def check(self, resources):
        Status = False
        deployments = (kubernetes.client.AppsV1Api().list_namespaced_deployment("kube-system").items)
        
        is_cluster_autoscaler_deployed = False
        
        for deployment in deployments:
            if deployment.metadata.name == "cluster-autoscaler":
                is_cluster_autoscaler_deployed = True
                ca_replicas = deployment.spec.replicas
                if ca_replicas >= 3:
                    Info = "K8s Cluster Autoscaler has {} replicas".format(ca_replicas)
                    Status = True
                else:
                    Info = "K8s Cluster Autoscaler has only {} replicas".format(ca_replicas)
                    Status = False
                break        

        if not is_cluster_autoscaler_deployed:
            Info = "Kubernetes Cluster Autoscaler is not deployed in the cluster"
            Status = False
            
        
        self.result = Result(status=Status, resource_type="K8s CA Replica Count", info=Info)

class ensure_uniform_instance_types_in_nodegroups(Rule):
    _type = "cluster_wide"
    pillar = "cluster_autoscaling"
    section = "cluster_autoscaler"
    message = "Ensure Uniform Instance Types in Node groups"
    url = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/"

    def check(self, resources):
        
        resourceType = "Uniform Instance Types in Node group"
        offenders = []
        uniformNodeGroups = []
        
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        
        nodegroupList = {}
        nodegroupInstanceSizesList={}
        
        nodeList = (client.CoreV1Api().list_node().items)
        for node in nodeList:
            labels = node.metadata.labels
            #print("nodeName={} nodegroup={}".format(node.metadata.name, labels ))
            if 'eks.amazonaws.com/nodegroup' in labels.keys():
                #print("nodeName={} managed nodegroup={}".format(node.metadata.name, labels['eks.amazonaws.com/nodegroup'] ))
                nodegroupName = labels['eks.amazonaws.com/nodegroup']
                if nodegroupName not in nodegroupList.keys():
                    nodegroupList[nodegroupName] = []
                
                nodegroupList[nodegroupName].append(labels['beta.kubernetes.io/instance-type'])
                #eksmnglist.add(labels['eks.amazonaws.com/nodegroup'])
            elif 'alpha.eksctl.io/nodegroup-name' in labels.keys():
                nodegroupName = labels['alpha.eksctl.io/nodegroup-name']
                if nodegroupName not in nodegroupList.keys():
                    nodegroupList[nodegroupName] = []
                nodegroupList[nodegroupName].append(labels['beta.kubernetes.io/instance-type'])            
                #print("nodeName={} self managed nodegroup={}".format(node.metadata.name, labels['alpha.eksctl.io/nodegroup-name'] ))
                #selfmnglist.add(labels['alpha.eksctl.io/nodegroup-name'])
            elif 'karpenter.sh/provisioner-name' in labels.keys():          
                #print("nodeName={} Karpeneter managed provisioner={}".format(node.metadata.name, labels['karpenter.sh/provisioner-name'] ))
                pass
            else:
                pass
                
                #print("nodeName={} self managed with node labels={}".format(node.metadata.name, labels ))
                
        
        #nodegroupList['ng-3f4edeea'].append('m5.xlarge')
        #nodegroupList['mng2'].append('m5.2xlarge')
        #print("nodegroupList={}".format(nodegroupList))
        
        descriptionMessage = "These nodegroups contain non uniform instance types :"
        
        ec2client = boto3.client('ec2')
        isNonUniformNodegroupsExists = None
        for nodegroupName, instanceTypesList in nodegroupList.items():
            instanceTypesData = ec2client.describe_instance_types(InstanceTypes=instanceTypesList)
            #print("instanceTypesData={}".format(instanceTypesData))
            nodegroupInstanceSizesList[nodegroupName] = set()      
            for instanceData in instanceTypesData['InstanceTypes']:
                #print("InstanceType={} DefaultVCpus={} SizeInMiB={}".format(instanceData['InstanceType'], instanceData['VCpuInfo']['DefaultVCpus'], instanceData['MemoryInfo']['SizeInMiB']))
                DefaultVCpus=instanceData['VCpuInfo']['DefaultVCpus']
                SizeInMiB=instanceData['MemoryInfo']['SizeInMiB']
                nodegroupInstanceSizesList[nodegroupName].add((DefaultVCpus, int(SizeInMiB/1024)))
            
            if len(nodegroupInstanceSizesList[nodegroupName]) > 1:
                offenders.append(nodegroupName)
            else:
                uniformNodeGroups.append(nodegroupName)
        #print("nodegroupInstanceSizesList={}".format(nodegroupInstanceSizesList))
        #print("offenders={} uniformNodeGroups={}".format(offenders, uniformNodeGroups))
    
        if offenders:
            Info = "Node group does not have uniform Instance Types"
            self.result = Result(
                status=False,
                resource_type=resourceType,
                resources=[i for i in offenders],
                info = Info
            )
        else:
            Info = "Node group has uniform Instance Types"
            self.result = Result(
                status=True,
                resource_type=resourceType,
                resources=[i for i in uniformNodeGroups],
                info = Info
            )
            