### Breakdown of the Folder Structure

#### Torrent clients

qBittorrent, Deluge, ruTorrent

The reason why we use `/data/torrents` for the torrent client is because it only needs access to the torrent files. In the torrent software settings, you’ll need to reconfigure paths and you can sort into sub-folders like `/data/torrents/{tv|movies|music}`.

{! include-markdown "./docker-tree-torrents.md" !}

`Container Path:` => `/data/torrents/`

`Host Path:` => `/volume1/data/torrents/`

#### Usenet clients

NZBGet or SABnzbd

The reason why we use `/data/usenet` for the Usenet client is that it only needs access to the Usenet files. In the Usenet software settings, you’ll need to reconfigure paths and you can sort into sub-folders like `/data/usenet/complete/{tv|movies|music}`.

{! include-markdown "./docker-tree-usenet.md" !}

`Container Path:` => `/data/usenet/`

`Host Path:` => `/volume1/data/usenet/`

#### The Starr Apps

Sonarr, Radarr, Readarr and Lidarr

Sonarr, Radarr, Readarr and Lidarr get access to everything using `/data` because the download folder(s) and media folder will look like and be one file system. Hardlinks will work and moves will be atomic, instead of copy + delete.

{! include-markdown "./docker-tree-full.md" !}

`Container Path:` => `/data`

`Host Path:` => `/volume1/data/`

#### Media Server

Plex, Emby, JellyFin and Bazarr

Plex, Emby, JellyFin and Bazarr only need access to your media library using `/data/media`, which can have any number of subfolders like Movies, Kids Movies, TV, Documentary TV and/or Music as subfolders.

{! include-markdown "./docker-tree-media.md" !}

`Container Path:` => `/data/media`

`Host Path:` => `/volume1/data/media/`

---

**Don't forget to look at the [Examples](/File-and-Folder-Structure/Examples/) how to set up the paths inside the applications.**
