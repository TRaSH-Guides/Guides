### Unpackerr

[Unpackerr](https://github.com/Unpackerr/unpackerr){:target="\_blank" rel="noopener noreferrer"} is a daemon that extracts compressed downloads so Sonarr, Radarr, Lidarr, and Readarr can import them, then cleans up after itself.

- Handles Tar, Rar, Zip, 7-Zip, Gzip, tarred gzip/bzip, encrypted Rar/7-Zip, and ISO images — extracts recursively, including archives nested inside archives.
- Detects completed downloads by polling each Starr app's own API for items sitting in the import queue; supports multiple instances of each app.
- Deletes the extracted files once the Starr app has successfully imported them — no manual cleanup, and no leftover extracted copies eating disk space.
- Also runs as a plain folder-watcher with zero Starr apps configured, if that's all you need.
