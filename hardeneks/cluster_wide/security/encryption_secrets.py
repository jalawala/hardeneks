from ...resources import Resources
from hardeneks.rules import Rule, Result


class use_encryption_with_ebs(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "encryption_secrets"
    message = "EBS Storage Classes should have encryption parameter."
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
        Info = "All EFS PVs have have tls in the mount option"

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
    message = "EFS Persistent volumes should leverage access points."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/data/#use-efs-access-points-to-simplify-access-to-shared-datasets"

    def check(self, resources: Resources):

        offenders = []

        for persistent_volume in resources.persistent_volumes:
            csi = persistent_volume.spec.csi
            if csi and csi.driver == "efs.csi.aws.com":
                if "::" not in csi.volume_handle:
                    offenders.append(persistent_volume)

        self.result = Result(status=True, resource_type="PersistentVolume")

        if offenders:
            self.result = Result(
                status=False,
                resource_type="PersistentVolume",
                resources=[i.metadata.name for i in offenders],
            )
