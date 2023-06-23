import boto3

from ...resources import Resources
from hardeneks.rules import Rule, Result


class check_logs_are_enabled(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "detective_controls"
    message = "Enable audit logs"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/detective/#enable-audit-logs"

    def check(self, resources: Resources):
        
        Status = False
        Info = ""
        client = boto3.client("eks", region_name=resources.region)
        cluster_metadata = client.describe_cluster(name=resources.cluster)
        
        clusterLoggingTypes = cluster_metadata["cluster"]["logging"]["clusterLogging"]
        
        #print("clusterLoggingTypes={}".format(clusterLoggingTypes))
        
        for logType in clusterLoggingTypes:
            if 'audit' in logType['types'] and logType['enabled'] == True:
                Status = True
                
            if logType['enabled'] == True:
                Info += " Logs Enabled : " + " ".join(logType['types'])
            else:   
                Info += " Logs Disabled : " + " ".join(logType['types'])
                
        self.result = Result(status=Status, resource_type="Log Configuration", info=Info)
 