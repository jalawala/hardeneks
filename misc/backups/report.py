from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich import print


colorMap = {
      True: "green", 
      False: "red" 
}

ruledocsLinkMap = {
    "check_any_cluster_autoscaler_exists": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/",
    "ensure_cluster_autoscaler_and_cluster_versions_match": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/",
    "ensure_cluster_autoscaler_has_autodiscovery_mode": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/",
    "ensure_cluster_autoscaler_has_three_replicas": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/",
    "use_separate_iam_role_for_cluster_autoscaler": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#employ-least-privileged-access-to-the-iam-role",
    "employ_least_privileged_access_to_the_IAM_role": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#employ-least-privileged-access-to-the-iam-role",
    "use_managed_nodegroups": "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/",
    "ensure_uniform_instance_types_in_nodegroups":   "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/",
    
        
    "consider_public_and_private_mode": "https://aws.github.io/aws-eks-best-practices/networking/subnets/#consider-public-and-private-mode-for-cluster-endpoint",
    "deploy_vpc_cni_managed_add_on": "https://aws.github.io/aws-eks-best-practices/networking/vpc-cni/#deploy-vpc-cni-managed-add-on",
    "use_separate_iam_role_for_cni": "https://aws.github.io/aws-eks-best-practices/networking/vpc-cni/#use-separate-iam-role-for-cni",
    "monitor_IP_adress_inventory": "https://aws.github.io/aws-eks-best-practices/networking/vpc-cni/#monitor-ip-address-inventory",
    "use_dedicated_and_small_subnets_for_cluster_creation": "https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html",
    
        
    "EKS WAF BENCH Report for Pillar : cluster-autoscaling": "https://aws.github.io/aws-eks-best-practices/",
    "EKS WAF BENCH Report for Pillar : networking": "https://aws.github.io/aws-eks-best-practices/"
}

console = Console()


def print_role_table(roles, message, docs, type):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for role in roles:
        table.add_row(type, role.metadata.namespace, role.metadata.name)

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_instance_metadata_table(instances, message, docs):
    table = Table()

    table.add_column("InstanceId", style="cyan")
    table.add_column("HttpPutResponseHopLimit", style="magenta")

    for instance in instances:
        table.add_row(
            instance["Instances"][0]["InstanceId"],
            str(
                instance["Instances"][0]["MetadataOptions"][
                    "HttpPutResponseHopLimit"
                ]
            ),
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_instance_public_table(instances, message, docs):
    table = Table()

    table.add_column("InstanceId", style="cyan")
    table.add_column("PublicDnsName", style="magenta")

    for instance in instances:
        table.add_row(
            instance["Instances"][0]["InstanceId"],
            str(instance["Instances"][0]["PublicDnsName"]),
        )

    print(Panel(table, title=message))
    console.print()


def print_repository_table(repositories, attribute, message, docs):
    table = Table()
    table.add_column("Repository", style="cyan")
    table.add_column(attribute, style="magenta")
    for repository in repositories:
        table.add_row(
            repository["repositoryName"],
            repository[attribute],
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_pod_table(pods, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for pod in pods:
        table.add_row("Pod", pod.metadata.namespace, pod.metadata.name)

    print(Panel(table, title=message, subtitle=docs))
    console.print()

        
        
#def print_console_message(objectsList, kind, color, rule, message, docs_link):
def print_console_message(ret, rule, message, objectsList, kind):    
    
    color = colorMap[ret]
    colorStr = "[" + color + "]"
    ruleStr = "Rule: " + rule
    titleMessage = colorStr + ruleStr
    
    descriptionMessage = colorStr + message
    docs_link = ruledocsLinkMap[rule]
    docs_url = "[link=" + docs_link + "]Click to see the guide[/link]"

        
    if objectsList and kind:
        table = Table()
        if kind == "IP":
            table.add_column("SubnetId", style="cyan")
            table.add_column("CidrBlock", style="magenta")
            table.add_column("AvailableIpAddressCount", style="green")  
            totalAvailableIpAddressCount = 0
            for objectData in objectsList:
                table.add_row(objectData['SubnetId'], objectData['CidrBlock'], str(objectData['AvailableIpAddressCount']))
                totalAvailableIpAddressCount += objectData['AvailableIpAddressCount']
            table.add_row("", "[green]totalAvailableIpAddressCount", str(totalAvailableIpAddressCount))    
        elif kind == "CIDR":
            table.add_column("SubnetId", style="cyan")
            table.add_column("CidrBlock", style="magenta")
            for objectData in objectsList:
                table.add_row(objectData['SubnetId'], objectData['CidrBlock'])
        elif kind == "Report":
            
            
            
            titleMessage = colorStr + rule
            totalNumOfRules = len(objectsList[message]['pass']) + len(objectsList[message]['fail'])
            sno=1
            table.add_column("S.No", style="cyan")
            table.add_column("Rule", style="magenta")
            table.add_column("Status", style="green")
            table.add_column("Message", style="yellow")
            #for i, objectData in enumerate(objectsList[message]['pass']):
            for objectData in objectsList[message]['pass']:
                table.add_row("[green]"+str(sno)+"/"+str(totalNumOfRules), "[green]"+objectData, "[green]PASS")
                sno += 1
            for objectData in objectsList[message]['fail']:
                table.add_row("[red]"+str(sno)+"/"+str(totalNumOfRules), "[red]"+objectData, "[red]FAIL")
                sno += 1                
        else:
            table.add_column("Kind", style="cyan")
            table.add_column("Namespace", style="magenta")
            table.add_column("Name", style="green")        
            for objectData in objectsList:
                table.add_row(kind, objectData.metadata.namespace, objectData.metadata.name)

        print(Panel(renderable=table, title=titleMessage, subtitle=docs_url))
        #print(Panel(renderable=outputMessage, title=outputMessage, subtitle=docs_url))
    else:
        print(Panel(renderable=descriptionMessage, title=titleMessage, subtitle=docs_url))
        
    console.print()




def print_workload_table(workloads, message, docs, kind):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for workload in workloads:
        table.add_row(
            kind, workload.metadata.namespace, workload.metadata.name
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_namespace_table(namespaces, message, docs):
    table = Table()

    table.add_column("Namespace", style="cyan")

    for namespace in namespaces:
        table.add_row(
            namespace,
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_service_table(services, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for workload in services:
        table.add_row(
            "Service", workload.metadata.namespace, workload.metadata.name
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_deployment_table(deployments, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for workload in deployments:
        table.add_row(
            "Deployment", workload.metadata.namespace, workload.metadata.name
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_storage_class_table(storage_classes, message, docs):
    table = Table()

    table.add_column("StorageClass", style="cyan")
    table.add_column("Encyrpted", style="magenta")

    for storage_class in storage_classes:
        table.add_row(storage_class.metadata.name, "false")

    print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_persistent_volume_table(persistent_volumes, message, docs):
    table = Table()

    table.add_column("PersistentVolume", style="cyan")
    table.add_column("Encrypted", style="magenta")

    for persistent_volume in persistent_volumes:
        table.add_row(persistent_volume.metadata.name, "false")

    print(Panel(table, title=message, subtitle=docs))
    console.print()
