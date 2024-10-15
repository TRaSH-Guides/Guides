# File and Folder Structure

## Introduction

It is important that your media server has a well organised file and folder structure. Along with generally easier file and folder management, you will benefit from:

- Improved security, by only granting the appropriate applications and tools access to your files.
- [Hardlinks](/File-and-Folder-Structure/Hardlinks-and-instant-moves#what-are-hardlinks), so that the same file can appear in multiple places whilst only taking up the disk space of one copy.
- [Instant moves](/File-and-Folder-Structure/Hardlinks-and-instant-moves#what-are-instant-moves-atomic-moves) (also known as 'Atomic Moves') so that files can be moved to other parts of the file system instantaneously.

The first requirement is that all your media files and folders should be part of the same file system. That is, everything must be contained on a single physical or virtual drive. Second, all of your applications should have a consistent view of where your files and folders are - i.e., your files should appear in the same place to all of your applications.

We recommend setting up a file and folder structure on your host server that looks like this:

{! include-markdown "../../includes/file-and-folder-structure/docker-tree-full.md" !}

The `data` folder can be placed wherever you like. As an example, in Unraid, you would set up a share called `data`. This would then be accessible within Unraid's file system at `/mnt/user/data`.

If you are installing applications directly on the host system (natively), then they will already have visibility of that file and folder structure, assuming permissions are set correctly. If you are installing applications non-natively, for example via Docker, then each application should be granted access to the lowest level folder that is required whilst maintaining consistent pathing to the top level folder, which here is `data`. For example, a torrent client installed via Docker would have `/mnt/user/data/torrents` mapped to `/data/torrents`. This means that the download client would see the contents of the host's `/mnt/user/data/torrents` folder in the `/data/torrents` folder inside the container.

More detailed examples can be found in the [How To Set Up](/File-and-Folder-Structure/How-to-set-up/) section.

--8<-- "includes/support.md"
