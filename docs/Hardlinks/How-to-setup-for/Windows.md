# Windows

Windows is very limited when it comes to hardlinks/instant moves (Atomic Moves) support. Basically, it comes down to just using one disk for your download location and media library. However, we will try to explain an option that you can make use of hardlinks/instant moves (Atomic Moves) if you run a two-disk setup.

## Recommendation

We would recommend switching to another operating system if you want to make use of a hardlink setup. For more information and suggestions on this topic, we recommend joining our Discord support channel. The link can be found at the bottom of every guide.

### Alternative recommendation

If you have multiple disks and still want to keep using Windows, we suggest forgetting about hardlinks/instant moves (Atomic Moves) and going for the next best, most recommended option for Windows, namely [StableBit DrivePool](https://stablebit.com/){:target="\_blank" rel="noopener noreferrer"}. This will make it possible to make it look like you have one big disk, making it much easier to maintain and set up your file and folder structure.

!!! warning "There are rumors that Storage Spaces supports hardlinks, but you should question yourself if you're willing to run Storage Spaces."

## Folder Structure

The `data` folder has sub-folders for `torrents` and `usenet`, and each of these has sub-folders for `tv`, `movie`, and `music` downloads to keep things organized. The `media` folder has nicely named `TV`, `Movies` and `Music` sub-folders, this is where your library resides, and what you’d pass to Plex, Emby, or JellyFin.

You can name the root folder/share `data` however you want. We suggest following the guide folder naming to make it easier for yourself and others to help you.

### Folder Structure (one-disk setup or using DrivePool)

For this example, we will assume you have a one-disk setup with a large drive added as drive `D:\` or are using [StableBit DrivePool](https://stablebit.com/){:target="\_blank" rel="noopener noreferrer"} that created one big disk as drive `D:\`.

```none
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

After you create the base folders to use it's time to follow the #examples-how-to-set-up-your-paths-inside-your-applications for a one-disk setup.

### Folder Structure (two-disk setup)

This is a bit more work, but the next best option you can do if you don't want to use the #alternative-recommendation with [StableBit DrivePool](https://stablebit.com/){:target="\_blank" rel="noopener noreferrer"}.

For this example, we will assume you have one disk added as drive `D:\` and a second disk as `E:\`.

#### disk 1

```none
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

```none
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

After you create the base folders to use it's time to follow the #examples-how-to-set-up-your-paths-inside-your-applications for a two-disk setup.

## Examples how to set up your paths INSIDE your applications

At the moment, we do not have Windows-based screenshots for all of the apps, but they might be added later.

So, in the meantime, use the [Examples](/Hardlinks/Examples/) of how to setup your paths INSIDE your applications.
However, for the paths, use the info provided below depending on whether you have a one-disk setup or a two-disk setup.

!!! warning "Linux used forward slash `/` and Windows uses backslash `\`<br>So if you see paths with a forward slash replace it with a backslash for Windows"

=== "One-Disk Setup"

    We will assume you have a one-disk setup with a large drive added as drive `D:/` or are using [StableBit DrivePool](https://stablebit.com/){:target="\_blank" rel="noopener noreferrer"} that created one big disk as drive `D:\`.

    === "Sonarr"

        ```none
        D:\data\media\tv
        ```

    === "Radarr"

        ```none
        D:\data\media\movies
        ```

    === "SABnzbd"

        ```none
        D:\data\usenet\complete
        ```

        ```none
        D:\data\usenet\incomplete
        ```

    === "NZBGet"

        ```none
        D:\data\usenet
        ```

    === "qBittorrent"

        ```none
        D:\data\torrents
        ```

    === "Deluge"

        ```none
        D:\data\torrents
        ```

    === "ruTorrent"

        ```none
        D:\data\torrents
        ```

=== "Two-Disk Setup"

    We will assume you have one disk added as drive `D:/` and a second disk as `E:\`.

    === "Disk 1"

        === "Radarr"

            ```none
            D:\data\media\movies
            ```

        === "SABnzbd"

            Make sure your category paths are set up correctly so the media file ends up in the correct folder.

            ```none
            D:\data\usenet\complete
            ```

            ```none
            D:\data\usenet\incomplete
            ```

        === "NZBGet"

            Make sure your category paths are set up correctly so the media file ends up in the correct folder.

            ```none
            D:\data\usenet
            ```

        === "qBittorrent"

            Make sure your category paths are set up correctly so the media file ends up in the correct folder.

            ```none
            D:\data\torrents
            ```

        === "Deluge"

            Make sure your label paths are set correctly so the media file ends up in the correct folder.

            ```none
            D:\data\torrents
            ```

        === "ruTorrent"

            ```none
            D:\data\torrents
            ```

    === "Disk 2"

        === "Sonarr"

            ```none
            E:\data\media\tv
            ```

        === "SABnzbd"

            Make sure your category paths are set up correctly so the media file ends up in the correct folder.

            ```none
            E:\data\usenet\complete
            ```

            ```none
            E:\data\usenet\incomplete
            ```

        === "NZBGet"

            Make sure your category paths are set up correctly so the media file ends up in the correct folder.

            ```none
            E:\data\usenet
            ```

        === "qBittorrent"

            Make sure your category paths are set up correctly so the media file ends up in the correct folder.

            ```none
            E:\data\torrents
            ```

        === "Deluge"

            Make sure your label paths are set up correctly so the media file ends up in the correct folder.

            ```none
            E:\data\torrents
            ```

        === "ruTorrent"

            ```none
            E:\data\torrents
            ```

--8<-- "includes/support.md"
