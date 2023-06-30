from rich import print

from ...resources import NamespacedResources
from ...report import print_pod_table


def disallow_linux_capabilities(namespaced_resources: NamespacedResources):
    
    status = None
    objectsList = []
    objectType = "Pod"
    message = ""
    
    allowed_list = [
        "AUDIT_WRITE",
        "CHOWN",
        "DAC_OVERRIDE",
        "FOWNER",
        "FSETID",
        "KILL",
        "MKNOD",
        "NET_BIND_SERVICE",
        "SETFCAP",
        "SETGID",
        "SETPCAP",
        "SETUID",
        "SYS_CHROOT",
    ]
    
    #print("pods={}".format(namespaced_resources.pods))
    
    for pod in namespaced_resources.pods:
        #print("namespace={} pod={} containers={}".format(namespaced_resources.namespace, pod.metadata.name, pod.spec.containers))
        for container in pod.spec.containers:
            if (
                container.security_context
                and container.security_context.capabilities
            ):
                #print("add={}".format(container.security_context.capabilities.add))
                if container.security_context.capabilities.add:
                    capabilities = set(container.security_context.capabilities.add)
                    #print("capabilities={}".format(capabilities))
                    if not capabilities.issubset(set(allowed_list)):
                        objectsList.append(pod)

    if objectsList:
        status = False
        message = "Capabilities beyond the allowed list are allowed"
    else:
        status = True
        message = "Capabilities beyond the allowed list are disallowed"
    
    #print("objectsList={}".format(objectsList))
    return (status, message, objectsList, objectType)



