import boto3
from kubernetes import client

from hardeneks.rules import Rule, Result
from ...resources import Resources




class check_EKS_version(Rule):
    _type = "cluster_wide"
    pillar = "scalability"
    section = "control_plane"
    message = "EKS Version Should be greater or equal to 1.24."
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    def check(self, resources: Resources):
        client = kubernetes.client.VersionApi()
        version = client.get_code()
        minor = version.minor

        if int(re.sub("[^0-9]", "", minor)) < 24:
            self.result = Result(
                status=False,
                resources=f"{version.major}.{minor}",
                resource_type="Cluster Version",
            )
        else:
            self.result = Result(status=True, resource_type="Cluster Version")
            
            
class check_cluster_highlevel_details(Rule):
    _type = "cluster_wide"
    pillar = "cluster-data"
    section = "cluster-data"
    message = "Cluster High Level Details"
    url = "https://aws.github.io/aws-eks-best-practices/"

    def check(self, resources: Resources):
        current_eks_version = "1.25"
        eks_cluster_data = []
        
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        cluster_version = cluster_metadata["cluster"]["version"]
        
        if cluster_version == current_eks_version:
            eks_cluster_data.append(  ["green", resources.cluster, cluster_version, "Cluster version is latest version"])
        else:
            eks_cluster_data.append(  ["yellow", resources.cluster, cluster_version, "Upgrade to latest version: {}".format(current_eks_version)])
    
            
        deployments = [
            i.metadata.name
            for i in client.AppsV1Api()
            .list_deployment_for_all_namespaces()
            .items
        ]
        if not (
            "cluster-autoscaler" in deployments or "karpenter" in deployments
        ):
            self.result = Result(status=False, resource_type="Deployment")
        else:
            self.result = Result(status=True, resource_type="Deployment")

        return self.result


def cluster_data(resources, config, _type):

    current_eks_version = "1.25"
    eks_cluster_data = []
    
    eksclient = boto3.client("eks", region_name=resources.region)
    cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
    cluster_version = cluster_metadata["cluster"]["version"]
    
    if cluster_version == current_eks_version:
        eks_cluster_data.append(  ["green", resources.cluster, cluster_version, "Cluster version is latest version"])
    else:
        eks_cluster_data.append(  ["yellow", resources.cluster, cluster_version, "Upgrade to latest version: {}".format(current_eks_version)])

    cluster_endpoint = cluster_metadata["cluster"]["endpoint"]
    eks_cluster_data.append(  ["green", "Cluster Endpoint URL", cluster_endpoint, ""])

    vpcId  = cluster_metadata["cluster"]["resourcesVpcConfig"]["vpcId"]
    subnetIds = cluster_metadata["cluster"]["resourcesVpcConfig"]["subnetIds"]
    
    
    eks_cluster_data.append(  ["green", "Cluster VPC Id", vpcId, ""])

    subnetIdsString = " ".join(subnetIds)
    eks_cluster_data.append(  ["green", "Cluster Subnets Id", subnetIdsString, ""])

    endpoint_public_access  = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
    endpoint_private_access = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"]
    
    endpoibtAccessString = "public: " + str(endpoint_public_access) + ", " + "private: " + str(endpoint_private_access)
    eks_cluster_data.append(  ["green", "Cluster Endpoint Access", endpoibtAccessString, ""])

    subnets = boto3.resource("ec2").subnets.filter(
        Filters=[{"Name": "vpc-id", "Values": [vpcId]}]
    )
    subnet_ids = [sn.id for sn in subnets]
    

    ec2client = boto3.client('ec2')
    subnetsList = ec2client.describe_subnets(SubnetIds=subnet_ids)
    
    totalAvailableIpAddressCount = 0
    for subnet in subnetsList['Subnets']:
        totalAvailableIpAddressCount += subnet['AvailableIpAddressCount']
        
    eks_cluster_data.append(  ["green", "Total Available IPs in the VPC", str(totalAvailableIpAddressCount), ""])    
        
    deployments = client.AppsV1Api().list_deployment_for_all_namespaces().items
    eks_cluster_data.append(  ["green", "Total No. of Deployments in Cluster", str(len(deployments)), ""])    
    
    services = client.CoreV1Api().list_service_for_all_namespaces().items
    eks_cluster_data.append(  ["green", "Total No. of Services in Cluster", str(len(services)), ""])    
    
    pods = client.CoreV1Api().list_pod_for_all_namespaces().items
    eks_cluster_data.append(  ["green", "Total No. of Pods in Cluster", str(len(pods)), ""])    
    
    
    nodeList = (client.CoreV1Api().list_node().items)
    eks_cluster_data.append(  ["green", "Total No. of Nodes in Cluster", str(len(nodeList)), ""])    

    eksmnglist = set()
    selfmnglist=set()
    
    for node in nodeList:
        labels = node.metadata.labels
        
        if 'eks.amazonaws.com/nodegroup' in labels.keys():
            
            eksmnglist.add(labels['eks.amazonaws.com/nodegroup'])
        elif 'alpha.eksctl.io/nodegroup-name' in labels.keys():
            
            selfmnglist.add(labels['alpha.eksctl.io/nodegroup-name'])
        elif 'karpenter.sh/provisioner-name' in labels.keys():          
            
            pass
        else:
            selfmnglist.add(node.metadata.name)
            
            
    if len(eksmnglist) >=1 :
        eks_cluster_data.append(  ["green", "List of EKS Managed node groups in the Cluster", ' '.join(eksmnglist), ""])
        
    if len(selfmnglist) >=1 :
        eks_cluster_data.append(  ["green", "List of Self Managed node groups in the Cluster", ' '.join(selfmnglist), ""])
        
                
    print_console_message(True, "aws-eks-best-practices", None, eks_cluster_data, "ClusterData")

    
