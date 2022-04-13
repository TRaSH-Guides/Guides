# Collection of Custom Formats

Here I will try to collect a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on discord or that I created with help from others.
Special thanks to [rg9400](https://github.com/rg9400), [bakerboy448](https://github.com/bakerboy448) and Team Radarr.

With Radarr V3, Custom Formats are much more advanced/powerful than with v0.2, although this also means a Custom Format is much more complicated to setup.

After requesting at Team Radarr we now have the options to import/export the Custom Formats in a JSON format that we can use here what makes it easier to share the different kind of Custom Formats.

I also made 3 guides related to this one.

- [How to import Custom Formats](/Radarr/Radarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to import the Custom Formats.
- [How to upgrade Custom Formats](/Radarr/Radarr-how-to-update-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to upgrade your existing the Custom Formats.
- [How to setup Custom Formats](/Radarr/Radarr-setup-custom-formats){:target="_blank" rel="noopener noreferrer"} Where I will try to explain how to make the most use of Custom Formats and show some personal examples that I'm using. That you can use to get a idea how to setup yours.

!!! tip

    I also suggest to change the Propers and Repacks settings in Radarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repack-proper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Formats preferences will be used and not ignored.

--8<-- "includes/support.md"

------

## INDEX

------

| Audio Advanced #1                         | Audio Advanced #2               | Audio Channels               | HDR Metadata                      |
| ----------------------------------------- | ------------------------------- | ---------------------------- | --------------------------------- |
| [TrueHD ATMOS](#truehd-atmos)             | [FLAC](#flac)                   | [1.0 Mono](#10-mono)         | [DV HDR10](#dv-hdr10)             |
| [DTS X](#dts-x)                           | [PCM](#pcm)                     | [2.0 Stereo](#20-stereo)     | [DV](#dv)                         |
| [ATMOS (undefined)](#atmos-undefined)     | [DTS-HD HRA](#dts-hd-hra)       | [3.0 Sound](#30-sound)       | [DV HLG](#dv-hlg)                 |
| [DD+ ATMOS](#dd-atmos)                    | [AAC](#aac)                     | [4.0 Sound](#40-sound)       | [DV SDR](#dv-sdr)                 |
| [TrueHD](#truehd)                         | [DD](#dd)                       | [5.1 Surround](#51-surround) | [HDR10+](#hdr10plus)              |
| [DTS-HD MA](#dts-hd-ma)                   | [MP3](#mp3)                     | [6.1 Surround](#61-surround) | [HDR10](#hdr10)                   |
| [DD+](#ddplus)                            | [Opus](#opus)                   | [7.1 Surround](#71-surround) | [HDR](#hdr)                       |
| [DTS-ES](#dts-es)                         |                                 | [9.1 Surround](#91-surround) | [HDR (undefined)](#hdr-undefined) |
| [DTS](#dts)                               |                                 |                              | [PQ](#pq)                         |
|                                           |                                 |                              | [HLG](#hlg)                       |

------

| Movie Versions                                | Unwanted                           | Misc                                  | HQ Source Groups      | Streaming Services           |
| --------------------------------------------- | ---------------------------------- | ------------------------------------- | --------------------- | ---------------------------- |
| [Hybrid](#hybrid)                             | [BR-DISK](#br-disk)                | [Repack/Proper](#repack-proper)       | [HQ-Remux](#hq-remux) | [Amazon](#amazon)            |
| [Remaster](#remaster)                         | [EVO (no WEBDL)](#evo-no-webdl)    | [Multi](#multi)                       | [HQ](#hq)             | [Apple TV+](#apple-tvplus)   |
| [4K Remaster](#4k-remaster)                   | [LQ](#lq)                          | [x264](#x264)                         | [HQ-WEBDL](#hq-webdl) | [Disney+](#disneyplus)       |
| [Special Editions](#special-edition)          | [x265 (720/1080p)](#x265-7201080p) | [x265](#x265)                         |                       | [HBO Max](#hbo-max)          |
| [Criterion Collection](#criterion-collection) | [3D](#3d)                          | [MPEG2](#mpeg2)                       |                       | [Hulu](#hulu)                |
| [Theatrical Cut](#theatrical-cut)             | [No-RlsGroup](#no-rlsgroup)        | [FreeLeech](#freeleech)               |                       | [Netflix](#netflix)          |
| [IMAX](#imax)                                 | [Obfuscated](#obfuscated)          | [Dutch Groups](#dutch-groups)         |                       | [Peacock TV](#peacock-tv)    |
| [IMAX Enhanced](#imax-enhanced)               | [DV (WEBDL)](#dv-webdl)            | [Anime Dual Audio](#anime-dual-audio) |                       | [Paramount+](#paramountplus) |

------

## Audio Advanced

------

### TrueHD ATMOS

??? faq "TrueHD ATMOS - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}

    Dolby Atmos is a surround sound technology developed by Dolby Laboratories. It expands on existing surround sound systems by adding height channels, allowing sounds to be interpreted as three-dimensional objects.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS X

??? faq "DTS X - [CLICK TO EXPAND]"

    DTS:X is an object-based audio codec, which aims to create a multi-dimensional sound that “moves around you like it would in real life”

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-x.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DD+ ATMOS

??? faq "DD+ ATMOS - [CLICK TO EXPAND]"

    Atmos via UHD Blu-ray will be lossless, or lossy via streaming services so in this case it will be lossy + Atmos

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### TrueHD

??? faq "TrueHD - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}

    Dolby TrueHD is a lossless, multi-channel audio codec developed by Dolby Laboratories for home video, used principally in Blu-ray Disc and compatible hardware.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

??? faq "DTS-HD MA - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}

    DTS-HD Master Audio is a multi-channel, lossless audio codec developed by DTS as an extension of the lossy DTS Coherent Acoustics codec (DTS CA; usually itself referred to as just DTS). Rather than being an entirely new coding mechanism, DTS-HD MA encodes an audio master in lossy DTS first, then stores a concurrent stream of supplementary data representing whatever the DTS encoder discarded. This gives DTS-HD MA a lossy "core" able to be played back by devices that cannot decode the more complex lossless audio. DTS-HD MA's primary application is audio storage and playback for Blu-ray Disc media.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### FLAC

??? faq "FLAC - [CLICK TO EXPAND]"

    FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

??? faq "PCM - [CLICK TO EXPAND]"

    PCM is the method of encoding typically used for uncompressed digital audio

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

??? faq "DTS-HD HRA - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-hd-hra.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

??? faq "DTS-ES - [CLICK TO EXPAND]"

    DTS-ES (DTS Extended Surround) includes two variants, DTS-ES Discrete 6.1, and DTS-ES Matrix 5.1, depending on how the sound was originally mastered and stored.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS

<sub>DTS = Basic DTS</sub>

??? faq "DTS - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dts.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/aac.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MP3

??? faq "MP3 - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Opus

??? faq "Opus - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}

    Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Audio Channels

------

### 1.0 Mono

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stereo

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3.0 Sound

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4.0 Sound

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 5.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 6.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 7.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 9.1 Surround

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/91-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HDR metadata

------

### DV HDR10

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV HDR10 - [CLICK TO EXPAND]"

    Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

    Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dv-hdr10.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/dv.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/dv-hlg.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/dv-sdr.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/hdr10plus.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/hdr10.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (undefined)

??? faq "HDR (undefined) - [CLICK TO EXPAND]"

    Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.

    For now it's only FraMeSToR/HQMUX that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hdr-undefined.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/pq.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/hlg.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/hybrid.json' %]][[% endfilter %]]
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
     [[% filter indent(width=4) %]][[% include 'json/radarr/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 4K Remaster

??? faq "4K Remaster - [CLICK TO EXPAND]"

    A remastered or mastered in 4K should give you usually the best picture and audio currently for the movie. Both are just names to describe the best possible currently for the movie.

    To be clear, the final digital films on the Mastered in 4K Blu-rays still only have the same 1920 x 1080 pixels of actual resolution as normal Blu-rays. But the argument goes that because these full HD files were derived from higher-resolution masters, their images will be more precise, with better colours, less noise, and enhanced sharpness and detail. Not least because the higher-resolution mastering process will provide more detail from the original print for the Blu-ray masters to draw on when going through their (hopefully…) frame-by-frame compression process.

    Another important element of the Mastered in 4K discs is that they’re all mastered with ‘x.v.YCC’ colour specification. This delivers an expanded colour range closer to that contained in original source material.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/4k-remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Criterion Collection

??? faq "Criterion Collection - [CLICK TO EXPAND]"

    The Criterion Collection, Inc. (or simply Criterion) is an American home video distribution company which focuses on licensing "important classic and contemporary films" and selling them to film aficionados.Criterion has helped to standardize characteristics of home video such as film restoration, using the letterbox format for widescreen films, and adding bonus features and commentary tracks.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/criterion-collection.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Theatrical Cut

??? faq "Theatrical Cut - [CLICK TO EXPAND]"

    The Theatrical Cut is the version of the film that was shown at cinemas.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/theatrical-cut.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/special-edition.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### IMAX

??? faq "IMAX - [CLICK TO EXPAND]"
    IMAX: Get More Picture Instead of Black Bars

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/imax.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/imax-enhanced.json' %]][[% endfilter %]]
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
        This is a cosmetic annoyance till I come up for another way to solve this,
        being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
        Several reasons why this is happening:

        - Blame the often wrongly used naming of x265 encodes.
        - Radarr v3/v4 uses dynamic custom formats.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### EVO (no WEBDL)

??? faq "EVO (no WEBDL) - [CLICK TO EXPAND]"

    This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-10000`

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/evo-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ

<sub>Low Quality Releases = LQ</sub>

??? faq "LQ - [CLICK TO EXPAND]"

    A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality.

    !!! note

        You might want to add the following also [EVO (no WEBDL)](#evo-no-webdl)

        - BLOCK1 = Low-Quality Releases (often banned groups)
        - BLOCK2 = Another Small list of often banned groups.
        - BLOCK3 = Banned release groups.
        - BLOCK4 = Low-quality and/or dishonest release groups.
        - BLOCK5 = Banned Release Groups.
        - BLOCK6 = Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.
        - RiffTrax = RiffTrax is an American company that produces scripted humorous audio commentary tracks intended to be played in unison with particular television programs and films, In short just annoying !!!

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x265 (720/1080p)

<sub>720/1080p no x265 = x265 (720/1080p)</sub>

??? faq "720/1080p no x265 - [CLICK TO EXPAND]"

    This blocks/ignores 720/1080p releases that are encoded in x265

    You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-10000`

    !!! fail ""
        --8<-- "includes/docker/x265.md"

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/x265-7201080p.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### 3D

??? faq "3D - [CLICK TO EXPAND]"

    If you prefer or not prefer 3D.

    You can use Custom Format or use Restrictions (`Settings` => `Indexers` => `Restrictions`) what ever you prefer.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/3d.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### No-RlsGroup

??? faq "No-RlsGroup - [CLICK TO EXPAND]"

    Some indexers strip out the release group what could result in LQ groups getting a higher score.
    For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match

    !!! warning

        If you don't use a decent filenames like not adding release groups don't add this Custom Format, except if you want to upgrade them.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Obfuscated

??? faq "Obfuscated - [CLICK TO EXPAND]"

    Optional (use these only if you dislike renamed and retagged releases)

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DV (WEBDL)

<sub>Dolby Vision = DoVi = DV</sub>

??? faq "DV (WEBDL) - [CLICK TO EXPAND]"
    This is a special Custom Format that Block WEBDL **with** Dolby Vision but **without** HDR10 fallback.

    This Custom Format works together with the normal [DV](#dv) Custom Format that you can use to prefer Dolby Vision.

    Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

    Remuxes and Bluray have a fallback to HDR10.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dv-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc

------

### Repack Proper

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### x264

??? faq "x264 - [CLICK TO EXPAND]"

    x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/x264.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/x265.json' %]][[% endfilter %]]
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
    [[% filter indent(width=4) %]][[% include 'json/radarr/freeleech.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dutch Groups

??? faq "Dutch Groups - [CLICK TO EXPAND]"

    If you prefer movies with also a Dutch audio track.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/dutch-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Anime Dual Audio

??? faq "Anime Dual Audio - [CLICK TO EXPAND]"
    Description placeholder

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### MPEG2

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## HQ Source Groups

------

### HQ

<sub>HQ-Releases = HQ</sub>

??? faq "HQ - [CLICK TO EXPAND]"

    A collection of P2P groups that are known for their high quality releases.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HQ-WEBDL

??? faq "HQ-WEBDL - [CLICK TO EXPAND]"

    A personal collection of P2P WEB-DL groups that are known for their high quality releases.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hq-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HQ-Remux

??? faq "HQ-Remux - [CLICK TO EXPAND]"

    A personal collection of P2P Remux groups that are known for their high quality releases.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hq-remux.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

## Streaming Services

------

### Amazon

<sub>Amazon</sub>

??? faq "Amazon - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Amazon_Prime_Video){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/amazon.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Apple TVplus

<sub>Apple TV+</sub>

??? faq "Apple TV+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Apple_TV%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/apple-tvplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### DisneyPlus

<sub>Disney+</sub>

??? faq "Disney+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Disney%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/disneyplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### HBO Max

<sub>HBO Max</sub>

??? faq "HBO Max - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/HBO_Max){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hbo-max.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Hulu

<sub>Hulu</sub>

??? faq "Hulu - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Hulu){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Netflix

<sub>Netflix</sub>

??? faq "Netflix - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Netflix){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/netflix.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### Peacock TV

<sub>Peacock TV</sub>

??? faq "Peacock TV - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Peacock_(streaming_service)){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/peacock-tv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

------

### ParamountPlus

<sub>Paramount+</sub>

??? faq "Paramount+ - [CLICK TO EXPAND]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Paramount%2B){:target="_blank" rel="noopener noreferrer"}

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/paramountplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>
