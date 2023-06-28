from hardeneks.rules import Rule, Result
from hardeneks.resources import NamespacedResources


class use_encryption_with_aws_load_balancers(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "network_security"
    message = "Use encryption with AWS load balancers"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/network/#use-encryption-with-aws-load-balancers"

    def check(self, namespaced_resources: NamespacedResources):
        offenders = []
        for service in namespaced_resources.services:
            annotations = service.metadata.annotations
            if annotations:
                ssl_cert = (
                    "service.beta.kubernetes.io/aws-load-balancer-ssl-cert"
                    in annotations
                )
                ssl_cert_port = annotations.get(
                    "service.beta.kubernetes.io/aws-load-balancer-ssl-ports"
                )
                if not (ssl_cert and ssl_cert_port == "443"):
                    offenders.append(service.metadata.name)

        
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Service",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Service", namespace=namespaced_resources.namespace)
            