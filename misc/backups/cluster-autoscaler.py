import boto3
from pprint import pprint
from kubernetes import client
from rich import print

import sys

from ...resources import Resources
from ...report import print_role_table, print_instance_metadata_table, print_console_message


def check_any_cluster_autoscaler_exists(resources: Resources):
    
    func_name = sys._getframe().f_code.co_name
    docs_link = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/"
    deployments = [
        i.metadata.name
        for i in client.AppsV1Api().list_deployment_for_all_namespaces().items
    ]
    
    #pprint("deployments={}".format(deployments))

    if "cluster-autoscaler" in deployments:
        print_console_message(None, None, "green", func_name, "Kubernetes Cluster Autoscaler is deployed", docs_link)
    elif "karpenter" in deployments:
        docs_link = "https://aws.github.io/aws-eks-best-practices/karpenter/"
        #print_console_message(None, None, "green", "Karpeneter is deployed", docs_link)
        print_console_message(None, None, "green", func_name, "Karpeneter is deployed", docs_link)
    else:
        print_console_message(None, None, "red", func_name, "Kubernetes Cluster Autoscaler or Karpeneter is not deployed", docs_link)
        return False
    
    return True
    
def ensure_cluster_autoscaler_and_cluster_versions_match(resources: Resources):
    
    func_name = sys._getframe().f_code.co_name
    docs_link = "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/"
    
    eksclient = boto3.client("eks", region_name=resources.region)
    cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
    
    cluster_version = cluster_metadata["cluster"]["version"]
    
    print("cluster_version={}".format(cluster_version))
    
    deployments = (client.AppsV1Api().list_namespaced_deployment("kube-system").items)
        
    #print("deployments={}".format(deployments))    
    
    ca_version = None
    ca_containers = None
    
    for deployment in deployments:
        if deployment.metadata.name == "cluster-autoscaler":
            ca_replicas = deployment.spec.replicas
            ca_containers = deployment.spec.template.spec.containers
            #ca_image = deployment.spec.template.spec.containers[0]['image']
            #ca_image = ca_containers[0]['image']
            
            #print("type={}".format(type(ca_containers)))
            #print(type(ca_containers))
            
            ca_image = ca_containers[0].image
            ca_image_version = ca_image.split(':')[-1]
            print(ca_image)
            print(ca_image_version)
            
            
            #for i in ca_containers:
                #print("i={}".format(i))
                #print("image={}".format(i.image))
                
            #print("ca_replicas={} ca_image={} ca_containers={}".format(ca_replicas, ca_image, ca_containers))
            #print("deployment={}".format(deployment))
            
            #ca_object = deployment
        
    #deployments = [
    #    i.metadata.name
    #    for i in client.AppsV1Api().list_deployment_for_all_namespaces().items
    #]
    
    if "cluster-autoscaler" in deployments:
        print_console_message(None, None, "green", func_name, "Kubernetes Cluster Autoscaler is deployed", docs_link)
        
        
        
    else:
        print_console_message(None, None, "red", func_name, "Kubernetes Cluster Autoscaler or Karpeneter is not deployed", docs_link)
        return False
    
    return True    