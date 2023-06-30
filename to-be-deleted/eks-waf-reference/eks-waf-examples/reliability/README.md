# reliability


# namespace_based

## applications

### check_horizontal_pod_autoscaling_exists


```bash
cd jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/reliability/applications
kubectl autoscale deployment deploy1 --cpu-percent=50 --min=1 --max=10
kubectl apply -f hpa1.yaml
```
### schedule_replicas_across_nodes


```bash
kubectl apply -f topology.yaml

```
### check_pod_disruption_budgets

```bash
cd jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/reliability/applications

```
### use_nodeLocal_DNSCache

```bash
cd /home/ec2-user/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/reliability/data_plane

kubedns=`kubectl get svc kube-dns -n kube-system -o jsonpath={.spec.clusterIP}`
domain=cluster.local
localdns=169.254.20.10
sed -i "s/__PILLAR__LOCAL__DNS__/$localdns/g; s/__PILLAR__DNS__DOMAIN__/$domain/g; s/__PILLAR__DNS__SERVER__/$kubedns/g" nodelocaldns.yaml


jp:~/environment/jalawala/hardeneks/misc/eks-waf-reference/eks-waf-examples/reliability/data_plane (main) $ kubectl create -f nodelocaldns.yaml
serviceaccount/node-local-dns created
service/kube-dns-upstream created
configmap/node-local-dns created
daemonset.apps/node-local-dns created
service/node-local-dns created






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


