from ...resources import Resources
from hardeneks.rules import Rule, Result
import hardeneks
import copy

class ensure_namespace_quotas_exist(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "multi_tenancy"
    message = "Namespaces should have quotas assigned."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/multitenancy/#quotas"

    def check(self, resources: Resources):
        #offenders = resources.namespaces
        offenders = copy.deepcopy(resources.namespaces)
        namespaces_with_resource_quotas = []
    
        for quota in resources.resource_quotas:
            namespaces_with_resource_quotas.append(quota.metadata.namespace)
        
        #print("offenders={} ignoredNSList={} namespaces_with_resource_quotas={}".format(offenders,  hardeneks.ignoredNSList, namespaces_with_resource_quotas))
        
        namespaces_with_resource_quotas = list(set(namespaces_with_resource_quotas) - set(hardeneks.ignoredNSList))
                
        #print("namespaces_with_resource_quotas={}".format(namespaces_with_resource_quotas))
         
        for ns in namespaces_with_resource_quotas:
            #print("Removing ns {} from list {}".format(ns, offenders))    
            if ns in offenders:
                offenders.remove(ns)
        
        if offenders:
            Info = "Resource Quots does not exist for namespaces : " + " ".join(offenders)
            self.result = Result(status=False, resource_type="Namepsace", info=Info)
        else:
            Info = "All Namespaces have Resource Quotas"
            self.result = Result(status=True, resource_type="Namespace", info=Info)
            
