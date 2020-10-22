## How to provide a docker compose when you need help on Discord

When you're running dockers and you need help on discord etc you often hear the question:

"Provide a docker compose"

If you need to provide this info always remember to provide it from all your arrs (Sonarr, Radarr, Lidarr, Bazarr) and also from your download client(s).

If you're using a system with a GUI (Synology, unRAID, OMV, etc.) it's not always easy to provide a docker compose but it's possible,

> **!!! Please don't use screenshots to provide the info as they aren't always revealing all the needed info !!!**

Use one of the following from terminal(puTTy) to get the docker compose with or without the use of `sudo`.

 `sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock assaflavie/runlike CONTAINER_NAME CONTAINER_NAME2`

or

`sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock red5d/docker-autocompose CONTAINER_NAME CONTAINER_NAME2`

Paste the results on one of the following sites.

- <https://gist.github.com/>
- <https://hastebin.com/>
- <https://pastebin.com/>

> If you use docker run command to create your docker containers
> paste your run command in to [composerize](https://www.composerize.com/)
