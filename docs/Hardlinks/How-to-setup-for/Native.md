# Native

!!! note

    I'm not going to explain how to install all the applications, I will only explain which folder structure we recommend.

------

## Folder Structure

!!! attention

    It doesn't really matter which path you use for your media,

    the only thing you should  avoid is `/home`.

    Because user folders in `/home` are expected to have some restrictive permissions.

    It just could end up creating a permissions mess, so it's better to just avoid entirely.

For this example we're going to make use of a share called `data`.

The `data` folder has sub-folders for `torrents` and `usenet` and each of these have sub-folders for `tv`, `movie` and `music` downloads to keep things neat. The `media` folder has nicely named `TV`, `Movies` and `Music` sub-folders, this is your library and what you’d pass to Plex, Emby or JellyFin.

*I'm using lower case on all folder on purpose, being Linux is case sensitive.*

```none
data
├── torrents
│  ├── movies
│  ├── music
│  └── tv
├── usenet
│  ├── movies
│  ├── music
│  └── tv
└── media
   ├── movies
   ├── music
   └── tv
```

## Breakdown of the Folder Structure

### Torrent clients

qBittorrent, Deluge, ruTorrent

The reason why we use `/data/torrents` for the torrent client is because it only needs access to the torrent files. In the torrent software settings, you’ll need to reconfigure paths and you can sort into sub-folders like `/data/torrents/{tv|movies|music}`.

```none
data
└── torrents
   ├── movies
   ├── music
   └── tv
```

### Usenet clients

NZBGet or SABnzbd

The reason why we use `/data/usenet` for the usenet client is because it only needs access to the usenet files. In the usenet software settings, you’ll need to reconfigure paths and you can sort into sub-folders like `/data/usenet/{tv|movies|music}`.

```none
data
└── usenet
   ├── movies
   ├── music
   └── tv
```

### The arr(s)

Sonarr, Radarr and Lidarr

Sonarr, Radarr and Lidarr gets access to everything because the download folder(s) and media folder will look like and be one file system. Hard links will work and moves will be atomic, instead of copy + delete.

```none
data
├── torrents
│  ├── movies
│  ├── music
│  └── tv
├── usenet
│  ├── movies
│  ├── music
│  └── tv
└── media
   ├── movies
   ├── music
   └── tv
```

### Media Server

Plex, Emby, JellyFin and Bazarr

Plex, Emby, JellyFin and Bazarr only needs access to your media library, which can have any number of sub folders like Movies, Kids Movies, TV, Documentary TV and/or Music as sub folders.

```none
data
└── media
   ├── movies
   ├── music
   └── tv
```

------

## Permissions

Recursively chown user and group and Recursively chmod to 775/664

```bash
sudo chown -R $USER:$USER /data
sudo chmod -R a=,a+rX,u+w,g+w /data
```

**Don't forget to look at the [Examples](/Hardlinks/How-to-setup-for/) how to setup the paths inside the applications.**
