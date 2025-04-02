# Common Docker Commands

## Container Management
- `docker run [options] image [command]` - Create and start a new container
  - Example: `docker run -d -p 8080:80 nginx`
  - Common options:
    - `-d`: Run in detached mode (background)
    - `-p`: Port mapping (host:container)
    - `-v`: Volume mounting
    - `-e`: Set environment variables
    - `--name`: Name the container

- `docker ps` - List running containers
  - `docker ps -a` - List all containers (including stopped)
  - `docker ps -q` - List only container IDs

- `docker stop container_id` - Stop a running container
- `docker start container_id` - Start a stopped container
- `docker restart container_id` - Restart a container
- `docker rm container_id` - Remove a container
- `docker rm -f container_id` - Force remove a running container

## Image Management
- `docker images` - List all images
- `docker pull image_name` - Pull an image from Docker Hub
- `docker build -t image_name .` - Build an image from a Dockerfile
- `docker rmi image_id` - Remove an image
- `docker rmi -f image_id` - Force remove an image

## Container Inspection
- `docker logs container_id` - View container logs
  - `docker logs -f container_id` - Follow logs in real-time
- `docker exec -it container_id /bin/bash` - Execute a command in a running container
- `docker inspect container_id` - Get detailed information about a container
- `docker stats` - Display container resource usage statistics

## Network Management
- `docker network ls` - List all networks
- `docker network create network_name` - Create a new network
- `docker network rm network_name` - Remove a network
- `docker network connect network_name container_id` - Connect a container to a network

## Volume Management
- `docker volume ls` - List all volumes
- `docker volume create volume_name` - Create a new volume
- `docker volume rm volume_name` - Remove a volume
- `docker volume prune` - Remove all unused volumes

## System Commands
- `docker system prune` - Remove all unused containers, networks, images, and volumes
- `docker info` - Display system-wide information
- `docker version` - Show Docker version information

## Docker Compose
- `docker-compose up` - Create and start containers defined in docker-compose.yml
  - `docker-compose up -d` - Run in detached mode
- `docker-compose down` - Stop and remove containers defined in docker-compose.yml
- `docker-compose ps` - List containers defined in docker-compose.yml
- `docker-compose logs` - View logs from all containers
- `docker-compose build` - Build or rebuild services

## Tips
- Use `docker --help` to see all available commands
- Use `docker command --help` to see options for a specific command
- Container IDs can be shortened to the first few characters
- Use `docker-compose` for managing multi-container applications 