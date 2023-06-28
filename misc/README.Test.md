# awseks
This contains various example codes for Amazon EKS

test
 
text for the bash command

```bash

python3 -m venv /tmp/.venv
source /tmp/.venv/bin/activate
cd hardeneks

pip install hardeneks
hardeneks



python3 -m venv /tmp/.venv1

source /tmp/.venv1/bin/activate
cd hardeneks

pip install hardeneks
hardeneks

hardeneks
hardeneks  --pillars cluster_data,security  --export-html report.html
hardeneks  --pillars cluster_data,security  --export-html report.html

hardeneks --only_cluster_level_rules

hardeneks --only_namespace_level_rules

hardeneks --namespace default,kubecost --pillars reliability

hardeneks --pillars scalability  --only_cluster_level_rules

hardeneks --pillars security --sections iam --only_cluster_level_rules --rules restrict_access_to_instance_profile

hardeneks --pillars security --sections iam --namespaces default --only_namespace_level_rules --rules restrict_containers_run_as_privileged


hardeneks --pillars cluster_data,networking --only_cluster_level_rules
hardeneks --pillars security --only_cluster_level_rules

hardeneks --pillars security --sections iam,multi_tenancy --only_cluster_level_rules

hardeneks --pillars reliability --only_cluster_level_rules

hardeneks --pillars cluster_autoscaling --only_cluster_level_rules
hardeneks --pillars networking --only_cluster_level_rules

hardeneks --pillars security --only_namespace_level_rules
hardeneks --pillars reliability --only_namespace_level_rules --namespace default

hardeneks --pillars networking --only_namespace_level_rules --namespace default








hardeneks --namespace default,kubecost --pillars reliability --context arn:aws:eks:us-east-1:000474600478:cluster/eksworkshop-eksctl

hardeneks --namespace default,kubecost --pillars reliability --cluster eksworkshop-eksctl



hardeneks --config ./hardeneks/config-orig.yaml

hardeneks --config ./misc/config-orig.yaml

git clone git@github.com:dorukozturk/hardeneks.git
cd hardeneks
poetry install

poetry shell
pytest --cov=hardeneks tests/ --cov-report term-missing


hardeneks [OPTIONS]
Options:

--region TEXT: AWS region of the cluster. Ex: us-east-1
--context TEXT: K8s context
--cluster TEXT: EKS Cluster name
--namespace TEXT: Namespace to be checked (default is all namespaces)
--config TEXT: Path to a hardeneks config file
--insecure-skip-tls-verify: Skip TLS verification
--help: Show this message and exit.

hardeneks --config ./hardeneks/config.yaml --namespace default
hardeneks --config ./hardeneks/config.yaml --namespace default,cilium-test

hardeneks --config ./hardeneks/config.yaml --run_only_cluster_level_checks --pillars networking

hardeneks --config ./hardeneks/config.yaml --pillars networking
hardeneks --config ./hardeneks/config.yaml --pillars cluster_data
hardeneks  --pillars cluster_data  export-html report.html

hardeneks  --pillars cluster_data,security  --export-html report.html

cluster


hardeneks --config ./hardeneks/config.yaml --run_only_cluster_level_checks  --pillars security,reliability --debug

hardeneks --config ./hardeneks/config.yaml --run_only_cluster_level_checks  --pillars reliability --debug


hardeneks --config ./hardeneks/config.yaml --run_only_cluster_level_checks

hardeneks --config ./hardeneks/config.yaml --run_only_cluster_level_checks --context i-0d45e819f38a652ea@mgmt.us-east-1.eksctl.io

--context i-0d45e819f38a652ea@mgmt.us-east-1.eksctl.io


hardeneks --config ./hardeneks/config.yaml --run_only_cluster_level_checks --debug


hardeneks --config ./hardeneks/config.yaml --run_only_namespace_level_checks  --pillars security --debug
hardeneks --config ./hardeneks/config.yaml --run_only_namespace_level_checks  --pillars security,reliability --debug
hardeneks --config ./hardeneks/config.yaml --run_only_namespace_level_checks  --pillars reliability --debug
hardeneks --config ./hardeneks/config.yaml --run_only_namespace_level_checks  --pillars networking --debug
hardeneks --config ./hardeneks/config.yaml --run_only_namespace_level_checks  --pillars cluster-autoscaling --debug



hardeneks --config ./hardeneks/config-test.yaml --run_only_namespace_level_checks --namespace apps,apps-nginx



configure_pod_disruption_budget

utilize_pod_readiness_gates

Ensure Pods are Deregistered from Load Balancers before Termination
ensure_pods_deregist_from_LB_before_termination


hardeneks --config ./hardeneks/config-test.yaml  --context eksworkshop5

hardeneks --config ./hardeneks/config-test.yaml  --context eksworkshop3


check_any_cluster_autoscaler_exists

VPC and Subnet Considerations
vpc-and-subnet-considerations

networking

Consider Multi-AZ Deployment

Deploy VPC CNI Managed Add-On
deploy_vpc_cni_managed_add_on

Employ least privileged access to the IAM role

employ_least_privileged_access_to_the_IAM_role

aws iam list-role-policies --role-name eksctl-eksworkshop-eksctl-addon-iamserviceac-Role1-1Q1U2KKFIT78C
kubectl annotate pods

aws iam list-attached-role-policies --role-name eksctl-eksworkshop-eksctl-addon-iamserviceac-Role1-1Q1U2KKFIT78C
  
  
aws iam get-role-policy --role-name eksctl-eksworkshop-eksctl-addon-iamserviceac-Role1-1Q1U2KKFIT78C --policy-name k8s-asg-policy

aws iam get-role-policy --role-name eksctl-eksworkshop-eksctl-addon-iamserviceac-Role1-1Q1U2KKFIT78C --policy-name arn:aws:iam::000474600478:policy/k8s-asg-policy



Monitor IP Address Inventory

monitor_IP_adress_inventory


aws ec2 describe-instance-types     --instance-types m5.large
    
    
  
export AUTOSCALER_VERSION=1.24.0

kubectl -n kube-system \
    set image deployment.apps/cluster-autoscaler \
    cluster-autoscaler=us.gcr.io/k8s-artifacts-prod/autoscaling/cluster-autoscaler:v${AUTOSCALER_VERSION}


Use IP Target-Type Load Balancers
use_IP_target_type_load_balancers




```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```


text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```

text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```


text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```


text for the bash command

```bash

```
text for the bash command

```bash




```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```


text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```

text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```

text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```
text for the bash command

```bash

```


