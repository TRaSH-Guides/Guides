# Docker

!!! tip

    If you're new to dockers and want an easy setup, we suggest taking a look at [DockSTARTer](https://dockstarter.com/){:target="_blank" rel="noopener noreferrer"}.
    We've also created a short guide [HERE](/File-and-Folder-Structure/How-to-set-up/Dockstarter/) where we explain the settings for the most used applications.

    The main goal of DockSTARTer is to make it quick and easy to get up and running with Docker.
    You may choose to rely on DockSTARTer for various changes to your Docker system or use DockSTARTer as a stepping stone and learn to do more advanced configurations.

    *DockSTARTer was actually my first step into the world of dockers.*

!!! note

    I'm not going to explain how to get dockers installed and running, we will only explain which folder structure we recommend.

    The paths mentioned below refer to internal paths (or `Container Path`) for the containers!

    External paths (or `Host Path`) depend on where you mounted your share or your drives.

    For example `/<path_to_data>/data`, or even `/data`.

{! include-markdown "../../../includes/file-and-folder-structure/folder-structure.md" !}

{! include-markdown "../../../includes/file-and-folder-structure/bad-path-suggestion.md" !}

{! include-markdown "../../../includes/file-and-folder-structure/breakdown-folder-structure-docker.md" !}

{! include-markdown "../../../includes/file-and-folder-structure/permissions.md" !}

## Docker-compose Example

!!! example ""

    This is a docker-compose example based on a default Ubuntu install.

    The storage location used for the host is the same as in the container to make it easier to understand in this case `/data`.

    The appdata (`/config`) will be stored on the host in the `/docker/appdata/{appname}`

??? example "docker-compose - [Click to show/hide]"

    ```yaml
    --8<-- "includes/docker/docker-compose.yml"
    ```

{! include-markdown "../../../includes/file-and-folder-structure/docker-compose-commands.md" !}

--8<-- "includes/support.md"
