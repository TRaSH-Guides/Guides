# Plex Profiles

!!! info

    Here you will find a collection of profiles you only should use if Plex has issues direct playing your media on your devices, these profiles could help but results might vary.

!!! danger "The profiles aren't tested on the Shield 2019 or newer Chromecast models :warning:"

## How to

To make use of the profiles you need to add it in your your plex folder

### Docker

Example paths:

- Hotio's container: `/appdata/plex/Profiles`
- LSIO container: `/appdata/plex/database/Library/Application Support/Plex Media Server/Profiles` or `/appdata/plex/Library/Application Support/Plex Media Server/Profiles`

## Profiles

!!! tip

    If you got some to share, pls make a PR so we can collect them at one place

### Android Shield

??? info "Please name the file:"

    ``` none
        Android-SHIELD Android TV.xml
    ```

??? example "Shield Profile"

    ```sh
    [[% filter indent(width=4) %]][[% include '/Plex/profiles/Android-SHIELD/Android-SHIELD-Android-TV.xml' %]][[% endfilter %]]
    ```

### Chromecast

??? info "Please name the file:"

    ``` none
        Chromecast.xml
    ```

??? example "Chromecast Profile"

    ```sh
    [[% filter indent(width=4) %]][[% include '/Plex/profiles/Chromecast/Chromecast.xml' %]][[% endfilter %]]
    ```

--8<-- "includes/support.md"
