import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3

class get_EKS_version(Rule):
    _type = "cluster_wide"
    pillar = "cluster_data"
    section = "control_plane"
    message = "Get EKS Cluster Version"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    
    
    def check(self, resources: Resources):
        checkStatus = False
        client = kubernetes.client.VersionApi()
        version = client.get_code()
        minor = version.minor
        resources=f"{version.major}.{minor}"
        #print("version={} minor={} reg={} resources={}".format(version, minor, int(re.sub("[^0-9]", "", minor)), resources))

        if int(re.sub("[^0-9]", "", minor)) >= 25:
            checkStatus = True
            
        self.result = Result(status=checkStatus, resource_type="EKS Cluster Version")

        
        
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
        endpoibtAccessString = "public: " + str(endpoint_public_access) + ", " + "private: " + str(endpoint_private_access)
        resource = endpoibtAccessString + " " + cluster_endpoint
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
                    

