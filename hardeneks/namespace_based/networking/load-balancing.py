import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from ...resources import NamespacedResources
import boto3
from hardeneks import helpers

class use_ip_target_type_load_balancers(Rule):
    _type = "namespace_based"
    pillar = "networking"
    section = "load-balancing"
    message = "Use IP Target-Type Load Balancers"
    url = "https://aws.github.io/aws-eks-best-practices/networking/loadbalancing/loadbalancing/#use-ip-target-type-load-balancers"

    
    def check(self, namespaced_resources: NamespacedResources):    
        offenders = []
        Status = False
        Info = "All Services use IP Mode for Target Group"
        #services = kubernetes.client.CoreV1Api().list_service_for_all_namespaces().items
        
        for service in namespaced_resources.services:
            #print(service)
            service_type =  service.spec.type
            if service_type == 'LoadBalancer':
                #print(service.metadata.name)
                if 'service.beta.kubernetes.io/aws-load-balancer-nlb-target-type' in service.metadata.annotations.keys():
                    target_group_mode = service.metadata.annotations["service.beta.kubernetes.io/aws-load-balancer-nlb-target-type"]                
                    if target_group_mode == "ip":
                        Status = True
                    else:
                        offenders.append(service.metadata.name)
                        Info = "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type does not exist in the annotation"
                else:
                    Info = "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type is set to Instance Mode"
                    offenders.append(service.metadata.name)
                    
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Service",
                resources=[resource],
                namespace=namespaced_resources.namespace,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="Service",namespace=namespaced_resources.namespace, info=Info)