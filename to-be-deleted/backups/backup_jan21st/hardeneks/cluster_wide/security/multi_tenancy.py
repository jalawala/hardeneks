from rich.console import Console

import copy

from ...resources import Resources

from ...report import (
    print_namespace_table,
)

console = Console()


def ensure_namespace_quotas_exist(resources: Resources):

    status = None
    objectsList = []
    objectType = "Namespace"
    message = ""
    #namespacelist = ''
    
    #objectsList = resources.namespaces
    objectsList = copy.deepcopy(resources.namespaces)
    
    #print("objectsList={}".format(objectsList))
    #print("resource_quotas={}".format(resources.resource_quotas))

    for quota in resources.resource_quotas:
        #print("namespace={} objectsList={}".format(quota.metadata.namespace, objectsList))
        if quota.metadata.namespace in objectsList:
            objectsList.remove(quota.metadata.namespace)        
    
    #print("objectsList={}".format(objectsList))
    if objectsList:
        status = False
        message = "Namespaces does not have quotas assigned"
    else:
        status = True
        message = "Namespaces have quotas assigned"
    
    return (status, message, objectsList, objectType)