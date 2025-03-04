### Breakdown of the Folder Structure

#### Torrent clients

qBittorrent, Deluge, ruTorrent

The reason why we use `/data/torrents` for the torrent client is because it only needs access to the torrent files. In the torrent software settings, you’ll need to reconfigure paths and you can sort into sub-folders like `/data/torrents/{tv|movies|music}`.

{! include-markdown "./docker-tree-torrents.md" !}

#### Usenet clients

NZBGet or SABnzbd

The reason why we use `/data/usenet` for the Usenet client is because it only needs access to the Usenet files. In the Usenet software settings, you’ll need to reconfigure paths and you can sort into sub-folders like `/data/usenet/complete/{tv|movies|music}`.

{! include-markdown "./docker-tree-usenet.md" !}

#### The Starr Apps

Sonarr, Radarr, Readarr and Lidarr

Sonarr, Radarr, Readarr and Lidarr gets access to everything using `/data` because the download folder(s) and media folder will look like and be one file system. Hardlinks will work and moves will be atomic, instead of copy + delete.

{! include-markdown "./docker-tree-full.md" !}

#### Media Server

Plex, Emby, JellyFin and Bazarr

Plex, Emby, JellyFin and Bazarr only needs access to your media library using `/data/media`, which can have any number of sub folders like Movies, Kids Movies, TV, Documentary TV and/or Music as sub folders.

{! include-markdown "./docker-tree-media.md" !}

---

**Don't forget to look at the [Examples](/File-and-Folder-Structure/Examples/) how to set up the paths inside the applications.**
