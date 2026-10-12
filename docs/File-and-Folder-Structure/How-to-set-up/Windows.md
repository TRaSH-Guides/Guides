# Windows

Windows is less flexible than some other operating systems with respect to support for hardlinks and instant (Atomic) moves. In most cases, you need to use a single disk containing both your download location and media library. However, there is an option detailed below that will allow you to make use of hardlinks and instant (Atomic) moves if you run a two-disk setup.

## Recommendation

If you want to make extensive use of hardlinks, we would recommend switching to another operating system. For more information and suggestions on this topic, join our Discord support channel. The link is at the bottom of every guide page.

### Alternative recommendation

If moving away from using Windows with multiple disks is not an option, we suggest ignoring hardlinks and instant (Atomic) moves and using [StableBit DrivePool](https://stablebit.com/). This will allow you to pool multiple disks to appear as one big disk, making it much easier to maintain and set up your file and folder structure.

::: warning Windows Storage Spaces may support hardlinks, but the Guides team has not verified this. We are unable to provide support for setups that use Storage Spaces.

:::

## Folder Structure

The `data` folder contains subfolders for `torrents` and `usenet`, and each of these has subfolders for `tv`, `movie`, and `music` downloads to keep things organized.

The `media` folder has nicely named `TV`, `Movies` and `Music` sub-folders. These are where your libraries reside, and what you’d pass to Plex, Emby, or JellyFin.

Whilst we have used `data`, you can name the root folder/share whatever you want. We suggest following the guide folder naming to make it easier for you and others to help.

### Folder Structure (one-disk setup or using DrivePool)

For this example, we will assume you have a one-disk setup with a large drive added as drive `D:\`, or are using [StableBit DrivePool](https://stablebit.com/) that created one big disk as drive `D:\`.

```txt
D:\data
├── torrents
│   ├── books
│   ├── movies
│   ├── music
│   └── tv
├── usenet
│   ├── incomplete
│   └── complete
│       ├── books
│       ├── movies
│       ├── music
│       └── tv
└── media
    ├── books
    ├── movies
    ├── music
    └── tv
```

After you create the base folders to use, follow the #examples-how-to-set-up-your-paths-inside-your-applications for a one-disk setup.

### Folder Structure (two-disk setup)

This is a bit more work, but the next best option you can do if you don't want to use the #alternative-recommendation with [StableBit DrivePool](https://stablebit.com/).

For this example, we will assume you have one disk added as drive `D:\`, and a second disk as `E:\`.

#### disk 1

```txt
D:\data
├── torrents
│   └── movies
├── usenet
│   ├── incomplete
│   └── complete
│       └── movies
└── media
    └── movies
```

#### disk 2

```txt
E:\data
├── torrents
│   └── tv
├── usenet
│   ├── incomplete
│   └── complete
│       └── tv
└── media
    └── tv
```

After you create the base folders to use, follow the #examples-how-to-set-up-your-paths-inside-your-applications for a two-disk setup.

## Examples of how to set up your paths INSIDE your applications

At the moment, we do not have Windows screenshots for all the apps, but they may be added later.

So, in the meantime, use the [Examples](/File-and-Folder-Structure/Examples/) of how to set up your paths INSIDE your applications.
However, for the paths, use the information below, depending on whether you have a one-disk or two-disk setup.

::: warning Linux uses forward slash `/` and Windows uses backslash `\`<br>So if you see paths with a forward slash, replace it with a backslash for Windows

:::

::: tabs

== One-Disk Setup

We will assume you have a one-disk setup with a large drive added as drive `D:/` or that you are using [StableBit DrivePool](https://stablebit.com/) that created a single large disk as drive `D:\`.

::: tabs

== Sonarr

```txt
D:\data\media\tv
```

== Radarr

```txt
D:\data\media\movies
```

== SABnzbd

```txt
D:\data\usenet\complete
```

```txt
D:\data\usenet\incomplete
```

== NZBGet

```txt
D:\data\usenet
```

== qBittorrent

```txt
D:\data\torrents
```

== Deluge

```txt
D:\data\torrents
```

== ruTorrent

```txt
D:\data\torrents
```

:::

== Two-Disk Setup

We will assume you have one disk added as drive `D:/` and a second disk as `E:\`.

::: tabs

== Disk 1

::: tabs

== Radarr

```txt
D:\data\media\movies
```

== SABnzbd

Make sure your category paths are set up correctly so the media file ends up in the correct folder.

```txt
D:\data\usenet\complete
```

```txt
D:\data\usenet\incomplete
```

== NZBGet

Make sure your category paths are set up correctly so the media file ends up in the correct folder.

```txt
D:\data\usenet
```

== qBittorrent

Make sure your category paths are set up correctly so the media file ends up in the correct folder.

```txt
D:\data\torrents
```

== Deluge

Make sure your label paths are set correctly so the media file ends up in the correct folder.

```txt
D:\data\torrents
```

== ruTorrent

```txt
D:\data\torrents
```

:::

== Disk 2

::: tabs

== Sonarr

```txt
E:\data\media\tv
```

== SABnzbd

Make sure your category paths are set up correctly so the media file ends up in the correct folder.

```txt
E:\data\usenet\complete
```

```txt
E:\data\usenet\incomplete
```

== NZBGet

Make sure your category paths are set up correctly so the media file ends up in the correct folder.

```txt
E:\data\usenet
```

== qBittorrent

Make sure your category paths are set up correctly so the media file ends up in the correct folder.

```txt
E:\data\torrents
```

== Deluge

Make sure your label paths are set up correctly so the media file ends up in the correct folder.

```txt
E:\data\torrents
```

== ruTorrent

```txt
E:\data\torrents
```

:::

:::

:::

<!--@include: ../../../includes/support.md-->
