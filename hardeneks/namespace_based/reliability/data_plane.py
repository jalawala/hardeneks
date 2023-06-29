from ...resources import NamespacedResources
from hardeneks.rules import Rule, Result
import kubernetes
import pprint


class limit_container_resource_usage_within_namespace(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "data_plane"
    message = "Limit container resource usage within a namespace"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/dataplane/#limit-container-resource-usage-within-a-namespace"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        limit_range_names = []
        Status = False
        Info = "There are no LimitRange in the Namespace "

        limit_ranges_list = kubernetes.client.CoreV1Api().list_namespaced_limit_range(namespace=namespaced_resources.namespace).items
        
        
        #print(limit_ranges_list)
        
        if limit_ranges_list:
            Status = True
            for limit_range in limit_ranges_list:
                limit_range_names.append(limit_range.metadata.name)
            
            Info = "LimitRange in the Namespace : " + " ".join(limit_range_names)
            
        self.result = Result(status=Status, resource_type="LimitRange", namespace=namespaced_resources.namespace, info=Info)
            
