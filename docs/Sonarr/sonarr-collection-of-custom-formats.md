# Collection of Custom Formats

Here I will try to list a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on Discord or that I created with help from others.
Special thanks to everyone that helped testing and creating these Custom Formats.

With Sonarr V4+, Custom Formats are much more advanced/powerful than with the release profiles, although this also means a Custom Format is much more complicated to setup.

I also made 3 guides related to this one.

- [How to import Custom Formats](/Sonarr/sonarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to import the Custom Formats.
- [How to upgrade Custom Formats](/Sonarr/sonarr-how-to-update-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to upgrade your existing Custom Formats.
- [How to setup Custom Formats](/Sonarr/sonarr-setup-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to make the most use of Custom Formats and show some personal examples that I'm using. You can use these to get an idea on how to setup your own.

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
| [TrueHD ATMOS](#truehd-atmos)         | [FLAC](#flac)             | [1.0 Mono](#10-mono)         | [DV HDR10](#dv-hdr10)             |
| [DTS X](#dts-x)                       | [PCM](#pcm)               | [2.0 Stereo](#20-stereo)     | [DV](#dv)                         |
| [ATMOS (undefined)](#atmos-undefined) | [DTS-HD HRA](#dts-hd-hra) | [3.0 Sound](#30-sound)       | [DV HLG](#dv-hlg)                 |
| [DD+ ATMOS](#ddplus-atmos)            | [AAC](#aac)               | [4.0 Sound](#40-sound)       | [DV SDR](#dv-sdr)                 |
| [TrueHD](#truehd)                     | [DD](#dd)                 | [5.1 Surround](#51-surround) | [HDR10+](#hdr10plus)              |
| [DTS-HD MA](#dts-hd-ma)               | [MP3](#mp3)               | [6.1 Surround](#61-surround) | [HDR10](#hdr10)                   |
| [DD+](#ddplus)                        | [Opus](#opus)             | [7.1 Surround](#71-surround) | [HDR](#hdr)                       |
| [DTS-ES](#dts-es)                     |                           | [9.1 Surround](#91-surround) | [HDR (undefined)](#hdr-undefined) |
| [DTS](#dts)                           |                           |                              | [PQ](#pq)                         |
|                                       |                           |                              | [HLG](#hlg)                       |

------

| Series Versions       | Unwanted                           | HQ Source Groups            | Streaming Services  |
| --------------------- | ---------------------------------- | --------------------------- | ------------------- |
| [Hybrid](#hybrid)     | [BR-DISK](#br-disk)                | [WEB Tier 01](#web-tier-01) | [Amazon](#amzn)     |
| [Remaster](#remaster) | [LQ](#lq)                          | [WEB Tier 02](#web-tier-02) | [Apple TV+](#atvp)  |
|                       | [DV (WEBDL)](#dv-webdl)            | [WEB Tier 03](#web-tier-03) | [DC Universe](#dcu) |
|                       | [x265 (HD)](#x265-hd)              | [WEB Scene](#web-scene)     | [Disney+](#dsnp)    |
|                       | [x265 (no HDR/DV)](#x265-no-hdrdv) |                             | [HBO Max](#hmax)    |
|                       |                                    |                             | [HBO](#hbo)         |
|                       |                                    |                             | [Hulu](#hulu)       |
|                       |                                    |                             | [Netflix](#nf)      |
|                       |                                    |                             | [Paramount+](#pmtp) |
|                       |                                    |                             | [Peacock TV](#pcok) |
|                       |                                    |                             | [Quibi](#qibi)      |
|                       |                                    |                             | [SHOWTIME](#sho)    |
|                       |                                    |                             | [YouTube Red](#red) |
|                       |                                    |                             | [iTunes](#it)       |

------

| Misc                           | Optional                            | &nbsp; | &nbsp; |
| ------------------------------ | ----------------------------------- | ------ | ------ |
| [Repack/Proper](#repackproper) | [Season Packs](#season-pack)        | &nbsp; | &nbsp; |
| [Repack v2](#repack-v2)        | [Scene](#scene)                     | &nbsp; | &nbsp; |
| [Repack v3](#repack-v3)        | [No-RlsGroup](#no-rlsgroup)         | &nbsp; | &nbsp; |
| [Multi](#multi)                | [Obfuscated](#obfuscated)           | &nbsp; | &nbsp; |
| [MPEG2](#mpeg2)                | [Retags](#retags)                   | &nbsp; | &nbsp; |
| [x264](#x264)                  | [Bad Dual Groups](#bad-dual-groups) | &nbsp; | &nbsp; |
| [x265](#x265)                  |                                     | &nbsp; | &nbsp; |
|                                |                                     | &nbsp; | &nbsp; |

------

| Anime                                                                       | Anime                                                                 | Anime       | Anime Optional                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------- | ------------------------------------- |
| [Anime BD Tier 01 (Top SeaDex Muxers)](#anime-bd-tier-01-top-seadex-muxers) | [Anime Web Tier 01 (Muxers)](#anime-web-tier-01-muxers)               | [v0](#v0)   | [Uncensored](#uncensored)             |
| [Anime BD Tier 02 (SeaDex Muxers)](#anime-bd-tier-02-seadex-muxers)         | [Anime Web Tier 02 (Top FanSubs)](#anime-web-tier-02-top-fansubs)     | [v1](#v1)   | [10bit](#10bit)                       |
| [Anime BD Tier 03 (SeaDex Muxers)](#anime-bd-tier-03-seadex-muxers)         | [Anime Web Tier 03 (SubsPlease)](#anime-web-tier-03-subsplease)       | [v2](#v2)   | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 04 (SeaDex Muxers)](#anime-bd-tier-04-seadex-muxers)         | [Anime Web Tier 04 (Official Subs)](#anime-web-tier-04-official-subs) | [v3](#v3)   | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 05 (Remuxes)](#anime-bd-tier-05-remuxes)                     | [Anime Web Tier 05 (FanSubs)](#anime-web-tier-05-fansubs)             | [v4](#v4)   |                                       |
| [Anime BD Tier 06 (FanSubs)](#anime-bd-tier-06-fansubs)                     | [Anime Web Tier 06 (FanSubs)](#anime-web-tier-06-fansubs)             | [VRV](#vrv) |                                       |
| [Anime BD Tier 07 (P2P/Scene)](#anime-bd-tier-07-p2pscene)                  | [Anime Raws](#anime-raws)                                             |             |                                       |
| [Anime BD Tier 08 (Mini Encodes)](#anime-bd-tier-08-mini-encodes)           | [Anime LQ Groups](#anime-lq-groups)                                   |             |                                       |                                      |

## Audio Advanced

------

### TrueHD ATMOS

??? faq "TrueHD ATMOS - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}

    Dolby Atmos is a surround sound technology developed by Dolby Laboratories. It expands on existing surround sound systems by adding height channels, allowing sounds to be interpreted as three-dimensional objects.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS X

??? faq "DTS X - [CLICK TO EXPAND]"

    DTS:X is an object-based audio codec, which aims to create a multi-dimensional sound that “moves around you like it would in real life”

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-x.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATMOS (undefined)

??? faq "ATMOS (undefined) - [CLICK TO EXPAND]"

    Handles cases where only Atmos is specified in title but not DD+ or TrueHD (Where it is not specified if it is Lossy or Lossless)

    !!! note
        Give this the same score as Lossy Atmos, and then on import, it will get changed to either lossy or lossless based on mediainfo.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus ATMOS

<sub>DDPlus = DD+</sub>

??? faq "DD+ ATMOS - [CLICK TO EXPAND]"

    Atmos via UHD Blu-ray will be lossless, or lossy via streaming services so in this case it will be lossy + Atmos

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TrueHD

??? faq "TrueHD - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}

    Dolby TrueHD is a lossless, multi-channel audio codec developed by Dolby Laboratories for home video, used principally in Blu-ray Disc and compatible hardware.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

??? faq "DTS-HD MA - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}

    DTS-HD Master Audio is a multi-channel, lossless audio codec developed by DTS as an extension of the lossy DTS Coherent Acoustics codec (DTS CA; usually itself referred to as just DTS). Rather than being an entirely new coding mechanism, DTS-HD MA encodes an audio master in lossy DTS first, then stores a concurrent stream of supplementary data representing whatever the DTS encoder discarded. This gives DTS-HD MA a lossy "core" able to be played back by devices that cannot decode the more complex lossless audio. DTS-HD MA's primary application is audio storage and playback for Blu-ray Disc media.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FLAC

??? faq "FLAC - [CLICK TO EXPAND]"

    FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

??? faq "PCM - [CLICK TO EXPAND]"

    PCM is the method of encoding typically used for uncompressed digital audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

??? faq "DTS-HD HRA - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-hra.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus

<sub>Dolby Digital Plus = DD+ = DDPlus</sub>

??? faq "DD+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital_Plus){:target="_blank" rel="noopener noreferrer"}

    Dolby Digital Plus, also known as Enhanced AC-3 (and commonly abbreviated as DD+ or E-AC-3, or EC-3) is a digital audio compression scheme developed by Dolby Labs for transport and storage of multi-channel digital audio. It is a successor to Dolby Digital (AC-3).

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

??? faq "DTS-ES - [CLICK TO EXPAND]"

    DTS-ES (DTS Extended Surround) includes two variants, DTS-ES Discrete 6.1, and DTS-ES Matrix 5.1, depending on how the sound was originally mastered and stored.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

<sub>DTS = Basic DTS</sub>

??? faq "DTS - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### AAC

??? faq "AAC - [CLICK TO EXPAND]"

    Advanced Audio Coding

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
    Advanced Audio Coding (AAC) is an audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves higher sound quality than MP3 at the same bit rate.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/aac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DD

<sub>(Basic) Dolby Digital = DD</sub>

??? faq "DD - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital){:target="_blank" rel="noopener noreferrer"}

    Dolby Digital, also known as Dolby AC-3, the audio compression is lossy.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MP3

??? faq "MP3 - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Opus

??? faq "Opus - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}

    Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Audio Channels

------

### 1.0 Mono

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stereo

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3.0 Sound

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4.0 Sound

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 5.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 6.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 7.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 9.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/91-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HDR Formats

------

### DV HDR10

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV HDR10 - [CLICK TO EXPAND]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV - [CLICK TO EXPAND]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV HLG

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV HLG - [CLICK TO EXPAND]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV SDR

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV SDR - [CLICK TO EXPAND]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10Plus

<sub>HDR10Plus = HDR10+</sub>

??? faq "HDR10+ - [CLICK TO EXPAND]"

    **HDR10+ enhances upon a pre-existing HDR10 base layer allowing backwards compatibility with HDR10 devices. It adds dynamic metadata for the devices that support it.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    HDR10+, also known as HDR10 Plus, is an HDR video format, announced on 20 April 2017. It is the same as HDR10 but with the addition of a system of dynamic metadata developed by Samsung. It is free to use for content creators and has a maximum $10,000 annual license for some manufacturers. It has been positioned as an alternative to Dolby Vision without the same expenses.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10

<sub>HDR10</sub>

??? faq "HDR10 - [CLICK TO EXPAND]"

    **HDR10 is the most basic HDR format used in consumer media and is supported by all HDR-supported devices. It adds static metadata upon the PQ10 format.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    HDR10 Media Profile, more commonly known as HDR10, is an open HDR standard announced on 27 August 2015 by the Consumer Technology Association. It is the most widespread of the HDR formats. It is not backward compatible with SDR displays. It is technically limited to a maximum of 10,000 nits peak brightness; however, HDR10 content is commonly mastered with a peak brightness between 1000 and 4000 nits.

    HDR10 lacks dynamic metadata. On HDR10 displays that have lower color volume than the HDR10 content (e.g. lower peak brightness capability), the HDR10 metadata provides information to help the display adjust to the video. The metadata, however, is static and constant with respect to each individual video and doesn't inform the display exactly how the content should be adjusted. The interaction between display capabilities, video metadata, and the ultimate output (i.e. the presentation of the video) is mediated by the display, with the result that the original producer's intent may not be preserved.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR

<sub>HDR</sub>

??? faq "HDR - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    High-dynamic-range video (HDR video) is video having a dynamic range greater than that of standard-dynamic-range video (SDR video).HDR video involves capture, production, content/encoding, and display. HDR capture and displays are capable of brighter whites and deeper blacks. To accommodate this, HDR encoding standards allow for a higher maximum luminance and use at least a 10-bit dynamic range (color depth, compared to 8-bit for non-professional and 10-bit for professional SDR video) in order to maintain precision across this extended range.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (undefined)

??? faq "HDR (undefined) - [CLICK TO EXPAND]"

    Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.

    For now it's only FraMeSToR/HQMUX that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PQ

<sub>PQ = PQ10</sub>

??? faq "PQ - [CLICK TO EXPAND]"

    **PQ10 is the most basic HDR format which all other common formats are based upon. It is the barebones SMPTE 2084 specification and has no metadata.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    PQ10, sometimes simply referred as the PQ format, is an HDR format that can be used for both video and still images. It is the same as the HDR10 format without any metadata. It uses the PQ transfer function, Rec. 2020 color primaries and a bit depth of 10-bits. It is not backward compatible with SDR.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HLG

<sub>HLG = HLG10</sub>

??? faq "HLG - [CLICK TO EXPAND]"

    **HLG does not use dynamic metadata and is backwards compatible with SDR devices. It is mostly used in broadcasting.**

    [From Wikipedia, the free encyclopedia](https://en.m.wikipedia.org/wiki/High-dynamic-range_video){:target="_blank" rel="noopener noreferrer"}

    HLG10, commonly simply referred as the HLG format, is an HDR format that can be used for both video and still images. It uses the HLG transfer function, Rec. 2020 color primaries, and a bit depth of 10 bits. The format is backwards compatible with SDR UHDTV but not with older SDR displays that do not implement the Rec. 2020 color standards. It doesn't use metadata and is royalty free.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Series Versions

------

### Hybrid

??? faq "Hybrid - [CLICK TO EXPAND]"

    A hybrid release means any combination of sources (video + audio) and not a direct encode of a single source. Generally you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hybrid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remaster

??? faq "Remaster - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}

    For the software term, see Software remastering.
    Remaster (also digital remastering and digitally remastered) refers to changing the quality of the sound or of the image, or both, of previously created recordings, either audiophonic, cinematic, or videographic.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
     [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Unwanted

------

### BR-DISK

??? faq "BR-DISK - [CLICK TO EXPAND]"

    This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-10000`

    !!! note

        Depending on your renaming scheme it could happen that Sonarr will match renamed files after they are downloaded and imported as `BR-DISK`,
        This is a cosmetic annoyance until I come up with another way to solve this,
        being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
        Several reasons why this is happening:

        - Blame the often wrongly used naming of x265 encodes.
        - Sonarr v3/v4 uses dynamic custom formats.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ

<sub>Low Quality Releases = LQ</sub>

??? faq "LQ - [CLICK TO EXPAND]"

    A collection of known Low Quality groups that are often banned from the the top trackers because their lack of quality.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (HD)

<sub>720/1080p no x265 = x265 (720/1080p) = x265 (HD)</sub>

??? faq "x265 (HD) - [CLICK TO EXPAND]"

    This blocks/ignores 720/1080p(HD) releases that are encoded in x265

    In your quality profile use the following score for this Custom Format: `{{ sonarr['cf']['x265-hd']['trash_score'] }}`

    !!! fail ""
        --8<-- "includes/docker/x265.md"

            !!! Danger "Don't use this together with [{{ sonarr['cf']['x265-no-hdrdv']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-no-hdrdv), Only ever include one of them :warning:"

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-hd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (no HDR/DV)

??? faq "x265 (no HDR/DV) - [CLICK TO EXPAND]"

    This blocks/ignores 720/1080p (HD) releases that are encoded in x265.

    **But it will allow x265 releases if they have HDR and/or DV**

    *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

    In your quality profile use the following score for this Custom Format: `{{ sonarr['cf']['x265-no-hdrdv']['trash_score'] }}`

    !!! Danger "Don't use this together with [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-no-hdrdv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV (WEBDL)

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV (WEBDL) - [CLICK TO EXPAND]"
    This is a special Custom Format that block WEBDLs **with** Dolby Vision but **without** HDR10 fallback.

    This Custom Format works together with the normal [DV](#dv) Custom Format that you can use to prefer Dolby Vision.

    Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

    Remuxes and Bluray have a fallback to HDR10.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc

------

### Repack/Proper

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack v2

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack v3

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x264

??? faq "x264 - [CLICK TO EXPAND]"

    x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x264.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265

??? faq "x265 - [CLICK TO EXPAND]"

    x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    !!! fail ""
        Please don't forget to read the following [Microsized & Wrong Source](#microsized-wrong-source)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MPEG2

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Optional

------

### Season Pack

??? faq "Season Pack - [CLICK TO EXPAND]"

    This Custom Format can be used depending if you prefer or not prefer a season pack

    - Give it a score of `10` if you prefer a season pack.
    - Give it a score of `-10000` if you don't prefer a season pack.
    - `/\bS\d+\b(?!E\d+\b)/i` season packs are preferred: however, given the folder name is ignored the error/warning/issue occurs as the file names would not be a season pack of course.
    - keep in mind this is the only way to prefer season packs if you have preferred words due to the long standing bug => Preferred Words overrule season pack preference [Sonarr/Sonarr#3562](https://github.com/Sonarr/Sonarr/issues/3562){:target="_blank" rel="noopener noreferrer"}

    !!! danger "WARNING"
        - This Custom Format could result in a download loop :bangbang:
        - This will upgrade also your already downloaded single episodes :bangbang:

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/season-pack.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Scene

??? faq "Scene - [CLICK TO EXPAND]"

    This Custom Format will try to recognize so called Scene releases, depending on your preferences you can give it a negative score `-10000` or a positive score or just don't add it all.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### No-RlsGroup

??? faq "No-RlsGroup - [CLICK TO EXPAND]"

    Some indexers strip out the release group which could result in LQ groups getting a higher score.
    For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match

    !!! warning

        If you don't use decent filenames (like not adding release groups) don't add this Custom Format, except if you want to upgrade them.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Obfuscated

??? faq "Obfuscated - [CLICK TO EXPAND]"

    Optional (use these only if you dislike renamed releases)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Retags

??? faq "Retags - [CLICK TO EXPAND]"

    Optional (use these only if you dislike retagged releases)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/retags.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Bad Dual Groups

??? faq "Bad dual groups - [CLICK TO EXPAND]"
    These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bad-dual-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HQ Source Groups

------

### WEB Tier 01

??? faq "WEB Tier 01 - [CLICK TO EXPAND]"

    - Groups that are on a certain list and active
    - Groups that are on a certain list and did a minimum of x releases
    - Groups that are not on the list but have a few releases on their name, but won't be trumped by a season pack on the top tier trackers
    - Hybrid releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 02

??? faq "WEB Tier 02 - [CLICK TO EXPAND]"

    - Groups that are on a certain list and are less or not active anymore
    - Groups that only did a few releases
    - Groups that are not on the list but have a few releases on their name

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 03

??? faq "WEB Tier 03 - [CLICK TO EXPAND]"

    - Groups that are on a certain list and are less or not active anymore
    - Groups that hardly done any releases
    - Groups that are not on the list but have a few releases on their name

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Scene

??? faq "WEB Scene - [CLICK TO EXPAND]"

    One of the few scene groups that released quality releases.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Streaming Services

------

### AMZN

<sub>Amazon</sub>

??? faq "Amazon - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Amazon_Prime_Video){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/amzn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATVP

<sub>Apple TV+</sub>

??? faq "Apple TV+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Apple_TV%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atvp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DCU

<sub>DC Universe</sub>

??? faq "DC Universe - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DC_Universe_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dcu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DSNP

<sub>Disney+</sub>

??? faq "Disney+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Disney%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dsnp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HMAX

<sub>HBO Max</sub>

??? faq "HBO Max - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/HBO_Max){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hmax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HBO

<sub>HBO</sub>

??? faq "HBO - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/HBO){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hbo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Hulu

<sub>Hulu</sub>

??? faq "Hulu - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Hulu){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### NF

<sub>Netflix</sub>

??? faq "Netflix - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Netflix){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PMTP

<sub>Paramount+</sub>

??? faq "Paramount+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Paramount%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pmtp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCOK

<sub>Peacock TV</sub>

??? faq "Peacock TV - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Peacock_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcok.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Qibi

<sub>Quibi</sub>

??? faq "Quibi - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Quibi){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/qibi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SHO

<sub>SHOWTIME</sub>

??? faq "SHOWTIME - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Showtime_(TV_network)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sho.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### RED

<sub>RED = Youtube Red = Youtube Premium</sub>

??? faq "Youtube Red - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/YouTube_Premium){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/red.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IT

<sub>iT = iTunes</sub>

??? faq "iTunes - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/ITunes){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/it.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Anime

------

### Anime BD Tier 01 (Top SeaDex Muxers)

??? faq "Anime BD Tier 01 (Top SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-01-top-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 02 (SeaDex Muxers)

??? faq "Anime BD Tier 02 (SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-02-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 03 (SeaDex Muxers)

??? faq "Anime BD Tier 03 (SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-03-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 04 (SeaDex Muxers)

??? faq "Anime BD Tier 04 (SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-04-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 05 (Remuxes)

??? faq "Anime BD Tier 05 (Remuxes) - [CLICK TO EXPAND]"
    Groups that are consistent and do Remuxes

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-05-remuxes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 06 (FanSubs)

??? faq "Anime BD Tier 06 (FanSubs) - [CLICK TO EXPAND]"
    FanSub groups that are consistent

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 07 (P2P/Scene)

??? faq "Anime BD Tier 07 (P2P/Scene) - [CLICK TO EXPAND]"
    Known P2P and Scene Anime groups

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-07-p2pscene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 08 (Mini Encodes)

??? faq "Anime BD Tier 08 (Mini Encodes) - [CLICK TO EXPAND]"
    Know groups that do mini encodes

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-08-mini-encodes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 01 (Muxers)

??? faq "Anime Web Tier 01 (Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-01-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 02 (Top FanSubs)

??? faq "Anime Web Tier 02 (Top FanSubs) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-02-top-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 03 (SubsPlease)

??? faq "Anime Web Tier 03 (SubsPlease) - [CLICK TO EXPAND]"
    SubsPlease group. They are official subs but tend to be more consistent and release fast

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-03-subsplease.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 04 (Official Subs)

??? faq "Anime Web Tier 04 (Official Subs) - [CLICK TO EXPAND]"
    Official sub groups

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-04-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 05 (FanSubs)

??? faq "Anime Web Tier 05 (FanSubs) - [CLICK TO EXPAND]"
    FanSub groups that are consistent

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-05-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 06 (FanSubs)

??? faq "Anime Web Tier 06 (FanSubs) - [CLICK TO EXPAND]"
    FanSub groups that are consistent

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Raws

??? faq "Anime Raws - [CLICK TO EXPAND]"
    A collection of know groups that release raws

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-raws.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime LQ Groups

??? faq "Anime LQ Groups - [CLICK TO EXPAND]"
    A collection of known Low Quality groups.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-lq-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Uncensored

??? faq "Uncensored - [CLICK TO EXPAND]"
    This CF covers releases that are uncensored

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uncensored.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v0

??? faq "v0 - [CLICK TO EXPAND]"
    CF to cover releases named with v0 which we don't want

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v0.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v1

??? faq "v1 - [CLICK TO EXPAND]"
    CF to cover v1 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v2

??? faq "v2 - [CLICK TO EXPAND]"
    CF to cover v2 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v3

??? faq "v3 - [CLICK TO EXPAND]"
    CF to cover v3 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v4

??? faq "v4 - [CLICK TO EXPAND]"
    CF to cover v4 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VRV

??? faq "VRV - [CLICK TO EXPAND]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/VRV_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vrv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 10bit

??? faq "10bit - [CLICK TO EXPAND]"
    This CF covers releases that are 10bit

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Dual Audio

??? faq "Anime Dual Audio - [CLICK TO EXPAND]"
    This CF covers releases that have Dual Audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dubs Only

??? faq "Dubs Only - [CLICK TO EXPAND]"
    This CF covers releases that only have Dubs

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dubs-only.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------
