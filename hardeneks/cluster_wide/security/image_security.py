import boto3

from ...resources import Resources
from hardeneks.rules import Rule, Result
import pprint


class use_immutable_tags_with_ecr(Rule):
    _type = "cluster_wide"
    pillar = "security"
    section = "image_security"
    message = "Make image tags immutable."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/image/#use-immutable-tags-with-ecr"

    def check(self, resources: Resources):
        offenders = []
        
        Info = "All ECR Repos have Immutable Tags"

        client = boto3.client("ecr", region_name=resources.region)
        repositories = client.describe_repositories()
        for repository in repositories["repositories"]:
            print(pprint.pformat(repository, indent=4))
            exit()
            if repository["imageTagMutability"] != "IMMUTABLE":
                offenders.append(repository["repositoryName"])
    
        if offenders:
            Info = "ECR Repos without Immutable Tags " + " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="ECR Repository",
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="ECR Repository", info = Info)
            

class scan_images_for_vulnerabilities(Rule):
    
    _type = "cluster_wide"
    pillar = "security"
    section = "image_security"
    message = "Scan images for vulnerabilities regularly"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/image/#scan-images-for-vulnerabilities-regularly"

    def check(self, resources: Resources):
        offenders = []
        
        Info = "All ECR Repos have scanOnPush Enabled"

        client = boto3.client("ecr", region_name=resources.region)
        repositories = client.describe_repositories()
        for repository in repositories["repositories"]:
            print(pprint.pformat(repository, indent=4))
            exit()
            imageScanningConfiguration = repository['imageScanningConfiguration']
            
            if imageScanningConfiguration["scanOnPush"] != "False":
                offenders.append(repository["repositoryName"])
    
        if offenders:
            Info = "ECR Repos with scanOnPush Disabled " + " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="ECR Repository",
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="ECR Repository", info = Info)
                        


class check_iam_iam_policies_for_ecr_repositories(Rule):
    
    
    _type = "cluster_wide"
    pillar = "security"
    section = "image_security"
    message = "Create IAM policies for ECR repositories"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/image/#create-iam-policies-for-ecr-repositories"

    def check(self, resources: Resources):
        offenders = []
        
        Info = "All ECR Repos have IAM Policies"
        
      

        ecrclient = boto3.client("ecr", region_name=resources.region)
        repositories = ecrclient.describe_repositories()
        for repository in repositories["repositories"]:
            
            #print(pprint.pformat(repository, indent=4))
            try:
                response = ecrclient.get_repository_policy(
                    registryId=repository["registryId"],
                    repositoryName=repository["repositoryName"]
                )
                #print("repositoryName={}".format(repository["repositoryName"]))
                #print(pprint.pformat(response['policyText'], indent=4))                
            except Exception as exc:
                offenders.append(repository["repositoryName"])

            #exit()

        if offenders:
            Info = "ECR Repos without IAM Policies " + " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="ECR Repository",
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="ECR Repository", info = Info)
                        


class consider_using_ecr_private_endpoints(Rule):
    
    _type = "cluster_wide"
    pillar = "security"
    section = "image_security"
    message = "Consider using ECR private endpoints"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/image/#consider-using-ecr-private-endpoints"

    def check(self, resources: Resources):
        offenders = []

        eksclient = boto3.client("eks", region_name=resources.region)
        cluster_metadata = eksclient.describe_cluster(name=resources.cluster)
        vpcId  = cluster_metadata["cluster"]["resourcesVpcConfig"]["vpcId"] 
        
        ec2client = boto3.client("ec2", region_name=resources.region)
        
        serviceNames = [ "com.amazonaws." + resources.region + ".ecr.dkr", 
                         "com.amazonaws." + resources.region + ".ecr.api"
                       ] 
        
        response = ec2client.describe_vpc_endpoints(
            Filters=[
                {
                    'Name': 'service-name',
                    'Values': serviceNames
                },
                {
                    'Name': 'vpc-id',
                    'Values': [vpcId]
                },                
            ],
        )

        #print(pprint.pformat(response, indent=4))
        vpc_endpoints = response['VpcEndpoints']
        
        if not vpc_endpoints:
            Status = False
            Info = "VPC Endpoint for ECR does not exist in VPC : {}".format(vpcId)
        else:
            Info = "VPC Endpoint for ECR does exist in VPC : {}".format(vpcId)
            
        
        self.result = Result(status=Status, resource_type="ECR Repository", info = Info)
                        
                                                