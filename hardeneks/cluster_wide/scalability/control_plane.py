import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources
import boto3


class check_EKS_version(Rule):
    _type = "cluster_wide"
    pillar = "scalability"
    section = "control_plane"
    message = "EKS Version should be 1.27"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    def check(self, resources: Resources):
        
        eks_latest_version_str = "1.27"
        
        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        cluster_version_str = cluster_metadata["cluster"]["version"]
        current_version = int(cluster_version_str.split('.')[-1])
        latest_version = int(eks_latest_version_str.split('.')[-1])
        
        if current_version < latest_version:
            Status = False
            Info = "EKS Cluster Version {}. Upgrade to Latest Version {}".format(cluster_version_str, eks_latest_version_str)
        else:
            Status = True
            Info = "EKS Cluster Version {} is at Latest Version {}".format(cluster_version_str, eks_latest_version_str)            
            
        self.result = Result(status=Status, resource_type="EKS Cluster Version", info=Info)



#
# check_kubectl_compression
# checks all clusters in config for disable-compression flag set to true
# if any cluster does not have setting, it returns False
class check_kubectl_compression(Rule):
    _type = "cluster_wide"
    pillar = "scalability"
    section = "control_plane"
    message = "`disable-compression` in kubeconfig should equal True"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#disable-kubectl-compression"

    def check(self, resources: Resources):
        Status = False
        kubeconfig = helpers.get_kube_config()
        for cluster in kubeconfig.get("clusters", []):
            clusterName = cluster.get("name", "")
            if resources.cluster in clusterName:
                
                #print(cluster)
                #print(cluster['cluster'].keys())
                
                if 'disable-compression' in cluster['cluster'].keys():
                    disable_compression = cluster['cluster']['disable-compression']
                    if disable_compression == True:
                        Status = True
                    
                self.result = Result(status=Status, resource_type="Compression Setting")
                
                
