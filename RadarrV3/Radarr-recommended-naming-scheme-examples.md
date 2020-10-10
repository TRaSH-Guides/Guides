## Radarr recommended naming scheme examples

Often on Radarr discord people asking what's the recommended/best way to naming your files.
first of it's personal preference, but the support staff often recommend to add also non recoverable info.
Why ?

if you even need to do a re-install, re-import for what ever reason in Radarr or Plex/Emby/JellyFin it's nice to have all that info in the filename so it get's imported correctly and not been matched as HDTV or WEB-DL etc.

The Tokens not available in the release won't be used/shown. 

[Standard Movie Format Examples](#standard-movie-format-examples)

[Movie Folder Format Examples](#movie-folder-format-examples)

[Original Title vs  Original Filename](#original-title-vs-original-filename)

------

### Standard Movie Format Examples

> This naming scheme is made to be compatible with the [New Plex Agent](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517) that now support IMDB and TMDB IDs in file names.

`{Movie CleanTitle} {(Release Year)} {Edition Tags} [imdb-{ImdbId}]{[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRange]}[{Mediainfo VideoBitDepth}bit][{Mediainfo VideoCodec}]{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}]{-Release Group}`

RESULT:

 `The Movie Title (2010) Ultimate Extended Edition [imdb-tt0066921][Surround Sound x264][Bluray-1080p Proper][3D][HDR][10bit][x264][DTS 5.1]-EVOLVE`

------

> New Plex agent support + Added Custom Format + Audio Track Languages.

`{Movie Title} {(Release Year)} {Edition Tags} [imdb-{ImdbId}] {[Custom Formats]} {[Quality Full]} {[MediaInfo 3D]} {[MediaInfo VideoDynamicRange]}  [{Mediainfo VideoBitDepth}bit] [{Mediainfo VideoCodec}] {[Mediainfo AudioCodec} { Mediainfo AudioChannels}]{ MediaInfo AudioLanguages}{-Release Group}`

RESULT:

`The Movie - Title (2010) Ultimate Extended Edition [imdb-tt0066921] [Surround Sound x264] [Bluray-1080p Proper] [3D] [HDR] [10bit] [x264] [DTS 5.1] [DE]-EVOLVE`

------

> Want something shorter with the New Plex agent support ? 

`{Movie CleanTitle} {(Release Year)} {Edition Tags} [imdb-{ImdbId}]{[Quality Full]}{[MediaInfo AudioCodec}{ MediaInfo AudioChannels]}{[MediaInfo VideoCodec]}{-Release Group}`

RESULT:

`The Movie Title (2010) Ultimate Extended Edition [imdb-tt0066921][Bluray-1080p Proper][DTS 5.1][x264]-EVOLVE`

------
##### Original Title vs  Original Filename

> Want to keep the original release name that holds like all the info of the file then I suggest to use `{Original Title}` over  ` {Original Filename}` !!!
>
> Why ? 
>
> The filename can be Obscured where the Release naming isn't especially when you use Usenet.
>
> `{Original Title}` => `The.Movie.Title.2010.REMASTERED.1080p.BluRay.x264-GROUP`
>
> ` {Original Filename}` => `group-karatekid-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

------

### Movie Folder Format Examples

`{Movie CleanTitle} ({Release Year})`

RESULT:

`The Movie Title (2010)`

------

`{Movie Title} ({Release Year})`

RESULT:

`The Movie - Title (2010)`

------

> Keep in mind adding anything more after the release year could give issues during a fresh import in to Radarr, but in this examples it helps for movies that have the same release name and year.

`{Movie CleanTitle} {(Release Year)} [imdb-{ImdbId}]`

RESULT:

`The Movie Title (2010) [imdb-tt0066921]`

------

> Keep in mind adding anything more after the release year could give issues during a fresh import in to Radarr, but in this examples it helps for movies that have the same release name and year.

`{Movie Title} {(Release Year)} [imdb-{ImdbId}]`

RESULT:

`The Movie - Title (2010) [imdb-tt0066921]`