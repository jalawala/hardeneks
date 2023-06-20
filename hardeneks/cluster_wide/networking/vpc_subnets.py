import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3


class cluster_endpoint_public_and_private_mode(Rule):
    _type = "cluster_wide"
    pillar = "networking"
    section = "vpc_subnets"
    message = "Cluster Endpoint Mode"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


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
