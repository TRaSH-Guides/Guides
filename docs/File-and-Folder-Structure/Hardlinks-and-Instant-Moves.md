# Hardlinks and Instant Moves (Atomic-Moves)

## Description

!!! info

    If you’re wondering why hardlinks aren’t working or why a simple move is taking far longer than it should.

    Here we will try to explain it.

This guide consists of 4 sections.

1. This page with a short description.
2. [How to set up](/File-and-Folder-Structure/How-to-set-up/) for your installation method.
3. [Examples](/File-and-Folder-Structure/Examples/) What you should use for your path settings in your used applications.
4. [Check if hardlinks are working](/File-and-Folder-Structure/Check-if-hardlinks-are-working/)

So you want one of the following?

- Instant moves (Atomic-Moves) during import of the Starr Apps (useful when using Usenet)?
- You don't want to use twice the storage when using torrents. (hardlinks)?
- You want to perma-seed?

Then Continue to [How to set up](/File-and-Folder-Structure/How-to-set-up/) for your installation method.

## FAQ

### Hardlinks Limitations

!!! danger "- You <u>CAN'T</u> create hardlinks for directories :bangbang:<br>- You <u>CAN'T</u> hardlink across separate file systems, partitions, volumes or mounts :bangbang:<br>- Some file systems, such as exFAT, are known not to support hardlinks and should be avoided (double-check if you are unsure!)."

### What are Hardlinks

??? question "**What are hardlinks?** - [Click to show/hide]"

    - [**Short answer**] Having a file in multiple locations without using double your storage space.
    - [**Long answer**] Hardlinks allow a copy operation to be instant and not consume space for those additional copies.

        Every file is a hardlink: some metadata that points at blocks on the file system, **which is why they're restricted to the same file system**. There can be as many metadata files pointing at those blocks as needed, and the blocks know how many links point to them. Once the blocks have 0 links, they're considered deleted.

        This means:

        - You can delete any "copy" without impacting other instances (hardlinks).

            Your download client can remove its "copy" without impacting the library "copy". The library "copy" can also be removed by Plex, Sonarr/Radarr, or manually without impacting your download client's "copy".

        - Space is only reclaimed once all "copies" of hardlinked data are deleted.

        - Modifying any copy of a hardlinked file will impact all "copies".

            For example, modifying the id3 tags of a .mp3 download after import would change the download client "copy", breaking the torrent.

        [More info from Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Hard_link){:target="_blank" rel="noopener noreferrer"}

    !!! warning "Don't forget to read the [Hardlinks limitations](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#hardlinks-limitations)"

### What are Instant Moves (Atomic Moves)

??? question "**What are Instant Moves (Atomic Moves)?** - [Click to show/hide]"

    This is a real move, not a copying of a file from the download folder to the media folder and then deleting the file from the download folder.

### What are the Starr Apps

??? question "**What are the `Starr Apps`?** - [Click to show/hide]"

    Sonarr, Radarr, Lidarr, etc.

--8<-- "includes/support.md"
