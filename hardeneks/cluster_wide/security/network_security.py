import boto3
from kubernetes import client
import json

from ...resources import Resources
from hardeneks.rules import Rule, Result


class check_vpc_flow_logs(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "network_security"
    message = "Enable flow logs for your VPC."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/network/#log-network-traffic-metadata"

    def check(self, resources: Resources):
        Status = False
        
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        vpc_id = cluster_metadata["cluster"]["resourcesVpcConfig"]["vpcId"]
        
        ec2client = boto3.client("ec2", region_name=resources.region)

        response = ec2client.describe_flow_logs(
            Filters=[{"Name": "resource-id", "Values": [vpc_id]}]
        )
        
        flow_logs =  response["FlowLogs"]
        #print(response['FlowLogs'])

        
        if flow_logs:
            Status = True
            
        self.result = Result(status=Status, resource_type="VPC Configuration")
        
        

class check_awspca_exists(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "network_security"
    message = "Install aws privateca issuer for your certificates."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/network/#acm-private-ca-with-cert-manager"

    def check(self, resources: Resources):
        services = client.CoreV1Api().list_service_for_all_namespaces().items
        for service in services:
            if service.metadata.name.startswith("aws-privateca-issuer"):
                self.result = Result(status=True, resource_type="Service")

        self.result = Result(
            status=False,
            resource_type="Service",
            resources=["aws-privateca-issuer"],
        )


class check_default_deny_policy_exists(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "network_security"
    message = "Namespaces that does not have default network deny policies."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/network/#create-a-default-deny-policy"

    def check(self, resources: Resources):
        offenders = resources.namespaces

        for policy in resources.network_policies:
            offenders.remove(policy.metadata.namespace)

        self.result = Result(status=True, resource_type="Namespace")

        if offenders:
            self.result = Result(
                status=False, resource_type="Service", resources=offenders
            )
