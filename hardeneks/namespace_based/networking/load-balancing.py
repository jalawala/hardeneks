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
        is_there_any_lb_service_in_namespace = False
        #services = kubernetes.client.CoreV1Api().list_service_for_all_namespaces().items
        
        for service in namespaced_resources.services:
            #print(service)
            service_type =  service.spec.type
            if service_type == 'LoadBalancer':
                #print(service.metadata.name)
                is_there_any_lb_service_in_namespace = True
                if 'service.beta.kubernetes.io/aws-load-balancer-nlb-target-type' in service.metadata.annotations.keys():
                    target_group_mode = service.metadata.annotations["service.beta.kubernetes.io/aws-load-balancer-nlb-target-type"]                
                    if target_group_mode == "ip":
                        Status = True
                    else:
                        offenders.append(service.metadata.name)
                        Info = "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type is set to Instance Mode"
                else:
                    Info = "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type does not exist in the annotation"
                    offenders.append(service.metadata.name)
                    
        if not is_there_any_lb_service_in_namespace:
            Info = "There is no Service of Type LoadBalancer"
            
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
            
            

class use_ip_target_type_ingresses(Rule):
    _type = "namespace_based"
    pillar = "networking"
    section = "load-balancing"
    message = "Use IP Target-Type Ingresses"
    url = "https://aws.github.io/aws-eks-best-practices/networking/loadbalancing/loadbalancing/#use-ip-target-type-load-balancers"

    
    def check(self, namespaced_resources: NamespacedResources):    
        offenders = []
        Status = False
        Info = "All Ingresses use IP Mode for Target Group"
        #services = kubernetes.client.CoreV1Api().list_service_for_all_namespaces().items
        is_there_any_lb_ingress_in_namespace = False
        
        for ingress in namespaced_resources.ingresses:
            #print(service)
            is_there_any_lb_ingress_in_namespace = True
            if 'alb.ingress.kubernetes.io/target-type' in ingress.metadata.annotations.keys():
                target_group_mode = ingress.metadata.annotations["alb.ingress.kubernetes.io/target-type"]                
                if target_group_mode == "ip":
                    Status = True
                else:
                    offenders.append(ingress.metadata.name)
                    Info = "alb.ingress.kubernetes.io/target-type is set to Instance Mode"
            else:
                Info = "alb.ingress.kubernetes.io/target-type doesn't exists in annotations"
                offenders.append(ingress.metadata.name)
    

        if not is_there_any_lb_ingress_in_namespace:
            Info = "There is no Ingresses in the Namespace"
            
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Ingress",
                resources=[resource],
                namespace=namespaced_resources.namespace,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="Ingresses",namespace=namespaced_resources.namespace, info=Info)            