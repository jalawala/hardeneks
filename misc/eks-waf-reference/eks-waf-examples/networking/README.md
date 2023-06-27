# networking


# namespace_based

### load-balancing


```bash
eks126
cd /jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/networking/load-balancing

kubectl apply -f lb-svc-ip-mode.yaml

```
### use_pod_readiness_gate

```bash
jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/networking/load-balancing (main) $ kubectl create ns lb
namespace/lb created

kubectl label namespace lb elbv2.k8s.aws/pod-readiness-gate-inject=enabled

jp:~/environment $ kubectl label namespace lb elbv2.k8s.aws/pod-readiness-gate-inject=enabled
namespace/lb labeled

kubectl describe namespace lb

First create service or ingress
kubectl apply -f lb-svc-ip-mode-svc.yaml

and then create deployments

kubectl apply -f lb-svc-ip-mode-deploy.yaml



jp:~/environment $ kubectl -n lb get pod nginx-6f876d7d7d-hvl99 -oyaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    vpc.amazonaws.com/pod-ips: 192.168.123.3
  creationTimestamp: "2023-06-26T17:45:58Z"
  generateName: nginx-6f876d7d7d-
  labels:
    app: lb-svc-ip-node
    pod-template-hash: 6f876d7d7d
  name: nginx-6f876d7d7d-hvl99
  namespace: lb
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: nginx-6f876d7d7d
    uid: 968a7fde-b163-46fc-a344-7baa8dfe4006
  resourceVersion: "15607778"
  uid: 17159d80-32bc-4910-a6d8-70856c27840c
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-lj8lp
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: ip-192-168-113-123.ec2.internal
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  readinessGates:
  - conditionType: target-health.elbv2.k8s.aws/k8s-lb-lbsvcipn-1596fa5c23
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-lj8lp
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-06-26T17:46:03Z"
    message: Target registration is in progress
    reason: Elb.RegistrationInProgress
    status: "False"
    type: target-health.elbv2.k8s.aws/k8s-lb-lbsvcipn-1596fa5c23
  - lastProbeTime: null
    lastTransitionTime: "2023-06-26T17:45:58Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-06-26T17:45:58Z"
    message: the status of pod readiness gate "target-health.elbv2.k8s.aws/k8s-lb-lbsvcipn-1596fa5c23"
      is not "True", but False
    reason: ReadinessGatesNotReady
    status: "False"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2023-06-26T17:46:03Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-06-26T17:45:58Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: containerd://4a7888a7ee3f8122c4c881474a280b481ab8803e53818404a4573d80b33aded4
    image: docker.io/library/nginx:latest
    imageID: docker.io/library/nginx@sha256:593dac25b7733ffb7afe1a72649a43e574778bf025ad60514ef40f6b5d606247
    lastState: {}
    name: nginx
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2023-06-26T17:46:02Z"
  hostIP: 192.168.113.123
  phase: Running
  podIP: 192.168.123.3
  podIPs:
  - ip: 192.168.123.3
  qosClass: BestEffort
  startTime: "2023-06-26T17:45:58Z"
jp:~/environment $ 


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


