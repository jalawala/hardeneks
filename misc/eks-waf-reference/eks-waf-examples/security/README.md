# security
This contains various example codes for Amazon EKS

# cluster_wide
## iam

### disable_anonymous_access_for_cluster_roles

```bash
cd ~/environment
git clone https://github.com/FairwindsOps/rbac-lookup.git
cd ~/environment/rbac-lookup
cd rbac-lookup
make


```
text for the bash command

```bash
jp:~/environment/rbac-lookup (master) $ ./rbac-lookup 
SUBJECT                                                 SCOPE                           ROLE
cert-manager:cert-manager                               kube-system                     Role/cert-manager:leaderelection
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-approve:cert-manager-io
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-certificates
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-certificatesigningrequests
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-challenges
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-clusterissuers
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-ingress-shim
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-issuers
cert-manager:cert-manager                               cluster-wide                    ClusterRole/cert-manager-controller-orders
cert-manager:cert-manager-cainjector                    kube-system                     Role/cert-manager-cainjector:leaderelection
cert-manager:cert-manager-cainjector                    cluster-wide                    ClusterRole/cert-manager-cainjector
cert-manager:cert-manager-webhook                       cert-manager                    Role/cert-manager-webhook:dynamic-serving
cert-manager:cert-manager-webhook                       cluster-wide                    ClusterRole/cert-manager-webhook:subjectaccessreviews
eks:addon-manager                                       kube-system                     Role/eks:addon-manager
eks:addon-manager                                       opentelemetry-operator-system   Role/eks:addon-manager
eks:addon-manager                                       cluster-wide                    ClusterRole/cluster-admin
eks:addon-manager                                       cluster-wide                    ClusterRole/eks:addon-manager
eks:addon-manager                                       cluster-wide                    ClusterRole/eks:addon-manager-otel
eks:authenticator                                       kube-system                     Role/eks:authenticator
eks:az-poller                                           kube-system                     Role/eks:az-poller
eks:az-poller                                           cluster-wide                    ClusterRole/eks:az-poller
eks:certificate-controller                              kube-system                     Role/eks:certificate-controller
eks:certificate-controller                              cluster-wide                    ClusterRole/system:controller:certificate-controller
eks:certificate-controller                              cluster-wide                    ClusterRole/eks:certificate-controller-approver
eks:certificate-controller                              cluster-wide                    ClusterRole/eks:certificate-controller-signer
eks:cloud-controller-manager                            kube-system                     Role/extension-apiserver-authentication-reader
eks:cloud-controller-manager                            cluster-wide                    ClusterRole/eks:cloud-controller-manager
eks:cluster-event-watcher                               cluster-wide                    ClusterRole/eks:cluster-event-watcher
eks:fargate-manager                                     kube-system                     Role/eks:fargate-manager
eks:fargate-manager                                     cluster-wide                    ClusterRole/eks:fargate-manager
eks:fargate-scheduler                                   cluster-wide                    ClusterRole/eks:fargate-scheduler
eks:k8s-metrics                                         kube-system                     Role/eks:k8s-metrics
eks:k8s-metrics                                         cluster-wide                    ClusterRole/eks:k8s-metrics
eks:kube-proxy-windows                                  cluster-wide                    ClusterRole/system:node-proxier
eks:node-manager                                        kube-system                     Role/eks:node-manager
eks:node-manager                                        cluster-wide                    ClusterRole/eks:node-manager
eks:nodewatcher                                         cluster-wide                    ClusterRole/eks:nodewatcher
eks:pod-identity-mutating-webhook                       cluster-wide                    ClusterRole/eks:pod-identity-mutating-webhook
eks:vpc-resource-controller                             kube-system                     Role/eks-vpc-resource-controller-role
eks:vpc-resource-controller                             cluster-wide                    ClusterRole/vpc-resource-controller-role
kube-system:attachdetach-controller                     cluster-wide                    ClusterRole/system:controller:attachdetach-controller
kube-system:aws-load-balancer-controller                kube-system                     Role/aws-load-balancer-controller-leader-election-role
kube-system:aws-load-balancer-controller                cluster-wide                    ClusterRole/aws-load-balancer-controller-role
kube-system:aws-node                                    cluster-wide                    ClusterRole/aws-node
kube-system:bootstrap-signer                            kube-public                     Role/system:controller:bootstrap-signer
kube-system:bootstrap-signer                            kube-system                     Role/system:controller:bootstrap-signer
kube-system:certificate-controller                      cluster-wide                    ClusterRole/system:controller:certificate-controller
kube-system:cloud-provider                              kube-system                     Role/system:controller:cloud-provider
kube-system:clusterrole-aggregation-controller          cluster-wide                    ClusterRole/system:controller:clusterrole-aggregation-controller
kube-system:coredns                                     cluster-wide                    ClusterRole/system:coredns
kube-system:cronjob-controller                          cluster-wide                    ClusterRole/system:controller:cronjob-controller
kube-system:daemon-set-controller                       cluster-wide                    ClusterRole/system:controller:daemon-set-controller
kube-system:deployment-controller                       cluster-wide                    ClusterRole/system:controller:deployment-controller
kube-system:disruption-controller                       cluster-wide                    ClusterRole/system:controller:disruption-controller
kube-system:eks-vpc-resource-controller                 kube-system                     Role/eks-vpc-resource-controller-role
kube-system:eks-vpc-resource-controller                 cluster-wide                    ClusterRole/vpc-resource-controller-role
kube-system:endpoint-controller                         cluster-wide                    ClusterRole/system:controller:endpoint-controller
kube-system:endpointslice-controller                    cluster-wide                    ClusterRole/system:controller:endpointslice-controller
kube-system:endpointslicemirroring-controller           cluster-wide                    ClusterRole/system:controller:endpointslicemirroring-controller
kube-system:ephemeral-volume-controller                 cluster-wide                    ClusterRole/system:controller:ephemeral-volume-controller
kube-system:expand-controller                           cluster-wide                    ClusterRole/system:controller:expand-controller
kube-system:generic-garbage-collector                   cluster-wide                    ClusterRole/system:controller:generic-garbage-collector
kube-system:horizontal-pod-autoscaler                   cluster-wide                    ClusterRole/system:controller:horizontal-pod-autoscaler
kube-system:job-controller                              cluster-wide                    ClusterRole/system:controller:job-controller
kube-system:kube-controller-manager                     kube-system                     Role/system::leader-locking-kube-controller-manager
kube-system:kube-dns                                    cluster-wide                    ClusterRole/system:kube-dns
kube-system:kube-proxy                                  cluster-wide                    ClusterRole/system:node-proxier
kube-system:kube-scheduler                              kube-system                     Role/system::leader-locking-kube-scheduler
kube-system:namespace-controller                        cluster-wide                    ClusterRole/system:controller:namespace-controller
kube-system:node-controller                             cluster-wide                    ClusterRole/system:controller:node-controller
kube-system:persistent-volume-binder                    cluster-wide                    ClusterRole/system:controller:persistent-volume-binder
kube-system:pod-garbage-collector                       cluster-wide                    ClusterRole/system:controller:pod-garbage-collector
kube-system:pv-protection-controller                    cluster-wide                    ClusterRole/system:controller:pv-protection-controller
kube-system:pvc-protection-controller                   cluster-wide                    ClusterRole/system:controller:pvc-protection-controller
kube-system:replicaset-controller                       cluster-wide                    ClusterRole/system:controller:replicaset-controller
kube-system:replication-controller                      cluster-wide                    ClusterRole/system:controller:replication-controller
kube-system:resourcequota-controller                    cluster-wide                    ClusterRole/system:controller:resourcequota-controller
kube-system:root-ca-cert-publisher                      cluster-wide                    ClusterRole/system:controller:root-ca-cert-publisher
kube-system:route-controller                            cluster-wide                    ClusterRole/system:controller:route-controller
kube-system:service-account-controller                  cluster-wide                    ClusterRole/system:controller:service-account-controller
kube-system:service-controller                          cluster-wide                    ClusterRole/system:controller:service-controller
kube-system:statefulset-controller                      cluster-wide                    ClusterRole/system:controller:statefulset-controller
kube-system:tagging-controller                          cluster-wide                    ClusterRole/eks:tagging-controller
kube-system:token-cleaner                               kube-system                     Role/system:controller:token-cleaner
kube-system:ttl-after-finished-controller               cluster-wide                    ClusterRole/system:controller:ttl-after-finished-controller
kube-system:ttl-controller                              cluster-wide                    ClusterRole/system:controller:ttl-controller
opentelemetry-operator-system:opentelemetry-operator    opentelemetry-operator-system   Role/opentelemetry-operator-leader-election
opentelemetry-operator-system:opentelemetry-operator    cluster-wide                    ClusterRole/opentelemetry-operator-manager
opentelemetry-operator-system:opentelemetry-operator    cluster-wide                    ClusterRole/opentelemetry-operator-proxy
prometheus:amp-irsa-role                                cluster-wide                    ClusterRole/otel-prometheus-role
sample:external-dns                                     cluster-wide                    ClusterRole/external-dns
system:authenticated                                    cluster-wide                    ClusterRole/system:basic-user
system:authenticated                                    cluster-wide                    ClusterRole/system:discovery
system:authenticated                                    cluster-wide                    ClusterRole/system:public-info-viewer
system:bootstrappers                                    cluster-wide                    ClusterRole/eks:node-bootstrapper
system:kube-controller-manager                          kube-system                     Role/extension-apiserver-authentication-reader
system:kube-controller-manager                          kube-system                     Role/system::leader-locking-kube-controller-manager
system:kube-controller-manager                          cluster-wide                    ClusterRole/eks:cloud-provider-extraction-migration
system:kube-controller-manager                          cluster-wide                    ClusterRole/system:kube-controller-manager
system:kube-proxy                                       cluster-wide                    ClusterRole/system:node-proxier
system:kube-scheduler                                   kube-system                     Role/extension-apiserver-authentication-reader
system:kube-scheduler                                   kube-system                     Role/system::leader-locking-kube-scheduler
system:kube-scheduler                                   cluster-wide                    ClusterRole/system:kube-scheduler
system:kube-scheduler                                   cluster-wide                    ClusterRole/system:volume-scheduler
system:masters                                          cluster-wide                    ClusterRole/cluster-admin
system:monitoring                                       cluster-wide                    ClusterRole/system:monitoring
system:node-proxier                                     cluster-wide                    ClusterRole/system:node-proxier
system:nodes                                            cluster-wide                    ClusterRole/eks:node-bootstrapper
system:serviceaccounts                                  cluster-wide                    ClusterRole/system:service-account-issuer-discovery
system:unauthenticated                                  cluster-wide                    ClusterRole/system:public-info-viewer


jp:~/environment/rbac-lookup (master) $ ./rbac-lookup | grep -P 'system:(anonymous)|(unauthenticated)'
system:unauthenticated                                  cluster-wide                    ClusterRole/system:public-info-viewer


kubectl get ClusterRoleBinding -o json | jq -r '.items[] | select(.subjects[]?.name =="system:unauthenticated") | select(.metadata.name != "system:public-info-viewer") | .metadata.name'

kubectl get ClusterRoleBinding -o json | jq -r '.items[] | select(.subjects[]?.name =="system:unauthenticated") | select(.metadata.name != "system:public-info-viewer") | del(.subjects[] | select(.name =="system:unauthenticated"))' | kubectl apply -f -

jp:~/environment/rbac-lookup (master) $ kubectl describe clusterrolebindings system:discovery
Name:         system:discovery
Labels:       kubernetes.io/bootstrapping=rbac-defaults
Annotations:  rbac.authorization.kubernetes.io/autoupdate: true
Role:
  Kind:  ClusterRole
  Name:  system:discovery
Subjects:
  Kind   Name                  Namespace
  ----   ----                  ---------
  Group  system:authenticated 
  
  
jp:~/environment/rbac-lookup (master) $ kubectl describe clusterrolebindings system:basic-user
Name:         system:basic-user
Labels:       kubernetes.io/bootstrapping=rbac-defaults
Annotations:  rbac.authorization.kubernetes.io/autoupdate: true
Role:
  Kind:  ClusterRole
  Name:  system:basic-user
Subjects:
  Kind   Name                  Namespace
  ----   ----                  ---------
  Group  system:authenticated
  
  

```
### cluster_endpoint_public_and_private_mode

```bash

export EKS_CLUSTER_NAME="eks126"
aws eks update-cluster-config --name $EKS_CLUSTER_NAME --resources-vpc-config endpointPublicAccess=true,endpointPrivateAccess=true,publicAccessCidrs="18.210.11.148/32"

{
    "update": {
        "id": "bedca6ae-2249-4586-bc9b-9b1114d49473",
        "status": "InProgress",
        "type": "EndpointAccessUpdate",
        "params": [
            {
                "type": "EndpointPublicAccess",
                "value": "true"
            },
            {
                "type": "EndpointPrivateAccess",
                "value": "true"
            },
            {
                "type": "PublicAccessCidrs",
                "value": "[\"18.210.11.148/32\"]"
            }
        ],
        "createdAt": "2023-06-22T13:12:50.179000+00:00",
        "errors": []
    }
}

```
### check_aws_node_daemonset_service_account


```bash
cd /home/ec2-user/environment
git clone https://github.com/aws/aws-eks-best-practices.git
cd aws-eks-best-practices/projects/enable-irsa/src


source /tmp/.venv/bin/activate


mkdir -p /tmp/irsa/


python3 -m venv /tmp/irsa/.venv

source /tmp/irsa/.venv/bin/activate

pip install --trusted-host pypi.python.org -r requirements.txt
pip install pip --upgrade
pip install pyopenssl --upgrade

export EKS_CLUSTER_NAME="eks126"
python main.py --cluster-name $EKS_CLUSTER_NAME --role-name eks_cni_irsa_role  --region us-east-1 --account 000474600478

Obtaining OIDC URL and thumbprint.
Creating a OIDC provider. This is privileged operation. Do you want to proceed (yes/no)? yes
The OIDC provider already exists
Creating IAM role.
Attaching CNI policy to role.
Patching aws-node ServiceAccount
Do you want to patch the aws-node Daemonset(Yes/No)? This will trigger a rolling restart of the networking plugin: Yes
Patching aws-node daemonset


(.venv) jp:~/environment/aws-eks-best-practices/projects/enable-irsa/src (master) $ kubectl get pod -n kube-system
NAME                                            READY   STATUS    RESTARTS     AGE
aws-load-balancer-controller-65d588d98b-bp5rf   1/1     Running   3 (9d ago)   22d
aws-load-balancer-controller-65d588d98b-fd4hb   1/1     Running   3 (9d ago)   22d
aws-node-m2qx2                                  1/1     Running   0            11s
aws-node-q89bd                                  1/1     Running   0            8s
aws-node-vkcz7                                  1/1     Running   0            15s
coredns-55fb5d545d-h6qjf                        1/1     Running   4 (9d ago)   38d
coredns-55fb5d545d-lj5zd                        1/1     Running   4 (9d ago)   38d
kube-proxy-8k29j                                1/1     Running   4 (9d ago)   30d
kube-proxy-gzc9k                                1/1     Running   4 (9d ago)   23d
kube-proxy-prh6c                                1/1     Running   4 (9d ago)   30d
(.venv) jp:~/environment/aws-eks-best-practices/projects/enable-irsa/src (master) $ kubectl -n kube-system describe sa aws-node
Name:                aws-node
Namespace:           kube-system
Labels:              app.kubernetes.io/instance=aws-vpc-cni
                     app.kubernetes.io/name=aws-node
                     app.kubernetes.io/version=v1.12.5
                     k8s-app=aws-node
Annotations:         eks.amazonaws.com/role-arn: arn:aws:iam::000474600478:role/eks_cni_irsa_role
Image pull secrets:  <none>
Mountable secrets:   <none>
Tokens:              <none>
Events:              <none>









```
### check_access_to_instance_profile

```bash
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security (main) $ eksctl create nodegroup -f imdsv2.yml 
2023-06-22 19:05:51 [ℹ]  nodegroup "imdsv2" will use "" [AmazonLinux2/1.26]
2023-06-22 19:05:52 [ℹ]  3 existing nodegroup(s) (linux-ng,mng,windows-managed-ng-2022) will be excluded
2023-06-22 19:05:52 [ℹ]  1 nodegroup (imdsv2) was included (based on the include/exclude rules)
2023-06-22 19:05:52 [ℹ]  will create a CloudFormation stack for each of 1 managed nodegroups in cluster "eks126"
2023-06-22 19:05:52 [ℹ]  
2 sequential tasks: { fix cluster compatibility, 1 task: { 1 task: { create managed nodegroup "imdsv2" } } 
}
2023-06-22 19:05:52 [ℹ]  checking cluster stack for missing resources
2023-06-22 19:05:53 [ℹ]  cluster stack has all required resources
2023-06-22 19:05:54 [ℹ]  building managed nodegroup stack "eksctl-eks126-nodegroup-imdsv2"
2023-06-22 19:05:54 [ℹ]  deploying stack "eksctl-eks126-nodegroup-imdsv2"
2023-06-22 19:05:54 [ℹ]  waiting for CloudFormation stack "eksctl-eks126-nodegroup-imdsv2"
2023-06-22 19:06:24 [ℹ]  waiting for CloudFormation stack "eksctl-eks126-nodegroup-imdsv2"
2023-06-22 19:07:12 [ℹ]  waiting for CloudFormation stack "eksctl-eks126-nodegroup-imdsv2"
2023-06-22 19:08:47 [ℹ]  waiting for CloudFormation stack "eksctl-eks126-nodegroup-imdsv2"
2023-06-22 19:08:47 [ℹ]  no tasks
2023-06-22 19:08:47 [✔]  created 0 nodegroup(s) in cluster "eks126"
2023-06-22 19:08:47 [✔]  created 1 managed nodegroup(s) in cluster "eks126"
2023-06-22 19:08:48 [ℹ]  checking security group configuration for all nodegroups
```

## multi_tenancy

### ensure_namespace_quotas_exist

```bash

cat > ns-quota-sample.yaml <<EOF
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: namespace-quota
  namespace: sample
spec:
  hard:
    pods: 20
    requests.cpu: 10000m
    requests.memory: 10Gi
    limits.cpu: 20000m
    limits.memory: 20Gi
EOF

kubectl apply -f ns-quota-sample.yaml
kubectl apply -f ns-quota-amazon-guardduty.yaml
kubectl apply -f ns-quota-cert-manager.yaml
kubectl apply -f ns-quota-default.yaml
kubectl apply -f ns-quota-karpenter.yaml
kubectl apply -f ns-quota-opentelemetry-operator-system.yaml
kubectl apply -f ns-quota-prometheus.yaml
kubectl apply -f ns-quota-windows.yaml



```
## detective_controls
### check_logs_are_enabled

```bash
aws eks update-cluster-config --name eks126 \
--logging '{"clusterLogging":[{"types":["api","audit"],"enabled":true}]}'

{
    "update": {
        "id": "b53fde61-df0f-446a-9713-811a06e3d62f",
        "status": "InProgress",
        "type": "LoggingUpdate",
        "params": [
            {
                "type": "ClusterLogging",
                "value": "{\"clusterLogging\":[{\"types\":[\"api\",\"audit\"],\"enabled\":true}]}"
            }
        ],
        "createdAt": "2023-06-23T10:05:11.301000+00:00",
        "errors": []
    }
}




```
## network_security
### check_vpc_flow_logs

```bash


aws ec2 create-flow-logs \
    --resource-type VPC \
    --resource-ids vpc-03103b5e0fe171706 \
    --traffic-type ALL \
    --log-destination-type cloud-watch-logs \
    --log-group-name eks126-vpc-flow-logs \
    --deliver-logs-permission-arn arn:aws:iam::000474600478:role/MulticastECSBlog-FlowLogsRole-7W92ZOIUX3GI

{
    "ClientToken": "QJPAPX85N74936ZjhdUbBFmOyWn3USSAZxahDuhvDdk=",
    "FlowLogIds": [
        "fl-0fd34324dfeeaddc1"
    ],
    "Unsuccessful": []
}    
```

### check_awspca_exists

```bash
export ACM_PCA_ARN="arn:aws:acm-pca:us-east-1:000474600478:certificate-authority/730a7d12-c910-4e9b-83b7-c61d0b4f7ce7"

aws acm-pca get-certificate-authority-certificate --certificate-authority-arn $ACM_PCA_ARN --region us-east-1 --output text > cacert.pem


https://github.com/awslabs/eksdemo/blob/main/docs/install-cert-manager.md

eksdemo install cert-manager -c eks126 --dry-run

Creating 1 dependencies for cert-manager
Creating dependency: cert-manager-irsa

Eksctl Resource Manager Dry Run:
eksctl create iamserviceaccount -f - --approve
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: eks126
  region: us-east-1

iam:
  withOIDC: true
  serviceAccounts:
  - metadata:
      name: cert-manager
      namespace: cert-manager
    roleName: eksdemo.eks126.cert-manager.cert-manager
    roleOnly: true
    attachPolicy:      
      Version: '2012-10-17'
      Statement:
      - Effect: Allow
        Action:
        - route53:GetChange
        Resource: arn:aws:route53:::change/*
      - Effect: Allow
        Action:
        - route53:ChangeResourceRecordSets
        - route53:ListResourceRecordSets
        Resource: arn:aws:route53:::hostedzone/*
      - Effect: Allow
        Action: route53:ListHostedZonesByName
        Resource: "*"
      

Helm Installer Dry Run:
+---------------------+----------------------------+
| Application Version | v1.12.1                    |
| Chart Version       | 1.12.1                     |
| Chart Repository    | https://charts.jetstack.io |
| Chart Name          | cert-manager               |
| Release Name        | cert-manager               |
| Namespace           | cert-manager               |
| Wait                | false                      |
+---------------------+----------------------------+
Set Values: []
Values File:
---
installCRDs: true
replicaCount: 1
serviceAccount:
  name: cert-manager
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::000474600478:role/eksdemo.eks126.cert-manager.cert-manager
image:
  tag: v1.12.1

Creating 1 post-install resources for cert-manager
Creating post-install resource: cert-manager-cluster-issuer

Kubernetes Resource Manager Dry Run:
---
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - dns01:
        route53:
          region: us-east-1


eksdemo install cert-manager -c eks126
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ eksdemo install cert-manager -c eks126
Creating 1 dependencies for cert-manager
Creating dependency: cert-manager-irsa
2023-06-23 12:07:48 [ℹ]  5 existing iamserviceaccount(s) (cert-manager/cert-manager,karpenter/karpenter,kube-system/aws-load-balancer-controller,prometheus/amp-irsa-role,sample/external-dns) will be excluded
2023-06-23 12:07:48 [ℹ]  1 iamserviceaccount (cert-manager/cert-manager) was excluded (based on the include/exclude rules)
2023-06-23 12:07:48 [!]  serviceaccounts that exist in Kubernetes will be excluded, use --override-existing-serviceaccounts to override
2023-06-23 12:07:48 [ℹ]  no tasks
Downloading Chart: https://charts.jetstack.io/charts/cert-manager-v1.12.1.tgz
Helm installing...
Error: helm install failed: Kubernetes cluster unreachable: Get "https://BF03E35320602DCC0874D4B837FB9FE4.gr7.us-east-1.eks.amazonaws.com/version": getting credentials: decoding stdout: no kind "ExecCredential" is registered for version "client.authentication.k8s.io/v1alpha1" in scheme "pkg/runtime/scheme.go:100"
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml
namespace/cert-manager unchanged
customresourcedefinition.apiextensions.k8s.io/certificaterequests.cert-manager.io configured
customresourcedefinition.apiextensions.k8s.io/certificates.cert-manager.io configured
customresourcedefinition.apiextensions.k8s.io/challenges.acme.cert-manager.io configured
customresourcedefinition.apiextensions.k8s.io/clusterissuers.cert-manager.io configured
customresourcedefinition.apiextensions.k8s.io/issuers.cert-manager.io configured
customresourcedefinition.apiextensions.k8s.io/orders.acme.cert-manager.io configured
serviceaccount/cert-manager-cainjector configured
serviceaccount/cert-manager configured
serviceaccount/cert-manager-webhook configured
configmap/cert-manager-webhook configured
clusterrole.rbac.authorization.k8s.io/cert-manager-cainjector configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-issuers configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-clusterissuers configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-certificates configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-orders configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-challenges configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-ingress-shim configured
clusterrole.rbac.authorization.k8s.io/cert-manager-view configured
clusterrole.rbac.authorization.k8s.io/cert-manager-edit configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-approve:cert-manager-io configured
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-certificatesigningrequests configured
clusterrole.rbac.authorization.k8s.io/cert-manager-webhook:subjectaccessreviews configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-cainjector configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-issuers configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-clusterissuers configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-certificates configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-orders configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-challenges configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-ingress-shim configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-approve:cert-manager-io configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-certificatesigningrequests configured
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-webhook:subjectaccessreviews configured
role.rbac.authorization.k8s.io/cert-manager-cainjector:leaderelection configured
role.rbac.authorization.k8s.io/cert-manager:leaderelection configured
role.rbac.authorization.k8s.io/cert-manager-webhook:dynamic-serving configured
rolebinding.rbac.authorization.k8s.io/cert-manager-cainjector:leaderelection configured
rolebinding.rbac.authorization.k8s.io/cert-manager:leaderelection configured
rolebinding.rbac.authorization.k8s.io/cert-manager-webhook:dynamic-serving configured
service/cert-manager configured
service/cert-manager-webhook configured
deployment.apps/cert-manager-cainjector configured
deployment.apps/cert-manager configured
deployment.apps/cert-manager-webhook configured
mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
validatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ 


helm repo add awspca https://cert-manager.github.io/aws-privateca-issuer
helm repo update
helm install awspca/aws-privateca-issuer  --generate-name --namespace aws-pca-issuer

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl create ns aws-pca-issuer
namespace/aws-pca-issuer created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ helm install awspca/aws-privateca-issuer  --generate-name --namespace aws-pca-issuer
NAME: aws-privateca-issuer-1687522474
LAST DEPLOYED: Fri Jun 23 12:14:35 2023
NAMESPACE: aws-pca-issuer
STATUS: deployed
REVISION: 1
TEST SUITE: None




export TEST_DOMAIN='test.cloudtechconsulting.in'

cat > test-cert.yaml <<EOF
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: test
spec:
  secretName: test-cert-tls
  dnsNames:
    - $TEST_DOMAIN
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
EOF

kubectl apply -f test-cert.yaml

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f test-cert.yaml
certificate.cert-manager.io/test created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl get cert
NAME   READY   SECRET          AGE
test   False   test-cert-tls   10s
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl get cert
NAME   READY   SECRET          AGE
test   False   test-cert-tls   50s
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl get cert
NAME   READY   SECRET          AGE
test   False   test-cert-tls   54s

eksdemo get records -z cloudtechconsulting.in

jp:~/environment/eksdemo (main) $ eksdemo get records -z cloudtechconsulting.in
+---------------------------------------------------------------+-------+------------------------------+
|                             Name                              | Type  |            Value             |
+---------------------------------------------------------------+-------+------------------------------+
| cloudtechconsulting.in                                        | NS    | ns-443.awsdns-55.com.        |
|                                                               |       | ns-1108.awsdns-10.org.       |
|                                                               |       | ns-1985.awsdns-56.co.uk.     |
|                                                               |       | ns-987.awsdns-59.net.        |
| cloudtechconsulting.in                                        | SOA   | ns-443.awsdns-55.com.        |
|                                                               |       | awsdns-hostmaster.amazon.... |
|                                                               |       | 1 7200 900 1209600 86400     |
| _ef39da5327da1c992aed72996ef71504.cloudtechconsulting.in      | CNAME | _539e5e631fbf76f217deca34... |
| cname-yelb.cloudtechconsulting.in                             | TXT   | "heritage=external-dns,ex... |
| sample.cloudtechconsulting.in                                 | NS    | ns-1147.awsdns-15.org.       |
|                                                               |       | ns-267.awsdns-33.com.        |
|                                                               |       | ns-1923.awsdns-48.co.uk.     |
|                                                               |       | ns-554.awsdns-05.net.        |
| www.cloudtechconsulting.in                                    | A     | dualstack.k8s-yelb-yelbmy... |
| yelb.cloudtechconsulting.in                                   | A     | k8s-kubecost-kirkingr-1e3... |
| yelb.cloudtechconsulting.in                                   | TXT   | "heritage=external-dns,ex... |
| _6f9d35a05c750796b9fbaea157ce22cf.yelb.cloudtechconsulting.in | CNAME | _5be4dc8e6cb13633039a795c... |
+---------------------------------------------------------------+-------+------------------------------+
jp:~/environment/eksdemo (main) $ 


```
### check_default_deny_policy_exists

https://docs.aws.amazon.com/eks/latest/userguide/calico.html

https://docs.tigera.io/calico/3.25/getting-started/kubernetes/helm#install-calico

helm repo add projectcalico https://docs.tigera.io/calico/charts
kubectl create namespace tigera-operator
helm install calico projectcalico/tigera-operator --version v3.25.1 --namespace tigera-operator

NAME: calico
LAST DEPLOYED: Sat Jun 24 07:00:08 2023
NAMESPACE: tigera-operator
STATUS: deployed
REVISION: 1
TEST SUITE: None

watch kubectl get pods -n calico-system
jp:~/environment/code-samples (main) $ watch kubectl get pods -n calico-system
jp:~/environment/code-samples (main) $  kubectl get pods -n calico-system
NAME                                      READY   STATUS    RESTARTS   AGE
calico-kube-controllers-645bf7994-sm776   1/1     Running   0          28s
calico-node-47rrg                         1/1     Running   0          28s
calico-node-dswr8                         1/1     Running   0          28s
calico-node-fmdb2                         1/1     Running   0          28s
calico-typha-8d9858874-9vm62              1/1     Running   0          29s
calico-typha-8d9858874-cnjvp              1/1     Running   0          20s
csi-node-driver-477lv                     2/2     Running   0          28s
csi-node-driver-6jtp2                     2/2     Running   0          28s
csi-node-driver-hjg2z                     2/2     Running   0          28s

kubectl get all -n tigera-operator

jp:~/environment/code-samples (main) $ kubectl get all -n tigera-operator
NAME                                   READY   STATUS    RESTARTS   AGE
pod/tigera-operator-5d6845b496-r9m94   1/1     Running   0          56s

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/tigera-operator   1/1     1            1           56s

NAME                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/tigera-operator-5d6845b496   1         1         1       56s

kubectl get all -n calico-system

jp:~/environment/code-samples (main) $ kubectl get all -n calico-system
NAME                                          READY   STATUS    RESTARTS   AGE
pod/calico-kube-controllers-645bf7994-sm776   1/1     Running   0          78s
pod/calico-node-47rrg                         1/1     Running   0          78s
pod/calico-node-dswr8                         1/1     Running   0          78s
pod/calico-node-fmdb2                         1/1     Running   0          78s
pod/calico-typha-8d9858874-9vm62              1/1     Running   0          79s
pod/calico-typha-8d9858874-cnjvp              1/1     Running   0          70s
pod/csi-node-driver-477lv                     2/2     Running   0          78s
pod/csi-node-driver-6jtp2                     2/2     Running   0          78s
pod/csi-node-driver-hjg2z                     2/2     Running   0          78s

NAME                                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/calico-kube-controllers-metrics   ClusterIP   None            <none>        9094/TCP   74s
service/calico-typha                      ClusterIP   10.100.42.125   <none>        5473/TCP   79s

NAME                             DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/calico-node       3         3         3       3            3           kubernetes.io/os=linux   79s
daemonset.apps/csi-node-driver   3         3         3       3            3           kubernetes.io/os=linux   79s

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/calico-kube-controllers   1/1     1            1           79s
deployment.apps/calico-typha              2/2     2            2           79s

NAME                                                DESIRED   CURRENT   READY   AGE
replicaset.apps/calico-kube-controllers-645bf7994   1         1         1       79s
replicaset.apps/calico-typha-8d9858874              2         2         2       79s

kubectl logs tigera-operator-5d6845b496-r9m94 -n tigera-operator | grep ERROR
kubectl logs calico-node-47rrg -c calico-node -n calico-system | grep ERROR
kubectl logs calico-typha-8d9858874-9vm62 -n calico-system | grep ERROR



jp:~/environment/code-samples (main) $ kubectl logs tigera-operator-5d6845b496-r9m94 -n tigera-operator | grep ERROR
jp:~/environment/code-samples (main) $ kubectl logs tigera-operator-5d6845b496-r9m94 -n tigera-operator 
2023/06/24 07:00:12 [INFO] Version: v1.29.3
2023/06/24 07:00:12 [INFO] Go Version: go1.19.7 X:boringcrypto
2023/06/24 07:00:12 [INFO] Go OS/Arch: linux/amd64
2023/06/24 07:00:14 [INFO] Active operator: proceeding
{"level":"info","ts":1687590014.4589038,"logger":"setup","msg":"Checking type of cluster","provider":""}
{"level":"info","ts":1687590014.4598296,"logger":"setup","msg":"Checking if PodSecurityPolicies are supported by the cluster","supported":false}
{"level":"info","ts":1687590014.4609833,"logger":"setup","msg":"Checking if TSEE controllers are required","required":false}
{"level":"info","ts":1687590014.564405,"logger":"typha_autoscaler","msg":"Starting typha autoscaler","syncPeriod":10}
{"level":"info","ts":1687590014.564478,"logger":"setup","msg":"starting manager"}
I0624 07:00:14.665013       1 leaderelection.go:248] attempting to acquire leader lease tigera-operator/operator-lock...
I0624 07:00:14.674307       1 leaderelection.go:258] successfully acquired lease tigera-operator/operator-lock
{"level":"info","ts":1687590014.6745012,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.Installation"}
{"level":"info","ts":1687590014.674533,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.APIServer"}
{"level":"info","ts":1687590014.6745527,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.TigeraStatus"}
{"level":"info","ts":1687590014.6745567,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Installation"}
{"level":"info","ts":1687590014.6745608,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.6745632,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.ConfigMap"}
{"level":"info","ts":1687590014.6745672,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ConfigMap"}
{"level":"info","ts":1687590014.6745698,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.6745737,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ConfigMap"}
{"level":"info","ts":1687590014.6745763,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.674583,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.6745894,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.6745956,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.6746027,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.Secret"}
{"level":"info","ts":1687590014.6746068,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ConfigMap"}
{"level":"info","ts":1687590014.6746135,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.ImageSet"}
{"level":"info","ts":1687590014.6746266,"msg":"Starting EventSource","controller":"apiserver-controller","source":"kind source: *v1.TigeraStatus"}
{"level":"info","ts":1687590014.6746323,"msg":"Starting Controller","controller":"apiserver-controller"}
{"level":"info","ts":1687590014.674614,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ConfigMap"}
{"level":"info","ts":1687590014.6747496,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ConfigMap"}
{"level":"info","ts":1687590014.674757,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ImageSet"}
{"level":"info","ts":1687590014.674764,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.DaemonSet"}
{"level":"info","ts":1687590014.6747704,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ClusterRole"}
{"level":"info","ts":1687590014.6747775,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ClusterRoleBinding"}
{"level":"info","ts":1687590014.6747875,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.ServiceAccount"}
{"level":"info","ts":1687590014.6747932,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.APIService"}
{"level":"info","ts":1687590014.6748,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.Service"}
{"level":"info","ts":1687590014.6748142,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.KubeControllersConfiguration"}
{"level":"info","ts":1687590014.6748254,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.FelixConfiguration"}
{"level":"info","ts":1687590014.6748326,"msg":"Starting EventSource","controller":"tigera-installation-controller","source":"kind source: *v1.BGPConfiguration"}
{"level":"info","ts":1687590014.674843,"msg":"Starting Controller","controller":"tigera-installation-controller"}
{"level":"info","ts":1687590014.9767592,"msg":"Starting workers","controller":"tigera-installation-controller","worker count":1}
{"level":"info","ts":1687590014.9767544,"msg":"Starting workers","controller":"apiserver-controller","worker count":1}
{"level":"info","ts":1687590014.977069,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590014.9771297,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590014.9895718,"logger":"windows_upgrader","msg":"Starting main loop"}
{"level":"info","ts":1687590014.9905365,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590014.9906173,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590014.998275,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590014.9983213,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590015.2649622,"logger":"controller_installation","msg":"adding active configmap"}
{"level":"info","ts":1687590015.4100316,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"tigera-operator","Request.Name":"tigera-ca-private"}
{"level":"error","ts":1687590015.4100752,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"tigera-operator","Request.Name":"tigera-ca-private","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590016.5214705,"logger":"controller_installation","msg":"Failed to update object.","Name":"calico-node","Namespace":"calico-system","Kind":"DaemonSet","key":"calico-system/calico-node"}
{"level":"info","ts":1687590016.5214958,"logger":"controller_installation","msg":"Failed to update object, retrying.","component":"*render.nodeComponent","key":"calico-system/calico-node","conflict_message":"Operation cannot be fulfilled on daemonsets.apps \"calico-node\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590019.5715191,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
{"level":"error","ts":1687590019.5821075,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"apiserver","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590019.5824127,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590019.5824492,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590019.7040384,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590019.7040894,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590020.0870497,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590020.0870984,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590024.5689476,"logger":"typha_autoscaler","msg":"Updating typha replicas from 1 to 2"}
{"level":"info","ts":1687590024.5736635,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
{"level":"info","ts":1687590024.5808454,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"calico\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590024.582924,"logger":"KubeAPIWarningLogger","msg":"unknown field \"status.conditions\""}
{"level":"error","ts":1687590024.5831842,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"apiserver","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590024.6029682,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590024.6030939,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590029.579541,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"calico\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590029.588188,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"calico\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590029.6034722,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"error","ts":1687590029.6035213,"logger":"controller_apiserver","msg":"Waiting for Installation to be ready","Request.Namespace":"","Request.Name":"default","reason":"ResourceNotReady","stacktrace":"github.com/tigera/operator/pkg/controller/status.(*statusManager).SetDegraded\n\t/go/src/github.com/tigera/operator/pkg/controller/status/status.go:406\ngithub.com/tigera/operator/pkg/controller/apiserver.(*ReconcileAPIServer).Reconcile\n\t/go/src/github.com/tigera/operator/pkg/controller/apiserver/apiserver_controller.go:253\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Reconcile\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:121\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:320\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234"}
{"level":"info","ts":1687590029.791918,"logger":"KubeAPIWarningLogger","msg":"unknown field \"status.calicoVersion\""}
{"level":"info","ts":1687590029.7920902,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"info","ts":1687590030.4263365,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"tigera-operator","Request.Name":"calico-apiserver-certs"}
{"level":"info","ts":1687590030.6239512,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"info","ts":1687590034.5793407,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
{"level":"info","ts":1687590034.5889068,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"apiserver\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590034.6017728,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"apiserver\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590034.7516904,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
{"level":"info","ts":1687590044.573506,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
{"level":"info","ts":1687590044.5789342,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"apiserver\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590044.5881534,"logger":"status_manager","msg":"update to tigera status conflicted, retrying","reason":"Operation cannot be fulfilled on tigerastatuses.operator.tigera.io \"apiserver\": the object has been modified; please apply your changes to the latest version and try again"}
{"level":"info","ts":1687590044.7325304,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"info","ts":1687590044.8746805,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
{"level":"info","ts":1687590049.8594966,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"info","ts":1687590060.427039,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"default"}
{"level":"info","ts":1687590060.6250296,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"tigera-operator","Request.Name":"calico-apiserver-certs"}
{"level":"info","ts":1687590064.7524297,"logger":"controller_apiserver","msg":"Reconciling APIServer","Request.Namespace":"","Request.Name":"apiserver"}
jp:~/environment/code-samples (main) $ 



jp:~/environment/code-samples (main) $ kubectl logs calico-node-47rrg -c calico-node -n calico-system | grep ERROR

jp:~/environment/code-samples (main) $ kubectl logs calico-node-47rrg -c calico-node -n calico-system 



kubectl describe daemonset aws-node -n kube-system | grep amazon-k8s-cni: | cut -d ":" -f 3


v1.12.5-eksbuild.2

cat << EOF > append.yaml
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - patch
EOF


kubectl apply -f <(cat <(kubectl get clusterrole aws-node -o yaml) append.yaml)


clusterrole.rbac.authorization.k8s.io/aws-node configured


kubectl set env daemonset aws-node -n kube-system ANNOTATE_POD_IP=true

daemonset.apps/aws-node env updated

kubectl delete pod calico-kube-controllers-645bf7994-sm776 -n calico-system
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl delete pod calico-kube-controllers-645bf7994-sm776 -n calico-system
pod "calico-kube-controllers-645bf7994-sm776" deleted

kubectl get pods -n calico-system

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl get pods -n calico-system
NAME                                      READY   STATUS    RESTARTS   AGE
calico-kube-controllers-645bf7994-xtsjw   1/1     Running   0          18s
calico-node-47rrg                         1/1     Running   0          30m
calico-node-dswr8                         1/1     Running   0          30m
calico-node-fmdb2                         1/1     Running   0          30m
calico-typha-8d9858874-9vm62              1/1     Running   0          30m
calico-typha-8d9858874-cnjvp              1/1     Running   0          30m
csi-node-driver-477lv                     2/2     Running   0          30m
csi-node-driver-6jtp2                     2/2     Running   0          30m
csi-node-driver-hjg2z                     2/2     Running   0          30m

kubectl describe pod calico-kube-controllers-645bf7994-xtsjw -n calico-system | grep vpc.amazonaws.com/pod-ips

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl describe pod calico-kube-controllers-645bf7994-xtsjw -n calico-system | grep vpc.amazonaws.com/pod-ips
Annotations:          vpc.amazonaws.com/pod-ips: 192.168.125.239

kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/00-namespace.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/01-management-ui.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/02-backend.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/03-frontend.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/04-client.yaml

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/00-namespace.yaml
namespace/stars created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/01-management-ui.yaml
namespace/management-ui created
service/management-ui created
replicationcontroller/management-ui created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/02-backend.yaml
service/backend created
replicationcontroller/backend created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/03-frontend.yaml
service/frontend created
replicationcontroller/frontend created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/04-client.yaml
namespace/client created
replicationcontroller/client created
service/client created

kubectl get pods -A

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl get pods -A
NAMESPACE                       NAME                                                READY   STATUS             RESTARTS          AGE
amazon-guardduty                aws-guardduty-agent-2fvhv                           1/1     Running            1 (31h ago)       36h
amazon-guardduty                aws-guardduty-agent-5jn45                           1/1     Running            1 (7h33m ago)     36h
amazon-guardduty                aws-guardduty-agent-r4b6g                           1/1     Running            1 (7h33m ago)     36h
assets                          assets-6cf85dd9d4-lghwf                             1/1     Running            0                 57m
aws-pca-issuer                  aws-privateca-issuer-1687522474-6f84cf587f-4mjlk    1/1     Running            1 (7h33m ago)     19h
calico-apiserver                calico-apiserver-6ddffdb4fc-kwbcx                   1/1     Running            0                 35m
calico-apiserver                calico-apiserver-6ddffdb4fc-t5r28                   1/1     Running            0                 35m
calico-system                   calico-kube-controllers-645bf7994-xtsjw             1/1     Running            0                 5m20s
calico-system                   calico-node-47rrg                                   1/1     Running            0                 35m
calico-system                   calico-node-dswr8                                   1/1     Running            0                 35m
calico-system                   calico-node-fmdb2                                   1/1     Running            0                 35m
calico-system                   calico-typha-8d9858874-9vm62                        1/1     Running            0                 35m
calico-system                   calico-typha-8d9858874-cnjvp                        1/1     Running            0                 35m
calico-system                   csi-node-driver-477lv                               2/2     Running            0                 35m
calico-system                   csi-node-driver-6jtp2                               2/2     Running            0                 35m
calico-system                   csi-node-driver-hjg2z                               2/2     Running            0                 35m
carts                           carts-847dfcd6c4-n7rv5                              1/1     Running            0                 57m
carts                           carts-dynamodb-64fc88f7d6-97vbw                     1/1     Running            0                 57m
catalog                         catalog-689b4bcd78-sqf65                            1/1     Running            2 (63m ago)       63m
catalog                         catalog-mysql-0                                     1/1     Running            0                 63m
cert-manager                    cert-manager-bfcd95fbc-6kmgv                        1/1     Running            1 (7h33m ago)     27h
cert-manager                    cert-manager-cainjector-6c65c9f988-4vtjq            1/1     Running            1 (7h33m ago)     27h
cert-manager                    cert-manager-webhook-78b75fb78f-tphwp               1/1     Running            0                 27h
checkout                        checkout-55ddcfc5f8-phhxk                           1/1     Running            0                 57m
checkout                        checkout-redis-6698687878-547gn                     1/1     Running            0                 57m
client                          client-nmbd9                                        1/1     Running            0                 15s
karpenter                       karpenter-986b9456b-hqjz6                           1/1     Running            1 (7h33m ago)     25h
kube-system                     aws-load-balancer-controller-65d588d98b-nf4pn       1/1     Running            1 (7h33m ago)     27h
kube-system                     aws-load-balancer-controller-65d588d98b-pgmmt       1/1     Running            0                 27h
kube-system                     aws-node-bcrp5                                      1/1     Running            0                 5m50s
kube-system                     aws-node-jfgk7                                      1/1     Running            0                 5m54s
kube-system                     aws-node-pjd87                                      1/1     Running            0                 5m58s
kube-system                     coredns-55fb5d545d-7j545                            1/1     Running            1 (7h33m ago)     27h
kube-system                     coredns-55fb5d545d-h9bd9                            1/1     Running            1 (7h33m ago)     27h
kube-system                     kube-proxy-mc5gk                                    1/1     Running            1 (7h33m ago)     36h
kube-system                     kube-proxy-rgcw6                                    1/1     Running            1 (7h33m ago)     36h
kube-system                     kube-proxy-xm6b2                                    1/1     Running            1 (31h ago)       36h
management-ui                   management-ui-t55ss                                 1/1     Running            0                 21s
opentelemetry-operator-system   opentelemetry-operator-68dd777685-7zb76             2/2     Running            0                 27h
orders                          orders-5fdbcbdd7c-g6w67                             1/1     Running            0                 57m
orders                          orders-mysql-854b8b4f8f-2zrw7                       1/1     Running            0                 57m
prometheus                      observability-collector-7d4b898559-k7vlw            0/1     CrashLoopBackOff   326 (2m32s ago)   27h
rabbitmq                        rabbitmq-0                                          1/1     Running            0                 57m
sample                          external-dns-5f4f5ffcf9-l98ks                       0/1     CrashLoopBackOff   272 (72s ago)     27h
sample                          sample-ui-5d699dbf98-7gczt                          1/1     Running            0                 27h
stars                           backend-9n52b                                       1/1     Running            0                 19s
stars                           frontend-bdkb7                                      1/1     Running            0                 18s
tigera-operator                 tigera-operator-5d6845b496-r9m94                    1/1     Running            0                 35m
ui                              ui-5b4f9bdcd5-l2xtw                                 1/1     Running            0                 57m
windows                         windows-server-iis-ltsc2022-85dbb85495-dsvgn        0/1     Pending            0                 39d
windows                         windows-server-iis-ltsc2022-85dbb85495-wmw4c        0/1     Pending            0                 39d
windows                         windows-server-iis-ltsc2022-host-664dbfddc9-rnm42   0/1     Pending            0                 39d
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ 


kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/00-namespace.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/01-management-ui.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/02-backend.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/03-frontend.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/manifests/04-client.yaml

kubectl apply -n stars -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/default-deny.yaml
kubectl apply -n client -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/default-deny.yaml


kubectl delete -n stars -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/default-deny.yaml
kubectl delete -n client -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/default-deny.yaml


kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/allow-ui.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/allow-ui-client.yaml

kubectl delete -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/allow-ui.yaml
kubectl delete -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/allow-ui-client.yaml


kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/backend-policy.yaml
kubectl apply -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/frontend-policy.yaml

kubectl delete -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/backend-policy.yaml
kubectl delete -f https://docs.projectcalico.org/v3.5/getting-started/kubernetes/tutorials/stars-policy/policies/frontend-policy.yaml



kubectl port-forward service/management-ui -n management-ui 8080

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $ kubectl apply -f allow-route53.yaml 
networkpolicy.networking.k8s.io/allow-dns-access created
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security (main) $  kubectl get NetworkPolicy -A
NAMESPACE          NAME               POD-SELECTOR     AGE
calico-apiserver   allow-apiserver    apiserver=true   3h5m
stars              allow-dns-access   <none>           3s
stars              default-deny1      <none>           95s



```bash

```
## encryption_secrets
### use_encryption_with_ebs

```bash

eksdemo install storage-ebs-csi -c eks126

jp:~/environment $ eksdemo install storage-ebs-csi -c eks126
Creating 1 dependencies for storage-ebs-csi
Creating dependency: ebs-csi-irsa
2023-06-24 12:14:10 [ℹ]  6 existing iamserviceaccount(s) (cert-manager/cert-manager,karpenter/karpenter,kube-system/aws-load-balancer-controller,kube-system/ebs-csi-controller-sa,prometheus/amp-irsa-role,sample/external-dns) will be excluded
2023-06-24 12:14:10 [ℹ]  1 iamserviceaccount (kube-system/ebs-csi-controller-sa) was excluded (based on the include/exclude rules)
2023-06-24 12:14:10 [!]  serviceaccounts that exist in Kubernetes will be excluded, use --override-existing-serviceaccounts to override
2023-06-24 12:14:10 [ℹ]  no tasks
Checking for default StorageClass
Marking StorageClass "gp2" as non-default...done
Downloading Chart: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases/download/helm-chart-aws-ebs-csi-driver-2.19.0/aws-ebs-csi-driver-2.19.0.tgz
Helm installing...
2023/06/24 12:14:12 creating 1 resource(s)
2023/06/24 12:14:12 creating 18 resource(s)
Using chart version "2.19.0", installed "storage-ebs-csi" version "v1.19.0" in namespace "kube-system"
NOTES:
To verify that aws-ebs-csi-driver has started, run:

    kubectl get pod -n kube-system -l "app.kubernetes.io/name=aws-ebs-csi-driver,app.kubernetes.io/instance=storage-ebs-csi"

NOTE: The [CSI Snapshotter](https://github.com/kubernetes-csi/external-snapshotter) controller and CRDs will no longer be installed as part of this chart and moving forward will be a prerequisite of using the snap shotting functionality.



```
### use_encryption_with_efs


```bash

jp:~/environment $ kubectl get pod -n kube-system -l "app.kubernetes.io/name=aws-efs-csi-driver,app.kubernetes.io/instance=storage-efs-csi"
NAME                                  READY   STATUS    RESTARTS   AGE
efs-csi-controller-66f679d7cc-c4t5p   3/3     Running   0          116s
efs-csi-node-77lpb                    3/3     Running   0          116sefs-csi-node-svn2w                    3/3     Running   0          116s
efs-csi-node-x6km7                    3/3     Running   0          116s
jp:~/environment $ kubectl get pod -n kube-system -l "app.kubernetes.io/name=aws-efs-csi-driver,app.kubernetes.io/instance=storage-efs-csi"
NAME                                  READY   STATUS    RESTARTS   AGE
efs-csi-controller-66f679d7cc-c4t5p   3/3     Running   0          116s
efs-csi-node-77lpb                    3/3     Running   0          116sefs-csi-node-svn2w                    3/3     Running   0          116s
efs-csi-node-x6km7                    3/3     Running   0          116s

jp:~/environment $ kubectl get csidrivers
NAME              ATTACHREQUIRED   PODINFOONMOUNT   STORAGECAPACITY   TOKENREQUESTS   REQUIRESREPUBLISH   MODES        AGE
csi.tigera.io     true             true             false             <unset>         false               Ephemeral    7h9m
ebs.csi.aws.com   true             false            false             <unset>         false               Persistent   115m
efs.csi.aws.com   false            false            false             <unset>         false               Persistent   66m


CLUSTER_NAME=eks126
VPC_ID=$(aws eks describe-cluster --name $CLUSTER_NAME --query "cluster.resourcesVpcConfig.vpcId" --output text)
echo $VPC_ID
vpc-03103b5e0fe171706
CIDR_BLOCK=$(aws ec2 describe-vpcs --vpc-ids $VPC_ID --query "Vpcs[].CidrBlock" --output text)
echo $CIDR_BLOCK
192.168.0.0/16


MOUNT_TARGET_GROUP_NAME="eks-efs-group"
MOUNT_TARGET_GROUP_DESC="NFS access to EFS from EKS worker nodes"
MOUNT_TARGET_GROUP_ID=$(aws ec2 create-security-group --group-name $MOUNT_TARGET_GROUP_NAME --description "$MOUNT_TARGET_GROUP_DESC" --vpc-id $VPC_ID | jq --raw-output '.GroupId')
aws ec2 authorize-security-group-ingress --group-id $MOUNT_TARGET_GROUP_ID --protocol tcp --port 2049 --cidr $CIDR_BLOCK


{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-06a90aac69d8f5ac2",
            "GroupId": "sg-00f5be698daec90ff",
            "GroupOwnerId": "000474600478",
            "IsEgress": false,
            "IpProtocol": "tcp",
            "FromPort": 2049,
            "ToPort": 2049,
            "CidrIpv4": "192.168.0.0/16"
        }
    ]
}

FILE_SYSTEM_ID=$(aws efs create-file-system | jq --raw-output '.FileSystemId')

fs-0d8e0b886dfb5c77a

aws efs describe-file-systems --file-system-id $FILE_SYSTEM_ID

{
    "FileSystems": [
        {
            "OwnerId": "000474600478",
            "CreationToken": "e65865fc-7e20-43e9-9f53-f655f4351fd2",
            "FileSystemId": "fs-0d8e0b886dfb5c77a",
            "FileSystemArn": "arn:aws:elasticfilesystem:us-east-1:000474600478:file-system/fs-0d8e0b886dfb5c77a",
            "CreationTime": "2023-06-24T14:16:01+00:00",
            "LifeCycleState": "available",
            "NumberOfMountTargets": 0,
            "SizeInBytes": {
                "Value": 6144,
                "ValueInIA": 0,
                "ValueInStandard": 6144
            },
            "PerformanceMode": "generalPurpose",
            "Encrypted": false,
            "ThroughputMode": "bursting",
            "Tags": []
        }
    ]
}



TAG1=tag:alpha.eksctl.io/cluster-name
TAG2=tag:kubernetes.io/role/elb
subnets=($(aws ec2 describe-subnets --filters "Name=$TAG1,Values=$CLUSTER_NAME" "Name=$TAG2,Values=1" | jq --raw-output '.Subnets[].SubnetId'))
for subnet in ${subnets[@]}
do
    echo "creating mount target in " $subnet
    aws efs create-mount-target --file-system-id $FILE_SYSTEM_ID --subnet-id $subnet --security-groups $MOUNT_TARGET_GROUP_ID
done


reating mount target in  subnet-07393d3be7a4110b2
{
    "OwnerId": "000474600478",
    "MountTargetId": "fsmt-0cc60b19941e45340",
    "FileSystemId": "fs-0d8e0b886dfb5c77a",
    "SubnetId": "subnet-07393d3be7a4110b2",
    "LifeCycleState": "creating",
    "IpAddress": "192.168.39.130",
    "NetworkInterfaceId": "eni-0efe181026794bffe",
    "AvailabilityZoneId": "use1-az5",
    "AvailabilityZoneName": "us-east-1f",
    "VpcId": "vpc-03103b5e0fe171706"
}
creating mount target in  subnet-014dd53d0c2b6eb29
{
    "OwnerId": "000474600478",
    "MountTargetId": "fsmt-061df2eb4f1382041",
    "FileSystemId": "fs-0d8e0b886dfb5c77a",
    "SubnetId": "subnet-014dd53d0c2b6eb29",
    "LifeCycleState": "creating",
    "IpAddress": "192.168.1.204",
    "NetworkInterfaceId": "eni-0ab4901564e3f4010",
    "AvailabilityZoneId": "use1-az2",
    "AvailabilityZoneName": "us-east-1b",
    "VpcId": "vpc-03103b5e0fe171706"
}
jp:~/environment $ 

aws efs describe-mount-targets --file-system-id $FILE_SYSTEM_ID | jq --raw-output '.MountTargets[].LifeCycleState'
creating
creating

wget https://archive.eksworkshop.com/beginner/190_efs/efs.files/efs-pvc.yaml

namespace/storage created
storageclass.storage.k8s.io/efs-sc created
persistentvolume/efs-pvc created
persistentvolumeclaim/efs-storage-claim created


kubectl get pvc -n storage
NAME                STATUS   VOLUME    CAPACITY   ACCESS MODES   STORAGECLASS   AGE
efs-storage-claim   Bound    efs-pvc   5Gi        RWX            efs-sc         56s

kubectl get pv

NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                       STORAGECLASS   REASON   AGE
efs-pvc   5Gi        RWX            Retain           Bound    storage/efs-storage-claim   efs-sc                  79s

kubectl apply -f efs-writer.yaml
kubectl apply -f efs-reader.yaml

jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/encryption_secrets (main) $ kubectl exec -it efs-writer -n storage -- tail /shared/out.txt
efs-writer.storage - Sat Jun 24 14:24:40 UTC 2023
efs-writer.storage - Sat Jun 24 14:24:45 UTC 2023





```
### use_efs_access_points

```bash
kubectl logs efs-csi-controller-66f679d7cc-c4t5p -n kube-system -c csi-provisioner --tail 10
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/encryption_secrets (main) $ kubectl logs efs-csi-controller-66f679d7cc-c4t5p -n kube-system -c csi-provisioner --tail 10                                                         
I0624 17:32:09.744848       1 controller.go:1472] delete "pvc-1e8859ae-e108-477d-8cf6-c411affea290": started
I0624 17:32:09.786946       1 controller.go:1487] delete "pvc-1e8859ae-e108-477d-8cf6-c411affea290": volume deleted
I0624 17:32:09.795569       1 controller.go:1537] delete "pvc-1e8859ae-e108-477d-8cf6-c411affea290": persistentvolume deleted
I0624 17:32:09.795592       1 controller.go:1542] delete "pvc-1e8859ae-e108-477d-8cf6-c411affea290": succeeded
I0624 17:32:24.947032       1 controller.go:1332] provision "default/efs-claim" class "efs-sc2": started
I0624 17:32:24.947201       1 event.go:282] Event(v1.ObjectReference{Kind:"PersistentVolumeClaim", Namespace:"default", Name:"efs-claim", UID:"c7bc663d-f3e9-498e-938a-ed1782360b06", APIVersion:"v1", ResourceVersion:"14562726", FieldPath:""}): type: 'Normal' reason: 'Provisioning' External provisioner is provisioning volume for claim "default/efs-claim"
I0624 17:32:25.074068       1 controller.go:838] successfully created PV pvc-c7bc663d-f3e9-498e-938a-ed1782360b06 for PVC efs-claim and csi volume name fs-0d8e0b886dfb5c77a::fsap-0a3e1af5b22ae20a5
I0624 17:32:25.074100       1 controller.go:1439] provision "default/efs-claim" class "efs-sc2": volume "pvc-c7bc663d-f3e9-498e-938a-ed1782360b06" provisioned
I0624 17:32:25.074123       1 controller.go:1456] provision "default/efs-claim" class "efs-sc2": succeeded
I0624 17:32:25.083494       1 event.go:282] Event(v1.ObjectReference{Kind:"PersistentVolumeClaim", Namespace:"default", Name:"efs-claim", UID:"c7bc663d-f3e9-498e-938a-ed1782360b06", APIVersion:"v1", ResourceVersion:"14562726", FieldPath:""}): type: 'Normal' reason: 'ProvisioningSucceeded' Successfully provisioned volume pvc-c7bc663d-f3e9-498e-938a-ed1782360b06


jp:~/environment/jalawala/hardeneks (main) $ kubectl get pv,pvc
NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM                       STORAGECLASS   REASON   AGE
persistentvolume/efs-pvc                                    5Gi        RWX            Retain           Bound       storage/efs-storage-claim   efs-sc                  3h12m
persistentvolume/efs-pvc1                                   5Gi        RWX            Retain           Available                               efs-sc                  162m
persistentvolume/pvc-c7bc663d-f3e9-498e-938a-ed1782360b06   20Gi       RWX            Delete           Bound       default/efs-claim           efs-sc2                 2m6s

NAME                              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/efs-claim   Bound    pvc-c7bc663d-f3e9-498e-938a-ed1782360b06   20Gi       RWX            efs-sc2        2m7s
jp:~/environment/jalawala/hardeneks (main) $ 

kubectl get pods -o wide

jp:~/environment/jalawala/hardeneks (main) $ kubectl get pods -o wide
NAME          READY   STATUS    RESTARTS   AGE     IP                NODE                              NOMINATED NODE   READINESS GATES
efs-example   1/1     Running   0          2m43s   192.168.112.186   ip-192-168-102-122.ec2.internal   <none>           <none>
jp:~/environment/jalawala/hardeneks (main) $ kubectl exec efs-example -- bash -c "cat example/out.txt"
Sat Jun 24 17:32:33 UTC 2023
Sat Jun 24 17:32:38 UTC 2023
Sat Jun 24 17:32:43 UTC 2023
Sat Jun 24 17:32:48 UTC 2023
Sat Jun 24 17:32:54 UTC 2023
Sat Jun 24 17:32:59 UTC 2023
Sat Jun 24 17:33:04 UTC 2023
Sat Jun 24 17:33:09 UTC 2023
Sat Jun 24 17:33:14 UTC 2023
Sat Jun 24 17:33:19 UTC 2023
Sat Jun 24 17:33:24 UTC 2023
Sat Jun 24 17:33:29 UTC 2023
Sat Jun 24 17:33:34 UTC 2023
Sat Jun 24 17:33:39 UTC 2023
Sat Jun 24 17:33:44 UTC 2023
Sat Jun 24 17:33:49 UTC 2023
Sat Jun 24 17:33:54 UTC 2023
Sat Jun 24 17:33:59 UTC 2023
Sat Jun 24 17:34:04 UTC 2023
Sat Jun 24 17:34:09 UTC 2023
Sat Jun 24 17:34:14 UTC 2023
Sat Jun 24 17:34:19 UTC 2023
Sat Jun 24 17:34:24 UTC 2023
Sat Jun 24 17:34:29 UTC 2023
Sat Jun 24 17:34:34 UTC 2023
Sat Jun 24 17:34:39 UTC 2023
Sat Jun 24 17:34:44 UTC 2023
Sat Jun 24 17:34:49 UTC 2023
Sat Jun 24 17:34:54 UTC 2023
Sat Jun 24 17:34:59 UTC 2023
Sat Jun 24 17:35:04 UTC 2023
Sat Jun 24 17:35:09 UTC 2023
Sat Jun 24 17:35:14 UTC 2023


```
# namespace_based
## iam

### use_dedicated_service_accounts_for_each_deployment

```bash

```
## pod_security

https://bishopfox.com/blog/kubernetes-pod-privilege-escalation

### disallow_host_path_or_make_it_read_only

```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpath/pod/hostpath-exec-pod.yaml
kubectl exec -it hostpath-exec-pod -- bash
```

### use_encryption_with_aws_load_balancers

```bash
cd /home/ec2-user/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/network_security

kubectl apply -f lb-encryption.yaml
```
## encryption_secrets

### disallow_secrets_from_env_vars

```bash
~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/encryption_secrets (main) $ echo -n "username" | base64                                                                                                                
dXNlcm5hbWU=
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/security/encryption_secrets (main) $ echo -n "password" | base64                                                                                                                
cGFzc3dvcmQ=
```
## runtime_security

### disallow_linux_capabilities


```bash
kubectl apply -f pod_linux_capabilities.yaml

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


