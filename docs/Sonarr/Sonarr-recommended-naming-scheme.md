# Recommended naming scheme

On the [Sonarr Discord](https://discord.gg/M6BvZn5){:target="_blank" rel="noopener noreferrer"} people often ask, "What's the recommended/best way to
name your files?" First off, it's personal preference, but it's often recommended to add non-recoverable info.

Why?

If, for what ever reason, you ever need to do a re-install or re-import in
the Starr Apps or Plex/Emby/Jellyfin it's nice to have all that info in the filename so
it gets imported correctly and isn't incorrectly matched as HDTV or WEB-DL etc.

!!! info "The Tokens not available in the release won't be used/shown."

------

## Standard Episode Format

```bash
{Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRangeType]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{[MediaInfo VideoCodec]}{-Release Group}
```

!!! warning "Sonarr V4 - Is now using Custom Formats instead of Release Profiles. Use the below naming scheme instead :warning:"

    ```bash
    {Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} [{Custom Formats }{Quality Full}]{[MediaInfo VideoDynamicRangeType]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{[MediaInfo VideoCodec]}{-Release Group}
    ```

??? summary "RESULTS: - [CLICK TO EXPAND]"

    Single Episode:

    `The Series Title! (2010) - S01E01 - Episode Title 1 [AMZN WEBDL-1080p Proper][DV HDR10][DTS 5.1][x264]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - S01E01-E03 - Episode Title [AMZN WEBDL-1080p Proper][DV HDR10][DTS 5.1][x264]-RlsGrp`

------

## Daily Episode Format

```bash
{Series TitleYear} - {Air-Date} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRangeType]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{[MediaInfo VideoCodec]}{-Release Group}
```

!!! warning "Sonarr V4 - Is now using Custom Formats instead of Release Profiles. Use the below naming scheme instead :warning:"

    ```bash
    {Series TitleYear} - {Air-Date} - {Episode CleanTitle} [{Custom Formats }{Quality Full}]{[MediaInfo VideoDynamicRangeType]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{[MediaInfo VideoCodec]}{-Release Group}
    ```

??? summary "RESULTS: - [CLICK TO EXPAND]"

    `The Series Title! (2010) - 2013-10-30 - Episode Title 1 [AMZN WEBDL-1080p Proper][DV HDR10][DTS 5.1][x264]-RlsGrp`

------

## Anime Episode Format

```bash
{Series TitleYear} - S{season:00}E{episode:00} - {absolute:000} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRangeType]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}[{Mediainfo AudioCodec} { Mediainfo AudioChannels}]{MediaInfo AudioLanguages}{-Release Group}
```

!!! warning "Sonarr V4 - Is now using Custom Formats instead of Release Profiles. Use the below naming scheme instead :warning:"

    ```bash
    {Series TitleYear} - S{season:00}E{episode:00} - {absolute:000} - {Episode CleanTitle} [{Custom Formats }{Quality Full}]{[MediaInfo VideoDynamicRangeType]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}[{Mediainfo AudioCodec} { Mediainfo AudioChannels}]{MediaInfo AudioLanguages}{-Release Group}
    ```

??? summary "RESULTS: - [CLICK TO EXPAND]"

    Single Episode:

    `The Series Title! (2010) - S01E01 - 001 - Episode Title 1 [iNTERNAL HDTV-720p v2][HDR10][10bit][x264][DTS 5.1][JA]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - S01E01-E03 - 001-003 - Episode Title [iNTERNAL HDTV-720p v2][HDR10][10bit][x264][DTS 5.1][JA]-RlsGrp`

------

### Series Folder Format

```bash
{Series TitleYear}
```

RESULT:

`The Series Title! (2010)`

#### Optional Series Folder Format for the Plex TV Series Scanner and Jellyfin/Emby

This naming scheme is made to be compatible with the new [Plex TV Series Scanner](https://forums.plex.tv/t/beta-new-plex-tv-series-scanner/696242){:target="_blank" rel="noopener noreferrer"} that now support IMDB and TVDB IDs in file names.

For Plex:

```bash
{Series TitleYear} [imdb-{ImdbId}]
```

RESULT:

`The Series Title! (2010) [imdb-tt1520211]`

For Jellyfin/Emby:

```bash
{Series TitleYear} [tvdbid-{TvdbId}]
```

RESULT:

`The Series Title! (2010) [tvdbid-tt1520211]`

!!! tip
    IMDb IDs are going to be very accurate and rarely change, TVDB/TMDB IDs, on the other hand, do change or are removed more frequently.

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
Prefixed Range
```

RESULTS:

![results](images/results.png)

------

## Original Title vs  Original Filename

Another option is to use `{Original Title}` rather than the recommeneded naming scheme outlined aboove. `{Original Title}` will use the title of the release which will contain all of the information included in the release itself. The benefit of this naming scheme is to prevent download loops which can occur on import when there is a discrepancy in the release title compared to the contents of the file itself (for example, if the release title says DTS-ES but the contents are actually DTS). The downside is less flexibility with how the files are named.

If using this alternate naming scheme I suggest using `{Original Title}` over `{Original Filename}`

Why?

The filename can be Obscured where the Release naming isn't, especially when you use Usenet.

`{Original Title}` => `The.Series.Title.S01E01.Episode.Title.1080p.AMZN.WEB-DL.DDP5.1.H.264-RlsGrp`

`{Original Filename}` => `show episode 1-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

------

Thanks:

A big Thanks to [fryfrog](https://github.com/fryfrog), [rg9400](https://github.com/rg9400) and [bakerboy448](https://github.com/bakerboy448) for the suggestions.

{! include-markdown "../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
