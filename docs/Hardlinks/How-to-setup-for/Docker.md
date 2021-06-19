# Docker

!!! tip

    If you're new to dockers and want a easy setup I suggest to take a look at [DockSTARTer](https://dockstarter.com/){:target="_blank" rel="noopener noreferrer"}.
    I've also created a short guide [HERE](/Hardlinks/How-to-setup-for/Dockstarter/) where I explain the settings for the most used applications.

    The main goal of DockSTARTer is to make it quick and easy to get up and running with Docker.
    You may choose to rely on DockSTARTer for various changes to your Docker system or use DockSTARTer as a stepping stone and learn to do more advanced configurations.

    *DockSTARTer was actually my first steps in to the world of dockers.*

!!! note

    I'm not going to explain how to get dockers installed and running, I will only explain which folder structure we recommend.

    The paths mentioned below refer to internal paths for the containers!

    External paths depends where you mounted your share or your drives.

    For example `/<path_to_data>/data`, or even `/data`.

!!! info

    The paths you use on the inside matter. Because of how Docker’s volumes work, passing in two or three volumes such as the commonly suggested `/tv`, `/movies` and `/downloads` makes them look like two or three file systems, even if they aren’t. This means hard links won’t work and instead of an instant move, a slower and more I/O intensive copy + delete is used.

--8<-- "includes/hardlinks/folder-structure.md"

--8<-- "includes/hardlinks/breakdown-folder-structure.md"

--8<-- "includes/hardlinks/permissions.md"

## Docker-compose Example

!!! example ""
    This is a docker-compose example based on a default Ubuntu install.

    The storage location used for the host is actually the same as in the container to make it easier to understand in this case `/data`.

    The appdata (`/config`) will be stored on the host in the `/docker/appdata/{appname}`

??? example "docker-compose"

    ```yml
    --8<-- "includes/docker/docker-compose.yml"
    ```

--8<-- "includes/hardlinks/docker-compose-commands.md"
