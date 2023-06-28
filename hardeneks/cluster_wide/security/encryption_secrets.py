from ...resources import Resources
from hardeneks.rules import Rule, Result
import boto3
import pprint
from hardeneks import helpers

class use_encryption_with_ebs(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "encryption_secrets"
    message = "Encrypt data at rest"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/data/#encryption-at-rest"

    def check(self, resources: Resources):
        offenders = []

        for storage_class in resources.storage_classes:
            if storage_class.provisioner == "ebs.csi.aws.com":
                encrypted = storage_class.parameters.get("encrypted")
                #print(encrypted)
                if not encrypted:
                    offenders.append(storage_class)
                elif encrypted == "false":
                    offenders.append(storage_class)

        if offenders:
            self.result = Result(
                status=False,
                resource_type="StorageClass",
                resources=[i.metadata.name for i in offenders],
            )
        else:
            self.result = Result(status=True, resource_type="StorageClass")

class use_encryption_with_efs(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "encryption_secrets"
    message = "EFS Persistent volumes should have tls mount option."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/data/#encryption-at-rest"

    def check(self, resources: Resources):

        offenders = []
        Info = "All EFS PVs have tls in the mount option"

        for persistent_volume in resources.persistent_volumes:
            csi = persistent_volume.spec.csi
            if csi and csi.driver == "efs.csi.aws.com":
                pv = persistent_volume.metadata.name
                mount_options = persistent_volume.spec.mount_options
                #print("name={} mount_options={}".format(pv, mount_options))
                if not mount_options:
                    offenders.append(pv)
                else:
                    if "tls" not in mount_options:
                        offenders.append(pv)

        if offenders:
            Info = "EFS PVs without tls in the mount option " + " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="PersistentVolume",
                resources=offenders,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="PersistentVolume", info=Info)

class use_efs_access_points(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "encryption_secrets"
    message = "Use EFS access points to simplify access to shared datasets"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/data/#use-efs-access-points-to-simplify-access-to-shared-datasets"

    def check(self, resources: Resources):

        offenders = []
        Info = "All EFS PVs have access points"

        for persistent_volume in resources.persistent_volumes:
            csi = persistent_volume.spec.csi
            if csi and csi.driver == "efs.csi.aws.com":
                if "::" not in csi.volume_handle:
                    offenders.append(persistent_volume.metadata.name)

        

        if offenders:
            Info = "EFS PVs without access points " + " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="PersistentVolume",
                resources=offenders,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="PersistentVolume", info=Info)
            

class rotate_cmk_for_eks_envelope_encryption(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "encryption_secrets"
    message = "Rotate KMS CMK for KMS Envelope Encryption of K8s Secrets"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/data/#use-efs-access-points-to-simplify-access-to-shared-datasets"


    def check(self, resources: Resources):
        Status = False
        Info = "EKS Envelope Encryption is not Enabled"
        
        
        kmsclient = boto3.client('kms')
        eksclient = boto3.client("eks", region_name=resources.region)
        
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)        
        #print(pprint.pformat(cluster_metadata, indent=4))
        
        is_envelope_encryption_enabled = False
        
        #print(cluster_metadata["cluster"].keys())
        if 'encryptionConfig' in cluster_metadata["cluster"].keys():
            for config in cluster_metadata["cluster"]["encryptionConfig"]:
                #print(config)
                key_arn =  config['provider']['keyArn']
                #print(key_arn)
                if 'secrets' in config['resources'] and key_arn:
                    is_envelope_encryption_enabled = True
                    
            if is_envelope_encryption_enabled:
                response = kmsclient.get_key_rotation_status(KeyId=key_arn)
                #print(pprint.pformat(response, indent=4))
                is_key_rotation_enabled = response['KeyRotationEnabled']
                if is_key_rotation_enabled:
                    Status = True
                    Info = "EKS Envelope Encryption is Enabled and Key Rotation is Enabled"
                else:
                    Info = "EKS Envelope Encryption is Enabled but Key Rotaion is Disabled"         
 
        self.result = Result(status=Status, resource_type="EKS Envelope Encryption", info=Info)
        
        
class use_external_secret_provider_with_aws_secret_manager(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "encryption_secrets"
    message = "Use an external secrets provider"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/data/#use-an-external-secrets-provider"

    def check(self, resources: Resources):
        Status = False
        Info = ""
        
        (ret1, serviceData) = helpers.is_daemonset_exists_in_cluster("secrets-provider-aws-secrets-store-csi-driver-provider-aws")
        if ret1:
            Info += "ASCP is deployed"
        else:
            Info += "ASCP is not deployed"
        
        (ret2, serviceData) = helpers.is_daemonset_exists_in_cluster("csi-secrets-store-secrets-store-csi-driver")
        
        if ret2:
            Info += " Secrets CSI Driver is deployed"
        else:
            Info += " Secrets CSI Driver is not deployed"
            
        #print("ret1={} ret2={}".format(ret1,ret2))
        if ret1 and ret2:
            Status = True
    

        self.result = Result(
            status=Status,
            resource_type="Service",
            info=Info,
        )
        