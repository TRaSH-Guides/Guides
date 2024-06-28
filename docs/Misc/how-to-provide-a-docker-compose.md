# How to provide a docker compose

When you're running dockers and you need help on Discord etc you often hear the question:

"Provide a docker compose"

If you need to provide this info always remember to provide it from all your Starr Apps (Sonarr, Radarr, Lidarr, Bazarr) and also from your download client(s).

If you're using a system with a GUI (Synology, unRAID, OMV, etc.) it's not always easy to provide a docker compose but it's possible.

!!! warning

    Please don't use screenshots to provide the info as they aren't always revealing all the needed info

Use one of the following commands in the terminal of your choice (e.g. puTTY) to generate the docker compose, with or without the use of `sudo`. Note that you can pass in multiple container names.

```bash
sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/red5d/docker-autocompose CONTAINER_NAME CONTAINER_NAME2
```

??? example "Example:"

    ```bash
    sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/red5d/docker-autocompose sonarr radarr bazarr nzbget
    ```

!!! warning

    Please do not share the output directly to Discord, Reddit, forums, etc.

Copy and paste the results on one of the following sites.

- [Notifiarr.com Privatebin](https://logs.notifiarr.com/){:target="\_blank" rel="noopener noreferrer"} (Recommended)
- [Github Gist](https://gist.github.com){:target="\_blank" rel="noopener noreferrer"} (Alternative)
- [hastebin.com](https://hastebin.com){:target="\_blank" rel="noopener noreferrer"}
- [privatebin.net](https://privatebin.net/){:target="\_blank" rel="noopener noreferrer"}
- [bpaste](https://bpa.st/){:target="\_blank" rel="noopener noreferrer"}

If you use the `docker run` command to create your docker containers, paste your run command into [composerize](https://www.composerize.com/){:target="\_blank" rel="noopener noreferrer"}
