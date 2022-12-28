# Recommended naming scheme

On the [Radarr Discord](https://discord.gg/u3x3Kp8){:target="_blank" rel="noopener noreferrer"} people often ask, "What's the recommended/best way to
name your files?" First off, it's personal preference, but it's often recommended to add non-recoverable info.

Why?

If, for what ever reason, you ever need to do a re-install or re-import in
the Starr Apps or Plex/Emby/Jellyfin it's nice to have all that info in the filename so
it gets imported correctly and isn't incorrectly matched as HDTV or WEB-DL etc.

The Tokens not available in the release won't be used/shown.

------

## Standard Movie Format

This naming scheme is made to be compatible with the [New Plex Agent](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517) that now supports IMDb and TMDb IDs in filenames, if you don't need it or want it just remove `{imdb-{ImdbId}}`

!!! caution "Starting from v4.2.2.6489, Radarr now supports Plex Multiple Edition tags in naming."

    If you're using a lower version or don't need it replace:

    `{edition-{Edition Tags}}` with `{Edition Tags}`

```bash
{Movie CleanTitle} {(Release Year)} {imdb-{ImdbId}} {edition-{Edition Tags}} {[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRangeType]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}][{Mediainfo VideoCodec}]{-Release Group}
```

??? summary "RESULTS: - [CLICK TO EXPAND]"

    `The Movie Title (2010) {imdb-tt0066921} {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`

If you do Anime

```bash
{Movie CleanTitle} {(Release Year)} {imdb-{ImdbId}} {edition-{Edition Tags}} {[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRangeType]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}]{MediaInfo AudioLanguages}[{MediaInfo VideoBitDepth}bit][{Mediainfo VideoCodec}]{-Release Group}
```

??? summary "RESULTS: - [CLICK TO EXPAND]"

    `The Movie Title (2010) {imdb-tt0066921} {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`

------

## Original Title vs  Original Filename

Another option is to use `{Original Title}` rather than the recommeneded naming scheme outlined aboove. `{Original Title}` will use the title of the release which will contain all of the information included in the release itself. The benefit of this naming scheme is to prevent download loops which can occur on import when there is a discrepancy in the release title compared to the contents of the file itself (for example, if the release title says DTS-ES but the contents are actually DTS). The downside is less flexibility with how the files are named.

If using this alternate naming scheme I suggest using `{Original Title}` over `{Original Filename}`

Why?

The filename can be Obscured where the Release naming isn't, especially when you use Usenet.

`{Original Title}` => `The.Movie.Title.2010.REMASTERED.1080p.BluRay.x264-GROUP`

`{Original Filename}` => `group-karatekid-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

------

## Movie Folder Format

!!! danger ""

    ** Please note that folder names are created (in the database) whenever the movie is added to Radarr, and it may be missing or incorrect at that time and your folder would have a blank ID!!!**

    If you instead add it in the filename, the IMDb ID will be freshly pulled for any download or upgrade.

    Another potential negative of using it in the folder is that folder renames are complex, lengthy, and potentially destructive in Radarr compared to file renames.

### Minimal needed and recommended

```bash
{Movie CleanTitle} ({Release Year})
```

RESULT:

`The Movie Title (2010)`

------

!!! note
    Keep in mind adding anything more after the release year could give issues during a fresh import in to Radarr, but it helps for movies that have the same release name and year.

    **Radarr supports IMDb ID and TMDb ID in the folder name.**

    !!! quote "Quote from a developer"

        TMDb is usually better as it guarantees a match, IMDb only gets matched if the TMDb entry has the correct IMDb ID association. We don't actually talk to IMDb.

------

Thanks:

A big Thanks to [fryfrog](https://github.com/fryfrog) and [rg9400](https://github.com/rg9400) for the suggestions.

{! include-markdown "../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
