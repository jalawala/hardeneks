import boto3
import json

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
        guardduty_client = boto3.client('guardduty', region_name=resources.region       )
        
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
        
        response = guardduty_client.list_detectors()
        if 'DetectorIds' in response.keys():
            detector_id = response['DetectorIds'][0]
            
        #print("detector_id={}".format(detector_id))
        
        # Check if EKS protection is enabled
        response = guardduty_client.get_detector(DetectorId=detector_id)
        
        
        #json_formatted_str = json.dumps(response, indent=4)
        #print(json_formatted_str)
        
        guardDutyEKSAudiLogStatus = response['DataSources']['Kubernetes']['AuditLogs']['Status']
        
        if guardDutyEKSAudiLogStatus == 'ENABLED':
            Status  = True
        
        Info += " guardDutyEKSAudiLogStatus = {}".format(guardDutyEKSAudiLogStatus)     
                
        self.result = Result(status=Status, resource_type="Log Configuration", info=Info)
 