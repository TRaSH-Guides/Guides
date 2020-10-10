## Sonarr recommended naming scheme examples

Often on Sonarr discord people asking what's the recommended/best way to naming your files.
first of it's personal preference, but the support staff often recommend to add also non recoverable info.
Why ?

if you even need to do a re-install, re-import for what ever reason in Radarr or Plex/Emby/JellyFin it's nice to have all that info in the filename so it get's imported correctly and not been matched as HDTV or WEB-DL etc.

The Tokens not available in the release won't be used/shown. 

[Standard Episode Format](#standard-movie-format-examples)

[Daily Episode Format](#daily-episode-format)

[Anime Episode Format](#anime-episode-format)

[Series Folder Format](#series-folder-format)

[Season Folder Format](#season-folder-format)

[Multi-Episode Style][#multi-episode-style]

[Original Title vs  Original Filename](#original-title-vs-original-filename)

------

### Standard Episode Format

`{Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} {[Quality Full]}{[MediaInfo Simple]}{[Preferred Words]}{-Release Group}`

RESULT:

Single Episode: `The Series Title! (2010) - S01E01 - Episode Title 1 [HDTV-720p Proper][x264 DTS][iNTERNAL]-RlsGrp`

Multi Episode: `The Series Title! (2010) - S01E01-E02-E03 - Episode Title [HDTV-720p Proper][x264 DTS][iNTERNAL]-RlsGrp`

------

`{Series TitleYear} - S{season:00}E{episode:00} - {Episode Title} {[Quality Full]} {[MediaInfo VideoDynamicRange]} [{Mediainfo VideoBitDepth}bit] [{Mediainfo VideoCodec}] [{Mediainfo AudioCodec} { Mediainfo AudioChannels}]{ MediaInfo AudioLanguages}{-Release Group}`

RESULTS:

Single Episode: `The Series Title! (2010) - S01E01 - Episode Title (1) [HDTV-720p Proper] [HDR] [10bit] [x264] [DTS 5.1]-RlsGrp`

Multi Episode: `The Series Title! (2010) - S01E01-E02-E03 - Episode Title [HDTV-720p Proper] [HDR] [10bit] [x264] [DTS 5.1]-RlsGrp`

------

### Daily Episode Format

`{Series Title} - {Air-Date} - {Episode CleanTitle} {[Quality Full]} {[MediaInfo Simple]}{-Release Group}`

RESULT:

`The Series Title! - 2013-10-30 - Episode Title 1 [HDTV-720p Proper] [x264 DTS]-RlsGrp`

------

### Anime Episode Format

`{Series Title} - {absolute:000} - S{season:00}E{episode:00} - {Episode CleanTitle} {[Quality Full]} {[MediaInfo Simple]}{-Release Group}`

RESULT:

Single Episode: `The Series Title! - 001 - S01E01 - Episode Title 1 [HDTV-720p v2] [x264 DTS]-RlsGrp`

Multi Episode: `The Series Title! - 001-002-003 - S01E01-E02-E03 - Episode Title [HDTV-720p v2] [x264 DTS]-RlsGrp`

------
##### Original Title vs  Original Filename

> Want to keep the original release name that holds like all the info of the file then I suggest to use `{Original Title}` over  ` {Original Filename}` !!!
>
> Why ? 
>
> The filename can be Obscured where the Release naming isn't especially when you use Usenet.
>
> `{Original Title}` => `The.Series.Title.S01E01.Episode.Title.1080p.AMZN.WEB-DL.DDP5.1.H.264-RlsGrp`
>
> ` {Original Filename}` => `show episode 1-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

------

### Series Folder Format

`{Series TitleYear}`

RESULT:

`The Series Title! (2010)`

------

### Season Folder Format

> For this theirs only one real option to use in my opinion.

`Season {season:00}`

RESULT:

`Season 01`

------

### Multi-Episode Style

`Scene`

RESULTS:

 ![image-20201010205202708](../SonarrV3/images/image-20201010205202708.png)

