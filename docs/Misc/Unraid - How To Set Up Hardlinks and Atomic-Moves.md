## Unraid - How To Set Up Hardlinks and Atomic-Moves

!!! note

    The first thing you need to do is forget the suggested paths from the Spaceinvader One YouTube Tutorials,

    And don't use the predefined paths from the unraid templates.

    (Spaceinvader One YouTube guides are great to learn how to start with unraid or how to setup certain applications, and yes I did and still do use them. Probably the main reason why he's using those path is because they are predefined in the template)

!!! attention

    To get Hardlinks and Atomic-Moves working with Unraid you will need to make use of **ONE** share with subfolders.

### Create the main share

For this example I'm using my own setup and preferred share `data`.

go to your dashboard and on the top select `shares` select `add share` .

 ![image-20201111225320772](images/image-20201111225320772.png)

1. use `data`
1. if you got a cache drive and want to make use of it put it on `Yes` or keep it disabled (Hardlinks will stay in tact if you're using the cache)
1. click on `ADD SHARE`

!!! note

    Keep in mind regarding the use of the Cache drive, The mover can't move files that are in use, like  when `seeding` with torrents. You will need to shutdown your client or stop/pause the torrents so the mover can move them to your Array.

    With Usenet  you won't have any issues.

### Folder Structure

On the host (Unraid) you will need to add `/mnt/user` before it.

The `data` folder has sub-folders for `torrents` and `usenet` and each of these have sub-folders for `tv`, `movie` and `music` downloads to keep things neat. The `media` folder has nicely named `TV`, `Movies` and `Music` sub-folders, this is your library and what you’d pass to Plex, Emby or JellyFin.

These subfolders you need to create your self, you can use krusader or winscp to create them or any other way you prefer.

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

*I'm using lower case on all folder on  purpose, being Linux is case sensitive.*

### Setting up the containers

After you created all the needed folders it's time to setup the paths in the docker containers.

Go to your dashboard and select your docker container you want to edit or if you're starting fresh add the docker containers you want to use or prefer.

Unraid makes it actually  pretty clear what's the Host Path and what's the Container Path.

`Container Path:` => The path that will be used inside the container.

`Host Path`: => The path on your Unraid Server (The Host).

#### Torrent clients

qBittorrent, Deluge, ruTorrent

 ![image-20201112201012153](images/image-20201112201012153.png)

`Container Path:` => `/data/torrent`

`Host Path`: => `/mnt/user/data/torrents`

!!! note

    The reason why we use `/data/torrent` for the torrent client is because it only needs access to the torrent files. In the torrent software settings, you’ll need to reconfigure paths and you can sort into sub-folders like/data/torrents/{tv|movies|music}.

```none
data
└── torrents
    ├── movies
    ├── music
    └── tv
```

#### Usenet clients

NZBGet or SABnzbd

 ![image-20201112203013210](images/image-20201112203013210.png)

`Container Path:` => `/data/usenet`

`Host Path`: => `/mnt/user/data/usenet`

!!! note

    The reason why we use `/data/usenet` for the usenet client is because it only needs access to the usenet files. In the usenet software settings, you’ll need to reconfigure paths and you can sort into sub-folders like/data/usenet/{tv|movies|music}.

```none
data
└── usenet
    ├── movies
    ├── music
    └── tv
```

#### The arr(s)

Sonarr, Radarr and Lidarr

 ![image-20201112204406692](images/image-20201112204406692.png)

`Container Path:` => `/data`

`Host Path`: => `/mnt/user/data/`

!!! note

    Sonarr, Radarr and Lidarr get's access to everything because the download folder(s) and media folder will look like and be one file system. Hard links will work and moves will be atomic, instead of copy + delete.

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

#### Media Server

Plex, Emby, JellyFin and Bazarr

 ![image-20201112205218382](images/image-20201112205218382.png)

`Container Path:` => `/data/media`

`Host Path`: => `/mnt/user/data/media/`

!!! note

    Plex, Emby, JellyFin and Bazarr only needs access to your media library, which can have any number of sub folders like Movies, Kids Movies, TV, Documentary TV and/or Music as sub folders.

```none
data
└── media
    ├── movies
    ├── music
    └── tv
```

### Final Result

 ![image-20201112210400294](images/image-20201112210400294.png)
