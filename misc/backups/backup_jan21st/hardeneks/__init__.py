import os, sys
from pathlib import Path
from pkg_resources import resource_filename
import tempfile
import urllib3
import yaml

from botocore.exceptions import EndpointConnectionError
import boto3
import kubernetes
from kubernetes import client, config
from rich.console import Console
import typer

from .resources import (
    NamespacedResources,
    Resources,
)
from .harden import harden, cluster_data


app = typer.Typer()


def _config_callback(value: str):

    config = Path(value)

    if config.is_dir():
        raise typer.BadParameter(f"{config} is a directory")
    elif not config.exists():
        raise typer.BadParameter(f"{config} doesn't exist")

    with open(value, "r") as f:
        try:
            yaml.load(f, Loader=yaml.FullLoader)
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
    
        
    
def _get_current_context(contextFromUser, clusterFromUser):
    
    contextName = None
    clusterName = None
    
    #print("contextFromUser={} clusterFromUser={}".format(contextFromUser, clusterFromUser))    
    
    contextList, active_context = kubernetes.config.list_kube_config_contexts()
    
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
        #print("contextName={} and clusterName={} are not valid. Exiting the program".format(contextName, clusterName)) 
        sys.exit()


def _get_namespaces(ignored_ns: list, clustercontext) -> list:
    api_client_obj=config.new_client_from_config(context=clustercontext)
    v1 = kubernetes.client.CoreV1Api(api_client=api_client_obj)
    namespaces = [i.metadata.name for i in v1.list_namespace().items]
    return list(set(namespaces) - set(ignored_ns))

def _get_pillars() -> list:
    pillarsList = ["security", "reliability", "cluster-autoscaling", "networking"]
    return pillarsList
    
    
def _get_cluster_name(context, region):
    try:
        client = boto3.client("eks", region_name=region)
        for name in client.list_clusters()["clusters"]:
            #print("name={}".format(name))
            if name in context:
                return name
    except EndpointConnectionError:
        raise ValueError(f"{region} seems like a bad region name")


def _get_region():
    return boto3.session.Session().region_name


def _load_kube_config():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    kube_config_orig = f"{Path.home()}/.kube/config"
    tmp_config = tempfile.NamedTemporaryFile().name

    with open(kube_config_orig, "r") as fd:
        kubeconfig = yaml.load(fd, Loader=yaml.FullLoader)
    for cluster in kubeconfig["clusters"]:
        cluster["cluster"]["insecure-skip-tls-verify"] = True
    with open(tmp_config, "w") as fd:
        yaml.dump(kubeconfig, fd, default_flow_style=False)

    kubernetes.config.load_kube_config(tmp_config)
    os.remove(tmp_config)


@app.command()
def run_hardeneks(
    region: str = typer.Option(
        default=None, help="AWS region of the cluster. Ex: us-east-1"
    ),
    context: str = typer.Option(
        default=None,
        help="K8s context.",
    ),
    cluster: str = typer.Option(
        default=None, 
        help="Cluster name."
    ),
    namespace: str = typer.Option(
        default=None,
        help="Specific namespaces to harden. Default is all namespaces.",
    ),
    pillars: str = typer.Option(
        default=None,
        help="Specific pillars to harden. Default is all pillars.",
    ),    
    config: str = typer.Option(
        default=resource_filename(__name__, "config.yaml"),
        callback=_config_callback,
        help="Path to a hardeneks config file.",
    ),
    insecure_skip_tls_verify: bool = typer.Option(
        False,
        "--insecure-skip-tls-verify",
    ),
    run_only_cluster_level_checks: bool = typer.Option(
        False,
        "--run_only_cluster_level_checks",
    ),
    run_only_namespace_level_checks: bool = typer.Option(
        False,
        "--run_only_namespace_level_checks",
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
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
        insecure-skip-tls-verify (str): Skip tls verification

    Returns:
        None

    """
    
    (context, cluster) = _get_current_context(context, cluster)
    
    if insecure_skip_tls_verify:
        _load_kube_config()
    else:
        kubernetes.config.load_kube_config(context=context)

    

    #if not cluster:
    #    cluster = _get_cluster_name(context, region)

    if not region:
        region = _get_region()

    console = Console()
    console.rule("[b]HARDENEKS", characters="*  ")
    console.print(f"You are operating at {region}")
    console.print(f"You context is {context}")
    console.print(f"Your cluster name is {cluster}")
    console.print(f"You are using {config} as your config file")
    console.print()

    with open(config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        #print("config={}".format(config))

    #print("namespace={}".format(namespace))
    
    if not namespace:
        namespaces = _get_namespaces(config["ignore-namespaces"], context)
    else:
        #namespaces = [namespace]
        namespaces = namespace.split(',')
    
    if not pillars:
        pillarsList = _get_pillars()
    else:
        #namespaces = [namespace]
        pillarsList = pillars.split(',')
    
    #print("pillarsList={}".format(pillarsList))    
        
    #print("namespace={}".format(namespace))
    
    rules = config["rules"]

    #console.rule("[b]Checking cluster wide rules", characters="- ")
    #print()

    #if not run_only_namespace_level_checks:
    resources = Resources(region, context, cluster, namespaces, debug)
    resources.set_resources()
    cluster_data(resources, rules, "cluster_wide")
        
    
    if not run_only_namespace_level_checks:
        #resources = Resources(region, context, cluster, namespaces, debug)
        #resources.set_resources()
        harden(resources, rules, "cluster_wide", pillarsList)

    if not run_only_cluster_level_checks:
        for ns in namespaces:
            #console.rule(f"[b]Checking rules against namespace: {ns}", characters=" -")
            #console.print()
            resources = NamespacedResources(region, context, cluster, ns, debug)
            resources.set_resources()
            harden(resources, rules, "namespace_based", pillarsList)
            console.print()
