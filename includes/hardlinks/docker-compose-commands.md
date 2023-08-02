### Docker-Compose Commands

??? tip "docker-compose commands - [Click to show/hide]"

    - `sudo docker-compose up -d` (This Docker-compose command helps builds the image, then creates and starts Docker containers. The containers are from the services specified in the compose file. If the containers are already running and you run docker-compose up, it recreates the container.)
    - `sudo docker-compose pull` (Pulls an image associated with a service defined in a docker-compose.yml)
    - `sudo docker-compose down` (The Docker-compose down command also stops Docker containers like the stop command does. But it goes the extra mile. Docker-compose down, doesn’t just stop the containers, it also removes them.)
    - `sudo docker system prune -a --volumes --force` (Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.)
