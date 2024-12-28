# Collection of Custom Formats

Below is a collection of what we've come to regard as the most needed and commonly used Custom Formats.
These CFs have been collected from discussions on Discord or created with help from others.

Special thanks to everyone who has helped in the creation and testing of these Custom Formats, my team at TRaSH guides, and the community.

Sonarr V4+ introduces Custom Formats. These are much more advanced/powerful than the release profiles, although this also means a Custom Format can require more knowledge to set up or create.
We've made 3 guides related to this.

- [How to import Custom Formats](/Sonarr/sonarr-import-custom-formats){:target="\_blank" rel="noopener noreferrer"} - Explains how to import the Custom Formats.
- [How to upgrade Custom Formats](/Sonarr/sonarr-how-to-update-custom-formats){:target="\_blank" rel="noopener noreferrer"} - Explains how to upgrade your existing Custom Formats.
- [How to set up Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="\_blank" rel="noopener noreferrer"} - Explains how to make the most use of Custom Formats and shows some specifics of my configuration. You can use these examples to get an idea of how to set up your preferences.

!!! tip

    It also is recommended to change the Propers and Repacks settings in Sonarr's `Settings`.

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repackproper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Format scoring and preferences will be fully utilized.

--8<-- "includes/support.md"

---

## INDEX

---

| Audio Advanced #1                     | Audio Advanced #2         | Audio Channels               | HDR Formats                       |
| ------------------------------------- | ------------------------- | ---------------------------- | --------------------------------- |
| [TrueHD ATMOS](#truehd-atmos)         | [FLAC](#flac)             | [1.0 Mono](#10-mono)         | [DV HDR10+](#dv-hdr10plus)        |
| [DTS X](#dts-x)                       | [PCM](#pcm)               | [2.0 Stereo](#20-stereo)     | [DV HDR10](#dv-hdr10)             |
| [ATMOS (undefined)](#atmos-undefined) | [DTS-HD HRA](#dts-hd-hra) | [3.0 Sound](#30-sound)       | [DV](#dv)                         |
| [DD+ ATMOS](#ddplus-atmos)            | [AAC](#aac)               | [4.0 Sound](#40-sound)       | [DV HLG](#dv-hlg)                 |
| [TrueHD](#truehd)                     | [DD](#dd)                 | [5.1 Surround](#51-surround) | [DV SDR](#dv-sdr)                 |
| [DTS-HD MA](#dts-hd-ma)               | [MP3](#mp3)               | [6.1 Surround](#61-surround) | [HDR10+](#hdr10plus)              |
| [DD+](#ddplus)                        | [Opus](#opus)             | [7.1 Surround](#71-surround) | [HDR10](#hdr10)                   |
| [DTS-ES](#dts-es)                     |                           |                              | [HDR](#hdr)                       |
| [DTS](#dts)                           |                           |                              | [HDR (undefined)](#hdr-undefined) |
|                                       |                           |                              | [PQ](#pq)                         |
|                                       |                           |                              | [HLG](#hlg)                       |

---

| Series Versions       | Unwanted                                | HQ Source Groups                        |
| --------------------- | --------------------------------------- | --------------------------------------- |
| [Hybrid](#hybrid)     | [AV1](#av1)                             | [Remux Tier 01](#remux-tier-01)         |
| [Remaster](#remaster) | [BR-DISK](#br-disk)                     | [Remux Tier 02](#remux-tier-02)         |
|                       | [Extras](#extras)                       | [HD Bluray Tier 01](#hd-bluray-tier-01) |
|                       | [LQ](#lq)                               | [HD Bluray Tier 02](#hd-bluray-tier-02) |
|                       | [LQ (Release Title)](#lq-release-title) | [WEB Tier 01](#web-tier-01)             |
|                       | [Upscaled](#upscaled)                   | [WEB Tier 02](#web-tier-02)             |
|                       | [x265 (HD)](#x265-hd)                   | [WEB Tier 03](#web-tier-03)             |
|                       |                                         | [WEB Scene](#web-scene)                 |

---

| General Streaming Services | French Streaming Services | Asian Streaming Services | Dutch Streaming Services |
| -------------------------- | ------------------------- | ------------------------ | ------------------------ |
| [Amazon](#amzn)            | [MyCANAL](#mycanal)       | [FOD](#fod)              | [NLZiet](#nlz)           |
| [Apple TV+](#atvp)         | [AUViO](#auvio)           | [Disney+ Hotstar](#htsr) | [Videoland](#vdl)        |
| [Comedy Central](#cc)      | [SALTO](#salto)           | [TVer](#tver)            |                          |
| [DC Universe](#dcu)        |                           | [TVING](#tving)          |                          |
| [Disney+](#dsnp)           |                           | [U-NEXT](#u-next)        |                          |
| [HBO Max](#hmax)           |                           | [VIU](#viu)              |                          |
| [HBO](#hbo)                |                           |                          |                          |
| [Hulu](#hulu)              |                           |                          |                          |
| [iTunes](#it)              |                           |                          |                          |
| [Max](#max)                |                           |                          |                          |
| [Netflix](#nf)             |                           |                          |                          |
| [Paramount+](#pmtp)        |                           |                          |                          |
| [Peacock TV](#pcok)        |                           |                          |                          |
| [SHOWTIME](#sho)           |                           |                          |                          |
| [Stan](#stan)              |                           |                          |                          |
| [Syfy](#syfy)              |                           |                          |                          |

| UK Streaming Services | Misc Streaming Services | Anime Streaming Services | Optional Streaming Services                 |
| --------------------- | ----------------------- | ------------------------ | ------------------------------------------- |
| [4OD](#4od)           | [AUBC](#aubc)           | [ABEMA](#abema)          | [UHD Streaming Boost](#uhd-streaming-boost) |
| [ALL4](#all4)         | [CBC](#cbc)             | [ADN](#adn)              | [UHD Streaming Cut](#uhd-streaming-cut)     |
| [BBC iPlayer](#ip)    | [Crave](#crav)          | [B-Global](#b-global)    |                                             |
| [ITVX](#itvx)         | [Discovery+](#dscp)     | [Bilibili](#bilibili)    |                                             |
| [MY5](#my5)           | [OViD](#ovid)           | [Crunchyroll](#cr)       |                                             |
| [NOW](#now)           | [Star+](#strp)          | [Funimation](#funi)      |                                             |
|                       | [YouTube Red](#red)     | [HIDIVE](#hidive)        |                                             |
|                       | [Quibi](#qibi)          | [VRV](#vrv)              |                                             |
|                       |                         | [WKN](#wkn)              |                                             |

---

| Miscellaneous                          | French Audio Version | French Source Groups                          |
| -------------------------------------- | -------------------- | --------------------------------------------- |
| [Bad Dual Groups](#bad-dual-groups)    | [VFF](#vff)          | [FR Remux Tier 01](#fr-remux-tier-01)         |
| [DV (Disk)](#dv-disk)                  | [VOF](#vof)          | [FR HD Bluray Tier 01](#fr-hd-bluray-tier-01) |
| [DV (WEBDL)](#dv-webdl)                | [VFI](#vfi)          | [FR WEB Tier 01](#fr-web-tier-01)             |
| [DV HDR10+ Boost](#dv-hdr10plus-boost) | [VF2](#vf2)          | [FR WEB Tier 02](#fr-web-tier-02)             |
| [FreeLeech](#freeleech)                | [VFQ](#vfq)          | [FR WEB Tier 03](#fr-web-tier-03)             |
| [HDR10+ Boost](#hdr10plus-boost)       | [VOQ](#voq)          | [FR Anime Tier 01](#fr-anime-tier-01)         |
| [HFR](#hfr)                            | [VQ](#vq)            | [FR Anime Tier 02](#fr-anime-tier-02)         |
| [Internal](#internal)                  | [VFB](#vfb)          | [FR Anime Tier 03](#fr-anime-tier-03)         |
| [MPEG2](#mpeg2)                        | [VOSTFR](#vostfr)    | [FR Anime FanSub](#fr-anime-fansub)           |
| [Multi](#multi)                        | [FanSUB](#fansub)    | [FR Scene Groups](#fr-scene-groups)           |
| [No-RlsGroup](#no-rlsgroup)            | [FastSUB](#fastsub)  | [FR LQ](#fr-lq)                               |
| [Obfuscated](#obfuscated)              |                      |                                               |
| [Repack v2](#repack-v2)                |                      |                                               |
| [Repack v3](#repack-v3)                |                      |                                               |
| [Repack/Proper](#repackproper)         |                      |                                               |
| [Retags](#retags)                      |                      |                                               |
| [Scene](#scene)                        |                      |                                               |
| [SDR (no WEBDL)](#sdr-no-webdl)        |                      |                                               |
| [SDR](#sdr)                            |                      |                                               |
| [Season Packs](#season-pack)           |                      |                                               |
| [VC-1](#vc-1)                          |                      |                                               |
| [VP9](#vp9)                            |                      |                                               |
| [x264](#x264)                          |                      |                                               |
| [x265 (no HDR/DV)](#x265-no-hdrdv)     |                      |                                               |
| [x265](#x265)                          |                      |                                               |
| [x266](#x266)                          |                      |                                               |

---

| Anime Source Groups                                                         | Anime Source Groups                                                   | Anime Misc | Anime Optional                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------- | ------------------------------------- |
| [Anime BD Tier 01 (Top SeaDex Muxers)](#anime-bd-tier-01-top-seadex-muxers) | [Anime Web Tier 01 (Muxers)](#anime-web-tier-01-muxers)               | [v0](#v0)  | [Uncensored](#uncensored)             |
| [Anime BD Tier 02 (SeaDex Muxers)](#anime-bd-tier-02-seadex-muxers)         | [Anime Web Tier 02 (Top FanSubs)](#anime-web-tier-02-top-fansubs)     | [v1](#v1)  | [10bit](#10bit)                       |
| [Anime BD Tier 03 (SeaDex Muxers)](#anime-bd-tier-03-seadex-muxers)         | [Anime Web Tier 03 (Official Subs)](#anime-web-tier-03-official-subs) | [v2](#v2)  | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 04 (SeaDex Muxers)](#anime-bd-tier-04-seadex-muxers)         | [Anime Web Tier 04 (Official Subs)](#anime-web-tier-04-official-subs) | [v3](#v3)  | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 05 (Remuxes)](#anime-bd-tier-05-remuxes)                     | [Anime Web Tier 05 (FanSubs)](#anime-web-tier-05-fansubs)             | [v4](#v4)  |                                       |
| [Anime BD Tier 06 (FanSubs)](#anime-bd-tier-06-fansubs)                     | [Anime Web Tier 06 (FanSubs)](#anime-web-tier-06-fansubs)             |            |                                       |
| [Anime BD Tier 07 (P2P/Scene)](#anime-bd-tier-07-p2pscene)                  | [Anime Raws](#anime-raws)                                             |            |                                       |
| [Anime BD Tier 08 (Mini Encodes)](#anime-bd-tier-08-mini-encodes)           | [Anime LQ Groups](#anime-lq-groups)                                   |            |                                       |

---

| Language profiles                                                |
| ---------------------------------------------------------------- |
| [Language: German DL](#language-german-dl)                       |
| [Language: Not English (English Only)](#language-not-english)    |
| [Language: Not French (French Only)](#language-not-french)       |
| [Language: Not Original (Original Only)](#language-not-original) |
| [Language: Original + French](#language-original-plus-french)    |

---

## Audio Advanced

---

### TrueHD ATMOS

??? question "TrueHD ATMOS - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/truehd-atmos.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS X

??? question "DTS:X - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-x.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-x.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### ATMOS (undefined)

??? question "ATMOS (undefined) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/atmos-undefined.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DDPlus ATMOS

<sub>DDPlus = DD+</sub>

??? question "DD+ ATMOS - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ddplus-atmos.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### TrueHD

??? question "TrueHD - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/truehd.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-HD MA

??? question "DTS-HD MA - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-hd-ma.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FLAC

??? question "FLAC - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/flac.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### PCM

??? question "PCM - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pcm.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-HD HRA

??? question "DTS-HD HRA - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-hd-hra.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-hd-hra.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DDPlus

<sub>Dolby Digital Plus = DD+ = DDPlus</sub>

??? question "DD+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ddplus.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-ES

??? question "DTS-ES - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-es.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS

<sub>DTS = Basic DTS</sub>

??? question "DTS - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dts.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### AAC

??? question "AAC - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/aac.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/aac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DD

<sub>(Basic) Dolby Digital = DD</sub>

??? question "DD - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dd.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### MP3

??? question "MP3 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/mp3.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Opus

??? question "Opus - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/opus.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Audio Channels

---

### 1.0 Mono

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 2.0 Stereo

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 3.0 Sound

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 4.0 Sound

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 5.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 6.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 7.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## HDR Formats

---

### DV HDR10Plus

<sub>DV = DoVi = Dolby Vision</sub><br>
<sub>HDR10+ = HDR10P = HDR10Plus</sub>

??? question "DV HDR10+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dv-hdr10plus.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV HDR10

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV HDR10 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dv-hdr10.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV - [Click to show/hide]"

    --8<-- "includes/cf-descriptions/dv.md"

<!-- the reason why we didn't use here `include-markdown` is because all the headers when using `include-markdown` will be looking in `/includes` and not the current markdown file, in this case, the pointer to `#dv-webdl` in `includes/dv.md`-->

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV HLG

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV HLG - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dv-hlg.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV SDR

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV SDR - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dv-sdr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR10Plus

<sub>HDR10+ = HDR10P = HDR10Plus</sub>

??? question "HDR10+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hdr10plus.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR10

<sub>HDR10</sub>

??? question "HDR10 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hdr10.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR

<sub>HDR</sub>

??? question "HDR - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hdr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR (undefined)

??? question "HDR (undefined) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hdr-undefined.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### PQ

<sub>PQ = PQ10</sub>

??? question "PQ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HLG

<sub>HLG = HLG10</sub>

??? question "HLG - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hlg.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hlg.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Series Versions

---

### Hybrid

??? question "Hybrid - [Click to show/hide]"

    A hybrid release means any combination of sources (video + audio) and not a direct encoding of a single source. Generally, you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hybrid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Remaster

??? question "Remaster - [Click to show/hide]"

    [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}

    For the software term, see Software remastering.
    Remaster (also digital remastering and digitally remastered) refers to changing the quality of the sound or of the image, or both, of previously created recordings, either audiophonic, cinematic, or videographic.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Unwanted

---

### AV1

??? question "AV1 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/av1.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/av1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### BR-DISK

??? question "BR-DISK - [Click to show/hide]"

    This is a custom format to help Sonarr recognize and ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.

    You will need to add the following as a new Custom Format, and when created adjust the scoring in your Quality Profile (`Setting` => `Profiles`) to `-10000`.

    !!! note

        Depending on your renaming scheme Sonarr could potentially match renamed files AFTER they are downloaded and imported as `BR-DISK`,
        This is only a cosmetic annoyance until we come up with another way to solve this,
        Because this Custom Format is used to exclude downloading of BR-DISK, it is still behaving as intended.

        Potential reasons why this is could occurr:

        - Blame the often wrongly used naming of x265 encodes.
        - Sonarr v3/v4 uses dynamic custom formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### LQ

<sub>Low-Quality Releases = LQ</sub>

??? question "LQ - [Click to show/hide]"

    A collection of known Low-Quality groups that are often banned from the top trackers due to their lack of quality releases.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### LQ (Release Title)

<sub>Low-Quality Releases = LQ</sub>

??? question "LQ (Release Title)- [Click to show/hide]"

    A collection of terms seen in the titles of Low-Quality releases that are not captured by using a release group name.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/lq-release-title.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Upscaled

??? question "Upscaled - [Click to show/hide]"

    This custom format is used to prevent Sonarr from grabbing upscaled releases.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/upscaled.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x265 (HD)

<sub>720/1080p no x265 = x265 (720/1080p) = x265 (HD)</sub>

??? question "x265 (HD) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x265-hd-sonarr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-hd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Extras

??? question "Extras - [Click to show/hide]"

    This blocks/ignores Extras (bonus footage, outtakes, etc)

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/extras.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Miscellaneous

---

### Repack/Proper

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack v2

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack v3

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/repack-v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x264

??? question "x264 - [Click to show/hide]"

    x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x264.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x265

??? question "x265 - [Click to show/hide]"

    x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

    This applies to all x265/HEVC releases that are not Remux.

    !!! failure ""

        Please don't forget to read the following [Microsized & Wrong Source](#microsized-wrong-source)

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x266

??? question "x266 - [Click to show/hide]"

    Versatile Video Coding (VVC), also known as H.266, ISO/IEC 23090-3, and MPEG-I Part 3, is a video compression standard finalized on 6 July 2020. [Wikipedia](https://en.wikipedia.org/wiki/Versatile_Video_Coding){:target="_blank" rel="noopener noreferrer"}.

    This applies to all x266/VVC releases that are not Remux.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x266.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### MPEG2

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Multi

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FreeLeech

??? question "FreeLeech - [Click to show/hide]"

    Torrent sites sometimes set a torrent to be freeleech. This means that the download of this torrent will not count towards your quota or ratio. This can be useful when starting a new account or if you do not have the best ratio yet.

    !!! warning

        Keep in mind not all trackers support this option.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/freeleech.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Bad Dual Groups

??? question "Bad dual groups - [Click to show/hide]"

    These groups take the original release and add their language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe is that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as the first track.
    Also they often even translate/rename the release name to Portuguese.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bad-dual-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV (WEBDL)

<sub>DV = DoVi = Dolby Vision</sub>

??? question "DV (WEBDL) - [Click to show/hide]"

    This is a special Custom Format that blocks WEBDLs **with** Dolby Vision but **without** HDR10 fallback.

    You will need to add the following as a new Custom Format, and when created adjust the scoring in your Quality Profile (`Setting` => `Profiles`) to `-10000`.

    This Custom Format works together with the normal [DV](#dv) Custom Format that you would use to prefer Dolby Vision.

    Most WEBDL from Streaming Services don't have the fallback to HDR10. What can result during playback is issues with weird colors (typically a green hue) when you attempt to play it on a non-Dolby Vision-compatible setup.

    Remuxes and Bluray have a fallback to HDR10.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR10Plus Boost

??? question "HDR10+ Boost - [Click to show/hide]"

    Optional. Use this one only if you have a (Samsung) TV that supports HDR10+ and you don't have a Setup that supports DV or you prefer HDR10+.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hdr10plus-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV HDR10Plus Boost

??? question "DV HDR10+ Boost - [Click to show/hide]"

    Optional: use this one if you want to upgrade from DV HDR10 to DV HDR10+ to support the best of both worlds.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-hdr10plus-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### No-RlsGroup

??? question "No-RlsGroup - [Click to show/hide]"

    Some indexers strip out the release group which could result in LQ groups getting a higher score.
    For example, a lot of EVO releases end up stripped of the group name so they appear as "upgrades" and they end up getting a decent score if other things match

    !!! warning

        If you don't use decent filenames (like not adding release groups) don't add this Custom Format, except if you want to upgrade them.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Obfuscated

??? question "Obfuscated - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/obfuscated.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Retags

??? question "Retags - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/retags.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/retags.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Scene

??? question "Scene - [Click to show/hide]"

    This Custom Format will try to recognize so-called "scene releases". Depending on your preferences, you can give it a negative score `-10000`, a positive score, or just skip adding it altogether.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Single Episode

!!! danger "WARNING"

    - This CF utilizes functionality only available starting in Sonarr v4.0.2.1262.

??? question "Single Episode - [Click to show/hide]"

    This Custom Format will recognize single-episode releases, instead of multi-episode or season packs, using Sonarr's built-in parser. Depending on your preference, you can give it a negative or positive score or skip adding it altogether.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/single-episode.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### Multi-Episode

!!! danger "WARNING"

    - This CF utilizes functionality only available in Sonarr v4.0.2.1262 or later.

??? question "Multi-Episode - [Click to show/hide]"

    This Custom Format will recognize multi-episode releases (e.g. episodes named with 'S01E01E02'), instead of single-episode or season packs, using Sonarr's built-in parser. Depending on your preference, you can give it a negative or positive score or skip adding it altogether.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/multi-episode.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### Season Pack

!!! danger "WARNING"

    - This CF utilizes functionality only available starting in Sonarr v4.0.2.1262.

??? question "Season Pack - [Click to show/hide]"

    This Custom Format can be used to prefer or exclude season packs

    - Give it a score of `10` if you prefer a season pack.
    - Give it a score of `-10000` if you prefer to not download season packs.
    - Utilizes the "Release Type" custom format condition added in v4.0.2.1262, Season Pack source status is now persistently stored alongside episodes.

    !!! info

        - This Custom Format could previously result in download loops. The new "Release Type" custom format condition now prevents this undesired behavior. :bangbang:
        - This will upgrade your already downloaded single episodes :bangbang:

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/season-pack.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x265 (no HDR/DV)

??? question "x265 (no HDR/DV) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x265-no-hdrdv-sonarr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/x265-no-hdrdv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VC-1

??? question "VC-1 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vc-1.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vc-1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

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

<sub><sup>[TOP](#index)</sup></sub>

---

### Internal

??? question "Internal - [Click to show/hide]"

    - For those that prefer scene releases may want to boost internals as they generally have higher settings that may not conform to ruleset.
    - In some rare cases P2P use also INTERNAL.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/internal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### SDR

??? question "SDR - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/sdr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### SDR (no WEBDL)

??? question "SDR (no WEBDL) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/sdr-no-webdl-sonarr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sdr-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV (Disk)

??? question "DV (Disk) - [Click to show/hide]"

    - This will boost the score for Dolby Vision Releases using the original full-quality Dolby Vision layer from the disc release to replace the old WEBDL HYBRID release.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dv-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HFR

??? question "HFR - [Click to show/hide]"

    - This will boost the score for HFR releases. HFR stands for High Frame Rate and refers to a video format that uses a higher number of frames per second than traditional video, resulting in smoother and more detailed motion.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## HQ Source Groups

---

### Remux Tier 01

??? question "Remux Tier 01 - [Click to show/hide]"

    Groups that:

    - Have established themselves as consistently delivering high-quality releases.
    - Produce remuxes from multiple sources (discs) and combine them to produce the best end result.
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Remux Tier 02

??? question "Remux Tier 02 - [Click to show/hide]"

    Groups that:

    - Only use one source (poetically dubbed "one disc wonders").
    - Use a fully automated method without double-checking.
    - Don't check/review their releases prior to uploading.
    - Haven't released much. (yet)
    - Have retired and don't have the best quality by today's standards
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

### HD Bluray Tier 01

??? question "HD Bluray Tier 01 - [Click to show/hide]"

    Groups that:

    - Have established themselves as consistently delivering high-quality releases.
    - Use remuxes as their source without micro-sizing them.
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 02

??? question "HD Bluray Tier 02 - [Click to show/hide]"

    Groups that:

    - Use remuxes as their source without micro-sizing them.
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

### WEB Tier 01

??? question "WEB Tier 01 - [Click to show/hide]"

    Groups that:

    - Have established themselves as consistently delivering high-quality releases.
    - Create hybrids.
    - Sign up for the gentleman list on a certain private tracker.
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 02

??? question "WEB Tier 02 - [Click to show/hide]"

    Groups that:

    - Sign up for the gentleman list on a certain private tracker.
    - Have only done a few releases
    - Are not on the list but have a few releases on their name
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 03

??? question "WEB Tier 03 - [Click to show/hide]"

    Groups that:

    - Sign up for the gentleman list on a certain private tracker.
    - Have only done a few releases
    - Are not on the list but have a few releases on their name
    - Follow the [Contributing General Guidelines](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md#general-guidelines){:target="_blank" rel="noopener noreferrer"}.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Scene

??? question "WEB Scene - [Click to show/hide]"

    One of the few scene groups that released quality releases.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/web-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Streaming Services

---

### General Streaming Services

---

#### AMZN

<sub>Amazon Prime Video</sub>

??? question "Amazon Prime Video - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/amzn.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/amzn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ATVP

<sub>Apple TV+</sub>

??? question "Apple TV+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/atvp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/atvp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### CC

<sub>CC = Comedy Central</sub>

??? question "CC - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/cc.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### DCU

<sub>DC Universe (streaming service)</sub>

??? question "DC Universe (streaming service) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dcu.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dcu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### DSNP

<sub>Disney+</sub>

??? question "Disney+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dsnp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dsnp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HMAX

<sub>HBO Max</sub>

??? question "Max (streaming service) aka HBO Max - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hmax.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hmax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HBO

<sub>HBO</sub>

??? question "HBO - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hbo.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hbo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Hulu

<sub>Hulu</sub>

??? question "Hulu - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hulu.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### IT

<sub>iT = iTunes</sub>

??? question "iTunes - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/it.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/it.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Max

<sub>Max (streaming service)</sub>

??? question "Max (streaming service) - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hmax.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/max.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### NF

<sub>Netflix</sub>

??? question "Netflix - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/nf.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### PMTP

<sub>Paramount+</sub>

??? question "Paramount+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pmtp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pmtp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### PCOK

<sub>Peacock TV</sub>

??? question "Peacock TV - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pcok.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/pcok.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### SHO

<sub>SHOWTIME</sub>

??? question "SHOWTIME - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/sho.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/sho.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### STAN

<sub>Stan</sub>

??? question "STAN - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/stan.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/stan.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### SYFY

<sub>Syfy</sub>

??? question "SYFY - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/syfy.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/syfy.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### French Streaming Services

---

#### AUViO

<sub>RTBF</sub>

??? question "AUViO/RTBF - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-auvio.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-auvio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### MyCANAL

<sub>MyCANAL = CANAL+/MyCANAL</sub>

??? question "MyCANAL - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-mycanal.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-mycanal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### SALTO

<sub>SALTO = SⱯLTO</sub>

??? question "SⱯLTO - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-salto.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-salto.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Asian Streaming Services

---

#### FOD

<sub>FOD = Fuji Television On Demand</sub>

??? question "Fuji Television On Demand - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/fod.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fod.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HTSR

<sub>Disney+ Hotstar</sub>

??? question "Disney+ Hotstar - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/htsr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/htsr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### TVer

<sub>TVer</sub>

??? question "TVer - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/tver.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/tver.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### TVING

<sub>TVING</sub>

??? question "TVING - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/tving.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/tving.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### U-NEXT

<sub>U-NEXT</sub>

??? question "U-NEXT - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/u-next.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/u-next.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### VIU

<sub>VIU</sub>

??? question "VIU - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/viu.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/viu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Dutch Streaming Services

---

#### NLZ

<sub>NLZiet</sub>

??? question "NLZiet - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/nlz.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/nlz.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### VDL

<sub>Videoland</sub>

??? question "Videoland - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vdl.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### UK Streaming Services

---

#### 4OD

<sub>4OD</sub>

??? question "4OD - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/all4.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/4od.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ALL4

<sub>ALL4</sub>

??? question "ALL4 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/all4.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/all4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### iP

<sub>BBC iPlayer aka iP</sub>

??? question "BBC iPlayer aka iP - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ip.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ip.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ITVX

<sub>ITVX aka ITV</sub>

??? question "ITVX aka ITV - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/itvx.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/itvx.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### MY5

<sub>MY5 aka Channel 5</sub>

??? question "MY5 aka Channel 5 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/my5.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/my5.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### NOW

<sub>NOW</sub>

??? question "NOW - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/now.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/now.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Misc Streaming Services

---

#### AUBC

<sub>Australian Broadcasting Corporation</sub>

??? question "AUBC - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/aubc.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/aubc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### CBC

<sub>CBC</sub>

??? question "CBC - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/cbc.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cbc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Crav

<sub>Crave</sub>

??? question "CRAVE - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/crav.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/crav.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### DSCP

<sub>Discovery+</sub>

??? question "Discovery+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dscp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dscp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### OViD

<sub>OViD</sub>

??? question "OViD - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ovid.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/ovid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### STRP

<sub>Star+</sub>

??? question "Star+ - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/strp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/strp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### RED

<sub>RED = Youtube Red = Youtube Premium</sub>

??? question "Youtube Red - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/red.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/red.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Qibi

<sub>Quibi</sub>

??? question "Quibi - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/qibi.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/qibi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Streaming Services

---

#### B-Global

??? question "B-Global - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/bglobal.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bglobal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Bilibili

??? question "Bilibili - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/bilibili.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/bilibili.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### CR

<sub>Crunchyroll</sub>

??? question "Crunchyroll - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/cr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/cr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### FUNI

<sub>Funimation</sub>

??? question "Funimation - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/funi.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/funi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HIDIVE

??? question "HIDIVE - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hidive.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/hidive.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### VRV

??? question "VRV - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vrv.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/vrv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ABEMA

??? question "Abema - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/abema.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/abema.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ADN

<sub>ADN = Animation Digital Network</sub>

??? question "ADN - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-adn.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-adn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### WKN

<sub>WKN = Wakanim</sub>

??? question "WKN - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-wkn.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-wkn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Optional Streaming Services

---

#### UHD Streaming Boost

??? question "UHD Streaming Boost - [Click to show/hide]"

    Some streaming services have UHD releases that are generally better than their HD counterparts. The UHD Streaming Boost custom format increases those streaming services' scores appropriately for UHD releases. Use this in conjunction with the regular streaming service custom formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uhd-streaming-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### UHD Streaming Cut

??? question "UHD Streaming Cut - [Click to show/hide]"

    Some streaming services have UHD releases that are generally worse than their HD counterparts. The UHD Streaming Cut custom format decreases those streaming services' scores appropriately for UHD releases. Use this in conjunction with the regular streaming service custom formats.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uhd-streaming-cut.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Anime

---

### Anime BD Tier 01 (Top SeaDex Muxers)

??? question "Anime BD Tier 01 (Top SeaDex Muxers) - [Click to show/hide]"

    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-01-top-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 02 (SeaDex Muxers)

??? question "Anime BD Tier 02 (SeaDex Muxers) - [Click to show/hide]"

    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-02-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 03 (SeaDex Muxers)

??? question "Anime BD Tier 03 (SeaDex Muxers) - [Click to show/hide]"

    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-03-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 04 (SeaDex Muxers)

??? question "Anime BD Tier 04 (SeaDex Muxers) - [Click to show/hide]"

    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-04-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 05 (Remuxes)

??? question "Anime BD Tier 05 (Remuxes) - [Click to show/hide]"

    Groups that are consistent and do Remuxes

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-05-remuxes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 06 (FanSubs)

??? question "Anime BD Tier 06 (FanSubs) - [Click to show/hide]"

    FanSub groups that are consistent

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 07 (P2P/Scene)

??? question "Anime BD Tier 07 (P2P/Scene) - [Click to show/hide]"

    Known P2P and Scene Anime groups

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-07-p2pscene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 08 (Mini Encodes)

??? question "Anime BD Tier 08 (Mini Encodes) - [Click to show/hide]"

    Know groups that do mini-encodes

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-bd-tier-08-mini-encodes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 01 (Muxers)

??? question "Anime Web Tier 01 (Muxers) - [Click to show/hide]"

    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-01-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 02 (Top FanSubs)

??? question "Anime Web Tier 02 (Top FanSubs) - [Click to show/hide]"

    Groups that do the best releases as per SeaDex. They are more consistent and trump others

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-02-top-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 03 (Official Subs)

??? question "Anime Web Tier 03 (Official Subs) - [Click to show/hide]"

    Official sub-groups that tend to be more consistent and release fast

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-03-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 04 (Official Subs)

??? question "Anime Web Tier 04 (Official Subs) - [Click to show/hide]"

    Official sub groups

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-04-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 05 (FanSubs)

??? question "Anime Web Tier 05 (FanSubs) - [Click to show/hide]"

    FanSub groups that are consistent

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-05-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 06 (FanSubs)

??? question "Anime Web Tier 06 (FanSubs) - [Click to show/hide]"

    FanSub groups that are consistent

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-web-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Raws

??? question "Anime Raws - [Click to show/hide]"

    A collection of known groups that release raws

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-raws.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime LQ Groups

??? question "Anime LQ Groups - [Click to show/hide]"

    A collection of known Low-Quality groups.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-lq-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Uncensored

??? question "Uncensored - [Click to show/hide]"

    This CF covers uncensored releases.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/uncensored.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v0

??? question "v0 - [Click to show/hide]"

    CF to cover releases named with v0 which we don't want

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v0.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v1

??? question "v1 - [Click to show/hide]"

    CF to cover v1 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v2

??? question "v2 - [Click to show/hide]"

    CF to cover v2 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v3

??? question "v3 - [Click to show/hide]"

    CF to cover v3 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v4

??? question "v4 - [Click to show/hide]"

    CF to cover v4 releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/v4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 10bit

??? question "10bit - [Click to show/hide]"

    This CF covers 10bit releases

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/10bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Dual Audio

??? question "Anime Dual Audio - [Click to show/hide]"

    This CF covers releases that have Dual Audio

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Dubs Only

??? question "Dubs Only - [Click to show/hide]"

    This CF covers releases that only have Dubs

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/dubs-only.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## French Audio Version

---

### VFF

??? question "VFF - [Click to show/hide]"

    Full French version (dubbing done in France) and French version (normally equivalent to VFQ).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vff.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VOF

??? question "VOF - [Click to show/hide]"

    Original French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vof.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VFI

??? question "VFI - [Click to show/hide]"

    International French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VF2

??? question "VF2 - [Click to show/hide]"

    VF[1-9] or FR[1-9] indicates the number of dubs present (normally VF2 being VFF and VFQ).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vf2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VFQ

??? question "VFQ - [Click to show/hide]"

    Canadian French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VOQ

??? question "VOQ - [Click to show/hide]"

    Quebec Original Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-voq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VQ

??? question "VQ - [Click to show/hide]"

    Quebec Version (strong Quebec accent, ex: The Simpsons movie).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VFB

??? question "VFB - [Click to show/hide]"

    Belgian French Version.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vfb.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VOSTFR

??? question "VOSTFR - [Click to show/hide]"

    Indicates soundtrack in the original language, with French subtitles. It should be noted that SUBFRENCH is included inside this Custom Format. However, SUB often means that the subtitle was embedded inside the picture (hardcoded). French releases tend to mix both, leading to some VOSTFR being labeled as SUBFRENCH and SUBFRENCH as VOSTFR.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-vostfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FanSUB

??? question "FanSUB - [Click to show/hide]"

    Action of subtitling a video for personal and non-professional purposes. The quality of FanSUBs can vary enormously (accuracy of translation, mistakes, etc.) and could lead to so-called FastSUBs.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FastSUB

??? question "FastSUB - [Click to show/hide]"

    FanSUB, but made as quickly as possible, at the expense of quality.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/fastsub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## French HQ Source Groups

---

### FR Remux Tier 01

??? question "Remux Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that produce remuxes from multiple sources (discs) and combine them to produce the best end result.
    - Groups actively doing remuxes from a single source (discs).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR HD Bluray Tier 01

??? question "FR HD Bluray Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that create encodes from remuxes without micro-sizing them.
    - Groups that add the best French audio track to an English release from Tier 01 or 02.
    - Groups that have a minimum of great releases (best encode in its class 1080p and lower).

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 01

??? question "FR WEB Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that get their releases directly from the source.
    - Groups that source and add the French audio track from the source to an English release from Tier 01 or 02.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 02

??? question "FR WEB Tier 02 - [Click to show/hide]"

    - WIP
    - Groups that get their releases directly from the source but are not so active.
    - Groups that source and add the French audio track from the source to an English release.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 03

??? question "FR WEB Tier 03 - [Click to show/hide]"

    - WIP
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups that retired and don't have the best quality by today's standards.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 01

??? question "FR Anime Tier 01 - [Click to show/hide]"

    - WIP
    - Groups that are known to be active and only doing Anime
    - Groups whose releases are at least comparable to SeaDex recommended.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 02

??? question "FR Anime Tier 02 - [Click to show/hide]"

    - WIP
    - Groups that are known to be active and only doing Anime, but with few releases per year.
    - Groups that are known to be active and doing Anime AND other types of releases.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 03

??? question "FR Anime Tier 03 - [Click to show/hide]"

    - WIP
    - Groups with no or little activity that have at some point made an interesting release which is either the only one available (in VOSTFR/MULTi) or still top of its category.
    - Groups that haven't released much or are not well recognized. (yet)
    - Groups doing only anime that have retired (or no longer exist) and may not have the best quality by today's standards.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime FanSub

??? question "FR Anime FanSub - [Click to show/hide]"

    Known good groups that only do FanSub in good quality.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-anime-fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Scene Groups

??? question "FR Scene Groups - [Click to show/hide]"

    Known French Scene groups.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR LQ

<sub>French Low-Quality Releases = FR LQ</sub>

??? question "FR LQ - [Click to show/hide]"

    A collection of known French Low-Quality groups that are often banned from the top trackers due to their lack of quality.

    !!! note

        - Ads/Watermarks = Groups that are known to put ads or watermarks in their releases.
        - Bad/False releases = Groups that are known for lying about their quality, type, or the name of their releases.
        - DeTAG/ReTAG = Detagging or stealing groups.
        - Other reasons = Banned Release Groups.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/french-lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Language Profiles

---

### Language: Not French

<sub>Language: French Only</sub>

??? question "Language: Not French - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-french.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/language-not-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not Original

<sub>Language: Original Only</sub>

??? question "Language: Not Original - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-original.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/language-not-original.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Original Plus French

<sub>Language: Original + French</sub>

??? question "Language: Original + French - [Click to show/hide]"

    Language Specification Original + French

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/language-original-plus-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not English

<sub>Language: English Only</sub>

??? question "Language: Not English - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-english.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/language-not-english.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: German DL

<sub>Language: German + Original</sub>

??? question "Language: German DL - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-german-dl.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/sonarr/cf/language-german-dl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>
