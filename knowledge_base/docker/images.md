# Docker Images

Source: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/

## Overview

A Docker image is a read-only template used to create containers.

Images contain the application code, runtime, libraries, dependencies, and configuration required to run an application.

## Image Layers

Docker images are built using multiple layers.

Each instruction in a Dockerfile can create a layer.

Layer caching improves build performance by reusing unchanged layers.

## Dockerfile

A Dockerfile is a text file containing instructions used to build a Docker image.

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "src.main"]
```

## Image Management

Common Docker image commands:

```bash
docker build -t my-app .
docker images
docker pull nginx
docker tag my-app my-app:v1
docker push my-app:v1
```

## Image Registries

Docker images can be stored and distributed through registries.

Examples include:

- Docker Hub.
- Amazon Elastic Container Registry (ECR).
- GitHub Container Registry (GHCR).

## Best Practices

- Prefer lightweight base images.
- Use specific image tags instead of relying on latest.
- Avoid including secrets in image layers.
- Use .dockerignore to exclude unnecessary files.
- Keep images updated.
- Use multi-stage builds when appropriate.