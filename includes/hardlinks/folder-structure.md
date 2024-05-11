## Folder Structure

!!! warning

    It doesn't really matter which path you use for your media and appdata,

    the only thing you should avoid is `/home`.

    Because user folders in `/home` are expected to have some restrictive permissions.

    It just could end up creating a permissions mess, so it's better to just avoid entirely.

For this example we're going to make use of a share called `data`.

The `data` folder has sub-folders for `torrents` and `usenet` and each of these have sub-folders for `tv`, `movie`, `books` and `music` downloads to keep things neat. The `media` folder has nicely named `TV`, `Movies`, `Books` and `Music` sub-folders, this is your library and what you’d pass to Plex, Emby or JellyFin.

_In this examples I'm using lower case on all folder on purpose, being Linux is case sensitive._

{! include-markdown "./docker-tree-full.md" !}
