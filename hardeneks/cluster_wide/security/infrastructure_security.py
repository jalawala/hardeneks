import boto3

from ...resources import Resources
from hardeneks.rules import Rule, Result
import kubernetes
import pprint


class deploy_workers_onto_private_subnets(Result):
    _type = "cluster_wide"
    pillar = "security"
    section = "infrastructure_security"
    message = "Deploy workers onto private subnets"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/hosts/#deploy-workers-onto-private-subnets"

    def check(self, resources: Resources):
        client = boto3.client("ec2", region_name=resources.region)

        offenders = []

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
            if instance["Instances"][0]["PublicDnsName"]:
                offenders.append(instance["Instances"][0]["InstanceId"])

        if offenders:
            self.result = Result(
                status=False, resource_type="Node", resources=offenders
            )
        else:
            self.result = Result(status=True, resource_type="Node")

class make_sure_inspector_is_enabled(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "infrastructure_security"
    message = "Run Amazon Inspector to assess hosts for exposure, vulnerabilities, and deviations from best practices"
    url = "Run Amazon Inspector to assess hosts for exposure, vulnerabilities, and deviations from best practices"

    def check(self, resources: Resources):
        client = boto3.client("inspector2", region_name=resources.region)
        account_id = boto3.client(
            "sts", region_name=resources.region
        ).get_caller_identity()["Account"]

        response = client.batch_get_account_status(
            accountIds=[
                account_id,
            ]
        )

        resource_state = response["accounts"][0]["resourceState"]
        #print("resource_state={}".format(resource_state))
        ec2_status = resource_state["ec2"]["status"]
        ecr_status = resource_state["ecr"]["status"]

        if ec2_status != "ENABLED" and ecr_status != "ENABLED":
            self.result = Result(
                status=False, resource_type="Inspector Configuration"
            )
        else:
            self.result = Result(
                status=True, resource_type="Inspector Configuration"
            )         
            
class use_OS_optimized_for_running_containers(Rule):
    
    _type = "cluster_wide"
    pillar = "security"
    section = "infrastructure_security"
    message = "Use an OS optimized for running containers"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/hosts/#use-an-os-optimized-for-running-containers"

    def check(self, resources: Resources):
        
        checkStatus = True
        
        nodeList = (kubernetes.client.CoreV1Api().list_node().items)
        
        oslist = set()
        
        for node in nodeList:
            #print(pprint.pformat(node.status.node_info, indent=4))            
            os = node.status.node_info.os_image
            #print(pprint.pformat(os, indent=4))
            if 'Bottlerocket OS' not in os:
                oslist.add(os)
            
        if oslist:
            Info = "Node OS is not optimized for containers "
            resource = " ".join(list(oslist))
            self.result = Result(
                status=False,
                resource_type="Node OS",
                resources=[resource],
                info = Info
            )
        else:
            Info = "Node OS is optimized for containers "
            self.result = Result(status=True, resource_type="Node OS", info = Info, )
            
        