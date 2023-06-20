import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3
from hardeneks import helpers

class deploy_aws_lb_controller(Rule):
    _type = "cluster_wide"
    pillar = "networking"
    section = "load-balancing"
    message = "Deploy AWS Load Balancer Controller"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    def check(self, resources: Resources):
        
        (ret, deploymentData) = helpers.is_deployment_exists_in_namespace("aws-load-balancer-controller", "kube-system")
        if ret:
            Status = True
            Info = "AWS LB Controller is deployed in the cluster"
        else:
            Status = False
            Info = "AWS LB Controller is not deployed in the cluster"
            
        self.result = Result(status=Status, resource_type="AWS Load Balancer Controller",info=Info)    
        
            