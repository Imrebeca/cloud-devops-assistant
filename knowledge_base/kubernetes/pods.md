# Kubernetes Pods

Source: https://kubernetes.io/docs/concepts/workloads/pods/

## Overview

A Pod is the smallest deployable unit in Kubernetes.

A Pod represents one or more containers that share network resources and storage.

## Pod Characteristics

- A Pod can contain one or multiple containers.
- Containers inside the same Pod share the same network namespace.
- Containers can communicate through localhost.
- Pods can share storage volumes.
- Pods are ephemeral and can be replaced by Kubernetes.

## Pod Lifecycle

A Pod can have different lifecycle phases:

- Pending: the Pod has been accepted but is not yet running.
- Running: at least one container is running.
- Succeeded: all containers completed successfully.
- Failed: all containers terminated and at least one failed.
- Unknown: the Pod state cannot be determined.

## Multi-container Pods

Multiple containers may run inside the same Pod when they need to work closely together.

Common patterns include:

- Sidecar: supports the main application.
- Ambassador: manages communication with external services.
- Adapter: transforms application output or data.

## Pod Networking

Each Pod receives its own IP address within the cluster network.

Containers inside the same Pod communicate using localhost.

## Pod Storage

Containers in a Pod can share volumes to exchange data or persist information during their lifecycle.

## Common Commands

```bash
kubectl get pods
kubectl describe pod POD_NAME
kubectl logs POD_NAME
kubectl delete pod POD_NAME
```

## Important Considerations

- Pods are usually managed by higher-level controllers.
- Deployments are commonly used to manage stateless application Pods.
- StatefulSets are used when stable identity and storage are required.
- Directly creating standalone Pods is generally less common in production environments.