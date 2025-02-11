from hardeneks.rules import Rule, Result
from ...resources import NamespacedResources
import pprint

class disallow_container_socket_mount(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "pod_security"
    message = "Never run Docker in Docker or mount the socket in the container"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#never-run-docker-in-docker-or-mount-the-socket-in-the-container"

    def check(self, namespaced_resources: NamespacedResources):
        offenders = []
        
        Info = "None of the Pods have socket mounts"

        sockets = [
            "/var/run/docker.sock",
            "/var/run/containerd.sock",
            "/var/run/crio.sock",
        ]

        for pod in namespaced_resources.pods:
            for volume in pod.spec.volumes:
                if volume.host_path and volume.host_path.path in sockets:
                    offenders.append(pod.metadata.name)

        
        if offenders:
            Info = "Pods with socket mounts : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Pod",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace, info=Info)

class disallow_host_path_or_make_it_read_only(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "pod_security"
    message = "Restrict the use of hostPath or if hostPath is necessary restrict which prefixes can be used and configure the volume as read-only"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#restrict-the-use-of-hostpath-or-if-hostpath-is-necessary-restrict-which-prefixes-can-be-used-and-configure-the-volume-as-read-only"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        
        Info = "None of the Pods have Restrict hostpath"

        for pod in namespaced_resources.pods:
            for volume in pod.spec.volumes:
                
                if volume.host_path:
                    volumeName = volume.name
                    #print("name={} volume={}".format(volume.name, volume.host_path))
                    
                    for container in pod.spec.containers:
                        #print("volume_mounts={}".format(container.volume_mounts))
                        for mount in container.volume_mounts:
                            if mount.name == volumeName:
                                read_only = mount.read_only
                                if read_only == True:
                                    Status = True
                                    #print(read_only)
                                else:
                                    Status = False
                                    offenders.append(pod.metadata.name)
                    
        if offenders:
            Info = "Pods without restricted hostpath : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Pod",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace, info=Info)

class set_requests_limits_for_containers(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "pod_security"
    message = "Set requests and limits for each container to avoid resource contention and DoS attacks"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#set-requests-and-limits-for-each-container-to-avoid-resource-contention-and-dos-attacks"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        for pod in namespaced_resources.pods:
            for container in pod.spec.containers:
                if not (
                    container.resources.limits and container.resources.requests
                ):
                    offenders.append(pod.metadata.name)

        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace)
            

class disallow_privilege_escalation(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "pod_security"
    message = "Do not allow privileged escalation"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#do-not-allow-privileged-escalation"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []

        for pod in namespaced_resources.pods:
            for container in pod.spec.containers:
                if (
                    container.security_context
                    and container.security_context.allow_privilege_escalation
                ):
                    offenders.append(pod.metadata.name)

        
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace)
            

class check_read_only_root_file_system(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "pod_security"
    message = "Configure your images with a read-only root file system."
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#configure-your-images-with-read-only-root-file-system"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        for pod in namespaced_resources.pods:
            for container in pod.spec.containers:
                if (
                    container.security_context
                    and not container.security_context.read_only_root_filesystem
                ):
                    offenders.append(pod.metadata.name)
                    
        if offenders:
            resource = " ".join(offenders)
            self.result = Result(
                status=False,
                resource_type="Pod",
                resources=[resource],
                namespace=namespaced_resources.namespace,
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace)
            
class disable_service_discovery(Rule):
    _type = "namespace_based"
    pillar = "security"
    section = "iam"
    message = "Disable service discovery"
    url = "https://aws.github.io/aws-eks-best-practices/security/docs/pods/#disable-service-discovery"

    def check(self, namespaced_resources: NamespacedResources):

        offenders = []
        Info = "All pods don't use coreDNS for Service Discovery"

        for pod in namespaced_resources.pods:
            #print(pprint.pformat(pod, indent=4))
            #print("pod = {} dnsPolicy = {} enable_service_links={}".format(pod.metadata.name, pod.spec.dns_policy, pod.spec.enable_service_links))
            
            if pod.spec.dns_policy != 'Default' and pod.spec.enable_service_links != False:
                offenders.append(pod.metadata.name)
            
        if offenders:
            Info = "Pods using coreDNS for Service Discovery : " + " ".join(offenders) 
            self.result = Result(
                status=False,
                resource_type="Pod",
                namespace=namespaced_resources.namespace,
                info = Info
            )
        else:
            self.result = Result(status=True, resource_type="Pod", namespace=namespaced_resources.namespace, info=Info)

            
            