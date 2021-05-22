# Recommended naming scheme

Often on the [Sonarr Discord](https://discord.gg/M6BvZn5){:target="_blank" rel="noopener noreferrer"} people ask what's the recommended/best way to
name your files.  First off it's personal preference, but it's often recommended
to add non-recoverable info.

Why?

If, for whatever reason, you ever need to do a re-install or re-import in
Sonarr or Plex/Emby/JellyFin it's nice to have all that info in the filename so
it gets imported correctly and isn't incorrectly matched as HDTV or WEB-DL etc.

The tokens not available in the release won't be used/shown.

------

## Standard Episode Format

> **All the details**

```bash
{Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRange]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! (2010) - S01E01 - Episode Title 1 [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - S01E01-E02-E03 - Episode Title [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp`

> **Minimal details + the irreplaceable data**

```bash
{Series Title} S{season:00}E{episode:00} {[Quality Title]}{[MediaInfo AudioCodec}{ MediaInfo AudioChannels]}{[MediaInfo VideoCodec]}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! S01E01 [HDTV-720p][DTS 5.1][x264]-RlsGrp`

    Multi Episode:

    `The Series Title! S01E01-E02-E03 [HDTV-720p][DTS 5.1][x264]-RlsGrp`

------

## Daily Episode Format

> **All the details**

```bash
{Series TitleYear} - {Air-Date} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRange]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{-Release Group}
```

??? summary "RESULTS:"

    `The Series Title! (2010) - 2013-10-30 - Episode Title 1 [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp`

> **Minimal details + the irreplaceable data**

```bash
{Series Title} - {Air-Date} - {Episode CleanTitle} {[Quality Title]}{[MediaInfo AudioCodec}{ MediaInfo AudioChannels]}{[MediaInfo VideoCodec]}{-Release Group}
```

??? summary "RESULTS:"

    `The Series Title! - 2013-10-30 - Episode Title 1 [HDTV-720p][DTS 5.1][x264]-RlsGrp`

------

## Anime Episode Format

> **All the details**

```bash
{Series TitleYear} - S{season:00}E{episode:00} - {absolute:000} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRange]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}[{Mediainfo AudioCodec} { Mediainfo AudioChannels}]{MediaInfo AudioLanguages}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! (2010) - S01E01 - 001 - Episode Title 1 [iNTERNAL HDTV-720p v2][HDR][10bit][x264][DTS 5.1][JA]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - S01E01-E02-E03 - 001-002-003 - Episode Title [iNTERNAL HDTV-720p v2][HDR][10bit][x264][DTS 5.1][JA]-RlsGrp`

> **Minimal details + the irreplaceable data**

```bash
{Series Title} - S{season:00}E{episode:00} - {absolute:000} - {[Quality Title]}[{Mediainfo AudioCodec} { Mediainfo AudioChannels}]{[MediaInfo VideoCodec]}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! - S01E01 - 001 - [HDTV-720p][DTS 5.1][x264]-RlsGrp`

    Multi Episode:

    `The Series Title! - S01E01-E02-E03 - 001-002-003 - [HDTV-720p][DTS 5.1][x264]-RlsGrp`

------

### Series Folder Format

```bash
{Series TitleYear}
```

RESULT:

`The Series Title! (2010)`

#### Optional Series Folder Format for the Plex TV Series Scanner

This naming scheme is made to be compatible with the beta [Plex TV Series Scanner](https://forums.plex.tv/t/beta-new-plex-tv-series-scanner/696242){:target="_blank" rel="noopener noreferrer"} that now support IMDB and TVDB IDs in file names.

```bash
{Series TitleYear} [imdb-{ImdbId}]
```

RESULT:

`The Series Title! (2010) [imdb-tt1520211]`

!!! note
    The officially supported format is `{imdb-{ImdbId}}` but plex should also support `(imdb-{ImdbId})` or `[imdb-{ImdbId}]`, though the above should work for now. IMDb IDs are going to be very accurate and rarely change, TVDB/TMDB IDs, on the other hand, do change or are removed more frequently.

!!! info
    It's actually not needed to add a ID to the folder or filename to use the beta Plex TV Series Scanner.

------

### Season Folder Format

For this there's only one real option to use in my opinion.

```bash
Season {season:00}
```

RESULT:

`Season 01`

------

### Multi-Episode Style

```bash
Scene
```

RESULTS:

![results](images/results.png)

------

## Original Title vs  Original Filename

Want to keep the original release name that holds like all the info of the file then I suggest to use `{Original Title}` over  `{Original Filename}`

Why?

The filename can be Obscured where the Release naming isn't especially when you use Usenet.

`{Original Title}` => `The.Series.Title.S01E01.Episode.Title.1080p.AMZN.WEB-DL.DDP5.1.H.264-RlsGrp`

`{Original Filename}` => `show episode 1-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

------

THNX:

A big thnx to [fryfrog](https://github.com/fryfrog), [rg9400](https://github.com/rg9400) and [bakerboy448](https://github.com/bakerboy448) for the suggestions.
