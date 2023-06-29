from hardeneks.rules import Rule, Result
import kubernetes
import pprint
from hardeneks.resources import Resources
from hardeneks import helpers


class use_nodeLocal_DNSCache(Rule):
    
    _type = "cluster_wide"
    pillar = "reliability"
    section = "data_plane"
    message = "Use NodeLocal DNSCache"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/dataplane/#use-nodelocal-dnscache"

    
    def check(self, resources: Resources):        

        (ret1, dsData) = helpers.is_daemonset_exists_in_cluster("node-local-dns")
        if ret1:
            Info = "NodeLocal DNSCache is deployed"
            Status = True
        else:
            Info = "NodeLocal DNSCache is not deployed"
            Status = False
        

        self.result = Result(
            status=Status,
            resource_type="Daemonset",
            info=Info,
        )
        
        
       