import boto3
from kubernetes import client
import json
import hardeneks

from ...resources import Resources
from hardeneks.rules import Rule, Result
from hardeneks import helpers


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
        Status = False
        (ret1, serviceData) = helpers.is_service_exists_in_cluster("aws-privateca-issuer")
        (ret2, serviceData) = helpers.is_service_exists_in_cluster("cert-manager")
        
        #print("ret1={} ret2={}".format(ret1,ret2))
        if ret1 and ret2:
            Status = True

        self.result = Result(
            status=Status,
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
        
        Info = "default deny policy exist for all namespaces"
        
        offenders = resources.namespaces

        namespaces_with_network_policies = []
    
        for policy in resources.network_policies:
            namespaces_with_network_policies.append(policy.metadata.namespace)
            
        namespaces_with_network_policies = list(set(namespaces_with_network_policies) - set(hardeneks.ignoredNSList))    
        #print(resources.network_policies)
        
        for policy in resources.network_policies:
            
            #print(policy)
            name = policy.metadata.name
            ns = policy.metadata.namespace
            match_labels = policy.spec.pod_selector.match_labels
            match_expressions = policy.spec.pod_selector.match_labels
            
            policy_types = policy.spec.policy_types
            
            if match_labels is None and match_expressions is None and 'Ingress' in policy_types and 'Egress' in policy_types:
                #print("Removing namespace {} from list as there is a default deny policy".format(ns))
                offenders.remove(ns)
            
            #print(type(policy_types))
            #print(type(match_expressions))
            #print("namespace={} name={}m match_labels={} match_expressions={} ".format(ns, name, match_labels, match_expressions))
            
        if offenders:
            Info = "default deny policy doesn't exist for namespaces : " + " ".join(offenders)
            self.result = Result(status=False, resource_type="Namespace", info=Info)
        else:
            self.result = Result(status=True, resource_type="Namespace", info=Info)
