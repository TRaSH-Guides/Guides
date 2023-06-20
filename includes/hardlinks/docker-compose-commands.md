### Docker-Compose Commands

??? tip "docker-compose Commands - [CLICK TO EXPAND]"

    - `sudo docker-compose up -d`: Helps build the image, then creates and starts Docker containers from the services specified in the compose file. **Note:** If any containers in the compose file are already running and you run 'docker-compose up', it recreates the container.
    - `sudo docker-compose pull`: Pulls an image associated with a service defined in a docker-compose.yml
    - `sudo docker-compose down`: The Docker-compose down command stops Docker containers (just like Docker's stop command). This command goes the extra mile, though, as it doesn’t just stop the containers, it also removes them.
    - `sudo docker system prune -a --volumes --force`: Removes all unused containers, networks, images (both dangling and unreferenced), and (optionally) volumes.
