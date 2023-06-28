from kubernetes import client

from hardeneks.rules import Rule, Result
from hardeneks.resources import Resources
from hardeneks import helpers

class check_metrics_server_is_running(Rule):
    _type = "cluster_wide"
    pillar = "reliability"
    section = "applications"
    message = "Run Kubernetes Metrics Server"
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#run-kubernetes-metrics-server"

    def check(self, resources: Resources):
        
        (Status, serviceData) = helpers.is_service_exists_in_cluster("metrics-server")
        
        self.result = Result(status=Status, resource_type="Service")
        

class check_vertical_pod_autoscaler_exists(Rule):
    _type = "cluster_wide"
    pillar = "reliability"
    section = "applications"
    message = "Vertical pod autoscaler is not deployed."
    url = "https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#run-kubernetes-metrics-server"

    def check(self, resources: Resources):


        (Status, deploymentData) = helpers.is_deployment_exists_in_namespace("vpa-recommender", "kube-system")
        self.result = Result(status=Status, resource_type="Deployment")
