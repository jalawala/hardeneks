from ...resources import Resources
from hardeneks.rules import Rule, Result
import hardeneks
from hardeneks import helpers

class policy_as_code(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "regulatory_compliance"
    message = "Policy as Code"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/multitenancy/#quotas"

    def check(self, resources: Resources):
        
        Status = False
        
        (isGKDeployed, deploymentData) = helpers.is_deployment_exists_in_namespace("gatekeeper-controller-manager", "gatekeeper-system")
        
        Info = "Deployment Status for Gatekeeper : {} ".format(isGKDeployed)
        
        if isGKDeployed:          
            Status = True            
        
        self.result = Result(status=Status, resource_type="Deployment", info=Info)
        
        