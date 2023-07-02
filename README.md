# Hardeneks

[![PyPI version](https://badge.fury.io/py/hardeneks.svg)](https://badge.fury.io/py/hardeneks)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/hardeneks.svg)](https://pypi.python.org/pypi/hardeneks/)
[![Python package](https://github.com/aws-samples/hardeneks/actions/workflows/ci.yaml/badge.svg)](https://github.com/aws-samples/hardeneks/actions/workflows/ci.yaml)
[![Downloads](https://pepy.tech/badge/hardeneks)](https://pepy.tech/project/hardeneks)


Runs checks to see if an EKS cluster follows [EKS Best Practices](https://aws.github.io/aws-eks-best-practices/).

**Quick Start**:

```
python3 -m venv /tmp/.venv
source /tmp/.venv/bin/activate
pip install hardeneks
hardeneks
```

**Usage**:

To check all rules for the default kube context

```console
hardeneks
```

To check all rules for a specific cluster using context name 

```console
hardeneks --context <context name>
```
To check all rules for a specific cluster using cluster name 

```console
hardeneks --cluster <cluster name>
```
To check all rules at the cluster level

```console
hardeneks --only_cluster_level_rules
```
To check all rules at the namespace level

```console
hardeneks --only_namespace_level_rules
```
To check all rules for a specific list of pillars (valid values : cluster_data,security,reliability,scalability,cluster_autoscaling,networking

```console
hardeneks --pillars <pillar name1>,<pillar name2> ...
```

To check all rules for a specific list of secttions for a given pillar (for valid values of sections. refer to config.yaml)

```console
hardeneks --pillars <pillar name1> --sections <section name1>,<section name2> ...
```

To check only a specific list of rules for a sectio and pillar (for valid values of rules. refer to config.yaml)

```console
hardeneks --pillars <pillar name1> --sections <section name1> --rules <rule id1>,<rule id2> ...
```

To export output report to an html file

```console
hardeneks --export_html <file_name>
```

**Options**:

* `--region TEXT`: AWS region of the cluster. Ex: us-east-1
* `--context TEXT`: K8s context
* `--cluster TEXT`: EKS Cluster name
* `--namespace TEXT`: Namespace to be checked (default is all namespaces)
* `--config TEXT`: Path to a hardeneks config file
* `--pillars TEXT`: Specific list of pillars to harden. Default is all pillars.
* `--sections TEXT`: Specific list of sections for a given pillar to harden. Default is all sections. --pillars option must be used specifying only one pillar
* `--rules TEXT`: Specific list of rules to harden. Default is all rules. --pillars, --sections and one of options (--only_cluster_level_rules or --only_namespace_level_rules) must be set
* `--only_cluster_level_rules`: Check against only cluster_wide rules in the config.yamls
* `--only_namespace_level_rules`: Check against only namespace_based rules in the config.yamls 
* `--export-txt TEXT`: Export the report in txt format
* `--export-html TEXT`: Export the report in html format
* `--export-json TEXT`: Export the report in json format
* `--insecure-skip-tls-verify`: Skip TLS verification
* `--help`: Show this message and exit.


- <b>K8S_CONTEXT<b> 
  
    You can get the contexts by running:
    ```
    kubectl config get-contexts
    ```
    or get the current context by running:
    ```
    kubectl config current-context
    ```

- <b>CLUSTER_NAME<b>
  
    You can get the cluster names by running:
    ```
    aws eks list-clusters --region us-east-1
    ```
  
**Configuration File**:

Default behavior is to run all the checks. If you want to provide your own config file to specify list of rules to run, you can use the --config flag.You can also add namespaces to be skipped. 

Following is a sample config file:

```yaml
---
ignore-namespaces:
  - kube-node-lease
  - kube-public
  - kube-system
  - kube-apiserver
  - karpenter
  - kubecost
  - external-dns
  - argocd
  - aws-for-fluent-bit
  - amazon-cloudwatch
  - vpa
rules: 
  cluster_wide:
    cluster_data:
      cluster_data:
        - get_EKS_version
        - get_EKS_cluster_endpoint_url
        - get_cluster_vpc_subnets
        - get_available_free_ips_in_vpc
        - get_cluster_size_details
        - get_nodegroups_provisioners
        - get_fargate_profiles
    security:
      iam:
        - disable_anonymous_access_for_cluster_roles
        - cluster_endpoint_public_and_private_mode
        - check_aws_node_daemonset_service_account
        - use_imds_v2
        - restrict_access_to_instance_profile
        - restrict_wildcard_for_cluster_roles
        - do_not_assign_system_masters_for_normal_users
        - use_iam_role_for_multiple_iam_users
        - create_cluster_with_dedicated_iam_role
      multi_tenancy:
        - ensure_namespace_quotas_exist
      detective_controls:
        - check_logs_are_enabled
      network_security:
        - check_vpc_flow_logs
        - check_awspca_exists
        - check_default_deny_policy_exists
      encryption_secrets:
        - use_encryption_with_ebs
        - use_encryption_with_efs
        - use_efs_access_points
        - rotate_cmk_for_eks_envelope_encryption
        - use_external_secret_provider_with_aws_secret_manager
      infrastructure_security:
        - deploy_workers_onto_private_subnets
        - make_sure_inspector_is_enabled
        - use_OS_optimized_for_running_containers
      pod_security:
        - ensure_namespace_psa_exist
      regulatory_compliance:
        - policy_as_code        
      image_security:
        - use_immutable_tags_with_ecr
        - scan_images_for_vulnerabilities
        - check_iam_iam_policies_for_ecr_repositories
        - consider_using_ecr_private_endpoints
        - check_endpoint_policies_for_ecr
        - implement_lifecycle_policies_for_ecr
    reliability:
      applications:
        - check_metrics_server_is_running
        - check_vertical_pod_autoscaler_exists
      data_plane:
        - use_nodeLocal_DNSCache     
    scalability:
      control_plane:
        - check_EKS_version
        - check_kubectl_compression
    cluster_autoscaling:
      cluster_autoscaler:
        - check_any_cluster_autoscaler_exists
        - ensure_cluster_autoscaler_and_cluster_versions_match
        - ensure_cluster_autoscaler_has_autodiscovery_mode
        - use_separate_iam_role_for_cluster_autoscaler
        - employ_least_privileged_access_cluster_autoscaler_role
        - use_managed_nodegroups
        - ensure_cluster_autoscaler_has_three_replicas
        - ensure_uniform_instance_types_in_nodegroups
        - configure_node_groups_for_mixedinstances
        - configure_node_groups_for_ha
    networking:
      vpc_subnets:
        - cluster_endpoint_public_and_private_mode
      vpc-cni:
        - deploy_vpc_cni_managed_add_on
        - use_separate_iam_role_for_cni
        #- monitor_IP_adress_inventory
        - use_small_dedicated_cluster_subnets
      prefix_mode:
        - use_prefix_mode
      load-balancing:
        - deploy_aws_lb_controller         
  namespace_based:
    security: 
      iam:
        - disable_anonymous_access_for_roles
        - restrict_wildcard_for_roles
        - disable_service_account_token_mounts
        - disable_run_as_root_user
        - restrict_containers_run_as_privileged
        - use_dedicated_service_accounts_for_each_deployment
        - use_dedicated_service_accounts_for_each_stateful_set
        - use_dedicated_service_accounts_for_each_daemon_set
      pod_security:
        - disallow_container_socket_mount
        - disallow_host_path_or_make_it_read_only
        - set_requests_limits_for_containers
        - disallow_privilege_escalation
        - check_read_only_root_file_system
        - disable_service_discovery
      network_security:
        - use_encryption_with_aws_load_balancers
      encryption_secrets:
        - disallow_secrets_from_env_vars    
      runtime_security:
        - disallow_linux_capabilities
    reliability:
      applications:
        - check_horizontal_pod_autoscaling_exists
        - schedule_replicas_across_nodes
        - run_multiple_replicas
        - avoid_running_singleton_pods
        - check_readiness_probes
        - check_liveness_probes
        - check_pod_disruption_budgets
      data_plane:
        - limit_container_resource_usage_within_namespace     
    networking:
      load-balancing:
        - use_ip_target_type_load_balancers
        - use_ip_target_type_ingresses
        - use_pod_readiness_gate
```

**RBAC**:
 
In order to run hardeneks we need to have some permissions both on AWS side and k8s side.

Minimal IAM role policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "eks:ListClusters",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "eks:DescribeCluster",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ecr:DescribeRepositories",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "inspector2:BatchGetAccountStatus",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeFlowLogs",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        }
    ]
}
```

Minimal ClusterRole:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hardeneks-runner
rules:
- apiGroups: [""]
  resources: ["namespaces", "resourcequotas", "persistentvolumes", "pods", "services"]
  verbs: ["list"]
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterroles", "clusterrolebindings", "roles", "rolebindings"]
  verbs: ["list"]
- apiGroups: ["networking.k8s.io"]
  resources: ["networkpolicies"]
  verbs: ["list"]
- apiGroups: ["storage.k8s.io"]
  resources: ["storageclasses"]
  verbs: ["list"]
- apiGroups: ["apps"]
  resources: ["deployments", "daemonsets", "statefulsets"]
  verbs: ["list", "get"]
- apiGroups: ["autoscaling"]
  resources: ["horizontalpodautoscalers"]
  verbs: ["list"]
```

## For Developers

**Prerequisites**:

* This cli uses poetry. Follow instructions that are outlined [here](https://python-poetry.org/docs/) to install poetry.


**Installation**:

```console
git clone git@github.com:jalawala/hardeneks.git
cd hardeneks
poetry install
```

**Running Tests**:

```console
poetry shell
pytest --cov=hardeneks tests/ --cov-report term-missing
```
