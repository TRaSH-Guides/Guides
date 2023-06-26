### Breakdown of the Folder Structure

#### Torrent clients

qBittorrent, Deluge, ruTorrent

The reason we use `/data/torrents` for the torrent client is because it only needs access to the torrent files. In the torrent software settings, you’ll need to reconfigure paths and can then sort into subfolders like `/data/torrents/{tv|movies|music}`.

{! include-markdown "docker-tree-torrents.md" !}

`Container Path:` => `/data/torrents/`

`Host Path:` => `/<path_to_data>/data/torrents/`

Abbreviated Docker-compose Volumes Example:

```none
[...]
    volumes:
      [...]
      - /<path_to_data>/data/torrents:/data/torrents
[...]
```

#### Usenet clients

NZBGet or SABnzbd

The reason we use `/data/usenet` for the usenet client is because it only needs access to the usenet files. In the usenet software settings, you’ll need to reconfigure paths and can then sort into subfolders like `/data/usenet/complete/{tv|movies|music}`.

{! include-markdown "docker-tree-usenet.md" !}

`Container Path:` => `/data/usenet/`

`Host Path:` => `/<path_to_data>/data/usenet/`

Abbreviated Docker-compose Volumes Example:

```none
[...]
    volumes:
      [...]
      - /<path_to_data>/data/usenet:/data/usenet
[...]
```

#### The Starr Apps

Sonarr, Radarr, Readarr and Lidarr

Sonarr, Radarr, Readarr and Lidarr get access to everything in `/data` because the download and media folder(s) will look like and will be one file system. Hardlinks will work and moves will be atomic (*instead of copy + delete*).

{! include-markdown "docker-tree-full.md" !}

`Container Path:` => `/data`

`Host Path:` => `/<path_to_data>/data/`

Abbreviated Docker-compose Volumes Example:

```none
[...]
    volumes:
      [...]
      - /<path_to_data>/data:/data
[...]
```

#### Media Server

Plex, Emby, JellyFin and Bazarr

Plex, Emby, JellyFin and Bazarr only need access to your media library using `/data/media`, which can have any number of subfolders like Movies, Kids Movies, TV, Documentary TV or Music.

{! include-markdown "docker-tree-media.md" !}

`Container Path:` => `/data/media`

`Host Path:` => `/<path_to_data>/data/media/`

Abbreviated Docker-compose Volumes Example:

```none
[...]
    volumes:
      [...]
      - /<path_to_data>/data/media:/data/media
[...]
```

------

**Don't forget to look at the [Examples](/Hardlinks/Examples/) for more information on how to setup the paths inside the applications.**

------
