# How to provide a Docker compose

When you're running Docker containers and you need help on Discord etc you often hear the question:

"Provide a Docker compose"

If you need to provide this info always remember to provide it from all your Starr Apps (Sonarr, Radarr, Lidarr, Bazarr) and also from your download client(s).

If you're using a system with a GUI (Synology, unRAID, OMV, etc.) it's not always easy to provide a Docker compose but it's possible.

::: warning

Please don't use screenshots to provide the info as they aren't always revealing all the needed info

:::

Use one of the following commands in the terminal of your choice (e.g. puTTY) to generate the Docker compose, with or without the use of `sudo`. Note that you can pass in multiple container names.

```bash
sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/red5d/docker-autocompose CONTAINER_NAME CONTAINER_NAME2
```

::: details Example:

```bash
sudo docker run --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/red5d/docker-autocompose sonarr radarr bazarr nzbget
```

:::

::: warning

Please do not share the output directly to Discord, Reddit, forums, etc.

:::

Copy and paste the results on one of the following sites.

- [Notifiarr.com Privatebin](https://logs.notifiarr.com/) (Recommended)
- [Github Gist](https://gist.github.com) (Alternative)
- [hastebin.com](https://hastebin.com)
- [privatebin.net](https://privatebin.net/)
- [bpaste](https://bpa.st/)

If you use the `docker run` command to create your Docker containers, paste your run command into [composerize](https://www.composerize.com/)
