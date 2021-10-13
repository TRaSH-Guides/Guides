### Docker-Compose Commands

??? hint "docker-compose commands - [CLICK TO EXPAND]"

    NOTE: Some OS's (Eg: Synology) require you to run the docker commands as root, i.e. use `sudo docker-compose ...` instead of `docker-compose ...`

    - `docker-compose up -d` (This Docker-compose command helps builds the image, then creates and starts Docker containers. The containers are from the services specified in the compose file. If the containers are already running and you run docker-compose up, it recreates the container.)
    - `docker-compose pull` (Pulls an image associated with a service defined in a docker-compose.yml)
    - `docker-compose down` (The Docker-compose down command also stops Docker containers like the stop command does. But it goes the extra mile. Docker-compose down, doesn’t just stop the containers, it also removes them.)
    - `docker system prune -a --volumes --force` (Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.)
