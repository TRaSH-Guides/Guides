# Recommended naming scheme

Often on the [Radarr Discord](https://discord.gg/u3x3Kp8){:target="_blank" rel="noopener noreferrer"} people ask what's the recommended/best way to
name your files.  First off it's personal preference, but it's often recommended
to add non-recoverable info.

Why?

If, for what ever reason, you ever need to do a re-install or re-import in
Radarr or Plex/Emby/JellyFin it's nice to have all that info in the filename so
it gets imported correctly and isn't incorrectly matched as HDTV or WEB-DL etc.

The Tokens not available in the release won't be used/shown.

------

## Standard Movie Format

### All the details

This naming scheme is made to be compatible with the [New Plex Agent](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517) that now support IMDB and TMDB IDs in file names, if you don't need it or want it just remove `[imdb-{ImdbId}]`

```bash
{Movie CleanTitle} {(Release Year)} {Edition Tags} [imdb-{ImdbId}]{[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRange]}[{Mediainfo VideoBitDepth}bit][{Mediainfo VideoCodec}]{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}]{-Release Group}
```

RESULT:

`The Movie Title (2010) Ultimate Extended Edition [imdb-tt0066921][Surround Sound x264][Bluray-1080p Proper][3D][HDR][10bit][x264][DTS 5.1]-EVOLVE`

??? info "If you do Anime"

    If you do Anime you might consider to add the `{MediaInfo AudioLanguages}` token to your naming scheme.

    ```bash
    {Movie CleanTitle} {(Release Year)} {Edition Tags} [imdb-{ImdbId}]{[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRange]}[{Mediainfo VideoBitDepth}bit][{Mediainfo VideoCodec}]{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}]{MediaInfo AudioLanguages}{-Release Group}
    ```

### Minimal details + the irreplaceable data

This naming scheme is made to be compatible with the [New Plex Agent](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517){:target="_blank" rel="noopener noreferrer"} that now support IMDB and TMDB IDs in file names, if you don't need it or want it just remove `[imdb-{ImdbId}]`

```bash
{Movie CleanTitle} {(Release Year)} [imdb-{ImdbId}]{[Quality Title]}{[MediaInfo AudioCodec}{ MediaInfo AudioChannels]}{[MediaInfo VideoCodec]}{-Release Group}
```

RESULT:

`The Movie Title (2010) [imdb-tt0066921][Bluray-1080p][DTS 5.1][x264]-EVOLVE`

!!! note
    The officially supported format is `{imdb-{ImdbId}}` but plex also support `(imdb-{ImdbId})` or `[imdb-{ImdbId}]` what you can read [here](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517){:target="_blank" rel="noopener noreferrer"}, though the above should work for now. IMDb IDs are going to be very accurate and rarely change, but they may be missing for some movies added to Radarr. TMDB IDs, on the other hand, do change or are removed more frequently, but Radarr will always have this ID for each movie.

------

## Original Title vs  Original Filename

Want to keep the original release name that holds like all the info of the file then I suggest to use `{Original Title}` over  `{Original Filename}`

Why?

The filename can be Obscured where the Release naming isn't especially when you use Usenet.

`{Original Title}` => `The.Movie.Title.2010.REMASTERED.1080p.BluRay.x264-GROUP`

`{Original Filename}` => `group-karatekid-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

------

## Movie Folder Format

### Minimal needed and recommended

```bash
{Movie CleanTitle} ({Release Year})
```

RESULT:

`The Movie Title (2010)`

------

!!! note
    Keep in mind adding anything more after the release year could give issues during a fresh import in to Radarr, but it helps for movies that have the same release name and year.

!!! hint

    Radarr does supports iMDb ID and TMDb ID in the folder name.

    !!! quote "Quote From the a developer"

        TMDb is usually better as it guarantees a match, imdb only gets matched if the TMDb entry has the correct imdb Id association. We don't actually talk to imdb

!!! warning

    ** Please note that folder names are created (in the database) whenever the movie is added to Radarr, and it may be missing or incorrect at that time and your folder would have a blank ID !!!**

    If you instead add it in the filename, the IMDb ID will be freshly pulled for any download or upgrade.

    Another potential negative of using it in the folder is that folder renames are complex, lengthy, and potentially destructive in Radarr compared to file renames.

------

THNX:

A big thnx to [fryfrog](https://github.com/fryfrog) and [rg9400](https://github.com/rg9400) for the suggestions.
