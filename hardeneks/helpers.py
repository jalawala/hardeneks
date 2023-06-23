from pathlib import Path
import urllib3
import yaml
import kubernetes
#
# get_kube_config
# returns kube config in json
# 
# we need to update this function to take in a config string, so users can pass in kubeconfig as a param
def get_kube_config():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # need to fix this, so user can pass in .kube/config as a param (joshkurz)
    kube_config_orig = f"{Path.home()}/.kube/config"

    with open(kube_config_orig, "r") as fd:
        kubeconfig = yaml.safe_load(fd)
    return kubeconfig
    

def is_deployment_exists_in_namespace(deploymentName, namespace):
    
    deployments = (kubernetes.client.AppsV1Api().list_namespaced_deployment(namespace).items)
    
    for deployment in deployments:
        if deployment.metadata.name == deploymentName:
            return (True, deployment)
    
    return (False, None)
    

def is_daemonset_exists_in_cluster(dsName):
    
    dsList = (kubernetes.client.AppsV1Api().list_daemon_set_for_all_namespaces().items)
    
    for ds in dsList:
        if ds.metadata.name == dsName:
            return (True, ds)
    
    return (False, None)    

def is_service_exists_in_cluster(serviceName):
    
    servicesList = kubernetes.client.CoreV1Api().list_service_for_all_namespaces().items

    for service in servicesList:
        if service.metadata.name.startswith(serviceName):
            return (True, service)
    
    return (False, None)

        