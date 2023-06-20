import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3


class use_prefix_mode(Rule):
    _type = "cluster_wide"
    pillar = "networking"
    section = "vpc-cni"
    message = "Deploy VPC CNI Managed Add-On"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"


    def check(self, resources: Resources):
        
        daemonset = kubernetes.client.AppsV1Api().read_namespaced_daemon_set(name="aws-node", namespace="kube-system")
        vpccni_containers = daemonset.spec.template.spec.containers
        vpccni_image = vpccni_containers[0].image
        vpccni_image_version = vpccni_image.split('/')[-1].split(':')[-1].split('-')[0]
        vpccni_image_version_digits = vpccni_image_version.split('.')
        
        if int(vpccni_image_version_digits[1]) >= 9 and int(vpccni_image_version_digits[2]) >= 0:
            isvpccni_version_correct=True
    
        #print("vpccni_image={} vpccni_image_version={} 2nd={} 3rd={}".format(vpccni_image, vpccni_image_version, vpccni_image_version[1], vpccni_image_version[2]))
        #print("vpccni_containers={}".format(vpccni_containers))
        #envList = vpccni_containers[0].env
        #print("envList={} type={}".format(envList, type(envList)))
        #for env in envList:
        for env in vpccni_containers[0].env:        
            print("name={} value={}".format(env.name, env.value))
            if env.name == 'ENABLE_PREFIX_DELEGATION':
                isPrefixModeEabled = env.value
            
        nodeList = (kubernetes.client.CoreV1Api().list_node().items)
        for node in nodeList:
            name = node.metadata.name
            pods = node.status.capacity['pods']
            #print("name={} pods={}".format(name, pods))
            if int(pods) < 110:
                isMaxPodsPerNodeIncorrect = True
                
            
            
        if not isMaxPodsPerNodeIncorrect and isvpccni_version_correct and isPrefixModeEabled == 'true':
            Status = True
            Info = "vpc cni prefix mode enabled and version is {} and max pods is set 110".format(vpccni_image_version)
        else:
            Status = False
            Info = "vpc cni prefix mode disabled and version is {} and ensure max pods is set to 110".format(vpccni_image_version)

        
        self.result = Result(status=Status, resource_type="VPC CNI Prefix Mode",info=Info)    
        