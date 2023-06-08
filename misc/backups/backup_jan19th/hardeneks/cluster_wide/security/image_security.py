import boto3

from ...report import print_repository_table
from ...resources import Resources


def use_immutable_tags_with_ecr(resources: Resources):
    status = None
    objectsList = []
    objectType = "Repository"
    message = ""

    client = boto3.client("ecr", region_name=resources.region)
    repositories = client.describe_repositories()
    for repository in repositories["repositories"]:
        if repository["imageTagMutability"] != "IMMUTABLE":
            objectsList.append(repository)

    if objectsList:
        status = False
        message = "Make image tags immutable"
    else:
        status = True
        message = "Image tags are immutable"
    
    return (status, message, objectsList, objectType)
    
