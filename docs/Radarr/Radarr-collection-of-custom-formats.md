# Collection of Custom Formats

Here I will try to list a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on Discord or that I created with help from others.
Special thanks to [rg9400](https://github.com/rg9400), [bakerboy448](https://github.com/bakerboy448) and Team Radarr.

With Radarr V3, Custom Formats are much more advanced/powerful than with v0.2, although this also means a Custom Format is much more complicated to setup.

After requesting it at Team Radarr, we now have the option to import/export the Custom Formats in a JSON format. This makes it easier to share the Custom Formats.

I also made 3 guides related to this one.

- [How to import Custom Formats](/Radarr/Radarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to import the Custom Formats.
- [How to upgrade Custom Formats](/Radarr/Radarr-how-to-update-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to upgrade your existing Custom Formats.
- [How to setup Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to make the most use of Custom Formats to help you to setup your quality profiles for your personal needs.

!!! tip

    I also suggest to change the Propers and Repacks settings in Radarr

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

| Movie Versions                                | Unwanted              | HQ Release Groups                         | Streaming Services     |
| --------------------------------------------- | --------------------- | ----------------------------------------- | ---------------------- |
| [Hybrid](#hybrid)                             | [BR-DISK](#br-disk)   | [Remux Tier 01](#remux-tier-01)           | [Amazon](#amzn)        |
| [Remaster](#remaster)                         | [LQ](#lq)             | [Remux Tier 02](#remux-tier-02)           | [Apple TV+](#atvp)     |
| [4K Remaster](#4k-remaster)                   | [3D](#3d)             | [UHD Bluray Tier 01](#uhd-bluray-tier-01) | [Disney+](#dsnp)       |
| [Special Edition](#special-edition)           | [x265 (HD)](#x265-hd) | [UHD Bluray Tier 02](#uhd-bluray-tier-02) | [HBO Max](#hmax)       |
| [Criterion Collection](#criterion-collection) |                       | [UHD Bluray Tier 03](#uhd-bluray-tier-03) | [Hulu](#hulu)          |
| [Masters of Cinema](#masters-of-cinema)       |                       | [HD Bluray Tier 01](#hd-bluray-tier-01)   | [Netflix](#nf)         |
| [Theatrical Cut](#theatrical-cut)             |                       | [HD Bluray Tier 02](#hd-bluray-tier-02)   | [Peacock TV](#pcok)    |
| [IMAX](#imax)                                 |                       | [WEB Tier 01](#web-tier-01)               | [Paramount+](#pmtp)    |
| [IMAX Enhanced](#imax-enhanced)               |                       | [WEB Tier 02](#web-tier-02)               | [Movies Anywhere](#ma) |
| [Open Matte](#open-matte)                     |                       | [WEB Tier 03](#web-tier-03)               |                        |

------

| Misc                           | Optional                            | French Audio Version          | French Source Groups                            |
| ------------------------------ | ----------------------------------- | ----------------------------- | ----------------------------------------------- |
| [Repack/Proper](#repackproper) | [Bad Dual Groups](#bad-dual-groups) | [Multi-French](#multi-french) | [FR Remux Tier 01](#fr-remux-tier-01)           |
| [Repack2](#repack2)            | [DV (WEBDL)](#dv-webdl)             | [Multi-Audio](#multi-audio)   | [FR Remux Tier 02](#fr-remux-tier-02)           |
| [Multi](#multi)                | [EVO (no WEBDL)](#evo-no-webdl)     | [French Audio](#french-audio) | [FR UHD Bluray Tier 01](#fr-uhd-bluray-tier-01) |
| [x264](#x264)                  | [HDR10+ Boost](#hdr10plus-boost)    | [VFF](#vff)                   | [FR UHD Bluray Tier 02](#fr-uhd-bluray-tier-02) |
| [x265](#x265)                  | [No-RlsGroup](#no-rlsgroup)         | [VOF](#vof)                   | [FR HD Bluray Tier 01](#fr-hd-bluray-tier-01)   |
| [MPEG2](#mpeg2)                | [Obfuscated](#obfuscated)           | [VFI](#vfi)                   | [FR HD Bluray Tier 02](#fr-hd-bluray-tier-02)   |
| [Dutch Groups](#dutch-groups)  | [Retags](#retags)                   | [VFQ](#vfq)                   | [FR WEB Tier 01](#fr-web-tier-01)               |
| [FreeLeech](#freeleech)        | [Scene](#scene)                     | [VQ](#vq)                     | [FR WEB Tier 02](#fr-web-tier-02)               |
|                                | [x265 (no HDR/DV)](#x265-no-hdrdv)  | [VFB](#vfb)                   | [FR Scene Groups](#fr-scene-groups)             |
|                                | [AV1](#av1)                         | [VOSTFR](#vostfr)             | [FR LQ](#fr-lq)                                 |
|                                | [SDR](#sdr)                         |                               |                                                 |
|                                | [DV (FEL)](#dv-fel)                 |                               |                                                 |

------

| Anime                                                                       | Anime                                                                 | Anime       | Anime Optional                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------- | ------------------------------------- |
| [Anime BD Tier 01 (Top SeaDex Muxers)](#anime-bd-tier-01-top-seadex-muxers) | [Anime Web Tier 01 (Muxers)](#anime-web-tier-01-muxers)               | [v0](#v0)   | [Uncensored](#uncensored)             |
| [Anime BD Tier 02 (SeaDex Muxers)](#anime-bd-tier-02-seadex-muxers)         | [Anime Web Tier 02 (Top FanSubs)](#anime-web-tier-02-top-fansubs)     | [v1](#v1)   | [10bit](#10bit)                       |
| [Anime BD Tier 03 (SeaDex Muxers)](#anime-bd-tier-03-seadex-muxers)         | [Anime Web Tier 03 (Official Subs)](#anime-web-tier-03-official-subs) | [v2](#v2)   | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 04 (SeaDex Muxers)](#anime-bd-tier-04-seadex-muxers)         | [Anime Web Tier 04 (Official Subs)](#anime-web-tier-04-official-subs) | [v3](#v3)   | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 05 (Remuxes)](#anime-bd-tier-05-remuxes)                     | [Anime Web Tier 05 (FanSubs)](#anime-web-tier-05-fansubs)             | [v4](#v4)   |                                       |
| [Anime BD Tier 06 (FanSubs)](#anime-bd-tier-06-fansubs)                     | [Anime Web Tier 06 (FanSubs)](#anime-web-tier-06-fansubs)             | [VRV](#vrv) |                                       |
| [Anime BD Tier 07 (P2P/Scene)](#anime-bd-tier-07-p2pscene)                  | [Anime Raws](#anime-raws)                                             |             |                                       |
| [Anime BD Tier 08 (Mini Encodes)](#anime-bd-tier-08-mini-encodes)           | [Anime LQ Groups](#anime-lq-groups)                                   |             |                                       |

## Audio Advanced

------

### TrueHD ATMOS

??? faq "TrueHD ATMOS - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}

    Dolby Atmos is a surround sound technology developed by Dolby Laboratories. It expands on existing surround sound systems by adding height channels, allowing sounds to be interpreted as three-dimensional objects.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS X

??? faq "DTS X - [CLICK TO EXPAND]"

    DTS:X is an object-based audio codec, which aims to create a multi-dimensional sound that “moves around you like it would in real life”

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-x.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DDPlus ATMOS

??? faq "DD+ ATMOS - [CLICK TO EXPAND]"

    Atmos via UHD Blu-ray will be lossless, or lossy via streaming services so in this case it will be lossy + Atmos

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ddplus-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TrueHD

??? faq "TrueHD - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}

    Dolby TrueHD is a lossless, multi-channel audio codec developed by Dolby Laboratories for home video, used principally in Blu-ray Disc and compatible hardware.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

??? faq "DTS-HD MA - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}

    DTS-HD Master Audio is a multi-channel, lossless audio codec developed by DTS as an extension of the lossy DTS Coherent Acoustics codec (DTS CA; usually itself referred to as just DTS). Rather than being an entirely new coding mechanism, DTS-HD MA encodes an audio master in lossy DTS first, then stores a concurrent stream of supplementary data representing whatever the DTS encoder discarded. This gives DTS-HD MA a lossy "core" able to be played back by devices that cannot decode the more complex lossless audio. DTS-HD MA's primary application is audio storage and playback for Blu-ray Disc media.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FLAC

??? faq "FLAC - [CLICK TO EXPAND]"

    FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

??? faq "PCM - [CLICK TO EXPAND]"

    PCM is the method of encoding typically used for uncompressed digital audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

??? faq "DTS-HD HRA - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-hd-hra.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

??? faq "DTS-ES - [CLICK TO EXPAND]"

    DTS-ES (DTS Extended Surround) includes two variants, DTS-ES Discrete 6.1, and DTS-ES Matrix 5.1, depending on how the sound was originally mastered and stored.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

<sub>DTS = Basic DTS</sub>

??? faq "DTS - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/aac.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MP3

??? faq "MP3 - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Opus

??? faq "Opus - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}

    Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Audio Channels

------

### 1.0 Mono

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stereo

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3.0 Sound

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4.0 Sound

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 5.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 6.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 7.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 9.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/91-surround.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-hdr10.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-hlg.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-sdr.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr10plus.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr10.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (undefined)

??? faq "HDR (undefined) - [CLICK TO EXPAND]"

    Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.

    For now it's only FraMeSToR/HQMUX that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr-undefined.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pq.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Movie Versions

------

### Hybrid

??? faq "Hybrid - [CLICK TO EXPAND]"

    A hybrid release means any combination of sources (video + audio) and not a direct encode of a single source. Generally you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hybrid.json' %]][[% endfilter %]]
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
     [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4K Remaster

??? faq "4K Remaster - [CLICK TO EXPAND]"

    A remastered or mastered in 4K should give you usually the best picture and audio currently for the movie. Both are just names to describe the best possible currently for the movie.

    To be clear, the final digital films on the Mastered in 4K Blu-rays still only have the same 1920 x 1080 pixels of actual resolution as normal Blu-rays. But the argument goes that because these full HD files were derived from higher-resolution masters, their images will be more precise, with better colors, less noise, and enhanced sharpness and detail. Not least because the higher-resolution mastering process will provide more detail from the original print for the Blu-ray masters to draw on when going through their (hopefully…) frame-by-frame compression process.

    Another important element of the Mastered in 4K discs is that they’re all mastered with ‘x.v.YCC’ color specification. This delivers an expanded color range closer to that contained in original source material.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/4k-remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Criterion Collection

??? faq "Criterion Collection - [CLICK TO EXPAND]"

    The Criterion Collection, Inc. (or simply Criterion) is an American home video distribution company which focuses on licensing "important classic and contemporary films" and selling them to film aficionados. Criterion has helped to standardize characteristics of home video such as film restoration, using the letterbox format for widescreen films, and adding bonus features and commentary tracks.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/criterion-collection.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Masters of Cinema

??? faq "Masters of Cinema - [CLICK TO EXPAND]"

    Masters of Cinema is a line of DVD and Blu-ray releases published through Eureka Entertainment. Because of the uniformly branded and spine-numbered packaging and the standard inclusion of booklets and analysis by recurring film historians, the line is often perceived as the UK equivalent of The Criterion Collection.

??? example "JSON - [CLICK TO EXPAND}"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/masters-of-cinema.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Theatrical Cut

??? faq "Theatrical Cut - [CLICK TO EXPAND]"

    The Theatrical Cut is the version of the film that was shown at cinemas.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/theatrical-cut.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Special Edition

??? faq "Special Edition - [CLICK TO EXPAND]"

    Custom format for several Special Editions

    - The Director's Cut is the version edited by the Director, usually for additional home media releases.
    - An Extended Cut is usually any version of the film which is longer than the theatrical cut (though in very rare cases, its shorter).

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/special-edition.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IMAX

??? faq "IMAX - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/imax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IMAX Enhanced

??? faq "IMAX Enhanced - [CLICK TO EXPAND]"
    IMAX Enhanced: Get More Picture Instead of Black Bars

    IMAX Enhanced exclusive expanded aspect ratio is 1:90:1, which offers up to 26% more picture for select sequences, meaning more of the action is visible on screen.

    ![!Imax Enhanced Example](images/imax-e/imax-e.1.png)

    ![!Imax Enhanced Example](images/imax-e/imax-e.2.png)

    ![!Imax Enhanced Example](images/imax-e/imax-e.3.png)

    ![!Imax Enhanced Example](images/imax-e/imax-e.4.png)

    ![!Imax Enhanced Example](images/imax-e/imax-e.5.png)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/imax-enhanced.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Open Matte

??? faq "Open Matte - [CLICK TO EXPAND]"

    Open matte is a filming technique that involves matting out the top and bottom of the film frame in the movie projector (known as a soft matte) for the widescreen theatrical release and then scanning the film without a matte (at Academy ratio) for a full screen home video release.

??? example "JSON - [CLICK TO EXPAND}"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/open-matte.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Unwanted

------

### BR-DISK

??? faq "BR-DISK - [CLICK TO EXPAND]"

    This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-10000`

    !!! note

        Depending on your renaming scheme it could happen that Radarr will match renamed files after they are downloaded and imported as `BR-DISK`,
        This is a cosmetic annoyance until I come up with another way to solve this,
        being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
        Several reasons why this is happening:

        - Blame the often wrongly used naming of x265 encodes.
        - Radarr v3/v4 uses dynamic custom formats.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ

<sub>Low Quality Releases = LQ</sub>

??? faq "LQ - [CLICK TO EXPAND]"

    A collection of known Low Quality groups that are often banned from the the top trackers because their lack of quality, Banned release groups, dishonest release groups or Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3D

??? faq "3D - [CLICK TO EXPAND]"

    If you prefer or not prefer 3D.

    You can use Custom Format or use Restrictions (`Settings` => `Indexers` => `Restrictions`) what ever you prefer.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/3d.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (HD)

<sub>720/1080p no x265 = x265 (720/1080p) = x265 (HD)</sub>

??? faq "x265 (HD) - [CLICK TO EXPAND]"

    This blocks 720/1080p (HD) releases that are encoded in x265.

    In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-hd']['trash_score'] }}`

    !!! fail ""
        --8<-- "includes/docker/x265.md"

            !!! Danger "Don't use this together with [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv), Only ever include one of them :warning:"

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x265-hd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Optional

------

### Bad Dual Groups

??? faq "Bad dual groups - [CLICK TO EXPAND]"
    These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/bad-dual-groups.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### EVO (no WEBDL)

??? faq "EVO (no WEBDL) - [CLICK TO EXPAND]"

    This group is often banned for the low quality Blu-ray releases, but their WEB-DLs are okay.

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-10000`

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/evo-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR10Plus Boost

??? faq "HDR10+ Boost - [CLICK TO EXPAND]"

    Optional (use this one only if you have a (Samsung) TV that supports HDR10+ and you don't have a Setup that supports DV or you prefer HDR10+.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr10plus-boost.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Obfuscated

??? faq "Obfuscated - [CLICK TO EXPAND]"

    Optional (use these only if you dislike renamed releases)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Retags

??? faq "Retags - [CLICK TO EXPAND]"

    Optional (use these only if you dislike retagged releases)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/retags.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Scene

??? faq "Scene - [CLICK TO EXPAND]"

    This Custom Format will try to recognize so called Scene releases, depending on your preferences you can give it a negative score `-10000` or a positive score or just don't add it all.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (no HDR/DV)

??? faq "x265 (no HDR/DV) - [CLICK TO EXPAND]"

    This blocks 720/1080p (HD) releases that are encoded in x265.

    **But it will allow x265 releases if they have HDR and/or DV**

    *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

    In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-no-hdrdv']['trash_score'] }}`

    !!! Danger "Don't use this together with [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x265-no-hdrdv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### AV1

??? faq "AV1 - [CLICK TO EXPAND]"

    - This is a new codec and you need modern devices that support it.
    - We also had reports of playback/transcoding issues.
    - No main group is actually using it (yet).
    - It's better to ignore this new codec to prevent compatibility issues.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/av1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### SDR

??? faq "SDR - [CLICK TO EXPAND]"

    - This will help to prevent to grab UHD/4k releases without HDR Formats.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV FEL

??? faq "DV (FEL) - [CLICK TO EXPAND]"

    - This will boost the score for Dolby Vision Releases using the original full quality Dolby Vision layer from the disc release to replace the old WEBDL HYBRID release.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-fel.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc

------

### Repack/Proper

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack2

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/repack2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x264

??? faq "x264 - [CLICK TO EXPAND]"

    x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x264.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FreeLeech

??? faq "FreeLeech - [CLICK TO EXPAND]"

    Sometimes, torrent sites set a torrent to be freeleech. This means, that the download of this torrent will not count towards your download quota or ratio. This is really useful, if you do not have the best ratio yet.

    !!! attention
        Keep in mind not all trackers support this option.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/freeleech.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dutch Groups

??? faq "Dutch Groups - [CLICK TO EXPAND]"

    If you prefer movies with also a Dutch audio track.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dutch-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MPEG2

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HQ Release Groups

------

### Remux Tier 01

??? faq "Remux Tier 01 - [CLICK TO EXPAND]"

    - Groups doing remuxes with multiple sources(discs) mixing what's best.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Remux Tier 02

??? faq "Remux Tier 02 - [CLICK TO EXPAND]"

    - Groups that only use one source.(So called one disc wonders.)
    - Groups that use use a automated way.
    - Groups that don't check their stuff.
    - Groups that haven't released much. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### UHD Bluray Tier 01

??? faq "UHD Bluray Tier 01 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.
    - HDR/DoVi (Depending what's offered and often both)
    - HD Audio (Atmos, TrueHD etc...)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uhd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### UHD Bluray Tier 02

??? faq "UHD Bluray Tier 02 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.
    - HDR/DoVi (Depending what's offered and often both)
    - HD Audio (Atmos, TrueHD etc...)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uhd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### UHD Bluray Tier 03

??? faq "UHD Bluray Tier 03 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.
    - HDR/DoVi (Depending what's offered and often both)
    - HD Audio (Atmos, TrueHD etc...)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uhd-bluray-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HD Bluray Tier 01

??? faq "HD Bluray Tier 01 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.
    - Groups that have a minimum of GP releases.(best encode in it's class  1080p and lower)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HD Bluray Tier 02

??? faq "HD Bluray Tier 02 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 01

??? faq "WEB Tier 01 - [CLICK TO EXPAND]"

    - Groups that create hybrids.
    - Groups that sign up for the gentleman list on a certain private tracker.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 02

??? faq "WEB Tier 02 - [CLICK TO EXPAND]"

    - placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### WEB Tier 03

??? faq "WEB Tier 03 - [CLICK TO EXPAND]"

    - placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/web-tier-03.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/amzn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ATVP

<sub>Apple TV+</sub>

??? faq "Apple TV+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Apple_TV%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/atvp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DSNP

<sub>Disney+</sub>

??? faq "Disney+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Disney%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dsnp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HMAX

<sub>HBO Max</sub>

??? faq "HBO Max - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/HBO_Max){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hmax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Hulu

<sub>Hulu</sub>

??? faq "Hulu - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Hulu){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### NF

<sub>Netflix</sub>

??? faq "Netflix - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Netflix){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/nf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCOK

<sub>Peacock TV</sub>

??? faq "Peacock TV - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Peacock_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pcok.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PMTP

<sub>Paramount+</sub>

??? faq "Paramount+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Paramount%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pmtp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MA

<sub>Movies Anywhere</sub>

??? faq "Movies Anywhere - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Movies_Anywhere){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

## Anime

------

### Anime BD Tier 01 (Top SeaDex Muxers)

??? faq "Anime BD Tier 01 (Top SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-01-top-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 02 (SeaDex Muxers)

??? faq "Anime BD Tier 02 (SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-02-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 03 (SeaDex Muxers)

??? faq "Anime BD Tier 03 (SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-03-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 04 (SeaDex Muxers)

??? faq "Anime BD Tier 04 (SeaDex Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-04-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 05 (Remuxes)

??? faq "Anime BD Tier 05 (Remuxes) - [CLICK TO EXPAND]"
    Groups that are consistent and do Remuxes

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-05-remuxes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 06 (FanSubs)

??? faq "Anime BD Tier 06 (FanSubs) - [CLICK TO EXPAND]"
    FanSub groups that are consistent

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 07 (P2P/Scene)

??? faq "Anime BD Tier 07 (P2P/Scene) - [CLICK TO EXPAND]"
    Known P2P and Scene Anime groups

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-07-p2pscene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime BD Tier 08 (Mini Encodes)

??? faq "Anime BD Tier 08 (Mini Encodes) - [CLICK TO EXPAND]"
    Know groups that do mini encodes

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-08-mini-encodes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 01 (Muxers)

??? faq "Anime Web Tier 01 (Muxers) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-01-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 02 (Top FanSubs)

??? faq "Anime Web Tier 02 (Top FanSubs) - [CLICK TO EXPAND]"
    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-02-top-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 03 (Official Subs)

??? faq "Anime Web Tier 03 Official Subs) - [CLICK TO EXPAND]"
    Official sub groups that tend to be more consistent and release fast

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-03-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 04 (Official Subs)

??? faq "Anime Web Tier 04 (Official Subs) - [CLICK TO EXPAND]"
    Official sub groups

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-04-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 05 (FanSubs)

??? faq "Anime Web Tier 05 (FanSubs) - [CLICK TO EXPAND]"
    FanSub groups that are consistent

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-05-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Web Tier 06 (FanSubs)

??? faq "Anime Web Tier 06 (FanSubs) - [CLICK TO EXPAND]"
    FanSub groups that are consistent

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Raws

??? faq "Anime Raws - [CLICK TO EXPAND]"
    A collection of know groups that release raws

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-raws.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime LQ Groups

??? faq "Anime LQ Groups - [CLICK TO EXPAND]"
    A collection of known Low Quality groups.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-lq-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Uncensored

??? faq "Uncensored - [CLICK TO EXPAND]"
    This CF covers releases that are uncensored

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uncensored.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v0

??? faq "v0 - [CLICK TO EXPAND]"
    CF to cover releases named with v0 which we don't want

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v0.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v1

??? faq "v1 - [CLICK TO EXPAND]"
    CF to cover v1 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v2

??? faq "v2 - [CLICK TO EXPAND]"
    CF to cover v2 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v3

??? faq "v3 - [CLICK TO EXPAND]"
    CF to cover v3 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### v4

??? faq "v4 - [CLICK TO EXPAND]"
    CF to cover v4 releases

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VRV

??? faq "VRV - [CLICK TO EXPAND]"
    [From Wikipedia, the free encyclopedia](https://www.wikiwand.com/en/VRV_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/vrv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 10bit

??? faq "10bit - [CLICK TO EXPAND]"
    This CF covers releases that are 10bit

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/10bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Dual Audio

??? faq "Anime Dual Audio - [CLICK TO EXPAND]"
    This CF covers releases that have Dual Audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dubs Only

??? faq "Dubs Only - [CLICK TO EXPAND]"
    This CF covers releases that only have Dubs

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dubs-only.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## French Audio Version

------

### Multi-French

??? faq "Multi-French - [CLICK TO EXPAND]"

    Recognize movies that include the original and the french audio. Work only after import as it need the result from FFprobe to get which audio are present. Will rename the release to keep the recognition of 'Multi' by the [Multi-Audio](#multi-audio) custom format.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/multi-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi-Audio

??? faq "Multi-Audio - [CLICK TO EXPAND]"

    A slightly modified [Multi](#multi) Custom Formats that recognize VF and VO inside the name.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/multi-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### French Audio

??? faq "French Audio - [CLICK TO EXPAND]"

    This will recognize every kind of French Audio.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFF

??? faq "VFF - [CLICK TO EXPAND]"

    Full French version (dubbing done in France) and French version (normally equivalent to VFQ).

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vff.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOF

??? faq "VOF - [CLICK TO EXPAND]"

    Original French Version.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vof.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFI

??? faq "VFI - [CLICK TO EXPAND]"

    International French Version. VF[1-9] or FR[1-9] indicates the number of dubs present (normally VF2 being VFF and VFQ) and is considered as an International French release.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vfi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFQ

??? faq "VFQ - [CLICK TO EXPAND]"

    Canadian French Version.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vfq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VQ

??? faq "VQ - [CLICK TO EXPAND]"

    Quebec Version (strong Quebec accent, ex: The Simpsons movie).

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VFB

??? faq "VFB - [CLICK TO EXPAND]"

    Belgian French Version.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vfb.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### VOSTFR

??? faq "VOSTFR - [CLICK TO EXPAND]"

    Indicates soundtrack in the original language, with French subtitles. It should be noted that SUBFRENCH is included inside this Custom Format. However, SUB often mean that the subtitle was embedded inside the picture (hardcoded). French releases tend to mix both, leading some VOSTFR being labelled as SUBFRENCH and SUBFRENCH as VOSTFR.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vostfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## French HQ Source Groups

------

### FR Remux Tier 01

??? faq "Remux Tier 01 - [CLICK TO EXPAND]"

    - Groups doing remuxes with multiple sources (discs) mixing what's best.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Remux Tier 02

??? faq "Remux Tier 02 - [CLICK TO EXPAND]"

    - Groups that use an automated way.
    - Groups active doing remuxes from a single sources (discs).
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR UHD Bluray Tier 01

??? faq "FR UHD Bluray Tier 01 - [CLICK TO EXPAND]"

    (WiP - This Custom Formats should be considered in alpha stage)
    - Groups that created encodes from the remuxes without micro-sizing them.
    - HDR/DoVi (Depending what's offered and often both).
    - HD Audio (Atmos, TrueHD etc...).

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-uhd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR UHD Bluray Tier 02

??? faq "FR UHD Bluray Tier 02 - [CLICK TO EXPAND]"

    (WiP - This Custom Formats should be considered in alpha stage)
    - Groups that created encodes from the remuxes without micro-sizing them.
    - HDR/DoVi (Depending what's offered and often both).
    - HD Audio (Atmos, TrueHD etc...).
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-uhd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR HD Bluray Tier 01

??? faq "FR HD Bluray Tier 01 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.
    - Groups that have a minimum of great releases (best encode in it's class 1080p and lower).

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR HD Bluray Tier 02

??? faq "FR HD Bluray Tier 02 - [CLICK TO EXPAND]"

    - Groups that created encodes from the remuxes without micro-sizing them.
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Tier 01

??? faq "FR WEB Tier 01 - [CLICK TO EXPAND]"

    - placeholder
    - Groups that source directly from the streaming service

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR WEB Tier 02

??? faq "FR WEB Tier 02 - [CLICK TO EXPAND]"

    - placeholder
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups that retired and don't have the best quality by todays standards.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR Scene Groups

??? faq "FR Scene Groups - [CLICK TO EXPAND]"

    Known French Scene groups.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FR LQ

<sub>French Low Quality Releases = FR LQ</sub>

??? faq "FR LQ - [CLICK TO EXPAND]"

    A collection of known French Low Quality groups that are often banned from the the top trackers because their lack of quality.

    !!! note

        - Ads/Watermarks = Groups that are know to put ads or watermark in their releases.
        - Bad/False releases = Groups that are known for lying on the quality, type or the name of their releases.
        - DeTAG/ReTAG = Detagging or stealing groups.
        - Other reasons = Banned Release Groups.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>
