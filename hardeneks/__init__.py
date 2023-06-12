import os
from pathlib import Path
from pkg_resources import resource_filename
import tempfile
import yaml
import json
from collections import defaultdict

from botocore.exceptions import EndpointConnectionError
import boto3
import kubernetes
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import typer

from .resources import (
    NamespacedResources,
    Resources,
)
from .harden import harden
from hardeneks import helpers

app = typer.Typer()
console = Console(record=True)

pillarsList = []

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


def _get_current_context(context):
    if context:
        return context
    _, active_context = kubernetes.config.list_kube_config_contexts()
    return active_context["name"]


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


def print_consolidated_results(rules: list):

    pillars = set([i.pillar for i in rules])


    for pillar in pillars:
        table = Table()
        table.add_column("Section")
        table.add_column("Namespace")
        table.add_column("Rule Name")
        table.add_column("Rule Description")
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
            
            #print("rule.result.namespace={} namespace={}".format(rule.result.namespace, namespace))
            
            for resource in rule.result.resources:
                table.add_row(
                    rule.section,
                    namespace,
                    rule.name,
                    rule.message,
                    resource,
                    rule.result.resource_type,
                    f"[link={rule.url}]Link[/link]",
                    style=color,
                )
        
        titleMessage=f"[cyan][bold] Report for {pillar} piller : {no_of_rules_passed}/{total_no_of_rules} rules passed"
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
        help="Specific pillars to harden. Default is all pillars.",
    ),
    only_cluster_level_rules: bool = typer.Option(
        False,
        "--only_cluster_level_rules",
    ),
    only_namespace_level_rules: bool = typer.Option(
        False,
        "--only_namespace_level_rules",
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
    global pillarsList
    
    if insecure_skip_tls_verify:
        _add_tls_verify()
    else:
        # should pass in config file
        kubernetes.config.load_kube_config(context=context)

    context = _get_current_context(context)

    if not cluster:
        cluster = _get_cluster_name(context, region)

    if not region:
        region = _get_region()

    console.rule("[b]HARDENEKS", characters="*  ")
    console.print(f"You are operating at {region}")
    console.print(f"You context used is {context}")
    console.print(f"Your cluster name is {cluster}")
    console.print(f"You are using {config} as your config file")
    console.print()

    with open(config, "r") as f:
        config = yaml.safe_load(f)

    if not namespace:
        namespaces = _get_namespaces(config["ignore-namespaces"])
    else:
        #namespaces = [namespace]
        namespaces = namespace.split(',')
    
    print("namespaces={}".format(namespaces))
        
    if not pillars:
        pillarsList = _get_default_pillars()
    else:
        pillarsList = pillars.split(',')
                
    print("pillarsList={} namespaces={}".format(pillarsList, namespaces))
    
    rules = config["rules"]

    resources = Resources(region, context, cluster, namespaces)
    resources.set_resources()

    results = []

    if not only_namespace_level_rules:
        console.rule("[b]Checking cluster wide rules", characters="- ")
        console.print()  
        cluster_wide_results = harden(resources, rules, "cluster_wide")
        results = results + cluster_wide_results
    #print("results={}".format(results))

    if not only_cluster_level_rules:
        console.rule("[b]Checking Namespace wide rules", characters="- ")
        console.print()
        for ns in namespaces:
            resources = NamespacedResources(region, context, cluster, ns)
            resources.set_resources()
            #print("calling harden for ns={}".format(ns))
            namespace_based_results = harden(resources, rules, "namespace_based")
            #print("ns={} namespace_based_results={}".format(ns, namespace_based_results))
            #print_consolidated_results(namespace_based_results)
            results = results + namespace_based_results

    console.rule("[b]Generating the Consolidated Report", characters="- ")
    console.print()
    
    print_consolidated_results(results)

    if export_txt:
        console.save_text(export_txt)
    if export_html:
        console.save_html(export_html)
    if export_json:
        _export_json(results, export_json)
