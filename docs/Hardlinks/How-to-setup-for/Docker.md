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

{! include-markdown "../../../includes/hardlinks/folder-structure.md" !}
<!-- --8<-- "includes/hardlinks/folder-structure.md" -->

{! include-markdown "../../../includes/hardlinks/bad-path-suggestion.md" !}
<!-- --8<-- "includes/hardlinks/bad-path-suggestion.md" -->

{! include-markdown "../../../includes/hardlinks/breakdown-folder-structure.md" !}
<!-- --8<-- "includes/hardlinks/breakdown-folder-structure.md" -->

{! include-markdown "../../../includes/hardlinks/permissions.md" !}
<!-- --8<-- "includes/hardlinks/permissions.md" -->

## Docker-compose Example

!!! example ""
    This is a docker-compose example based on a default Ubuntu install.

    The storage location used for the host is actually the same as in the container to make it easier to understand in this case `/data`.

    The appdata (`/config`) will be stored on the host in the `/docker/appdata/{appname}`

??? example "docker-compose - [CLICK TO EXPAND]"

    ```yml
    --8<-- "includes/docker/docker-compose.yml"
    ```

{! include-markdown "../../../includes/hardlinks/docker-compose-commands.md" !}
<!-- --8<-- "includes/hardlinks/docker-compose-commands.md" -->

{! include-markdown "../../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
