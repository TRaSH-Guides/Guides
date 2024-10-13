# Dockstarter

!!! note

    We're using the default paths in this example, and we will keep the other paths unchanged so nothing will break if you make a mistake.

## Folder Structure

We're going to use a mounted drive that we're going to use as storage for downloads and your media.
In this example, the mounted drive will be mounted to `/mnt/` with the following folder structure.

```none
storage
├── downloads
│  ├── torrents
│  │   ├── movies
│  │   ├── music
│  │   ├── books
│  │   └── tv
│  └── usenet
│      ├── movies
│      ├── music
│      ├── books
│      └── tv
└── medialibrary
    ├── movies
    ├── music
    ├── books
    └── tv
```

## Changes to the .env

To accomplish this we need to change first a few paths in your `.env` (Usually `~/.docker/compose/.env`)

```yaml
# Global Settings
COMPOSE_HTTP_TIMEOUT=60
DOCKERCONFDIR=~/.config/appdata
DOCKERGID=999
DOCKERHOSTNAME=DockSTARTer
DOCKERLOGGING_MAXFILE=10
DOCKERLOGGING_MAXSIZE=200k
DOCKERSTORAGEDIR=/mnt/storage
PGID=1000
PUID=1000
TZ=America/Chicago
```

### Changes to your paths

When that's all set then you will need to change the paths you're going to use in the containers from:

`/downloads` => `/storage/downloads`

`/audiobooks` => `/storage/medialibrary/audiobooks`

`/books` => `/storage/medialibrary/books`

`/comics` => `/storage/medialibrary/comics`

`/movies` => `/storage/medialibrary/movies`

`/music` => `/storage/medialibrary/music`

`/tv` => `/storage/medialibrary/tv`

## DockSTARTer Examples

!!! info

    The screenshots in the examples are using the following root path `/storage`

- [Sonarr](#sonarr)
- [Radarr](#radarr)
- [SABnzbd](#sabnzbd)
- [NZBGet](#nzbget)
- [qBittorrent](#qbittorrent)
- [Deluge](#deluge)
- [ruTorrent](#rutorrent)

??? example "Sonarr Examples - [Click to show/hide]"

    ##### Sonarr

    `Settings` => `Media Management` => `Importing`

    ![sonarr-enable-hardlinks](/File-and-Folder-Structure/images/sonarr-enable-hardlinks.png)

    `Settings` => `Media Management` => `Root Folders`

    ![ds-sonarr-root-folder](images/ds-sonarr-root-folder.png)

    `Series` => `Add New`

    ![ds-sonarr-add-new](images/ds-sonarr-add-new.png)

    ![ds-sonarr-tv](images/ds-sonarr-tv.png)

??? example "Radarr Examples - [Click to show/hide]"

    ##### Radarr

    `Settings` => `Media Management` => `Importing`

    ![radarr-enable-hardlinks](/File-and-Folder-Structure/images/radarr-enable-hardlinks.png)

    `Settings` => `Media Management` => `Root Folders`

    ![ds-radarr-root-folder](images/ds-radarr-root-folder.png)

    `Movies` => `Add New`

    ![ds-radarr-add-new](images/ds-radarr-add-new.png)

    ![ds-radarr-movies](images/ds-radarr-movies.png)

??? example "SABnzbd Examples - [Click to show/hide]"

    ##### SABnzbd

    `SABnzbd config` => `Folders`

    ![ds-sabnzbd-folders](images/ds-sabnzbd-folders.png)

    `SABnzbd config` => `Categories`

    ![ds-sabnzbd-categories](images/ds-sabnzbd-categories.png)

??? example "NZBGet Examples - [Click to show/hide]"

    ##### NZBGet

    `Settings` => `PATHS`

    ![ds-nzbget-settings-paths](images/ds-nzbget-settings-paths.png)

    `Settings` => `CATEGORIES`

    ![ds-nzbget-settings-categories](images/ds-nzbget-settings-categories.png)

??? example "qBittorrent Examples - [Click to show/hide]"

    ##### qBittorrent

    `Options` => `Downloads`

    ![ds-qbt-options-downloads](images/ds-qbt-options-downloads.png)

??? example "Deluge Example - [Click to show/hide]"

    ##### Deluge

    `Preferences` => `Downloads`

    ![ds-deluge-preferences-downloads](images/ds-deluge-preferences-downloads.png)

??? example "ruTorrent Examples - [Click to show/hide]"

    ##### ruTorrent

    `../config/rtorrent/config/rtorrent.rc` (path to your appdata)

    ![ds-rtorrent.rc](images/ds-rtorrent.rc.png)

    `Settings` => `Downloads`

    ![ds-rtorrent-settings-downloads](images/ds-rtorrent-settings-downloads.png)

    `Settings` => `Autotools`

    ![ds-rtorrent-settings-autotools](images/ds-rtorrent-settings-autotools.png)

--8<-- "includes/support.md"
