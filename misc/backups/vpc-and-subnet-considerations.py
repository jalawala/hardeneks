import boto3
from kubernetes import client
import sys

from ...resources import Resources
from ...report import  print_console_message

def consider_public_and_private_mode(resources: Resources):
    status = True
    func_name = sys._getframe().f_code.co_name
    docs_link = "https://aws.github.io/aws-eks-best-practices/networking/subnets/#consider-public-and-private-mode-for-cluster-endpoint"
    client = boto3.client("eks", region_name=resources.region)
    cluster_metadata = client.describe_cluster(name=resources.cluster)
    #pprint("cluster_metadata={}".format(cluster_metadata))
    endpoint_public_access  = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
    endpoint_private_access = cluster_metadata["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"]

    if endpoint_public_access == True and endpoint_private_access == True:
        print_console_message(None, None, "green", func_name, "EKS Cluster Endpoint is in Public and Private Mode", docs_link)
    else:
        print_console_message(None, None, "red", func_name, "EKS Cluster Endpoint is not in Public and Private Mode", docs_link)
        status = False

    if endpoint_public_access:
        public_access_cidr_list  = cluster_metadata["cluster"]["resourcesVpcConfig"]["publicAccessCidrs"]
        if '0.0.0.0/0' in public_access_cidr_list :
            print_console_message(None, None, "red", func_name, "EKS Cluster Endpoint is Public and Open to Internet Access ['0.0.0.0/0']", docs_link)
        else:
            print_console_message(None, None, "green", func_name, "EKS Cluster Endpoint is Public and is not Open to Internet Access ['0.0.0.0/0']", docs_link)    
            status = False
    
    return status



