# Docker Containers

Source: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/

## Overview

A Docker container is a lightweight, isolated environment used to run applications and their dependencies.

Containers are created from Docker images and share the host operating system kernel.

## Container Characteristics

- Process isolation.
- Lightweight compared to virtual machines.
- Portable across compatible environments.
- Consistent application execution.
- Fast startup and deployment.

## Container Lifecycle

Common container states include:

- Created: the container has been created but not started.
- Running: the container is executing.
- Paused: container processes are suspended.
- Stopped: the container is no longer running.
- Deleted: the container has been removed.

## Container Management

Docker provides commands to manage containers.

```bash
docker run -d --name web nginx
docker ps
docker stop web
docker start web
docker rm web
```

## Container Networking

Docker provides networking capabilities that allow containers to communicate with each other and external systems.

Common network drivers include:

- Bridge.
- Host.
- None.
- Overlay.

## Container Storage

Containers have a writable layer, but data stored only in that layer is not designed for long-term persistence.

Docker volumes provide persistent storage independent of the container lifecycle.

## Important Considerations

- Containers should be designed to be replaceable.
- Persistent data should use volumes or other external storage.
- Container images should be kept updated.
- Avoid running containers with unnecessary privileges.