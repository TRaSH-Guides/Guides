## Folder Structure

!!! warning

    It doesn't really matter which path you use for your media and appdata,

    the only thing you should avoid is `/home` (because folders in `/home` are expected to have some restrictive permissions).

    As such, using `/home` could end up creating a permissions mess, so it's better to avoid this situation.

For this example, we're going to make use of a share called `data`.

The `data` folder has sub-folders for `torrents` and `usenet`, and each of these have sub-folders for `tv`, `movie`, `books` and `music` downloads to keep things neat. The `media` folder has nicely named `TV`, `Movies`, `Books` and `Music` sub-folders. *This is your library and what you’d pass to Plex, Emby or JellyFin.*

*In these examples, I'm purposefully using lowercase on all folders, as Linux is case-sensitive.*

{! include-markdown "docker-tree-full.md" !}
