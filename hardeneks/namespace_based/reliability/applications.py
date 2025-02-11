from ...resources import NamespacedResources
from hardeneks.rules import Rule, Result
import kubernetes
import pprint

class avoid_running_singleton_pods(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Avoid running singleton Pods"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#avoid-running-singleton-pods"

    def check(self, namespaced_resources: NamespacedResources):
        offenders = []
        for pod in namespaced_resources.pods:
            
            owner = pod.metadata.owner_references
            #print(owner)
            if not owner:
                offenders.append(pod.metadata.name)
        
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Pod",namespace=namespaced_resources.namespace)

class run_multiple_replicas(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Run multiple replicas"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#run-multiple-replicas"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        for deployment in namespaced_resources.deployments:
            if deployment.spec.replicas < 2:
                offenders.append(deployment.metadata.name)

        
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Deployment",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Deployment", namespace=namespaced_resources.namespace)

class schedule_replicas_across_nodes(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Schedule replicas across nodes"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#schedule-replicas-across-nodes"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        for deployment in namespaced_resources.deployments:
            spread = deployment.spec.template.spec.topology_spread_constraints
            if not spread:
                offenders.append(deployment.metadata.name)
            else:
                #print(spread)
                topology_keys = set([i.topology_key for i in spread])
                #print(topology_keys)
                if not set(["topology.kubernetes.io/zone"]).issubset(
                    topology_keys
                ):
                    offenders.append(deployment.metadata.name)

        
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Deployment",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Deployment", namespace=namespaced_resources.namespace)

class check_horizontal_pod_autoscaling_exists(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Deploy horizontal pod autoscaler for deployments."
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#horizontal-pod-autoscaler-hpa"

    
    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        hpas = [
            i.spec.scale_target_ref.name for i in namespaced_resources.hpas
        ]

        for deployment in namespaced_resources.deployments:
            if deployment.metadata.name not in hpas:
                offenders.append(deployment.metadata.name)

        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Deployment",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Deployment", namespace=namespaced_resources.namespace)
            

class check_readiness_probes(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Define readiness probes for pods."
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#use-readiness-probe-to-detect-partial-unavailability"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        for pod in namespaced_resources.pods:
            for container in pod.spec.containers:
                if not container.readiness_probe:
                    offenders.append(pod.metadata.name)
                    
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace)
            

class check_liveness_probes(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Define liveness probes for pods."
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#use-liveness-probe-to-remove-unhealthy-pods"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        for pod in namespaced_resources.pods:
            for container in pod.spec.containers:
                if not container.liveness_probe:
                    offenders.append(pod.metadata.name)

        
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace)
            
class check_pod_disruption_budgets(Rule):
    _type = "namespace_based"
    pillar = "reliability"
    section = "applications"
    message = "Protect critical workload with Pod Disruption Budgets"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#recommendations_2"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []


        pod_disruption_budgets = kubernetes.client.PolicyV1Api().list_namespaced_pod_disruption_budget(namespace=namespaced_resources.namespace).items
        #print(pprint.pformat(pod_disruption_budgets, indent=4)) 
    
        
        pdb_labels_list = []
       # Print the pod disruption budgets
        for pdb in pod_disruption_budgets:
            match_labels = pdb.spec.selector.match_labels
            pdb_labels_list.append(match_labels)

        
        #print(pdb_labels_list)
        for deployment in namespaced_resources.deployments:
            match_labels = deployment.spec.selector.match_labels
            if match_labels not in pdb_labels_list:
                offenders.append(deployment.metadata.name)
                #print("{} matches".format(match_labels))
        
            
            #print(deployment.metadata.name, match_labels)
        

        
        if offenders:
            Info = "Deployments without PDB : " + " ".join(offenders)
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            Info = "All deployments have PDBs "
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace, info=Info)
                        