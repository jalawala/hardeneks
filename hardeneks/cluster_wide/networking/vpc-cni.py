import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3


class deploy_vpc_cni_managed_add_on(Rule):
    _type = "cluster_wide"
    pillar = "networking"
    section = "vpc-cni"
    message = "Deploy VPC CNI Managed Add-On"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):

        eksclient = boto3.client("eks", region_name=resources.region)
        try:
            vpccni_add_on = client.describe_addon(clusterName=resources.cluster, addonName='vpc-cni')
            Status = True
            Info = "VPC CNI is Deployed as EKS Managed Add-On"
            #pprint("vpccni_add_on={}".format(vpccni_add_on))
        except Exception as exc:
            #print(f"[bold][red]{exc}")
            Info = "VPC CNI is not Deployed as EKS Managed Add-On"
            Status = False

        
        self.result = Result(status=Status, resource_type="VPC CNI Managed Add-on",info=Info)    

        

        
