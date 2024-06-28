# Hardlinks and Instant Moves (Atomic-Moves)

## Description

!!! info

    If you’re wondering why hard links aren’t working or why a simple move is taking far longer than it should.

    Here we will try to explain it.

This Guide exist out of 4 Sections

1. This page with a short description.
1. [How to set up for](/Hardlinks/How-to-setup-for/) your installation method.
1. [Examples](/Hardlinks/Examples/) what you should use for your path settings in your used applications.
1. [Check if hardlinks are working](/Hardlinks/Check-if-hardlinks-are-working/)

So you want one of the following ?

- Instant moves (Atomic-Moves) during import of the Starr Apps (useful when using Usenet)?
- You don't want to use twice the storage when using torrents. (hardlinks)?
- You want to perma seed?

Then Continue to [How to set up for](/Hardlinks/How-to-setup-for/) your installation method.

## FAQ

### What are Hardlinks

??? question "**What are hardlinks?** - [Click to show/hide]"

    - [**Short answer**] Having a file in multiple locations without using double your storage space.
    - [**Long answer**] Hard links are a way for a copy operation to be instant and not consume space for those additional copies.

        Every file is a hard link: some metadata that points at blocks on the file system, **which is why they're restricted to the same file system**. There can be as many metadata files pointing at those blocks as needed and the blocks know how many links point to them. Once the blocks have 0 links, they're considered deleted.

        This means:

            - You can delete any "copy" w/o impacting the others.

                Your download client can remove it's "copy" w/o impacting the library "copy". The library "copy" can be removed by Plex or Sonarr/Radarr or yourself w/o impacting the download client "copy".

            - Space is only regained when all "copies" are deleted.

            - Modifying the file will impact all "copies".

                For example, modifying the id3 tags of a .mp3 download after import would modify the download client "copy", resulting in breaking the torrent.

        [More info from Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Hard_link){:target="_blank" rel="noopener noreferrer"}

        !!! warning

            You can't create hard links for directories :bangbang:

            You can't cross file systems :bangbang:

### What are Instant Moves (Atomic Moves)

??? question "**What are Instant Moves (Atomic Moves)?** - [Click to show/hide]"

    A real move and not a copy file from download folder to media folder and then delete file from download folder.

### What are the Starr Apps

??? question "**What are the `Starr Apps`?** - [Click to show/hide]"

    Sonarr, Radarr, Lidarr, etc.
