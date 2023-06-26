from collections import Counter

from ...resources import NamespacedResources
from hardeneks.rules import Rule, Result


class disable_anonymous_access_for_roles(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Don't bind roles to anonymous or unauthenticated groups."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#review-and-revoke-unnecessary-anonymous-access"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        Info = "None of the roles bound to anonymous or unauthenticated groups."

        for role_binding in namespaced_resources.role_bindings:
            if role_binding.subjects:
                for subject in role_binding.subjects:
                    if (
                        subject.name == "system:unauthenticated"
                        or subject.name == "system:anonymous"
                    ):
                        offenders.append(role_binding.metadata.name)

        
        if offenders:
            Info = "RoleBinding with failed checks " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="RoleBinding",
                resources=offenders,
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="RoleBinding", namespace=namespaced_resources.namespace, info=Info)
        
        #print("self.result={}".format(self.result))
        

class restrict_wildcard_for_roles(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Roles should not have '*' in Verbs or Resources."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#employ-least-privileged-access-when-creating-rolebindings-and-clusterrolebindings"

    def check(self, namespaced_resources: NamespacedResources):
        offenders = []
        Info = "None of the roles have '*' in Verbs or Resources."

        if namespaced_resources.roles:
            for role in namespaced_resources.roles:
                name = role.metadata.name
                if role.rules:
                    for rule in role.rules:
                        if "*" in rule.verbs:
                            offenders.append(name)
                        if "*" in rule.resources:
                            offenders.append(name)

        
        if offenders:
            Info = "Roles with failed checks " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Role",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, 
            resource_type="Role", 
            namespace=namespaced_resources.namespace, 
            info = Info
            )

class disable_service_account_token_mounts(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Auto-mounting of Service Account tokens is not allowed."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#disable-auto-mounting-of-service-account-tokens"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        Info = "None of the pods have auto mounted SA"

        for pod in namespaced_resources.pods:
            #print(pod.spec.automount_service_account_token)
            #print(pod)
            if pod.spec.automount_service_account_token != False:
                offenders.append(pod.metadata.name)

        
        if offenders:
            Info = "Pods with auto mounted SA : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Pod",
                namespace=namespaced_resources.namespace,
                info =  Info
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace, info=Info)


class disable_run_as_root_user(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Running as root is not allowed."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#run-the-application-as-a-non-root-user"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        Info = "All pods run as non-root user"

        for pod in namespaced_resources.pods:
            security_context = pod.spec.security_context
            if (
                not security_context.run_as_group
                and not security_context.run_as_user
            ):
                offenders.append(pod.metadata.name)
        
        if offenders:
            Info = "Pods running as root : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Pod",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace, info=Info)

class use_dedicated_service_accounts_for_each_deployment(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Don't share service accounts between Deployments."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#use-dedicated-service-accounts-for-each-application"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        Info = "Each deployment uses dedicated SA"

        count = Counter(
            [
                i.spec.template.spec.service_account_name
                for i in namespaced_resources.deployments
            ]
        )
        
        #print(count)
        
        repeated_service_accounts = {
            x: repeatcount for x, repeatcount in count.items() if repeatcount > 1
        }
        
        #print(repeated_service_accounts)

        if len(namespaced_resources.deployments) > 0:
            for k, v in repeated_service_accounts.items():
                for deployment in namespaced_resources.deployments:
                    if k == deployment.spec.template.spec.service_account_name:
                        offenders.append(deployment.metadata.name)
        else:
            Info = "There are no Deployments in the Namespace"
            

        if offenders:
            Info = "Deployments with common SA : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Deployment",
                namespace=namespaced_resources.namespace,
                info=Info
            )
        else:
            self.result = Result(status=True, resource_type="Deployment", namespace=namespaced_resources.namespace, info=Info)
            

class use_dedicated_service_accounts_for_each_stateful_set(
    Rule,
):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Don't share service accounts between StatefulSets."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#use-dedicated-service-accounts-for-each-application"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        Info = "Each StatefulSet uses dedicated SA"
        
        count = Counter(
            [
                i.spec.template.spec.service_account_name
                for i in namespaced_resources.stateful_sets
            ]
        )
        repeated_service_accounts = {
            x: repeatcount for x, repeatcount in count.items() if repeatcount > 1
        }

        if len(namespaced_resources.stateful_sets) > 0:
            for k, v in repeated_service_accounts.items():
                for deployment in namespaced_resources.stateful_sets:
                    if k == deployment.spec.template.spec.service_account_name:
                        offenders.append(deployment.metadata.name)
        else:
            Info = "There are no StatefulSets in the Namespace"
        
        if offenders:
            Info = "StatefulSets with common SA : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="StatefulSet",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="StatefulSet", namespace=namespaced_resources.namespace, info=Info)

class use_dedicated_service_accounts_for_each_daemon_set(
    Rule,
):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Don't share service accounts between DaemonSets."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#use-dedicated-service-accounts-for-each-application"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        
        Info = "Each DaemonSet uses dedicated SA"

        count = Counter(
            [
                i.spec.template.spec.service_account_name
                for i in namespaced_resources.daemon_sets
            ]
        )
        repeated_service_accounts = {
            x: repeatcount for x, repeatcount in count.items() if repeatcount > 1
        }

        if len(namespaced_resources.daemon_sets) > 0:            
            for k, v in repeated_service_accounts.items():
                for daemon_set in namespaced_resources.daemon_sets:
                    if k == daemon_set.spec.template.spec.service_account_name:
                        offenders.append(daemon_set.metadata.name)

        else:
            Info = "There are no DaemonSets in the Namespace"
            
        if offenders:
            Info = "DaemonSets with common SA : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="DaemonSet",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="DaemonSet",namespace=namespaced_resources.namespace, info=Info)
            