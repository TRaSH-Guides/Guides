# Recommended naming scheme

Often on Sonarr discord people asking what's the recommended/best way to naming your files.
first of it's personal preference, but the support staff often recommend to add also non recoverable info.

Why?

if you even need to do a re-install, re-import for what ever reason in Radarr or Plex/Emby/JellyFin it's nice to have all that info in the filename so it get's imported correctly and not been matched as HDTV or WEB-DL etc.

The Tokens not available in the release won't be used/shown.

------

## Standard Episode Format

> **All the details**

```bash
{Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} {[Quality Full]}{ [Preferred Words]} {[MediaInfo VideoDynamicRange]} [{MediaInfo VideoBitDepth}bit] {[MediaInfo VideoCodec]} {[MediaInfo-AudioCodec}-{MediaInfo AudioChannels]}{[MediaInfo AudioLanguages]}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! (2010) - S01E01 - Episode Title 1 [HDTV-720p Proper] [iNTERNAL] [HDR] [10bit] [x264] [DTS 5.1]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - S01E01-E02-E03 - Episode Title [HDTV-720p Proper] [iNTERNAL] [HDR] [10bit] [x264] [DTS 5.1]-RlsGrp`

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
{Series TitleYear} - {Air-Date} - {Episode CleanTitle} {[Quality Full]}{ [Preferred Words]} {[MediaInfo VideoDynamicRange]} [{MediaInfo VideoBitDepth}bit] {[MediaInfo VideoCodec]} {[MediaInfo-AudioCodec}-{MediaInfo AudioChannels]}{[MediaInfo AudioLanguages]}{-Release Group}
```

??? summary "RESULTS:"

    `The Series Title! (2010) - 2013-10-30 - Episode Title 1 [HDTV-720p Proper] [iNTERNAL] [HDR] [10bit] [x264] [DTS-5.1]-RlsGrp`

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
{Series TitleYear} - {absolute:000} - S{season:00}E{episode:00} - {Episode CleanTitle} {[Quality Full]}{ [Preferred Words]} {[MediaInfo VideoDynamicRange]} [{MediaInfo VideoBitDepth}bit] {[MediaInfo VideoCodec]} {[MediaInfo-AudioCodec}-{MediaInfo AudioChannels]}{[MediaInfo AudioLanguages]}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! (2010) - 001 - S01E01 - Episode Title 1 [HDTV-720p v2] [iNTERNAL] [HDR] [10bit] [x264] [DTS-5.1][[JA]]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - 001-002-003 - S01E01-E02-E03 - Episode Title [HDTV-720p v2] [iNTERNAL] [HDR] [10bit] [x264] [DTS-5.1][[JA]]-RlsGrp`

> **Minimal details + the irreplaceable data**

```bash
{Series Title} - {absolute:000} - S{season:00}E{episode:00} - {[Quality Title]}{[MediaInfo AudioCodec}{ MediaInfo AudioChannels]}{[MediaInfo VideoCodec]}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! - 001 - S01E01 - [HDTV-720p][DTS 5.1][x264]-RlsGrp`

    Multi Episode:

    `The Series Title! - 001-002-003 - S01E01-E02-E03 - [HDTV-720p][DTS 5.1][x264]-RlsGrp`

------

### Series Folder Format

```bash
{Series TitleYear}
```

RESULT:

`The Series Title! (2010)`

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
