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
            #print(pprint.pformat(repository, indent=4))
            #exit()
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
                        
            