import kubernetes

from ...resources import Resources
from hardeneks.rules import Rule, Result


class ensure_namespace_psa_exist(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "pod_security"
    message = "Use multiple Pod Security Admission (PSA) modes for a better user experience"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#pod-security-standards-pss-and-pod-security-admission-psa"

    def check(self, resources: Resources):
        offenders = []
        Info = "All Namespaces have PSA labels"

        namespaces = kubernetes.client.CoreV1Api().list_namespace().items
        psa_labels = [
            "pod-security.kubernetes.io/enforce",
            "pod-security.kubernetes.io/warn",
            "pod-security.kubernetes.io/audit",
        ]

        for namespace in namespaces:
            if namespace.metadata.name in resources.namespaces:
                labels = namespace.metadata.labels.keys()
                if not any(i in labels for i in psa_labels):
                    offenders.append(namespace.metadata.name)

        if offenders:
            Info = "Namespaces without PSA labels " + " ".join(offenders)
            self.result = Result(
                status=False, resource_type="Namespace", info=Info)
        else:
            self.result = Result(status=True, resource_type="Namespace", info=Info)