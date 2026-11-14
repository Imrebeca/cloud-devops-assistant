# Kubernetes Deployments

Source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

## Overview

A Deployment is a Kubernetes resource that manages replicated applications using ReplicaSets.

It provides declarative updates for Pods and allows applications to maintain a desired number of replicas.

## Main Features

- Manages ReplicaSets and Pods.
- Maintains the desired number of replicas.
- Supports rolling updates.
- Supports rollback to previous revisions.
- Provides declarative application updates.

## Replica Management

A Deployment defines the desired number of Pod replicas.

Kubernetes continuously monitors the current state and attempts to match it with the desired state.

## Rolling Updates

Rolling updates allow new application versions to be deployed gradually.

This reduces application downtime during updates.

## Rollbacks

A Deployment can revert to a previous revision when an update causes problems.

## Common Commands

```bash
kubectl get deployments
kubectl describe deployment DEPLOYMENT_NAME
kubectl rollout status deployment/DEPLOYMENT_NAME
kubectl rollout history deployment/DEPLOYMENT_NAME
kubectl rollout undo deployment/DEPLOYMENT_NAME
```

## Deployment YAML Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

## Important Considerations

- Deployments are commonly used for stateless applications.
- ReplicaSets ensure the desired number of Pods.
- Readiness and liveness probes can improve application reliability.
- Resource requests and limits should be configured appropriately.