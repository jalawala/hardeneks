import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources


class check_EKS_version(Rule):
    _type = "cluster_wide"
    pillar = "scalability"
    section = "control_plane"
    message = "EKS Version Should be greater or equal to 1.27"
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    def check(self, resources: Resources):
        checkStatus = False
        client = kubernetes.client.VersionApi()
        version = client.get_code()
        minor = version.minor
        resources=f"{version.major}.{minor}"
        #print("version={} minor={} reg={} resources={}".format(version, minor, int(re.sub("[^0-9]", "", minor)), resources))
        Info = "EKS Version is " + resources
        if int(re.sub("[^0-9]", "", minor)) == 27:
            checkStatus = True
            
        self.result = Result(status=checkStatus, resource_type="EKS Cluster Version", info=Info)



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
                
                
