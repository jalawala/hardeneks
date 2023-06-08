###############################################################################
# All commands used to check the various audit values were sourced from the   #
# CIS Bottlerocket Benchmark v1.0.0 unless the command was unavailable in     #
# Alpine Linux, which was used as the base image for the validation container #
###############################################################################

echo "This tool validates the Amazon EKS optimized AMI against CIS Bottlerocket Benchmark v1.0.0"


contexts=(
"arn:aws:eks:us-east-1:000474600478:cluster/appmesh-workshop"
"arn:aws:eks:us-east-1:000474600478:cluster/aws-preprod-test-eks"
"arn:aws:eks:us-east-1:000474600478:cluster/aws-preprod-test-eks-waf-cluster"
"arn:aws:eks:us-east-1:000474600478:cluster/bottlerocket-cis-blog-eks"
"arn:aws:eks:us-east-1:000474600478:cluster/dev-us-east-1-blueprint"
"arn:aws:eks:us-east-1:000474600478:cluster/east-test-1"
"arn:aws:eks:us-east-1:000474600478:cluster/eks122"
"arn:aws:eks:us-east-1:000474600478:cluster/EKS-CLUSTER-A"
"arn:aws:eks:us-east-1:000474600478:cluster/EKS-CLUSTER-B"
"arn:aws:eks:us-east-1:000474600478:cluster/eks-tetrate-istio"
"arn:aws:eks:us-east-1:000474600478:cluster/eks-waf-cluster"
"arn:aws:eks:us-east-1:000474600478:cluster/eksworkshop3"
"arn:aws:eks:us-east-1:000474600478:cluster/eksworkshop4"
"arn:aws:eks:us-east-1:000474600478:cluster/eksworkshop5"
"arn:aws:eks:us-east-1:000474600478:cluster/eksworkshop-eksctl"
"arn:aws:eks:us-east-1:000474600478:cluster/mgmt"
"arn:aws:eks:us-east-1:000474600478:cluster/multi-region-blog-eks1"
"arn:aws:eks:us-east-1:000474600478:cluster/prod-us-east-1-blueprint"
"arn:aws:eks:us-east-1:000474600478:cluster/test-us-east-1-blueprint"
"east"
"eksworkshop3"
"eksworkshop5"
"i-0d45e819f38a652ea@bottlerocket-cis-blog-eks.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eks122.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eks-cn-cluster-1.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eks-cn-cluster-2.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eks-cn-cluster-3.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eks-ref-cluster.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eksworkshop5.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@eksworkshop-eksctl.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@mgmt.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@multi-region-blog-eks1.us-east-1.eksctl.io"
"i-0d45e819f38a652ea@multi-region-blog-eks2.us-west-2.eksctl.io"
"i-0d45e819f38a652ea@my-ipv6-cluster.us-east-1.eksctl.io"
"west"
)

START=1
END=5

Num_Of_Clusters=1
 
for context in ${contexts[@]}; do
#for i in {$START..$END} do

 #      context=${contexts[$i]}
       echo "Running for cluster = $context"
       hardeneks --config ./hardeneks/config.yaml --debug --context $context > output_logs/"$Num_Of_Clusters".txt
       Num_Of_Clusters=$((Num_Of_Clusters+1))
       #kubectx $context
       #kubectl get nodes
done

#context="arn:aws:eks:us-east-1:000474600478:cluster/eksworkshop3"
#Num_Of_Clusters="12_error"
#hardeneks --config ./hardeneks/config.yaml --debug --context $context --run_only_namespace_level_checks --pillars security > output_logs/"$Num_Of_Clusters".txt
#hardeneks --config ./hardeneks/config.yaml --debug --context $context  --run_only_cluster_level_checks --pillars security > output_logs/"$Num_Of_Clusters".txt  



