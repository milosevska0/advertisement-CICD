# Advertisement Project

**Advertisement Project** is a Django web application that demonstrates Dockerization and orchestration using Docker and Kubernetes.

## Table of Contents

- [Getting Started](#getting-started)
- [Docker Setup](#docker-setup)
- [Kubernetes Setup](#kubernetes-setup)
- [Applying Migrations](#applying-migrations)

## Getting Started

This project uses a PostgreSQL database and provides Docker and Kubernetes setup instructions for easy deployment and orchestration. 

## Docker Setup

### Prerequisites

Before starting, ensure you have the following installed:

- Docker
- Docker Compose

### Steps to Run with Docker

1. **Create a `.env` file** in the root directory of the project with the following environment variables:

    ```env
    POSTGRES_USERNAME=<database username>
    POSTGRES_DATABASE=<database name>
    POSTGRES_PASSWORD=<database password>
    ```

2. **Start the Docker containers** by running:

    ```bash
    docker-compose up
    ```

This will build and start your containers, including PostgreSQL and your Django application.

## Kubernetes Setup

### Prerequisites

Ensure you have the following installed:

- k3d (for creating a Kubernetes cluster locally)
- kubectl

### Steps to Run with Kubernetes

1. **Create a Kubernetes cluster** using `k3d`:

    ```bash
    k3d cluster create advertisement -p "9000:80@loadbalancer"
    ```

2. **Apply the Kubernetes manifests** located in the `kubernetes` folder:

    ```bash
    kubectl apply -f namespace.yaml \
                  -f db-configmap.yaml \
                  -f db-secret.yaml \
                  -f db-pvc.yaml \
                  -f db-statefulset.yaml \
                  -f db-service.yaml \
                  -f configmap.yaml \
                  -f secret.yaml \
                  -f deployment.yaml \
                  -f service.yaml \
                  -f ingress.yaml
    ```

This will set up your PostgreSQL database, Django application, and any other resources necessary for the project.

## Applying Migrations

To apply the Django migrations (if they haven't been applied automatically), execute the following command:

```bash
kubectl exec -it <pod-name> -n advertisement-namespace -- python manage.py migrate
