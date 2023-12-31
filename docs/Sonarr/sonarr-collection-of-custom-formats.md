# Collection of Custom Formats

Here I will try to list a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on Discord or that I created with help from others.
Special thanks to everyone that helped testing and creating these Custom Formats.

With Sonarr V4+, Custom Formats are much more advanced/powerful than with the release profiles, although this also means a Custom Format is much more complicated to setup.

I also made 3 guides related to this one.

- [How to import Custom Formats](/Sonarr/sonarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to import the Custom Formats.
- [How to upgrade Custom Formats](/Sonarr/sonarr-how-to-update-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to upgrade your existing Custom Formats.
- [How to setup Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to make the most use of Custom Formats and show some personal examples that I'm using. You can use these to get an idea on how to setup your own.

!!! tip

    I also suggest to change the Propers and Repacks settings in Sonarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repackproper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Format preferences will be used instead.

--8<-- "includes/support.md"

------

## INDEX

------

| Audio Advanced #1                     | Audio Advanced #2         | Audio Channels               | HDR Formats                       |
| ------------------------------------- | ------------------------- | ---------------------------- | --------------------------------- |
| [TrueHD ATMOS](#truehd-atmos)         | [FLAC](#flac)             | [1.0 Mono](#10-mono)         | [DV HDR10Plus](#dv-hdr10plus)     |
| [DTS X](#dts-x)                       | [PCM](#pcm)               | [2.0 Stereo](#20-stereo)     | [DV HDR10](#dv-hdr10)             |
| [ATMOS (undefined)](#atmos-undefined) | [DTS-HD HRA](#dts-hd-hra) | [3.0 Sound](#30-sound)       | [DV](#dv)                         |
| [DD+ ATMOS](#ddplus-atmos)            | [AAC](#aac)               | [4.0 Sound](#40-sound)       | [DV HLG](#dv-hlg)                 |
| [TrueHD](#truehd)                     | [DD](#dd)                 | [5.1 Surround](#51-surround) | [DV SDR](#dv-sdr)                 |
| [DTS-HD MA](#dts-hd-ma)               | [MP3](#mp3)               | [6.1 Surround](#61-surround) | [HDR10+](#hdr10plus)              |
| [DD+](#ddplus)                        | [Opus](#opus)             | [7.1 Surround](#71-surround) | [HDR10](#hdr10)                   |
| [DTS-ES](#dts-es)                     |                           | [9.1 Surround](#91-surround) | [HDR](#hdr)                       |
| [DTS](#dts)                           |                           |                              | [HDR (undefined)](#hdr-undefined) |
|                                       |                           |                              | [PQ](#pq)                         |
|                                       |                           |                              | [HLG](#hlg)                       |

------

| Series Versions       | Unwanted                                | HQ Source Groups                        | Streaming Services                          |
| --------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------------- |
| [Hybrid](#hybrid)     | [BR-DISK](#br-disk)                     | [Remux Tier 01](#remux-tier-01)         | [Amazon](#amzn)                             |
| [Remaster](#remaster) | [LQ](#lq)                               | [Remux Tier 02](#remux-tier-02)         | [Apple TV+](#atvp)                          |
|                       | [LQ (Release Title)](#lq-release-title) | [HD Bluray Tier 01](#hd-bluray-tier-01) | [DC Universe](#dcu)                         |
|                       | [x265 (HD)](#x265-hd)                   | [HD Bluray Tier 02](#hd-bluray-tier-02) | [Disney+](#dsnp)                            |
|                       | [Extras](#extras)                       | [WEB Tier 01](#web-tier-01)             | [HBO Max](#hmax)                            |
|                       |                                         | [WEB Tier 02](#web-tier-02)             | [HBO](#hbo)                                 |
|                       |                                         | [WEB Tier 03](#web-tier-03)             | [Max](#max)                                 |
|                       |                                         | [WEB Scene](#web-scene)                 | [Hulu](#hulu)                               |
|                       |                                         |                                         | [IP](#ip)                                   |
|                       |                                         |                                         | [NLZiet](#nlz)                              |
|                       |                                         |                                         | [Netflix](#nf)                              |
|                       |                                         |                                         | [Paramount+](#pmtp)                         |
|                       |                                         |                                         | [Peacock TV](#pcok)                         |
|                       |                                         |                                         | [Quibi](#qibi)                              |
|                       |                                         |                                         | [SHOWTIME](#sho)                            |
|                       |                                         |                                         | [Stan](#stan)                               |
|                       |                                         |                                         | [Videoland](#vdl)                           |
|                       |                                         |                                         | [YouTube Red](#red)                         |
|                       |                                         |                                         | [iTunes](#it)                               |
|                       |                                         |                                         | [CANAL+](#canalplus)                        |
|                       |                                         |                                         | [SALTO](#salto)                             |
|                       |                                         |                                         | [RTBF](#rtbf)                               |
|                       |                                         |                                         | [Comedy Central](#cc)                       |
|                       |                                         |                                         | [Crave](#crav)                              |
|                       |                                         |                                         | [OViD](#ovid)                               |
|                       |                                         |                                         | [FOD](#fod)                                 |
|                       |                                         |                                         | [TVer](#tver)                               |
|                       |                                         |                                         | [U-NEXT](#u-next)                           |
|                       |                                         |                                         | [ALL4](#all4)                               |
|                       |                                         |                                         | [4OD](#4od)                                 |
|                       |                                         |                                         | [UHD Streaming Boost](#uhd-streaming-boost) |
|                       |                                         |                                         | [UHD Streaming Cut](#uhd-streaming-cut)     |

------

| Misc                           | Optional                            | French Audio Version          | French Source Groups                          |
| ------------------------------ | ----------------------------------- | ----------------------------- | --------------------------------------------- |
| [Repack/Proper](#repackproper) | [Bad Dual Groups](#bad-dual-groups) | [Multi-French](#multi-french) | [FR Remux Tier 01](#fr-remux-tier-01)         |
| [Repack v2](#repack-v2)        | [DV (WEBDL)](#dv-webdl)             | [Multi-Audio](#multi-audio)   | [FR HD Bluray Tier 01](#fr-hd-bluray-tier-01) |
| [Repack v3](#repack-v3)        | [HDR10+ Boost](#hdr10plus-boost)    | [French Audio](#french-audio) | [FR WEB Tier 01](#fr-web-tier-01)             |
| [Multi](#multi)                | [No-RlsGroup](#no-rlsgroup)         | [VFF](#vff)                   | [FR WEB Tier 02](#fr-web-tier-02)             |
| [MPEG2](#mpeg2)                | [Obfuscated](#obfuscated)           | [VOF](#vof)                   | [FR WEB Tier 03](#fr-web-tier-03)             |
| [x264](#x264)                  | [Retags](#retags)                   | [VFI](#vfi)                   | [FR Anime Tier 01](#fr-anime-tier-01)         |
| [x265](#x265)                  | [Scene](#scene)                     | [VF2](#vf2)                   | [FR Anime Tier 02](#fr-anime-tier-02)         |
|                                | [Season Packs](#season-pack)        | [VFQ](#vfq)                   | [FR Anime Tier 03](#fr-anime-tier-03)         |
|                                | [x265 (no HDR/DV)](#x265-no-hdrdv)  | [VOQ](#voq)                   | [FR Anime FanSub](#fr-anime-fansub)           |
|                                | [AV1](#av1)                         | [VQ](#vq)                     | [FR Scene Groups](#fr-scene-groups)           |
|                                | [SDR](#sdr)                         | [VFB](#vfb)                   | [FR LQ](#fr-lq)                               |
|                                | [SDR (no WEBDL)](#sdr-no-webdl)     | [VOSTFR](#vostfr)             |                                               |
|                                | [DV (Disk)](#dv-disk)               | [FanSUB](#fansub)             |                                               |
|                                | [HFR](#hfr)                         | [FastSUB](#fastsub)           |                                               |
|                                | [VP9](#vp9)                         |                               |                                               |
|                                | [Internal](#internal)               |                               |                                               |

------

| Anime Source Groups                                                         | Anime Source Groups                                                   | Anime Misc/Streaming Services | Anime Optional                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------- | ------------------------------------- |
| [Anime BD Tier 01 (Top SeaDex Muxers)](#anime-bd-tier-01-top-seadex-muxers) | [Anime Web Tier 01 (Muxers)](#anime-web-tier-01-muxers)               | [v0](#v0)                     | [Uncensored](#uncensored)             |
| [Anime BD Tier 02 (SeaDex Muxers)](#anime-bd-tier-02-seadex-muxers)         | [Anime Web Tier 02 (Top FanSubs)](#anime-web-tier-02-top-fansubs)     | [v1](#v1)                     | [10bit](#10bit)                       |
| [Anime BD Tier 03 (SeaDex Muxers)](#anime-bd-tier-03-seadex-muxers)         | [Anime Web Tier 03 (Official Subs)](#anime-web-tier-03-official-subs) | [v2](#v2)                     | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 04 (SeaDex Muxers)](#anime-bd-tier-04-seadex-muxers)         | [Anime Web Tier 04 (Official Subs)](#anime-web-tier-04-official-subs) | [v3](#v3)                     | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 05 (Remuxes)](#anime-bd-tier-05-remuxes)                     | [Anime Web Tier 05 (FanSubs)](#anime-web-tier-05-fansubs)             | [v4](#v4)                     |                                       |
| [Anime BD Tier 06 (FanSubs)](#anime-bd-tier-06-fansubs)                     | [Anime Web Tier 06 (FanSubs)](#anime-web-tier-06-fansubs)             | [B-Global](#b-global)         |                                       |
| [Anime BD Tier 07 (P2P/Scene)](#anime-bd-tier-07-p2pscene)                  | [Anime Raws](#anime-raws)                                             | [Bilibili](#bilibili)         |                                       |
| [Anime BD Tier 08 (Mini Encodes)](#anime-bd-tier-08-mini-encodes)           | [Anime LQ Groups](#anime-lq-groups)                                   | [Crunchyroll](#cr)            |                                       |
|                                                                             |                                                                       | [Funimation](#funi)           |                                       |
|                                                                             |                                                                       | [HIDIVE](#hidive)             |                                       |
|                                                                             |                                                                       | [VRV](#vrv)                   |                                       |
|                                                                             |                                                                       | [ABEMA](#abema)               |                                       |
|                                                                             |                                                                       | [ADN](#adn)                   |                                       |
|                                                                             |                                                                       | [WKN](#wkn)                   |                                       |

## Audio Advanced

------

### TrueHD ATMOS

??? question "TrueHD ATMOS - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}

    Dolby Atmos is a surround sound technology developed by Dolby Laboratories. It expands on existing surround sound systems by adding height channels, allowing sounds to be interpreted as three-dimensional objects.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS X

??? question "DTS:X - [Click to show/hide]"

    [DTS:X is an object-based audio codec](https://www.whathifi.com/advice/dtsx-what-it-how-can-you-get-it), which aims to create a multi-dimensional sound that “moves around you like it would in real life”.
    You may think that sounds a lot like Dolby Atmos, and you’d be right. But where DTS:X differs lies in the required speaker configuration. While Dolby Atmos requires you to add extra overhead channels to your 5.1 or 7.1 setup, DTS:X works with standard surround speaker setups – just like the one you might already have at home. It can support up to 32 speaker locations and up to an 11.2-channel system.
    DTS:X like other higher quality DTS formats (e.g. DTS-HD MA) is lossless.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-x.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATMOS (undefined)

??? question "ATMOS (undefined) - [Click to show/hide]"

    Handles cases where only Atmos is specified in title but not DD+ or TrueHD (Where it is not specified if it is Lossy or Lossless)

    !!! note
        Give this the same score as Lossy Atmos, and then on import, it will get changed to either lossy or lossless based on mediainfo.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus ATMOS

<sub>DDPlus = DD+</sub>

??? question "DD+ ATMOS - [Click to show/hide]"

    Atmos via UHD Blu-ray will be lossless, or lossy via streaming services so in this case it will be lossy + Atmos

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TrueHD

??? question "TrueHD - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}

    Dolby TrueHD is a lossless, multi-channel audio codec developed by Dolby Laboratories for home video, used principally in Blu-ray Disc and compatible hardware.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

??? question "DTS-HD MA - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}

    DTS-HD Master Audio is a multi-channel, lossless audio codec developed by DTS as an extension of the lossy DTS Coherent Acoustics codec (DTS CA; usually itself referred to as just DTS). Rather than being an entirely new coding mechanism, DTS-HD MA encodes an audio master in lossy DTS first, then stores a concurrent stream of supplementary data representing whatever the DTS encoder discarded. This gives DTS-HD MA a lossy "core" able to be played back by devices that cannot decode the more complex lossless audio. DTS-HD MA's primary application is audio storage and playback for Blu-ray Disc media.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FLAC

??? question "FLAC - [Click to show/hide]"

    FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

??? question "PCM - [Click to show/hide]"

    PCM is the method of encoding typically used for uncompressed digital audio

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

??? question "DTS-HD HRA - [Click to show/hide]"

    [Technical Whitepaper](https://www.opusproductions.com/pdfs/DTS_HD_WhitePaper.pdf){:target="_blank" rel="noopener noreferrer"}

    | Codec      | Page   | Paragraph |
    | ---------- | ------ | --------- |
    | DTS-HD MA  | Page 6 | 5.1.1     |
    | DTS-HD HRA | Page 7 | 5.1.2     |

    DTS-HD HRA is the lossy version of DTS-HD MA.

    | Codec          | DTS-HRA          | DTS-MA            |
    | -------------- | ---------------- | ----------------- |
    | Lossy/lossless | Lossy            | Lossless          |
    | Data rate      | 1.5 - 6.0 Mbit/s | VBR - 24.5 Mbit/s |
    | Channels       | Up to 7.1 ch     | Up to 7.1 ch      |
    | Sampling Freq. | 96 kHz           | 192 kHz           |
    | Resolution     | -                | Up to 24-bit      |

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-hra.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus

<sub>Dolby Digital Plus = DD+ = DDPlus</sub>

??? question "DD+ - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital_Plus){:target="_blank" rel="noopener noreferrer"}

    Dolby Digital Plus, also known as Enhanced AC-3 (and commonly abbreviated as DD+ or E-AC-3, or EC-3) is a digital audio compression scheme developed by Dolby Labs for transport and storage of multi-channel digital audio. It is a successor to Dolby Digital (AC-3).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

??? question "DTS-ES - [Click to show/hide]"

    DTS-ES (DTS Extended Surround) includes two variants, DTS-ES Discrete 6.1, and DTS-ES Matrix 5.1, depending on how the sound was originally mastered and stored.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

<sub>DTS = Basic DTS</sub>

??? question "DTS - [Click to show/hide]"
    Description placeholder

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### AAC

??? question "AAC - [Click to show/hide]"

    Advanced Audio Coding

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
    Advanced Audio Coding (AAC) is an audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves higher sound quality than MP3 at the same bit rate.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/aac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DD

<sub>(Basic) Dolby Digital = DD</sub>

??? question "DD - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital){:target="_blank" rel="noopener noreferrer"}

    Dolby Digital, also known as Dolby AC-3, the audio compression is lossy.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MP3

??? question "MP3 - [Click to show/hide]"
    Description placeholder

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Opus

??? question "Opus - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}

    Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Audio Channels

------

### 1.0 Mono

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stereo

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3.0 Sound

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4.0 Sound

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 5.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 6.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 7.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 9.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/91-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HDR Formats

------

### DV HDR10Plus

<sub>Dolby Vision = DoVi = DV</sub>

??? question "DV HDR10 - [Click to show/hide]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV HDR10

<sub>Dolby Vision = DoVi = DV</sub>

??? question "DV HDR10 - [Click to show/hide]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV

<sub>Dolby Vision = DoVi = DV</sub>

??? question "DV - [Click to show/hide]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV HLG

<sub>Dolby Vision = DoVi = DV</sub>

??? question "DV HLG - [Click to show/hide]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV SDR

<sub>Dolby Vision = DoVi = DV</sub>

??? question "DV SDR - [Click to show/hide]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10Plus

<sub>HDR10Plus = HDR10+</sub>

??? question "HDR10+ - [Click to show/hide]"

    **HDR10+ enhances upon a pre-existing HDR10 base layer allowing backwards compatibility with HDR10 devices. It adds dynamic metadata for the devices that support it.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    HDR10+, also known as HDR10 Plus, is an HDR video format, announced on 20 April 2017. It is the same as HDR10 but with the addition of a system of dynamic metadata developed by Samsung. It is free to use for content creators and has a maximum $10,000 annual license for some manufacturers. It has been positioned as an alternative to Dolby Vision without the same expenses.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10

<sub>HDR10</sub>

??? question "HDR10 - [Click to show/hide]"

    **HDR10 is the most basic HDR format used in consumer media and is supported by all HDR-supported devices. It adds static metadata upon the PQ10 format.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    HDR10 Media Profile, more commonly known as HDR10, is an open HDR standard announced on 27 August 2015 by the Consumer Technology Association. It is the most widespread of the HDR formats. It is not backward compatible with SDR displays. It is technically limited to a maximum of 10,000 nits peak brightness; however, HDR10 content is commonly mastered with a peak brightness between 1000 and 4000 nits.

    HDR10 lacks dynamic metadata. On HDR10 displays that have lower color volume than the HDR10 content (e.g. lower peak brightness capability), the HDR10 metadata provides information to help the display adjust to the video. The metadata, however, is static and constant with respect to each individual video and doesn't inform the display exactly how the content should be adjusted. The interaction between display capabilities, video metadata, and the ultimate output (i.e. the presentation of the video) is mediated by the display, with the result that the original producer's intent may not be preserved.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR

<sub>HDR</sub>

??? question "HDR - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    High-dynamic-range video (HDR video) is video having a dynamic range greater than that of standard-dynamic-range video (SDR video).HDR video involves capture, production, content/encoding, and display. HDR capture and displays are capable of brighter whites and deeper blacks. To accommodate this, HDR encoding standards allow for a higher maximum luminance and use at least a 10-bit dynamic range (color depth, compared to 8-bit for non-professional and 10-bit for professional SDR video) in order to maintain precision across this extended range.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (undefined)

??? question "HDR (undefined) - [Click to show/hide]"

    Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.

    For now it's only FraMeSToR/HQMUX that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PQ

<sub>PQ = PQ10</sub>

??? question "PQ - [Click to show/hide]"

    **PQ10 is the most basic HDR format which all other common formats are based upon. It is the barebones SMPTE 2084 specification and has no metadata.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    PQ10, sometimes simply referred as the PQ format, is an HDR format that can be used for both video and still images. It is the same as the HDR10 format without any metadata. It uses the PQ transfer function, Rec. 2020 color primaries and a bit depth of 10-bits. It is not backward compatible with SDR.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HLG

<sub>HLG = HLG10</sub>

??? question "HLG - [Click to show/hide]"

    **HLG does not use dynamic metadata and is backwards compatible with SDR devices. It is mostly used in broadcasting.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    HLG10, commonly simply referred as the HLG format, is an HDR format that can be used for both video and still images. It uses the HLG transfer function, Rec. 2020 color primaries, and a bit depth of 10 bits. The format is backwards compatible with SDR UHDTV but not with older SDR displays that do not implement the Rec. 2020 color standards. It doesn't use metadata and is royalty free.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Series Versions

------

### Hybrid

??? question "Hybrid - [Click to show/hide]"

    A hybrid release means any combination of sources (video + audio) and not a direct encode of a single source. Generally you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hybrid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remaster

??? question "Remaster - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}

    For the software term, see Software remastering.
    Remaster (also digital remastering and digitally remastered) refers to changing the quality of the sound or of the image, or both, of previously created recordings, either audiophonic, cinematic, or videographic.

??? example "JSON - [Click to show/hide]"

    ```json
     [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Unwanted

------

### BR-DISK

??? question "BR-DISK - [Click to show/hide]"

    This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-10000`.

    !!! note

        Depending on your renaming scheme it could happen that Sonarr will match renamed files after they are downloaded and imported as `BR-DISK`,
        This is a cosmetic annoyance until I come up with another way to solve this,
        being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
        Several reasons why this is happening:

        - Blame the often wrongly used naming of x265 encodes.
        - Sonarr v3/v4 uses dynamic custom formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ

<sub>Low Quality Releases = LQ</sub>

??? question "LQ - [Click to show/hide]"

    A collection of known Low Quality groups that are often banned from the the top trackers because their lack of quality.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ (Release Title)

<sub>Low Quality Releases = LQ</sub>

??? question "LQ (Release Title)- [Click to show/hide]"

    A collection of terms seen in the titles of Low Quality releases that are not captured by using a release group name.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq-release-title.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (HD)

<sub>720/1080p no x265 = x265 (720/1080p) = x265 (HD)</sub>

??? question "x265 (HD) - [Click to show/hide]"

    This blocks/ignores 720/1080p(HD) releases that are encoded in x265

    In your quality profile use the following score for this Custom Format: `{{ sonarr['cf']['x265-hd']['trash_scores']['default'] }}`

    !!! failure ""
        --8<-- "includes/docker/x265.md"

            !!! Danger "Don't use this together with [{{ sonarr['cf']['x265-no-hdrdv']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-no-hdrdv), Only ever include one of them :warning:"

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-hd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Extras

??? question "Extras - [Click to show/hide]"

    This blocks/ignores Extra's

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/extras.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc

------

### Repack/Proper

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack v2

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack v3

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x264

??? question "x264 - [Click to show/hide]"

    x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x264.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265

??? question "x265 - [Click to show/hide]"

    x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    !!! failure ""
        Please don't forget to read the following [Microsized & Wrong Source](#microsized-wrong-source)

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MPEG2

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Optional

------

### Bad Dual Groups

??? question "Bad dual groups - [Click to show/hide]"
    These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bad-dual-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV (WEBDL)

<sub>Dolby Vision = DoVi = DV</sub>

??? question "DV (WEBDL) - [Click to show/hide]"
    This is a special Custom Format that block WEBDLs **with** Dolby Vision but **without** HDR10 fallback.

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-10000`.

    This Custom Format works together with the normal [DV](#dv) Custom Format that you can use to prefer Dolby Vision.

    Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors (typically a green hue) if you want to play it on a not Dolby Vision compatible setup.

    Remuxes and Bluray have a fallback to HDR10.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10Plus Boost

??? question "HDR10+ Boost - [Click to show/hide]"

    Optional (use this one only if you have a (Samsung) TV that supports HDR10+ and you don't have a Setup that supports DV or you prefer HDR10+.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### No-RlsGroup

??? question "No-RlsGroup - [Click to show/hide]"

    Some indexers strip out the release group which could result in LQ groups getting a higher score.
    For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match

    !!! warning

        If you don't use decent filenames (like not adding release groups) don't add this Custom Format, except if you want to upgrade them.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Obfuscated

??? question "Obfuscated - [Click to show/hide]"

    Optional (use these only if you dislike renamed releases)

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Retags

??? question "Retags - [Click to show/hide]"

    Optional (use these only if you dislike retagged releases)

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/retags.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Scene

??? question "Scene - [Click to show/hide]"

    This Custom Format will try to recognize so called Scene releases, depending on your preferences you can give it a negative score `-10000` or a positive score or just don't add it all.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Season Pack

??? question "Season Pack - [Click to show/hide]"

    This Custom Format can be used depending if you prefer or not prefer a season pack

    - Give it a score of `10` if you prefer a season pack.
    - Give it a score of `-10000` if you don't prefer a season pack.
    - `/\bS\d+\b(?!E\d+\b)/i` season packs are preferred: however, given the folder name is ignored the error/warning/issue occurs as the file names would not be a season pack of course.
    - keep in mind this is the only way to prefer season packs if you have preferred words due to the long standing bug => Preferred Words overrule season pack preference [Sonarr/Sonarr#3562](https://github.com/Sonarr/Sonarr/issues/3562){:target="_blank" rel="noopener noreferrer"}

    !!! danger "WARNING"
        - This Custom Format could result in a download loop :bangbang:
        - This will upgrade also your already downloaded single episodes :bangbang:

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/season-pack.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (no HDR/DV)

??? question "x265 (no HDR/DV) - [Click to show/hide]"

    This blocks/ignores 720/1080p (HD) releases that are encoded in x265.

    **But it will allow x265 releases if they have HDR and/or DV**

    *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

    In your quality profile use the following score for this Custom Format: `{{ sonarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}`

    !!! Danger "Don't use this together with [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-no-hdrdv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### AV1

??? question "AV1 - [Click to show/hide]"

    - This is a new codec and you need modern devices that support it.
    - We also had reports of playback/transcoding issues.
    - No main group is actually using it (yet).
    - It's better to ignore this new codec to prevent compatibility issues.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/av1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VP9

??? question "VP9 - [Click to show/hide]"

    - This is a new codec and you need modern devices that support it.
    - We also had reports of playback/transcoding issues.
    - No main group is actually using it (yet).
    - It's better to ignore this new codec to prevent compatibility issues.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vp9.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Internal

??? question "Internal - [Click to show/hide]"

    - For those that prefer scene releases may want to boost internals as they generally have higher settings that may not conform to ruleset.
    - In some rare cases P2P use also INTERNAL.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/internal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SDR

??? question "SDR - [Click to show/hide]"

    - This will help to prevent to grab UHD/4k releases without HDR Formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SDR (no WEBDL)

??? question "SDR (no WEBDL) - [Click to show/hide]"

    - This will prevent grabbing UHD/4k Remux and Bluray encode releases without HDR Formats - i.e., SDR WEB releases will still be allowed. 4K SDR WEB releases can look better than the 1080p version, owing to improved bitrates.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sdr-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV (Disk)

??? question "DV (Disk) - [Click to show/hide]"

    - This will boost the score for Dolby Vision Releases using the original full quality Dolby Vision layer from the disc release to replace the old WEBDL HYBRID release.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HFR

??? question "HFR - [Click to show/hide]"

    - This will boost the score for HFR releases. HFR stands for High Frame Rate and refers to a video format that uses a higher number of frames per second than traditional video, resulting in smoother and more detailed motion.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HQ Source Groups

------

### Remux Tier 01

??? question "Remux Tier 01 - [Click to show/hide]"

    - Groups doing remuxes with multiple sources(discs) mixing what's best.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remux Tier 02

??? question "Remux Tier 02 - [Click to show/hide]"

    - Groups that only use one source.(So called one disc wonders.)
    - Groups that use an automated way.
    - Groups that don't check their stuff.
    - Groups that haven't released much. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

### HD Bluray Tier 01

??? question "HD Bluray Tier 01 - [Click to show/hide]"

    - Groups that created encodes from the remuxes without micro-sizing them.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HD Bluray Tier 02

??? question "HD Bluray Tier 02 - [Click to show/hide]"

    - Groups that created encodes from the remuxes without micro-sizing them.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

### WEB Tier 01

??? question "WEB Tier 01 - [Click to show/hide]"

    - Groups that are on a certain list and active
    - Groups that are on a certain list and did a minimum of x releases
    - Groups that are not on the list but have a few releases on their name, but won't be trumped by a season pack on the top tier trackers
    - Hybrid releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 02

??? question "WEB Tier 02 - [Click to show/hide]"

    - Groups that are on a certain list and are less or not active anymore
    - Groups that only did a few releases
    - Groups that are not on the list but have a few releases on their name

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 03

??? question "WEB Tier 03 - [Click to show/hide]"

    - Groups that are on a certain list and are less or not active anymore
    - Groups that hardly done any releases
    - Groups that are not on the list but have a few releases on their name

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Scene

??? question "WEB Scene - [Click to show/hide]"

    One of the few scene groups that released quality releases.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Streaming Services

------

### AMZN

<sub>Amazon</sub>

??? question "Amazon - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Amazon_Prime_Video){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/amzn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATVP

<sub>Apple TV+</sub>

??? question "Apple TV+ - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Apple_TV%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atvp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DCU

<sub>DC Universe</sub>

??? question "DC Universe - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DC_Universe_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dcu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DSNP

<sub>Disney+</sub>

??? question "Disney+ - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Disney%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dsnp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HMAX

<sub>HBO Max</sub>

??? question "HBO Max - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/HBO_Max){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hmax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HBO

<sub>HBO</sub>

??? question "HBO - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/HBO){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hbo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Max

<sub>Max</sub>

??? question "Max - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Max_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/max.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Hulu

<sub>Hulu</sub>

??? question "Hulu - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Hulu){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IP

<sub>BBC iPlayer</sub>

??? question "BBC iPlayer - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/BBC_iPlayer){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ip.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### NLZ

<sub>NLZiet</sub>

??? question "NLZiet - [Click to show/hide]"

    NLZIET is the online service of Dutch broadcasters that provides non-stop tv, commercial-free. The streaming service brings the best of all channels straight to your preferred device and lets you see your favorite tv content in high quality on all available platforms; anytime and anywhere.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nlz.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### NF

<sub>Netflix</sub>

??? question "Netflix - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Netflix){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PMTP

<sub>Paramount+</sub>

??? question "Paramount+ - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Paramount%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pmtp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCOK

<sub>Peacock TV</sub>

??? question "Peacock TV - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Peacock_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcok.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Qibi

<sub>Quibi</sub>

??? question "Quibi - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Quibi){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/qibi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SHO

<sub>SHOWTIME</sub>

??? question "SHOWTIME - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Showtime_(TV_network)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sho.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VDL

<sub>Videoland</sub>

??? question "Videoland - [Click to show/hide]"

    Videoland is a Dutch OTT online service provider owned by RTL Nederland. Originally it was a retail chain of video rental stores. Its main competitor is Netflix.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### STAN

<sub>Stan</sub>

??? question "STAN - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Stan_(service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/stan.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### RED

<sub>RED = Youtube Red = Youtube Premium</sub>

??? question "Youtube Red - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/YouTube_Premium){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/red.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IT

<sub>iT = iTunes</sub>

??? question "iTunes - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/ITunes){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/it.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### CANALPlus

<sub>CANALPlus = CANAL+/MyCANAL</sub>

??? question "Canal+ - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Canal%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-canalplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SALTO

<sub>SALTO = SⱯLTO</sub>

??? question "SⱯLTO - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Salto_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-salto.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### RTBF

<sub>RTBF = Radio-télévision belge de la Communauté française (Radio Télévision Belge Francophone)</sub>

??? question "RTBF - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/RTBF){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-rtbf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### CC

<sub>CC = Comedy Central</sub>

??? question "CC - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Comedy_Central){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Crav

<sub>Crave</sub>

??? question "CRAVE - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Crave_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/crav.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### OViD

<sub>OViD</sub>

??? question "OViD - [Click to show/hide]"

    [OViD Website](https://search.ovid.tv/other/about){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ovid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FOD

<sub>FOD</sub>

??? question "FOD - [Click to show/hide]"

    - Fuji Television On Demand
    - [From Wikipedia, the free encyclopedia](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%B8%E3%83%86%E3%83%AC%E3%83%93%E3%82%AA%E3%83%B3%E3%83%87%E3%83%9E%E3%83%B3%E3%83%89){:target="_blank" rel="noopener noreferrer"}
    - [FOD Website](https://fod-sp.fujitv.co.jp){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fod.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TVer

<sub>TVer</sub>

??? question "TVer - [Click to show/hide]"

    - [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/TVer_(streaming_service)){:target="_blank" rel="noopener noreferrer"}
    - [TVer Website](https://tver.jp){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/tver.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### U-NEXT

<sub>U-NEXT</sub>

??? question "U-NEXT - [Click to show/hide]"

    - [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/U-Next){:target="_blank" rel="noopener noreferrer"}
    - [U-NEXT Website](https://video.unext.jp){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/u-next.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ALL4

<sub>ALL4</sub>

??? question "ALL4 - [Click to show/hide]"

    - [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Channel_4_(VoD_service)){:target="_blank" rel="noopener noreferrer"}
    - ALL4 is a previous name for the UK's Channel4 VOD service. Releases are usually identified with either 'ALL4' or '4OD', not 'Channel4'.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/all4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4OD

<sub>4OD</sub>

??? question "4OD - [Click to show/hide]"

    - [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Channel_4_(VoD_service)){:target="_blank" rel="noopener noreferrer"}
    - 4OD is a previous name for the UK's Channel4 VOD service. Releases are usually identified with either 'ALL4' or '4OD', not 'Channel4'.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/4od.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### UHD Streaming Boost

??? question "UHD Streaming Boost - [Click to show/hide]"

    Some streaming services have UHD releases that are generally better than their HD counterparts. The UHD Streaming Boost custom format increases those streaming services' scores appropriately for UHD releases. Use this in conjunction with the regular streaming service custom formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uhd-streaming-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### UHD Streaming Cut

??? question "UHD Streaming Cut - [Click to show/hide]"

    Some streaming services have UHD releases that are generally worse than their HD counterparts. The UHD Streaming Cut custom format decreases those streaming services' scores appropriately for UHD releases. Use this in conjunction with the regular streaming service custom formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uhd-streaming-cut.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Anime

------

### Anime BD Tier 01 (Top SeaDex Muxers)

??? question "Anime BD Tier 01 (Top SeaDex Muxers) - [Click to show/hide]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-01-top-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 02 (SeaDex Muxers)

??? question "Anime BD Tier 02 (SeaDex Muxers) - [Click to show/hide]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-02-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 03 (SeaDex Muxers)

??? question "Anime BD Tier 03 (SeaDex Muxers) - [Click to show/hide]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-03-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 04 (SeaDex Muxers)

??? question "Anime BD Tier 04 (SeaDex Muxers) - [Click to show/hide]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-04-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 05 (Remuxes)

??? question "Anime BD Tier 05 (Remuxes) - [Click to show/hide]"
    Groups that are consistent and do Remuxes

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-05-remuxes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 06 (FanSubs)

??? question "Anime BD Tier 06 (FanSubs) - [Click to show/hide]"
    FanSub groups that are consistent

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 07 (P2P/Scene)

??? question "Anime BD Tier 07 (P2P/Scene) - [Click to show/hide]"
    Known P2P and Scene Anime groups

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-07-p2pscene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 08 (Mini Encodes)

??? question "Anime BD Tier 08 (Mini Encodes) - [Click to show/hide]"
    Know groups that do mini encodes

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-08-mini-encodes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 01 (Muxers)

??? question "Anime Web Tier 01 (Muxers) - [Click to show/hide]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-01-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 02 (Top FanSubs)

??? question "Anime Web Tier 02 (Top FanSubs) - [Click to show/hide]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-02-top-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 03 (Official Subs)

??? question "Anime Web Tier 03 (Official Subs) - [Click to show/hide]"
    Official sub groups that tend to be more consistent and release fast

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-03-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 04 (Official Subs)

??? question "Anime Web Tier 04 (Official Subs) - [Click to show/hide]"
    Official sub groups

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-04-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 05 (FanSubs)

??? question "Anime Web Tier 05 (FanSubs) - [Click to show/hide]"
    FanSub groups that are consistent

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-05-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 06 (FanSubs)

??? question "Anime Web Tier 06 (FanSubs) - [Click to show/hide]"
    FanSub groups that are consistent

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Raws

??? question "Anime Raws - [Click to show/hide]"
    A collection of know groups that release raws

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-raws.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime LQ Groups

??? question "Anime LQ Groups - [Click to show/hide]"
    A collection of known Low Quality groups.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-lq-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Uncensored

??? question "Uncensored - [Click to show/hide]"
    This CF covers releases that are uncensored

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uncensored.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v0

??? question "v0 - [Click to show/hide]"
    CF to cover releases named with v0 which we don't want

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v0.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v1

??? question "v1 - [Click to show/hide]"
    CF to cover v1 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v2

??? question "v2 - [Click to show/hide]"
    CF to cover v2 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v3

??? question "v3 - [Click to show/hide]"
    CF to cover v3 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v4

??? question "v4 - [Click to show/hide]"
    CF to cover v4 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### B-Global

??? question "B-Global - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/Bilibili){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bglobal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Bilibili

??? question "Bilibili - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/Bilibili){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bilibili.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### cr

<sub>Crunchyroll</sub>

??? question "Crunchyroll - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/Crunchyroll){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### funi

<sub>Funimation</sub>

??? question "Funimation - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/Funimation){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/funi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HIDIVE

??? question "HIDIVE - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/HIDIVE){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hidive.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VRV

??? question "VRV - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/VRV_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vrv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ABEMA

??? question "ABMEA - [Click to show/hide]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/Abema){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/abema.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ADN

<sub>ADN = Animation Digital Network</sub>

??? question "ADN - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://fr.wikipedia.org/wiki/Animation_Digital_Network){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-adn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WKN

<sub>WKN = Wakanim</sub>

??? question "WKN - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://fr.wikipedia.org/wiki/Wakanim){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-wkn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 10bit

??? question "10bit - [Click to show/hide]"
    This CF covers releases that are 10bit

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Dual Audio

??? question "Anime Dual Audio - [Click to show/hide]"
    This CF covers releases that have Dual Audio

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dubs Only

??? question "Dubs Only - [Click to show/hide]"
    This CF covers releases that only have Dubs

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dubs-only.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## French Audio Version

------

### Multi-French

??? question "Multi-French - [Click to show/hide]"

    Recognize movies that include the original and the french audio. Work only after import as it need the result from FFprobe to get which audio are present. Will rename the release to keep the recognition of 'Multi' by the [Multi-Audio](#multi-audio) custom format.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi-Audio

??? question "Multi-Audio - [Click to show/hide]"

    A slightly modified [Multi](#multi) Custom Formats that recognize VF and VO inside the name.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### French Audio

??? question "French Audio - [Click to show/hide]"

    This will recognize every kind of French Audio.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFF

??? question "VFF - [Click to show/hide]"

    Full French version (dubbing done in France) and French version (normally equivalent to VFQ).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vff.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOF

??? question "VOF - [Click to show/hide]"

    Original French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vof.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFI

??? question "VFI - [Click to show/hide]"

    International French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VF2

??? question "VF2 - [Click to show/hide]"

    VF[1-9] or FR[1-9] indicates the number of dubs present (normally VF2 being VFF and VFQ).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vf2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFQ

??? question "VFQ - [Click to show/hide]"

    Canadian French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOQ

??? question "VOQ - [Click to show/hide]"

    Quebec Original Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-voq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VQ

??? question "VQ - [Click to show/hide]"

    Quebec Version (strong Quebec accent, ex: The Simpsons movie).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFB

??? question "VFB - [Click to show/hide]"

    Belgian French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfb.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOSTFR

??? question "VOSTFR - [Click to show/hide]"

    Indicates soundtrack in the original language, with French subtitles. It should be noted that SUBFRENCH is included inside this Custom Format. However, SUB often mean that the subtitle was embedded inside the picture (hardcoded). French releases tend to mix both, leading some VOSTFR being labelled as SUBFRENCH and SUBFRENCH as VOSTFR.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vostfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FanSUB

??? question "FanSUB - [Click to show/hide]"

    Action of subtitling a video for personal and non-professional purposes. The quality of FanSUBs can vary enormously (accuracy of translation, mistakes, etc.) and could lead to so called FastSUBs.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FastSUB

??? question "FastSUB - [Click to show/hide]"

    FanSUB, but made as quickly as possible, at the expense of quality.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fastsub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## French HQ Source Groups

------

### FR Remux Tier 01

??? question "Remux Tier 01 - [Click to show/hide]"

    - WIP
    - Groups doing remuxes with multiple sources (discs) mixing what's best.
    - Groups active doing remuxes from a single sources (discs).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR HD Bluray Tier 01

??? question "FR HD Bluray Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that created encodes from the remuxes without micro-sizing them.
    - Groups that source and add the best French audio track from the source to an English release from Tier 01 or 02.
    - Groups that have a minimum of great releases (best encode in it's class 1080p and lower).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Tier 01

??? question "FR WEB Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that get their releases directly from the source.
    - Groups that source and add the French audio track from the source to an English release from Tier 01 or 02.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Tier 02

??? question "FR WEB Tier 02 - [Click to show/hide]"

    - WIP
    - Groups that get their releases directly from the source but are not so active.
    - Groups that source and add the French audio track from the source to an English release.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Tier 03

??? question "FR WEB Tier 03 - [Click to show/hide]"

    - WIP
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime Tier 01

??? question "FR Anime Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that are know to be still active and doing only Anime
    - Groups which releases are at least comparable to SeaDex recommended.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime Tier 02

??? question "FR Anime Tier 02 - [Click to show/hide]"

    - WIP
    - Groups that are known to be still active and doing only Anime but with few releases per year.
    - Groups that are known to be still active and doing Anime and other type of release.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime Tier 03

??? question "FR Anime Tier 03 - [Click to show/hide]"

    - WIP
    - Groups with no or little activity that have at some point made an interesting release. Which is either the only one available (in VOSTFR/MULTi) or still top of its category.
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups doing only anime, that have retired (or no longer exist) and may not have the best quality by todays standards.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Anime FanSub

??? question "FR Anime FanSub - [Click to show/hide]"

    Known good groups that are doing only FanSub and in good quality.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Scene Groups

??? question "FR Scene Groups - [Click to show/hide]"

    Known French Scene groups.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR LQ

<sub>French Low Quality Releases = FR LQ</sub>

??? question "FR LQ - [Click to show/hide]"

    A collection of known French Low Quality groups that are often banned from the the top trackers because their lack of quality.

    !!! note

        - Ads/Watermarks = Groups that are know to put ads or watermark in their releases.
        - Bad/False releases = Groups that are known for lying on the quality, type or the name of their releases.
        - DeTAG/ReTAG = Detagging or stealing groups.
        - Other reasons = Banned Release Groups.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>
