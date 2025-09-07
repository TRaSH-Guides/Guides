# Collection of Custom Formats for Radarr

{! include-markdown "../../includes/starr/cf-not-compatible.md" !}

Below is a collection of what we've come to regard as the most needed and commonly used Custom Formats.
These CFs have been collected from discussions on Discord or created with help from others.

Special thanks to everyone who has helped in the creation and testing of these Custom Formats, my team at TRaSH guides, Team Radarr, and the community.

After requesting with Team Radarr, we now have the option to import/export the Custom Formats in a JSON format. This provides everyone with an easy way to share and use Custom Formats.

We've made 3 guides related to this.

- [How to import Custom Formats](/Radarr/Radarr-import-custom-formats){:target="\_blank" rel="noopener noreferrer"} - Explains how to import the Custom Formats.
- [How to upgrade Custom Formats](/Radarr/Radarr-how-to-update-custom-formats){:target="\_blank" rel="noopener noreferrer"} - Explains how to upgrade your existing Custom Formats.
- [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="\_blank" rel="noopener noreferrer"} - Explains how to make the most use of Custom Formats and shows some specifics of our recommended configuration. You can use these examples to get an idea of how to set up your preferences.

!!! tip

    It also is recommended to change the Propers and Repacks settings in Radarr's `Settings`.

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repackproper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Format scoring and preferences will be fully utilized.

--8<-- "includes/support.md"

---

## INDEX

---

| Audio Formats                         | Audio Channels               | HDR Formats                      | HDR Optional                                 |
| ------------------------------------- | ---------------------------- | -------------------------------- | -------------------------------------------- |
| [TrueHD ATMOS](#truehd-atmos)         | [1.0 Mono](#10-mono)         | [HDR](#hdr)                      | [DV (Disk)](#dv-disk)                        |
| [DTS X](#dts-x)                       | [2.0 Stereo](#20-stereo)     | [DV Boost](#dv-boost)            | [DV (w/o HDR fallback)](#dv-wo-hdr-fallback) |
| [ATMOS (undefined)](#atmos-undefined) | [3.0 Sound](#30-sound)       | [HDR10+ Boost](#hdr10plus-boost) | [SDR](#sdr)                                  |
| [DD+ ATMOS](#ddplus-atmos)            | [4.0 Sound](#40-sound)       |                                  | [SDR (no WEBDL)](#sdr-no-webdl)              |
| [TrueHD](#truehd)                     | [5.1 Surround](#51-surround) |                                  |                                              |
| [DTS-HD MA](#dts-hd-ma)               | [6.1 Surround](#61-surround) |                                  |                                              |
| [DD+](#ddplus)                        | [7.1 Surround](#71-surround) |                                  |                                              |
| [DTS-ES](#dts-es)                     |                              |                                  |                                              |
| [DTS](#dts)                           |                              |                                  |                                              |
| [FLAC](#flac)                         |                              |                                  |                                              |
| [PCM](#pcm)                           |                              |                                  |                                              |
| [DTS-HD HRA](#dts-hd-hra)             |                              |                                  |                                              |
| [AAC](#aac)                           |                              |                                  |                                              |
| [DD](#dd)                             |                              |                                  |                                              |
| [MP3](#mp3)                           |                              |                                  |                                              |
| [Opus](#opus)                         |                              |                                  |                                              |

---

| Movie Versions                                | Unwanted                                        | HQ Release Groups                         |
| --------------------------------------------- | ----------------------------------------------- | ----------------------------------------- |
| [4K Remaster](#4k-remaster)                   | [3D](#3d)                                       | [Remux Tier 01](#remux-tier-01)           |
| [Criterion Collection](#criterion-collection) | [AV1](#av1)                                     | [Remux Tier 02](#remux-tier-02)           |
| [Hybrid](#hybrid)                             | [BR-DISK](#br-disk)                             | [Remux Tier 03](#remux-tier-03)           |
| [IMAX Enhanced](#imax-enhanced)               | [Extras](#extras)                               | [UHD Bluray Tier 01](#uhd-bluray-tier-01) |
| [IMAX](#imax)                                 | [Generated Dynamic HDR](#generated-dynamic-hdr) | [UHD Bluray Tier 02](#uhd-bluray-tier-02) |
| [Masters of Cinema](#masters-of-cinema)       | [LQ](#lq)                                       | [UHD Bluray Tier 03](#uhd-bluray-tier-03) |
| [Open Matte](#open-matte)                     | [LQ (Release Title)](#lq-release-title)         | [HD Bluray Tier 01](#hd-bluray-tier-01)   |
| [Remaster](#remaster)                         | [Sing-Along Versions](#sing-along-versions)     | [HD Bluray Tier 02](#hd-bluray-tier-02)   |
| [Special Edition](#special-edition)           | [Upscaled](#upscaled)                           | [HD Bluray Tier 03](#hd-bluray-tier-03)   |
| [Theatrical Cut](#theatrical-cut)             | [x265 (HD)](#x265-hd)                           | [WEB Tier 01](#web-tier-01)               |
| [Vinegar Syndrome](#vinegar-syndrome)         |                                                 | [WEB Tier 02](#web-tier-02)               |
|                                               |                                                 | [WEB Tier 03](#web-tier-03)               |

---

| General Streaming Services | Asian Streaming Services | Dutch Streaming Services |
| -------------------------- | ------------------------ | ------------------------ |
| [Amazon](#amzn)            | [FOD](#fod)              | [Pathe Thuis](#pathe)    |
| [Apple TV+](#atvp)         | [Disney+ Hotstar](#htsr) | [Videoland](#vdl)        |
| [Bravia Core](#bcore)      | [TVer](#tver)            |                          |
| [Criterion Channel](#crit) | [TVING](#tving)          |                          |
| [Disney+](#dsnp)           | [U-NEXT](#u-next)        |                          |
| [HBO](#hbo)                | [VIU](#viu)              |                          |
| [HBO Max](#hmax)           |                          |                          |
| [Hulu](#hulu)              |                          |                          |
| [iTunes](#it)              |                          |                          |
| [Max](#max)                |                          |                          |
| [Movies Anywhere](#ma)     |                          |                          |
| [Netflix](#nf)             |                          |                          |
| [Peacock TV](#pcok)        |                          |                          |
| [Paramount+](#pmtp)        |                          |                          |
| [Stan](#stan)              |                          |                          |

| UK Streaming Services | Misc Streaming Services | Anime Streaming Services |
| --------------------- | ----------------------- | ------------------------ |
| [BBC iPlayer](#ip)    | [AUBC](#aubc)           | [VRV](#vrv)              |
| [ITVX](#itvx)         | [CBC](#cbc)             |                          |
| [MY5](#my5)           | [Crave](#crav)          |                          |
| [NOW](#now)           | [OViD](#ovid)           |                          |
|                       | [Star+](#strp)          |                          |

---

| Miscellaneous                                         | Language profiles                                                  |
| ----------------------------------------------------- | ------------------------------------------------------------------ |
| [720p](#720p)                                         | [Language: German](#language-german)                               |
| [1080p](#1080p)                                       | [Language: German DL](#language-german-dl)                         |
| [2160p](#2160p)                                       | [Language: German DL (undefined)](#language-german-dl-undefined)   |
| [Bad Dual Groups](#bad-dual-groups)                   | [Language: Not English (English Only)](#language-not-english)      |
| [Black and White Editions](#black-and-white-editions) | [Language: Not French (French Only)](#language-not-french)         |
| [Dutch Groups](#dutch-groups)                         | [Language: Not Original (Original Only)](#language-not-original)   |
| [FreeLeech](#freeleech)                               | [Language: Original + French](#language-original-plus-french)      |
| [HFR](#hfr)                                           | [Language: Not German or English](#language-not-german-or-english) |
| [Internal](#internal)                                 |                                                                    |
| [MPEG2](#mpeg2)                                       |                                                                    |
| [Multi](#multi)                                       |                                                                    |
| [No-RlsGroup](#no-rlsgroup)                           |                                                                    |
| [Obfuscated](#obfuscated)                             |                                                                    |
| [Repack/Proper](#repackproper)                        |                                                                    |
| [Repack2](#repack2)                                   |                                                                    |
| [Repack3](#repack3)                                   |                                                                    |
| [Retags](#retags)                                     |                                                                    |
| [Scene](#scene)                                       |                                                                    |
| [VC-1](#vc-1)                                         |                                                                    |
| [VP9](#vp9)                                           |                                                                    |
| [x264](#x264)                                         |                                                                    |
| [x265 (no HDR/DV)](#x265-no-hdrdv)                    |                                                                    |
| [x265](#x265)                                         |                                                                    |
| [x266](#x266)                                         |                                                                    |

---

| Anime                                                                       | Anime                                                                 | Anime     | Anime Optional                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------- | ------------------------------------- |
| [Anime BD Tier 01 (Top SeaDex Muxers)](#anime-bd-tier-01-top-seadex-muxers) | [Anime Web Tier 01 (Muxers)](#anime-web-tier-01-muxers)               | [v0](#v0) | [Uncensored](#uncensored)             |
| [Anime BD Tier 02 (SeaDex Muxers)](#anime-bd-tier-02-seadex-muxers)         | [Anime Web Tier 02 (Top FanSubs)](#anime-web-tier-02-top-fansubs)     | [v1](#v1) | [10bit](#10bit)                       |
| [Anime BD Tier 03 (SeaDex Muxers)](#anime-bd-tier-03-seadex-muxers)         | [Anime Web Tier 03 (Official Subs)](#anime-web-tier-03-official-subs) | [v2](#v2) | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 04 (SeaDex Muxers)](#anime-bd-tier-04-seadex-muxers)         | [Anime Web Tier 04 (Official Subs)](#anime-web-tier-04-official-subs) | [v3](#v3) | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 05 (Remuxes)](#anime-bd-tier-05-remuxes)                     | [Anime Web Tier 05 (FanSubs)](#anime-web-tier-05-fansubs)             | [v4](#v4) |                                       |
| [Anime BD Tier 06 (FanSubs)](#anime-bd-tier-06-fansubs)                     | [Anime Web Tier 06 (FanSubs)](#anime-web-tier-06-fansubs)             |           |                                       |
| [Anime BD Tier 07 (P2P/Scene)](#anime-bd-tier-07-p2pscene)                  | [Anime Raws](#anime-raws)                                             |           |                                       |
| [Anime BD Tier 08 (Mini Encodes)](#anime-bd-tier-08-mini-encodes)           | [Anime LQ Groups](#anime-lq-groups)                                   |           |                                       |

---

| German Source Groups                            | German Miscellaneous                                  | French Source Groups                            | French Audio Version |
| ----------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------- | -------------------- |
| [German Remux Tier 01](#german-remux-tier-01)   | [German LQ](#german-lq)                               | [FR Remux Tier 01](#fr-remux-tier-01)           | [VFF](#vff)          |
| [German Remux Tier 02](#german-remux-tier-02)   | [German LQ (Release Title)](#german-lq-release-title) | [FR Remux Tier 02](#fr-remux-tier-02)           | [VOF](#vof)          |
| [German Bluray Tier 01](#german-bluray-tier-01) | [German Microsized](#german-microsized)               | [FR UHD Bluray Tier 01](#fr-uhd-bluray-tier-01) | [VFI](#vfi)          |
| [German Bluray Tier 02](#german-bluray-tier-02) | [German 1080p Booster](#german-1080p-booster)         | [FR UHD Bluray Tier 02](#fr-uhd-bluray-tier-02) | [VF2](#vf2)          |
| [German Bluray Tier 03](#german-bluray-tier-03) | [German 2160p Booster](#german-2160p-booster)         | [FR HD Bluray Tier 01](#fr-hd-bluray-tier-01)   | [VFQ](#vfq)          |
| [German Web Tier 01](#german-web-tier-01)       | [Line/Mic Dubbed](#linemic-dubbed)                    | [FR HD Bluray Tier 02](#fr-hd-bluray-tier-02)   | [VOQ](#voq)          |
| [German Web Tier 02](#german-web-tier-02)       |                                                       | [FR WEB Tier 01](#fr-web-tier-01)               | [VQ](#vq)            |
| [German Web Tier 03](#german-web-tier-03)       |                                                       | [FR WEB Tier 02](#fr-web-tier-02)               | [VFB](#vfb)          |
| [German Scene](#german-scene)                   |                                                       | [FR Anime Tier 01](#fr-anime-tier-01)           | [VOSTFR](#vostfr)    |
|                                                 |                                                       | [FR Anime Tier 02](#fr-anime-tier-02)           | [FanSUB](#fansub)    |
|                                                 |                                                       | [FR Anime Tier 03](#fr-anime-tier-03)           | [FastSUB](#fastsub)  |
|                                                 |                                                       | [FR Anime FanSub](#fr-anime-fansub)             |                      |
|                                                 |                                                       | [FR Scene Groups](#fr-scene-groups)             |                      |
|                                                 |                                                       | [FR LQ](#fr-lq)                                 |                      |

---

## Audio Formats

---

### TrueHD ATMOS

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/truehd-atmos.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/truehd-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS X

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-x.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-x.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### ATMOS (undefined)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/atmos-undefined.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/atmos-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DDPlus ATMOS

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ddplus-atmos.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ddplus-atmos.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### TrueHD

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/truehd.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/truehd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-HD MA

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-hd-ma.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-hd-ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FLAC

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/flac.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/flac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### PCM

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pcm.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pcm.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-HD HRA

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-hd-hra.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-hd-hra.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DDPlus

<sub>Dolby Digital Plus = DD+ = DDPlus</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ddplus.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ddplus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-ES

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts-es.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts-es.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS

<sub>DTS = Basic DTS</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dts.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dts.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### AAC

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/aac.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/aac.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DD

<sub>(Basic) Dolby Digital = DD</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dd.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### MP3

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/mp3.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/mp3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Opus

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/opus.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/opus.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Audio Channels

---

### 1.0 Mono

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/10-mono.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 2.0 Stereo

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/20-stereo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 3.0 Sound

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/30-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 4.0 Sound

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/40-sound.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 5.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/51-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 6.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/61-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 7.1 Surround

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/71-surround.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## HDR Formats

---

### HDR

<sub>HDR</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hdr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV-Boost

<sub>DV = DoVi = Dolby Vision</sub>

??? question "Description - [Click to show/hide]"

    --8<-- "includes/cf-descriptions/dv-boost.md"

<!-- the reason why we didn't use here `include-markdown` is because all the headers when using `include-markdown` will be looking in `/includes` and not the current markdown file, in this case, the pointer to `#dv-wo-hdr-fallback` in `includes/dv.md` -->

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR10Plus Boost

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hdr10plus-boost.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hdr10plus-boost.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## HDR Optional

---

### DV (Disk)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dv-disk.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### DV (w/o HDR fallback)

<sub>DV = DoVi = Dolby Vision</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dv-wo-hdr-fallback.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dv-wo-hdr-fallback.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### SDR

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/sdr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/sdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### SDR (no WEBDL)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/sdr-no-webdl-radarr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/sdr-no-webdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Movie Versions

---

### Hybrid

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hybrid.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hybrid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Remaster

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/remaster.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 4K Remaster

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/4k-remaster.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/4k-remaster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Criterion Collection

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/criterion-collection.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/criterion-collection.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Masters of Cinema

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/masters-of-cinema.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/masters-of-cinema.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Vinegar Syndrome

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vinegar-syndrome.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/vinegar-syndrome.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Theatrical Cut

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/theatrical-cut.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/theatrical-cut.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Special Edition

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/special-edition.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/special-edition.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### IMAX

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/imax.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/imax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### IMAX Enhanced

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/imax-enhanced.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/imax-enhanced.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Open Matte

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/open-matte.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/open-matte.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Unwanted

---

### AV1

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/av1.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/av1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### BR-DISK

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/br-disk.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/br-disk.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Generated Dynamic HDR

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/generated-dynamic-hdr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/generated-dynamic-hdr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### LQ

<sub>Low-Quality Releases = LQ</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/lq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### LQ (Release Title)

<sub>Low-Quality Releases = LQ</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/lq-release-title.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/lq-release-title.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Sing-Along Versions

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/sing-along-versions.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/sing-along-versions.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 3D

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/3d.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/3d.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x265 (HD)

<sub>720/1080p no x265 = x265 (720/1080p) = x265 (HD)</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x265-hd-radarr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x265-hd.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Upscaled

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/upscaled.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/upscaled.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Extras

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/extras.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/extras.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Miscellaneous

---

### 720p

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/720p.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/720p.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 1080p

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/1080p.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/1080p.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 2160p

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/2160p.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/2160p.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Bad Dual Groups

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/bad-dual-groups.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/bad-dual-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Black and White Editions

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/black-and-white-editions.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/black-and-white-editions.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### No-RlsGroup

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/no-rlsgroup.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/no-rlsgroup.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Obfuscated

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/obfuscated.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/obfuscated.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Retags

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/retags.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/retags.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Scene

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/scene.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x265 (no HDR/DV)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x265-no-hdrdv-radarr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x265-no-hdrdv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VC-1

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vc-1.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/vc-1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VP9

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vp9.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/vp9.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Internal

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/internal.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/internal.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Line/Mic Dubbed

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/line-mic-dubbed.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/line-mic-dubbed.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HFR

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hfr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack/Proper

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/repack-proper.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack2

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/repack2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack3

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/repack3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x264

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x264.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x264.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x265

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x265.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x265.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### x266

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/x266.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/x266.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FreeLeech

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/freeleech.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/freeleech.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Dutch Groups

??? question "Description - [Click to show/hide]"

    If you prefer movies with also a Dutch audio track.

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dutch-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### MPEG2

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/mpeg2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Multi

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/multi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## HQ Release Groups

---

### Remux Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/remux-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Remux Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/remux-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Remux Tier 03

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/remux-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/remux-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### UHD Bluray Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/uhd-bluray-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uhd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### UHD Bluray Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/uhd-bluray-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uhd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### UHD Bluray Tier 03

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/uhd-bluray-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uhd-bluray-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hd-bluray-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hd-bluray-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 03

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hd-bluray-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hd-bluray-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/web-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/web-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 03

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/web-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Streaming Services

---

### General Streaming Services

#### AMZN

<sub>Amazon Prime Video</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/amzn.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/amzn.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ATVP

<sub>Apple TV+</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/atvp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/atvp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### BCORE

<sub>Bravia Core</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/bcore.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/bcore.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### CRiT

<sub>Criterion Channel</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/crit.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/crit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### DSNP

<sub>Disney+</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dsnp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dsnp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HBO

<sub>HBO</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hbo.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hbo.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HMAX

<sub>HBO Max</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hmax.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hmax.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Hulu

<sub>Hulu</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hulu.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/hulu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### IT

<sub>iT = iTunes</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/it.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/it.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Max

<sub>Max (streaming service)</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/hmax.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/max.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### MA

<sub>Movies Anywhere</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ma.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ma.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### NF

<sub>Netflix</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/nf.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/nf.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### PCOK

<sub>Peacock TV</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pcok.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pcok.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### PMTP

<sub>Paramount+</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pmtp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pmtp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### STAN

<sub>Stan</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/stan.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/stan.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Asian Streaming Services

---

#### FOD

<sub>FOD = Fuji Television On Demand</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/fod.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/fod.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### HTSR

<sub>Disney+ Hotstar</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/htsr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/htsr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### TVer

<sub>TVer</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/tver.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/tver.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### TVING

<sub>TVING</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/tving.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/tving.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### U-NEXT

<sub>U-NEXT</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/u-next.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/u-next.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### VIU

<sub>VIU</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/viu.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/viu.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Dutch Streaming Services

---

#### Pathe

<sub>Pathé Thuis</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/pathe.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/pathe.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### VDL

<sub>Videoland</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vdl.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/vdl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### UK Streaming Services

---

#### iP

<sub>BBC iPlayer aka iP</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ip.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ip.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### ITVX

<sub>ITVX aka ITV</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/itvx.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/itvx.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### MY5

<sub>MY5 aka Channel 5</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/my5.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/my5.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### NOW

<sub>NOW</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/now.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/now.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Misc Streaming Services

---

#### AUBC

<sub>Australian Broadcasting Corporation</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/aubc.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/aubc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### CBC

<sub>CBC</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/cbc.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/cbc.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### Crav

<sub>Crave</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/crav.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/crav.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### OViD

<sub>OViD</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/ovid.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/ovid.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

#### STRP

<sub>Star+</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/strp.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/strp.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Streaming Services

---

#### VRV

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/vrv.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/vrv.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Anime

---

### Anime BD Tier 01 (Top SeaDex Muxers)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-01-top-seadex-muxers.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-01-top-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 02 (SeaDex Muxers)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-02-seadex-muxers.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-02-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 03 (SeaDex Muxers)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-03-seadex-muxers.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-03-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 04 (SeaDex Muxers)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-04-seadex-muxers.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-04-seadex-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 05 (Remuxes)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-05-remuxes.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-05-remuxes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 06 (FanSubs)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-06-fansubs.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 07 (P2P/Scene)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-07-p2pscene.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-07-p2pscene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 08 (Mini Encodes)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-bd-tier-08-mini-encodes.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-bd-tier-08-mini-encodes.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 01 (Muxers)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-web-tier-01-muxers.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-01-muxers.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 02 (Top FanSubs)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-web-tier-02-top-fansubs.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-02-top-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 03 (Official Subs)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-web-tier-03-official-subs.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-03-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 04 (Official Subs)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-web-tier-04-official-subs.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-04-official-subs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 05 (FanSubs)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-web-tier-05-fansubs.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-05-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 06 (FanSubs)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-web-tier-06-fansubs.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-web-tier-06-fansubs.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Raws

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-raws.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-raws.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime LQ Groups

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-lq-groups.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-lq-groups.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Uncensored

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/uncensored.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/uncensored.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v0

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/v0.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v0.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v1

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/v1.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v1.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v2

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/v2.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v3

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/v3.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v3.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### v4

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/v4.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/v4.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### 10bit

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/10bit.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/10bit.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Dual Audio

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/anime-dual-audio.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/anime-dual-audio.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Dubs Only

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/dubs-only.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/dubs-only.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## French Audio Version

---

### VFF

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vff.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vff.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VOF

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vof.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vof.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VFI

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vfi.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vfi.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VF2

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vf2.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vf2.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VFQ

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vfq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vfq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VOQ

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-voq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-voq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VQ

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VFB

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vfb.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vfb.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### VOSTFR

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-vostfr.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-vostfr.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FanSUB

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/fansub.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FastSUB

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/fastsub.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/fastsub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## French HQ Source Groups

---

### FR Remux Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-remux-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Remux Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-remux-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR UHD Bluray Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-uhd-bluray-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-uhd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR UHD Bluray Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-uhd-bluray-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-uhd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR HD Bluray Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-hd-bluray-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-hd-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR HD Bluray Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-hd-bluray-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-hd-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-web-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-web-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 01

??? question "FR Anime Tier 01 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-anime-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-anime-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 02

??? question "FR Anime Tier 02 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-anime-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-anime-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 03

??? question "FR Anime Tier 03 - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-anime-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-anime-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime FanSub

??? question "FR Anime FanSub - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-anime-fansub.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-anime-fansub.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Scene Groups

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-scene.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### FR LQ

<sub>French Low-Quality Releases = FR LQ</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/french-lq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/french-lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## German Source Groups

---

### German Remux Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-remux-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-remux-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Remux Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-remux-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-remux-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Bluray Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-bluray-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-bluray-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Bluray Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-bluray-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-bluray-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Bluray Tier 03

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-bluray-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-bluray-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Web Tier 01

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-web-tier-01.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-web-tier-01.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Web Tier 02

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-web-tier-02.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-web-tier-02.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Web Tier 03

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-web-tier-03.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-web-tier-03.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Scene

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-scene.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-scene.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## German Miscellaneous

---

### German LQ

<sub>German Low-Quality Releases = German LQ</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-lq.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-lq.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German LQ (Release Title)

<sub>Low-Quality Releases = LQ</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-lq-release-title.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-lq-release-title.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German Microsized

<sub>German Microsized Releases = German Microsized</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-microsized.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-microsized.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German 1080p Booster

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-1080p-booster.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-1080p-booster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### German 2160p Booster

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/german-2160p-booster.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/german-2160p-booster.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

## Language Profiles

---

### Language: Not French

<sub>Language: French Only</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-french.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-not-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not Original

<sub>Language: Original Only</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-original.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-not-original.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Original Plus French

<sub>Language: Original + French</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-original-plus-french.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-original-plus-french.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not English

<sub>Language: English Only</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-english.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-not-english.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: German DL

<sub>Language: German + Original</sub>

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-german-dl.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-german-dl.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: German DL (undefined)

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-german-dl-undefined.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-german-dl-undefined.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: German

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-german.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-german.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not German or English

??? question "Description - [Click to show/hide]"

    {! include-markdown "../../includes/cf-descriptions/language-not-german-or-english.md" !}

??? example "JSON - [Click to show/hide]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/radarr/cf/language-not-german-or-english.json' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup></sub>
