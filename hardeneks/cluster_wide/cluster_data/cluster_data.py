import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3
import pprint

class get_EKS_version(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "control_plane"
    message = "Get EKS Cluster Version"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    
    
    def check(self, resources: Resources):

        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        versionStr = cluster_metadata["cluster"]["version"]
        #version = int(versionStr.split('.')[-1))
        
        Info = "EKS Cluster Version {}".format(versionStr)
            
        self.result = Result(status=True, resource_type="EKS Cluster Version", info=Info)

        
        
class get_EKS_cluster_endpoint_url(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "control_plane"
    message = "Get EKS Cluster Endpoint URL"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        checkStatus = True
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        cluster_endpoint = cluster_metadata["cluster"]["endpoint"]
        endpoint_public_access  = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
        endpoint_private_access = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"]
        endpointAccessString = "public: " + str(endpoint_public_access) + ", " + "private: " + str(endpoint_private_access)
        resource = endpointAccessString + " " + cluster_endpoint
        self.result = Result(status=checkStatus, resource_type="EKS Cluster Endpoint URL",resources=[resource],)
        

                
class get_cluster_vpc_subnets(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "data_plane"
    message = "Get EKS Cluster VPC & Subnets"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        checkStatus = True
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        vpcId  = cluster_metadata["cluster"]["resourcesVpcConfig"]["vpcId"]
        subnetIds = cluster_metadata["cluster"]["resourcesVpcConfig"]["subnetIds"]
        subnetIdsString = " ".join(subnetIds)
        resource=f"vpcId {vpcId} subnetIds {subnetIdsString}"
        self.result = Result(status=checkStatus, resource_type="EKS Cluster VPC & Subnet Ids",resources=[resource],)
                    

        
class get_available_free_ips_in_vpc(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "data_plane"
    message = "Check Available Free IPs in EKS VPC"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        checkStatus = True
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        vpcId  = cluster_metadata["cluster"]["resourcesVpcConfig"]["vpcId"]
        subnetIds = cluster_metadata["cluster"]["resourcesVpcConfig"]["subnetIds"]
        subnets = boto3.resource("ec2").subnets.filter(
            Filters=[{"Name": "vpc-id", "Values": [vpcId]}]
        )        
        subnet_ids = [sn.id for sn in subnets]
        ec2client = boto3.client('ec2')
        subnetsList = ec2client.describe_subnets(SubnetIds=subnet_ids)
        
        totalAvailableIpAddressCount = 0
        for subnet in subnetsList['Subnets']:
            totalAvailableIpAddressCount += subnet['AvailableIpAddressCount']
        
        resource=f"Availablle Free IPs {totalAvailableIpAddressCount}"
        self.result = Result(status=checkStatus, resource_type="Available Free IPs in EKS VPC",resources=[resource],)
                    


class get_cluster_size_details(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "data_plane"
    message = "Get Cluster Size Details"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        checkStatus = True
        
        deployments = kubernetes.client.AppsV1Api().list_deployment_for_all_namespaces().items
        services = kubernetes.client.CoreV1Api().list_service_for_all_namespaces().items
        pods = kubernetes.client.CoreV1Api().list_pod_for_all_namespaces().items
        nodeList = (kubernetes.client.CoreV1Api().list_node().items)
        
        resource=f"Services : {len(services)} Deployments : {len(deployments)} Pods: {len(pods)} Nodes: {len(nodeList)}"
        
        self.result = Result(status=checkStatus, resource_type="Size of the Cluster",resources=[resource],)
                    

class get_nodegroups_provisioners(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "data_plane"
    message = "Get Node groups and Provisioners"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        checkStatus = True
        
        nodeList = (kubernetes.client.CoreV1Api().list_node().items)
        
        eksmnglist = set()
        selfmnglist=set()
        provisionerlist=set()
        linuxnglist=set()
        windowsnglist=set()
        
        for node in nodeList:
            labels = node.metadata.labels
            
            if 'eks.amazonaws.com/nodegroup' in labels.keys():
                nodeName = labels['eks.amazonaws.com/nodegroup']
                eksmnglist.add(nodeName)
            elif 'alpha.eksctl.io/nodegroup-name' in labels.keys():
                nodeName = labels['alpha.eksctl.io/nodegroup-name']
                selfmnglist.add(nodeName)
            elif 'karpenter.sh/provisioner-name' in labels.keys():
                nodeName = labels['karpenter.sh/provisioner-name']
                provisionerlist.add(nodeName)
            else:
                nodeName = "Unkown-nodegroup"
            
            if labels['kubernetes.io/os'] == "linux":
                linuxnglist.add(nodeName)
            elif labels['kubernetes.io/os'] == "windows":
                windowsnglist.add(nodeName)
                                                    
        linux_ng = " ".join(list(linuxnglist))
        windows_ng = " ".join(list(windowsnglist))
        resource=f"EKS MNG : {len(eksmnglist)} Self MNG : {len(selfmnglist)} Provisioners: {len(provisionerlist)} Linux NGs: {linux_ng} Windows NGs: {windows_ng}"
        self.result = Result(status=checkStatus, resource_type="Node groups and Provisioners",resources=[resource],)
                    

class get_fargate_profiles(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "data_plane"
    message = "Get EKS Fargate Profiles"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        
        eksclient = boto3.client("eks", region_name=resources.region)       
        response = eksclient.list_fargate_profiles(clusterName=resources.cluster,)
        
        Info = "EKS Fargate Profiles: " + " ".join(response['fargateProfileNames'])
        #print(pprint.pformat(response['fargateProfileNames'], indent=4))
        
        self.result = Result(status=True, resource_type="EKS Fargate Profiles", info=Info)
                    
