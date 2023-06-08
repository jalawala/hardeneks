import boto3
from kubernetes import client
from rich.console import Console
from rich.panel import Panel
from rich import print
import sys, copy


from ...resources import Resources
from ...report import print_namespace_table


console = Console()


def check_vpc_flow_logs(resources: Resources):
    status = None
    objectsList = []
    objectType = "ClusterRole"
    message = ""
    clusterrolenameslist = ""
    
    client = boto3.client("eks", region_name=resources.region)
    cluster_metadata = client.describe_cluster(name=resources.cluster)

    vpc_id = cluster_metadata["cluster"]["resourcesVpcConfig"]["vpcId"]
    client = boto3.client("ec2", region_name=resources.region)

    flow_logs = client.describe_flow_logs(
        Filters=[{"Name": "resource-id", "Values": [vpc_id]}]
    )["FlowLogs"]

    if not flow_logs:
        status = False
        message = "Enable flow logs for your VPC"
    else:
        status = True
        message = "VPC flow logs are enabled"
            
    return (status, message, objectsList, objectType)


def check_awspca_exists(resources: Resources):
    
    status = False
    objectsList = []
    objectType = None
    message = "Install aws privateca issuer for your certificates."
    
    services = client.CoreV1Api().list_service_for_all_namespaces().items
    for service in services:
        if service.metadata.name.startswith("aws-privateca-issuer"):
            status = True
            message = "aws privateca issuer for certificates exists"

    return (status, message, objectsList, objectType)


def check_default_deny_policy_exists(resources: Resources):
    
    status = None
    objectsList = []
    objectType = "Namespace"
    message = ""
    
    #objectsList = resources.namespaces
    objectsList = copy.deepcopy(resources.namespaces)
    
    #print("objectsList={}".format(objectsList))
    
    for policy in resources.network_policies:
        #print("namespace={} objectsList={}".format(policy.metadata.namespace, objectsList))
        objectsList.remove(policy.metadata.namespace)
    
    if objectsList:
        status = False
        message = "Namespaces does not have default network deny policies"
    else:
        status = True
        message = "Namespaces have default network deny policies"
    
    return (status, message, objectsList, objectType)
