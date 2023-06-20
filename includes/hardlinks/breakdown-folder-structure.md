### Breakdown of the Folder Structure

#### Torrent Clients

qBittorrent, Deluge, ruTorrent

The reason we use `/data/torrents` for the torrent client is because it only needs access to the torrent files. In the torrent software settings, you’ll need to reconfigure paths and can then sort into sub-folders like `/data/torrents/{tv|movies|music}`.

{! include-markdown "docker-tree-torrents.md" !}

#### Usenet Clients

NZBGet or SABnzbd

The reason we use `/data/usenet` for the usenet client is because it only needs access to the usenet files. In the usenet software settings, you’ll need to reconfigure paths and can then sort into sub-folders like `/data/usenet/complete/{tv|movies|music}`.

{! include-markdown "docker-tree-usenet.md" !}

#### The Starr Apps

Sonarr, Radarr, Readarr and Lidarr

Sonarr, Radarr, Readarr and Lidarr get access to everything using `/data` because the download folder(s) and media folder(s) will look like and be one file system. Hardlinks will work and moves will be atomic, instead of copy + delete.

{! include-markdown "docker-tree-full.md" !}

#### Media Server

Plex, Emby, JellyFin and Bazarr

Plex, Emby, JellyFin and Bazarr only need access to your media library using `/data/media`, which can have any number of subfolders like Movies, Kids Movies, TV, Documentary TV, or Music.

{! include-markdown "docker-tree-media.md" !}

------

**Don't forget to look at the [Examples](/Hardlinks/Examples/) for more information on how to setup the paths inside the applications.**
