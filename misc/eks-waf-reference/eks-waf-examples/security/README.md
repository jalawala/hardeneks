# security
This contains various example codes for Amazon EKS

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


