# Building a Basic Kubernetes Cluster

**Platform:** Pluralsight  
**Level:** Beginner  
**Status:** Completed hands-on guided lab  
**Environment:** Single-node Kubernetes cluster with application workloads running on the control plane

## Overview

I completed Pluralsight's "Building a Basic Kubernetes Cluster" lab, practicing the setup of a Kubernetes control plane and the deployment of a web application. The exercise used a fictional Globomantics scenario to move a containerized application onto Kubernetes.

## Work completed

- Checked that kubeadm and kubectl were available and containerd was running.
- Confirmed swap was disabled before initializing the control plane.
- Initialized Kubernetes with kubeadm using the pod network CIDR `10.244.0.0/16`.
- Configured my user's kubeconfig and checked API server connectivity.
- Applied the provided Flannel CNI manifest to enable pod networking.
- Checked node readiness and system pod status.
- Removed the control-plane scheduling taint to allow workloads on the lab's single node.
- Created an nginx Deployment named `globomantics-web` and scaled it to two replicas.
- Exposed the Deployment through a NodePort Service.
- Tested HTTP access from the control plane using the Service's cluster IP and the assigned node port.

## Skills practiced

Kubernetes bootstrapping, kubeadm, kubectl, containerd, kubeconfig, CNI networking, Flannel, pod scheduling, taints, Deployments, replica scaling, Services, and basic connectivity checks.

## Key takeaways

- Initializing the control plane is only part of cluster setup: pod networking is needed before the node and dependent system components become ready.
- A Deployment manages application replicas, while a Service provides access to the application.
- Two replicas on one node demonstrate scaling but do not provide resilience against failure of that node.
- Removing the control-plane taint enabled this single-node exercise; it is a scheduling decision that deserves separate consideration in a production architecture.
- Kubeconfig grants access to the cluster and should be handled as sensitive configuration.

## Scope and evidence

This entry summarizes a guided lab I completed, based on my completion report and the supplied lab outline. No terminal captures, screenshots, or exported cluster resources are included here. The checks above describe the lab activities; this repository does not contain independent execution evidence.

The exercise covered foundational cluster operation. Production hardening, multi-node availability, RBAC design, network policies, and security monitoring were outside its scope.

## Attribution

Learning source: Pluralsight, **Building a Basic Kubernetes Cluster**. This is my portfolio summary of the exercise; the provider's full lab instructions are not reproduced.
