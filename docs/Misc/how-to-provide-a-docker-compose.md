# How to provide a docker compose

When you're running dockers and you need help on discord etc you often hear the question:

"Provide a docker compose"

If you need to provide this info always remember to provide it from all your Starr Apps (Sonarr, Radarr, Lidarr, Bazarr) and also from your download client(s).

If you're using a system with a GUI (Synology, unRAID, OMV, etc.) it's not always easy to provide a docker compose but it's possible.

!!! warning
    Please don't use screenshots to provide the info as they aren't always revealing all the needed info

Use one of the following from terminal(puTTy) to get the docker compose with or without the use of `sudo`.

```bash
sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/red5d/docker-autocompose CONTAINER_NAME CONTAINER_NAME2
```

??? example "Example:"

    ```bash
    sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/red5d/docker-autocompose sonarr radarr bazarr nzbget
    ```

Paste the results on one of the following sites.

- [Notifiarr.com](https://logs.notifiarr.com/) (Recommended)
- [Github Gist](https://gist.github.com){:target="_blank" rel="noopener noreferrer"} (Alternative)
- [hastebin.com](https://hastebin.com){:target="_blank" rel="noopener noreferrer"}
- [privatebin.net](https://privatebin.net/){:target="_blank" rel="noopener noreferrer"}
- [bpaste](https://bpa.st/){:target="_blank" rel="noopener noreferrer"}

If you use docker run command to create your docker containers, paste your run command in to [composerize](https://www.composerize.com/){:target="_blank" rel="noopener noreferrer"}
