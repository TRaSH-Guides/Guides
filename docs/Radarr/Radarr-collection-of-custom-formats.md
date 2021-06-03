# Collection of Custom Formats

Here I will try to collect a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on discord or that I created with help from others.
Special thanks to [rg9400](https://github.com/rg9400), [bakerboy448](https://github.com/bakerboy448) and Team Radarr.

With Radarr V3, Custom Formats are much more advanced/powerful than with v0.2, although this also means a Custom Format is much more complicated to setup.

After requesting at Team Radarr we now have the options to import/export the Custom Formats in a JSON format that we can use here what makes it easier to share the different kind of Custom Formats.

I also made 2 guides related to this one.

- [How to import Custom Formats](/Radarr/Radarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to import the Custom Formats.
- [How to setup Custom Formats](/Radarr/Radarr-setup-custom-formats){:target="_blank" rel="noopener noreferrer"} Where I will try to explain how to make the most use of Custom Formats and show some personal examples that I'm using. That you can use to get a idea how to setup yours.

!!! tip

    I also suggest to change the Propers and Repacks settings in Radarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repack-proper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Formats preferences will be used and not ignored.

------

## INDEX

------

| Audio                                    | Audio Advanced #1                         | Audio Advanced #2               | Audio Channels               |
| :--------------------------------------- | ----------------------------------------- | ------------------------------- | ---------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [TrueHD ATMOS](#truehd-atmos)             | [FLAC](#flac)                   | [1.0 Mono](#10-mono)         |
| [DTS-HD/DTS:X](#dts-hddtsx)              | [DTS X](#dts-x)                           | [PCM](#pcm)                     | [2.0 Stereo](#20-stereo)     |
| [Surround Sound](#surround-sound)        | [ATMOS (undefined)](#atmos-undefined)     | [DTS-HD HRA](#dts-hd-hra)       | [3.0 Sound](#30-sound)       |
|                                          | [DD+ ATMOS](#dd-atmos)                    | [AAC](#aac)                     | [4.0 Sound](#40-sound)       |
|                                          | [TrueHD](#truehd)                         | [Dolby Digital](#dolby-digital) | [5.1 Surround](#51-surround) |
|                                          | [DTS-HD MA](#dts-hd-ma)                   | [MP3](#mp3)                     | [6.1 Surround](#61-surround) |
|                                          | [Dolby Digital Plus](#dolby-digital-plus) | [Opus](#opus)                   | [7.1 Surround](#71-surround) |
|                                          | [DTS-ES](#dts-es)                         |                                 | [9.1 Surround](#91-surround) |
|                                          | [DTS](#dts)                               |                                 |                              |

------

| HDR Metadata                            | Movie Versions                                | Misc (-1000)                        | Misc                                      |
| --------------------------------------- | --------------------------------------------- | ----------------------------------- | ----------------------------------------- |
| [Dolby Vision](#dovi)                   | [Hybrid](#hybrid)                             | [BR-DISK](#br-disk)                 | [Repack/Proper](#repack-proper)           |
| [Dolby Vision (Single Layer)](#dovi-sl) | [Remaster](#remaster)                         | [EVO (no WEBDL)](#evo-no-webdl)     | [Streaming Services](#streaming-services) |
| [HDR](#hdr)                             | [4K Remaster](#4k-remaster)                   | [Low Quality Releases](#lq)         | [High Quality Releases](#hq)              |
| [HDR (undefined)](#hdr-undefined)       | [Special Editions](#special-edition)          | [720/1080p no x265](#x265-7201080p) | [x264](#x264)                             |
| [10 Bit](#10-bit)                       | [Criterion Collection](#criterion-collection) | [3D](#3d)                           | [x265](#x265)                             |
|                                         | [Theatrical Cut](#theatrical-cut)             | [No-RlsGroup](#no-rlsgroup)         | [MPEG2](#mpeg2)                           |
|                                         | [IMAX](#imax)                                 | [Obfuscated](#obfuscated)           | [FreeLeech](#freeleech)                   |
|                                         |                                               | [DoVi (WEBDL)](#dovi-webdl)         | [Dutch Groups](#dutch-groups)             |
|                                         |                                               |                                     | [Anime Dual Audio](#anime-dual-audio)     |
|                                         |                                               |                                     | [Multi](#multi)                           |
|                                         |                                               |                                     | [HQ-WEBDL](#hq-webdl)                     |

## Audio

------

### Dolby TrueHD/ATMOS

>If you prefer TrueHD|Atmos audio tracks.

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dolby-truehdatmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD/DTS:X

>If you prefer DTS-HD/DTS:X audio tracks.

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-hddtsx.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Surround Sound

>If you prefer all kind of surround sounds

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/surround-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Audio Advanced

------

### TrueHD ATMOS

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}
>
>Dolby Atmos is a surround sound technology developed by Dolby Laboratories. It expands on existing surround sound systems by adding height channels, allowing sounds to be interpreted as three-dimensional objects.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS X

>DTS:X is an object-based audio codec, which aims to create a multi-dimensional sound that “moves around you like it would in real life”

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-x.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATMOS (undefined)

>Handles cases where only Atmos is specified in title but not DD+ or TrueHD (Where it is not specified if it is Lossy or Lossless)

!!! note
    Give this the same score as Lossy Atmos, and then on import, it will get changed to either lossy or lossless based on mediainfo.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DD+ ATMOS

>Atmos via UHD Blu-ray will be lossless, or lossy via streaming services so in this case it will be lossy + Atmos

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TrueHD

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}
>
>Dolby TrueHD is a lossless, multi-channel audio codec developed by Dolby Laboratories for home video, used principally in Blu-ray Disc and compatible hardware.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}
>
>DTS-HD Master Audio is a multi-channel, lossless audio codec developed by DTS as an extension of the lossy DTS Coherent Acoustics codec (DTS CA; usually itself referred to as just DTS). Rather than being an entirely new coding mechanism, DTS-HD MA encodes an audio master in lossy DTS first, then stores a concurrent stream of supplementary data representing whatever the DTS encoder discarded. This gives DTS-HD MA a lossy "core" able to be played back by devices that cannot decode the more complex lossless audio. DTS-HD MA's primary application is audio storage and playback for Blu-ray Disc media.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FLAC

>FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

>PCM is the method of encoding typically used for uncompressed digital audio

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

>Description placeholder

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-hd-hra.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dolby Digital Plus

<sub>Dolby Digital Plus = DD+</sub>
>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital_Plus){:target="_blank" rel="noopener noreferrer"}
>
>Dolby Digital Plus, also known as Enhanced AC-3 (and commonly abbreviated as DD+ or E-AC-3, or EC-3) is a digital audio compression scheme developed by Dolby Labs for transport and storage of multi-channel digital audio. It is a successor to Dolby Digital (AC-3).

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dolby-digital-plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

>DTS-ES (DTS Extended Surround) includes two variants, DTS-ES Discrete 6.1, and DTS-ES Matrix 5.1, depending on how the sound was originally mastered and stored.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

<sub>DTS = Basic DTS</sub>
>Description placeholder

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### AAC

Advanced Audio Coding
>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
>Advanced Audio Coding (AAC) is an audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves higher sound quality than MP3 at the same bit rate.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/aac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dolby Digital

<sub>(Basic) Dolby Digital = DD</sub>
>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital){:target="_blank" rel="noopener noreferrer"}
>
>Dolby Digital, also known as Dolby AC-3, the audio compression is lossy.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dolby-digital.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MP3

>Description placeholder

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Opus

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}
>
>Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Audio Channels

------

### 1.0 Mono

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stereo

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3.0 Sound

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4.0 Sound

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 5.1 Surround

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 6.1 Surround

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 7.1 Surround

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 9.1 Surround

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/91-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HDR metadata

------

### DoVi

<sub>Dolby Vision = DoVi</sub>
>Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.
>
>Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dovi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DoVi (SL)

<sub><sub><sub>Score [295]</sub>

<sub>Dolby Vision (Single Layer) = DoVi (SL)</sub>
>Custom Format for Single Layer Dolby Vision releases.

!!! note

    This used to be the the preferred option for PLeX with a Shield 2019 model that supports DV.

    But now DV is part of the MKV spec and ExoPlayer added native support.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dovi-sl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
>
>High-dynamic-range video (HDR video) is video having a dynamic range greater than that of standard-dynamic-range video (SDR video).HDR video involves capture, production, content/encoding, and display. HDR capture and displays are capable of brighter whites and deeper blacks. To accommodate this, HDR encoding standards allow for a higher maximum luminance and use at least a 10-bit dynamic range (color depth, compared to 8-bit for non-professional and 10-bit for professional SDR video) in order to maintain precision across this extended range.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (undefined)

>Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.
>
>For now it's only FraMeSToR that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hdr-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 10 Bit

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/10-bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Movie Versions

------

### Hybrid

>A hybrid release means any combination of sources (video + audio) and not a direct encode of a single source. Generally you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hybrid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remaster

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}
>
>For the software term, see Software remastering.
Remaster (also digital remastering and digitally remastered) refers to changing the quality of the sound or of the image, or both, of previously created recordings, either audiophonic, cinematic, or videographic.

??? example "json"

    ```json
     [[% filter indent(width=4) %]][[% include 'json/radarr/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4K Remaster

>A remastered or mastered in 4K should give you usually the best picture and audio currently for the movie. Both are just names to describe the best possible currently for the movie.
>
>To be clear, the final digital films on the Mastered in 4K Blu-rays still only have the same 1920 x 1080 pixels of actual resolution as normal Blu-rays. But the argument goes that because these full HD files were derived from higher-resolution masters, their images will be more precise, with better colours, less noise, and enhanced sharpness and detail. Not least because the higher-resolution mastering process will provide more detail from the original print for the Blu-ray masters to draw on when going through their (hopefully…) frame-by-frame compression process.
>
>Another important element of the Mastered in 4K discs is that they’re all mastered with ‘x.v.YCC’ colour specification. This delivers an expanded colour range closer to that contained in original source material.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/4k-remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Criterion Collection

>The Criterion Collection, Inc. (or simply Criterion) is an American home video distribution company which focuses on licensing "important classic and contemporary films" and selling them to film aficionados.Criterion has helped to standardize characteristics of home video such as film restoration, using the letterbox format for widescreen films, and adding bonus features and commentary tracks.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/criterion-collection.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Theatrical Cut

>The Theatrical Cut is the version of the film that was shown at cinemas.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/theatrical-cut.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Special Edition

>Custom format for several Special Editions
>
> - The Director's Cut is the version edited by the Director, usually for additional home media releases.
> - An Extended Cut is usually any version of the film which is longer than the theatrical cut (though in very rare cases, its shorter).

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/special-edition.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IMAX

>Description placeholder

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/imax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc (-1000)

------

### BR-DISK

>This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
>
>You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-9999`

!!! note

    Depending on your renaming scheme it could happen that Radarr will match renamed files after they are downloaded and imported as `BR-DISK`,
    This is a cosmetic annoyance till I come up for another way to solve this,
    being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
    Several reasons why this is happening:

    - Blame the often wrongly used naming of x265 encodes.
    - Radarr v3 uses dynamic custom formats.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### EVO (no WEBDL)

>This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
>
>You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-9999`

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/evo-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ

<sub>Low Quality Releases = LQ</sub>
>A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality.

!!! note

    You might want to add the following also [EVO (no WEBDL)](#evo-no-webdl)

    - BLOCK1 = Low-Quality Releases (often banned groups)
    - BLOCK2 = Another Small list of often banned groups.
    - BLOCK3 = And Another list.
    - BLOCK4 = Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.
    - BLOCK5 = RiffTrax is an American company that produces scripted humorous audio commentary tracks intended to be played in unison with particular television programs and films, In short just annoying !!!

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (720/1080p)

<sub>720/1080p no x265 = x265 (720/1080p)</sub>
>This blocks/ignores 720/1080p releases that are encoded in x265
>
>You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-9999`

!!! quote
    x265 is good for for 4k stuff or 1080p if they used the the remuxes as source.
    If the media isn't source quality/remux, then there will be a loss of quality every time.
    Also, once you go x265, typically that file is done.
    It can't be changed to something else without a huge loss of quality.

    Something like 95% of video files are x264 and have much better direct play support.
    If you have more than a couple users,
    you will notice much more transcoding.
    Just depends on your priorities.

    So basically if you are storage poor and just need to save space, use x265.
    The catch is if you want best quality x265, you need source quality files, so you still have huge file sizes.
    If you want maximum compatibility and the option to change your files to something else later,
    then x264.
    It's all really dependent on specific situations for different people

It's a shame that most x265 groups microsize the releases or use the x264 as source what results in low quality releases. And the few groups that do use the correct source suffer from it.

That's why I created my own golden rule.

- 720/1080p => x264
- 2160p/4k => x265

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/x265-7201080p.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3D

>If you prefer or not prefer 3D.
>
>You can use Custom Format or use Restrictions (`Settings` => `Indexers` => `Restrictions`) what ever you prefer.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/3d.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### No-RlsGroup

>Some indexers strip out the release group what could result in LQ groups getting a higher score.
>For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match

!!! warning

    If you don't use a decent filenames like not adding release groups don't add this Custom Format, except if you want to upgrade them.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Obfuscated

> Optional (use these only if you dislike renamed and retagged releases)

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DoVi (WEBDL)

<sub>Dolby Vision = DoVi</sub>

>This is a special Custom Format that ignores DV for WEB-DL but together with the normal [DoVi](#dovi) allows for other sources.
>
>WEB-DL from Streaming Services don't have the fallback to HDR(10), What can results in weird playback issues like weird colors if you want to play it on a not DoVi compatible setup.
>Remuxes and Bluray have a fallback to HDR(10).

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dovi-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc

------

### HQ

<sub>HQ-Releases = HQ</sub>
>A collection of P2P groups that are known for their high quality releases.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack Proper

<sub><sub><sub>Score [1]</sub>

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Streaming Services

>Collection of Streaming Services

!!! attention

    This CF only prefers the known streaming services and doesn't work the same way like the release profile that can be used in Sonarr to include the streaming service name in your renaming scheme when using `{[Custom Formats]}` !!!
    If you want to have this option then you need to add them all separate.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/streaming-services.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x264

>x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/x264.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265

>x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

!!! quote
    x265 is good for for 4k stuff or 1080p if they used the the remuxes as source.
    If the media isn't source quality/remux, then there will be a loss of quality every time.
    Also, once you go x265, typically that file is done.
    It can't be changed to something else without a huge loss of quality.

    Something like 95% of video files are x264 and have much better direct play support.
    If you have more than a couple users,
    you will notice much more transcoding.
    Just depends on your priorities.

    So basically if you are storage poor and just need to save space, use x265.
    The catch is if you want best quality x265, you need source quality files, so you still have huge file sizes.
    If you want maximum compatibility and the option to change your files to something else later,
    then x264.
    It's all really dependent on specific situations for different people

It's a shame that most x265 groups microsize the releases or use the x264 as source what results in low quality releases. And the few groups that do use the correct source suffer from it.

That's why I created my own golden rule.

- 720/1080p => x264
- 2160p/4k => x265

> If you want to make use of the Golden Rule you could make use of the following Custom Format [720/1080p no x265](#x265-7201080p)

Some extra info about 4K/X265

[4k, transcoding, and you - aka the rules of 4k - a FAQ](https://forums.plex.tv/t/plex-4k-transcoding-and-you-aka-the-rules-of-4k-a-faq/378203) - Plex.tv

1. Don’t bother transcoding 4k
1. If you cannot direct play 4k, then perhaps you should not even be collecting 4k.
1. If you don’t have the storage space for a copy of both 4k and 1080/720, then perhaps you should not even be collecting 4k.
1. To avoid transcoding for remote and non-4k clients, keep your 4k content in separate plex libraries.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FreeLeech

>Sometimes, torrent sites set a torrent to be freeleech. This means, that the download of this torrent will not count towards your download quota or ratio. This is really useful, if you do not have the best ratio yet.

!!! attention
    Keep in mind not all trackers support this option.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/freeleech.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dutch Groups

>If you prefer movies with also a Dutch audio track.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dutch-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Dual Audio

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MPEG2

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HQ-WEBDL

> A personal collection of P2P WEB-DL groups that are known for their high quality releases.

??? example "json"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hq-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>
