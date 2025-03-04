# File and Folder Structure

## Introduction

It is important that your media server has a well-organized file and folder structure. Along with generally easier file and folder management, you will benefit from:

- Improved security is achieved by only granting the appropriate applications and tools access to your files.
- [Hardlinks](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#what-are-hardlinks), so the same file can appear in multiple places while only taking up one copy's disk space.
- [Instant moves](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#what-are-instant-moves-atomic-moves) (also known as 'Atomic Moves') so that files can be moved to other parts of the file system instantaneously.

The first requirement is that all your media files and folders be in the same file system. Everything must be contained on a single physical or virtual drive. Second, all your applications should have a consistent view of where your files and folders are - i.e., your files should appear in the same place as all your applications.

We recommend setting up a file and folder structure on your host server that looks like this:

{! include-markdown "../../includes/file-and-folder-structure/docker-tree-full.md" !}

The `data` folder can be placed wherever you like. For example, in Unraid, you would set up a share called `data`. This would then be accessible within Unraid's file system at `/mnt/user/data`.

If you install applications directly on the host system (natively), they will already have visibility of that file and folder structure, assuming permissions are set correctly. Suppose you are installing applications non-natively, for example, via Docker. In that case, each application should be granted access to the required lowest-level folder while maintaining consistent pathing to the top-level folder, which here is `data`. For example, a torrent client installed via Docker would have `/mnt/user/data/torrents` mapped to `/data/torrents`. This means the download client would see the contents of the host's `/mnt/user/data/torrents` folder in the `/data/torrents` folder within the container.

The [How To Set Up](/File-and-Folder-Structure/How-to-set-up/) section provides more detailed examples.

--8<-- "includes/support.md"
