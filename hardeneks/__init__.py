from pathlib import Path
import os
from pkg_resources import resource_filename
import tempfile
import yaml
import json
import sys
from collections import defaultdict
import pprint

from botocore.exceptions import EndpointConnectionError
import boto3
import kubernetes
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import typer
import boto3

from .resources import (
    NamespacedResources,
    Resources,
)
from .harden import harden
from hardeneks import helpers

app = typer.Typer()
console = Console(record=True)

pillarsList = []
rulesList = []
ignoredNSList = []
sectionsMap = {}

defaultSectionsMap = {
    'cluster_data': ['cluster_data'],
    'security': ['iam', 'multi_tenancy', 'detective_controls', 'network_security', 'encryption_secrets', 'infrastructure_security', 'pod_security', 'image_security'],
    'reliability': ['applications'],
    'scalability': ['control_plane'],
    'cluster_autoscaling': ['cluster_autoscaler'],
    'networking': ['vpc_subnets', 'vpc-cni', 'prefix_mode', 'load-balancing'],
}
 
def _config_callback(value: str):

    config = Path(value)

    if config.is_dir():
        raise typer.BadParameter(f"{config} is a directory")
    elif not config.exists():
        raise typer.BadParameter(f"{config} doesn't exist")

    with open(value, "r") as f:
        try:
            yaml.safe_load(f)
        except yaml.YAMLError as exc:
            raise typer.BadParameter(exc)

    return value


def _get_cluster_name_from_context(clusterNameStr):
    
    if clusterNameStr.endswith('eksctl.io'):
        clusterName = clusterNameStr.split('.')[0]
    elif clusterNameStr.startswith('arn:'):
        clusterName = clusterNameStr.split('/')[-1]    
    else:
        clusterName = clusterNameStr
        
    return clusterName
    
    
    
def _get_cluster_context_and_name(contextFromUser, clusterFromUser):
    
    contextName = None
    clusterName = None
    
    #print("contextFromUser={} clusterFromUser={}".format(contextFromUser, clusterFromUser))    
    
    contextList, active_context = kubernetes.config.list_kube_config_contexts()
    
    #print(pprint.pformat(active_context, indent=4))
    #print(pprint.pformat(contextList, indent=4))
    
    if contextFromUser:
        contextName = contextFromUser
        if clusterFromUser:
            clusterName = clusterFromUser
        else:
            for contextData in contextList:
                #print("contextData={}".format(contextData))
                if contextData['name'] == contextFromUser:
                    clusterName = _get_cluster_name_from_context(contextData['context']['cluster'])
    else:
        if clusterFromUser:
            clusterName = clusterFromUser
            for contextData in contextList:
                clusterNameFromContext = _get_cluster_name_from_context(contextData['context']['cluster'])
                #print("clusterNameFromContext={} clusterFromUser={}".format(clusterNameFromContext, clusterFromUser))
                if clusterNameFromContext ==  clusterFromUser:
                    contextName = contextData['name']
                    print("contextName={}".format(contextName))
                    
        else:
            contextName = active_context['name']
            clusterName = _get_cluster_name_from_context(active_context['context']['cluster'])
    
    
    if  contextName and clusterName:
        #print("contextName={} clusterName={}".format(contextName, clusterName))
        return (contextName, clusterName)
    else:
        print("contextName={} and clusterName={} are not valid. Exiting the program".format(contextName, clusterName)) 
        sys.exit()


def _get_current_context(context):
    if context:
        return context
    _, active_context = kubernetes.config.list_kube_config_contexts()
    return active_context["name"]


def _get_filtered_namespaces(ignored_ns: list, selected_namespaces: str) -> list:
    v1 = kubernetes.client.CoreV1Api()
    all_namespaces_in_cluster = [i.metadata.name for i in v1.list_namespace().items]

    if not selected_namespaces:
        namespaces = list(set(all_namespaces_in_cluster) - set(ignored_ns))
    else:
        namespaces_not_available_in_cluster = []
        selected_namespaces_list = selected_namespaces.split(',')
        for ns in selected_namespaces_list:
            if ns not in all_namespaces_in_cluster:
                print("namespace {} does not exist in cluster. Removing it from the list".format(ns))
                namespaces_not_available_in_cluster.append(ns)
        
        namespaces = list(set(selected_namespaces_list) - set(namespaces_not_available_in_cluster))
        
    return namespaces



def _get_namespaces(ignored_ns: list) -> list:
    v1 = kubernetes.client.CoreV1Api()
    namespaces = [i.metadata.name for i in v1.list_namespace().items]
    return list(set(namespaces) - set(ignored_ns))


def _get_cluster_name(context, region):
    try:
        client = boto3.client("eks", region_name=region)
        for name in client.list_clusters()["clusters"]:
            if name in context:
                return name
    except EndpointConnectionError:
        raise ValueError(f"{region} seems like a bad region name")

def _get_default_pillars() -> list:
    return ["cluster_data", "security", "reliability", "cluster_autoscaling", "scalability"]

def _get_default_sections() -> list:
    return defaultSectionsMap

def get_pillars_list() -> list:
    return pillarsList
    
def _get_region():
    return boto3.session.Session().region_name


def _add_tls_verify():
    kubeconfig = helpers.get_kube_config()
    tmp_config = tempfile.NamedTemporaryFile().name

    for cluster in kubeconfig["clusters"]:
        cluster["cluster"]["insecure-skip-tls-verify"] = True
    with open(tmp_config, "w") as fd:
        yaml.dump(kubeconfig, fd, default_flow_style=False)

    kubernetes.config.load_kube_config(tmp_config)
    os.remove(tmp_config)


def _export_json(rules: list, json_path=str):
    def ndd():
        return defaultdict(ndd)

    json_blob = ndd()

    for rule in rules:
        result = {
            "status": rule.result.status,
            "resources": rule.result.resources,
            "resource_type": rule.result.resource_type,
            "namespace": rule.result.namespace,
        }
        json_blob[rule._type][rule.pillar][rule.section][rule.message] = result
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_blob, f, ensure_ascii=False, indent=4)


def print_consolidated_results(rules: list, show_rules_status_color: str):

    pillars = set([i.pillar for i in rules])


    for pillar in pillars:
        table = Table()
        table.add_column("Section")
        table.add_column("Namespace")
        table.add_column("Rule Name")
        table.add_column("Rule Description")
        table.add_column("Info")
        table.add_column("Resource", no_wrap=False)
        table.add_column("Resource Type")
        table.add_column("Resolution")
        filtered_rules = [i for i in rules if i.pillar == pillar]
        total_no_of_rules = len (filtered_rules)
        no_of_rules_passed = 0
        for rule in filtered_rules:
            color = "red"
            namespace = "Cluster Wide"
            if rule.result.status:
                color = "green"
                no_of_rules_passed += 1
                            
            if rule.result.namespace:
                namespace = rule.result.namespace
            
            #print("rule.result.namespace={} namespace={} rule.result.resources={}".format(rule.result.namespace, namespace, rule.result.resources))
            
            for resource in rule.result.resources:
                if not show_rules_status_color:
                    #print("namespace={} rule.name={} adding a row in table for {}".format(namespace, rule.name, resource))
                    table.add_row(
                        rule.section,
                        namespace,
                        rule.name,
                        rule.message,
                        rule.result.info,
                        resource,
                        rule.result.resource_type,
                        f"[link={rule.url}]Link[/link]",
                        style=color,
                    )
                else:
                    if show_rules_status_color == color:
                        table.add_row(
                            rule.section,
                            namespace,
                            rule.name,
                            rule.message,
                            rule.result.info,
                            resource,
                            rule.result.resource_type,
                            f"[link={rule.url}]Link[/link]",
                            style=color,
                        )                        
        
        
        if show_rules_status_color == "red":
            titleMessage=f"[cyan][bold] Report for {pillar} pillar : {total_no_of_rules-no_of_rules_passed}/{total_no_of_rules} rules failed"
        else:
            titleMessage=f"[cyan][bold] Report for {pillar} pillar : {no_of_rules_passed}/{total_no_of_rules} rules passed"
        console.print(Panel(table, title=titleMessage, title_align="left"))
        console.print()


@app.command()
def run_hardeneks(
    region: str = typer.Option(
        default=None, help="AWS region of the cluster. Ex: us-east-1"
    ),
    context: str = typer.Option(
        default=None,
        help="K8s context.",
    ),
    cluster: str = typer.Option(default=None, help="Cluster name."),
    namespace: str = typer.Option(
        default=None,
        help="Specific namespace to harden. Default is all namespaces.",
    ),
    config: str = typer.Option(
        default=resource_filename(__name__, "config.yaml"),
        callback=_config_callback,
        help="Path to a hardeneks config file.",
    ),
    export_txt: str = typer.Option(
        default=None,
        help="Export the report in txt format",
    ),
    export_html: str = typer.Option(
        default=None,
        help="Export the report in html format",
    ),
    export_json: str = typer.Option(
        default=None, help="Export the report in json format"
    ),
    insecure_skip_tls_verify: bool = typer.Option(
        False,
        "--insecure-skip-tls-verify",
    ),
    pillars: str = typer.Option(
        default=None,
        help="Specific list of pillars to harden. Default is all pillars.",
    ),
    sections: str = typer.Option(
        default=None,
        help="Specific list of sections for a given pillar to harden. Default is all sections. --pillars option must be used specifying only one pillar",
    ),
    rules: str = typer.Option(
        default=None,
        help="Specific list of rules to harden. Default is all rules. --pillars, --sections and one of options (--only_cluster_level_rules or --only_namespace_level_rules) must be set",
    ),    
    only_cluster_level_rules: bool = typer.Option(
        False,
        "--only_cluster_level_rules",
        help="To run checks only for cluster levels rules specified in config.yaml file.",
    ),
    only_namespace_level_rules: bool = typer.Option(
        False,
        "--only_namespace_level_rules",
        help="To run checks only for namespaced levels rules specified in config.yaml file.",
    ),
    only_show_passed_rules_report: bool = typer.Option(
        False,
        "--only_show_passed_rules_report",
        help="To show only passed rules in the final displayed report.",
    ),
    only_show_failed_rules_report: bool = typer.Option(
        False,
        "--only_show_failed_rules_report",
        help="To show only failed rules in the final displayed report.",
    ),
    
):
    """
    Main entry point to hardeneks.

    Args:
        region (str): AWS region of the cluster. Ex: us-east-1
        context (str): K8s context
        cluster (str): Cluster name
        namespace (str): Specific namespace to be checked
        config (str): Path to hardeneks config file
        export-txt (str): Export the report in txt format
        export-html (str): Export the report in html format
        export-json (str): Export the report in json format
        insecure-skip-tls-verify (str): Skip tls verification

    Returns:
        None

    """
    global pillarsList, ignoredNSList, sectionsMap, rulesList
    
    (context, cluster) = _get_cluster_context_and_name(context, cluster)
    
    if insecure_skip_tls_verify:
        _add_tls_verify()
    else:
        # should pass in config file
        kubernetes.config.load_kube_config(context=context)

    #context = _get_current_context(context)

    #if not cluster:
        #cluster = _get_cluster_name(context, region)
    
    

    if not region:
        region = _get_region()

    console.rule("[b]HARDENEKS", characters="*  ")
    console.print(f"You are operating at {region}")
    console.print(f"Your context used is {context}")
    console.print(f"Your cluster name is {cluster}")
    console.print(f"You are using {config} as your config file")
    console.print()

    with open(config, "r") as f:
        config = yaml.safe_load(f)

    #if not namespace:
        #namespaces = _get_namespaces(config["ignore-namespaces"])
    #else:
        #namespaces = [namespace]
        #namespaces = namespace.split(',')
    
    ignoredNSList = config["ignore-namespaces"]
    namespaces = _get_filtered_namespaces(ignoredNSList, namespace)
    

    #print("namespaces={}".format(namespaces))
    #namespaces = _get_namespaces(config["ignore-namespaces"])
    #print("namespaces={}".format(_get_namespaces(config["ignore-namespaces"])))
        
    if not pillars:
        pillarsList = _get_default_pillars()
    else:
        pillarsList = pillars.split(',')
        
    if not sections:
        sectionsMap = _get_default_sections()
    else:
        if not pillars:
            print("--pillars option must be used specifying only one pillar, when using --sections option. Exiting...")
            sys.exit()
        else:
            if len(pillarsList) > 1:
                print("Specify only one pillar with --pillars option when using --sections option. Exiting...")
                sys.exit()
        pillar = pillarsList[0]
        sectionsList = sections.split(',')
        sectionsMap[pillar] = sectionsList

    rulesMap = config["rules"]
    
    if not rules:
        rulesList = None
    else:
        if not pillars:
            print("--pillars option must be used specifying only one pillar, when using --rules option. Exiting...")
            sys.exit()
        else:
            if len(pillarsList) > 1:
                print("Specify only one pillar with --pillars option when using --rules option. Exiting...")
                sys.exit()
            else:
                pillar = pillarsList[0]
                
        if not sections:
            print("--sections option must be used specifying only one section, when using --rules option. Exiting...")
            sys.exit()
        else:
            if len(sectionsList) > 1:
                print("Specify only one section with --sections option when using --rules option. Exiting...")
                sys.exit()
            else:
                section = sectionsList[0]
                
        if not (only_namespace_level_rules or only_cluster_level_rules):
            print("one of options (--only_cluster_level_rules or --only_namespace_level_rules) must be set when using --rules option. Exiting...")
            sys.exit()
        elif only_namespace_level_rules:
            _type = "namespace_based"
        elif only_cluster_level_rules:
            _type = "cluster_wide"
            
        rulesPerSectionPerPillarList = rulesMap[_type][pillar][section]
        
        rulesList = rules.split(',')
        
        for rule in rulesList:
            if rule not in rulesPerSectionPerPillarList:
                print("Given Rule {} does not exist in Section {} in Pillar {} at Scope {}. Please check config.yaml. Exiting...".format(rule, section, pillar, _type))
                sys.exit()

            
    
    if only_show_passed_rules_report:
        show_rules_status_color = "green"
    elif only_show_failed_rules_report:
        show_rules_status_color = "red"
    else:
        show_rules_status_color = None
        
        
    try:
        eksclient = boto3.client("eks", region_name=region)
        cluster_metadata = eksclient.describe_cluster(name=cluster)
    except Exception as exc:
        print("The cluster {} does not exist in the region {}. Specify right cluster or region name. Error Message: {}".format(cluster, region, exc))
        sys.exit()
        
                
    #print("Running hardeneks for selected pillars list={}, sectionsMap={} and namespaces={} rulesList={}".format(pillarsList, sectionsMap, namespaces, rulesList))
    
    resources = Resources(region, context, cluster, namespaces)
    resources.set_resources()
    

        



    results = []

    if not only_namespace_level_rules:
        console.rule("[b]Checking cluster wide rules", characters="- ")
        console.print()  
        cluster_wide_results = harden(resources, rulesMap, "cluster_wide")
        results = results + cluster_wide_results
    #print("results={}".format(results))

    if not only_cluster_level_rules:
        console.rule("[b]Checking Namespace wide rules", characters="- ")
        console.print()
        for ns in namespaces:
            resources = NamespacedResources(region, context, cluster, ns)
            resources.set_resources()
            #print("calling harden for ns={}".format(ns))
            namespace_based_results = harden(resources, rulesMap, "namespace_based")
            #print("ns={} namespace_based_results={}".format(ns, namespace_based_results))
            #print_consolidated_results(namespace_based_results)
            results = results + namespace_based_results

    console.rule("[b]Generating the Consolidated Report", characters="- ")
    console.print()
    
    print_consolidated_results(results, show_rules_status_color)
    
    #print("export_txt={} export_html={} export_json={}".format(export_txt, export_html, export_json))

    if export_txt:
        console.save_text(export_txt)
    if export_html:
        #print("results={}".format(results))
        console.save_html(export_html)
    if export_json:
        _export_json(results, export_json)

    console.print()