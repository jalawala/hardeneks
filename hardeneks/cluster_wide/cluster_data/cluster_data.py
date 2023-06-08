import re
import kubernetes
from hardeneks import helpers
from hardeneks.rules import Rule, Result
from hardeneks import Resources

class check_EKS_version(Rule):
    _type = "cluster_wide"
    pillar = "scalability"
    section = "control_plane"
    message = "EKS Version Should be greater or equal to 1.24."
    url = "https://aws.github.io/aws-eks-best-practices/scalability/docs/control-plane/#use-eks-124-or-above"

    def check(self, resources: Resources):
        client = kubernetes.client.VersionApi()
        version = client.get_code()
        minor = version.minor

        if int(re.sub("[^0-9]", "", minor)) < 24:
            self.result = Result(
                status=False,
                resources=f"{version.major}.{minor}",
                resource_type="Cluster Version",
            )
        else:
            self.result = Result(status=True, resource_type="Cluster Version")
        
        print("result={}".format(self.result))    
            
