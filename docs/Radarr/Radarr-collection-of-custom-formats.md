# Collection of Custom Formats for Radarr

<!--@include: ../../includes/starr/cf-not-compatible.md-->

Below is a collection of what we've come to regard as the most needed and commonly used Custom Formats.
These CFs have been collected from discussions on Discord or created with help from others.

Special thanks to everyone who has helped in the creation and testing of these Custom Formats, my team at TRaSH guides, Team Radarr, and the community.

After requesting with Team Radarr, we now have the option to import/export the Custom Formats in a JSON format. This provides everyone with an easy way to share and use Custom Formats.

We've made 3 guides related to this.

- [How to import Custom Formats](/Radarr/Radarr-import-custom-formats) - Explains how to import the Custom Formats.
- [How to upgrade Custom Formats](/Radarr/Radarr-how-to-update-custom-formats) - Explains how to upgrade your existing Custom Formats.
- [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles) - Explains how to make the most use of Custom Formats and shows some specifics of our recommended configuration. You can use these examples to get an idea of how to set up your preferences.

::: tip

It also is recommended to change the Propers and Repacks settings in Radarr's `Settings`.

`Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repackproper) Custom Format.

![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

This way you make sure the Custom Format scoring and preferences will be fully utilized.

:::

<!--@include: ../../includes/support.md-->

---

## INDEX

---

| Audio Formats                         | Audio Channels               | HDR Formats                      | HDR Formats (Optional)                       |
|---------------------------------------|------------------------------|----------------------------------|----------------------------------------------|
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

| Streaming Services General | Streaming Services Asian  | Streaming Services Dutch |
|----------------------------|---------------------------|--------------------------|
| [Amazon](#amzn)            | [Coupang Play](#cpng)     | [Pathe Thuis](#pathe)    |
| [Apple TV](#atv)           | [Disney+ Hotstar](#htsr)  | [Videoland](#vdl)        |
| [Apple TV+](#atvp)         | [friDay Video](#friday)   |                          |
| [Bravia Core](#bcore)      | [Fuji-TV On Demand](#fod) |                          |
| [Criterion Channel](#crit) | [Hami Video](#hami)       |                          |
| [Disney+](#dsnp)           | [iQIYI](#iqiy)            |                          |
| [Google Play](#play)       | [KKTV](#kktv)             |                          |
| [HBO](#hbo)                | [KOCOWA](#kcw)            |                          |
| [HBO Max](#hmax)           | [LINE TV](#linetv)        |                          |
| [Hulu](#hulu)              | [myTV SUPER](#mytvsuper)  |                          |
| [iTunes](#it)              | [TVING](#tving)           |                          |
| [Max](#max)                | [TVer](#tver)             |                          |
| [Movies Anywhere](#ma)     | [U-NEXT](#u-next)         |                          |
| [Netflix](#nf)             | [Viki](#viki)             |                          |
| [Paramount+](#pmtp)        | [VIU](#viu)               |                          |
| [Peacock TV](#pcok)        | [Wavve](#wavve)           |                          |
| [ROKU](#roku)              | [WeTV](#wetv)             |                          |
| [Stan](#stan)              | [Youku](#youku)           |                          |
|                            |                           |                          |

| Streaming Services Misc | Streaming Services UK | Streaming Services Anime |
|-------------------------|-----------------------|--------------------------|
| [AUBC](#aubc)           | [BBC iPlayer](#ip)    | [Funimation](#funi)      |
| [Canal+](#cnlp)         | [ITVX](#itvx)         | [VRV](#vrv)              |
| [CBC](#cbc)             | [MY5](#my5)           |                          |
| [Crave](#crav)          | [NOW](#now)           |                          |
| [Fandango](#fah)        |                       |                          |
| [OViD](#ovid)           |                       |                          |
| [Star+](#strp)          |                       |                          |

---

| Movie Versions (Optional)                     | Unwanted Formats                                      | HQ Release Groups                         |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------|
| [4K Remaster](#4k-remaster)                   | [3D](#3d)                                             | [Remux Tier 01](#remux-tier-01)           |
| [Criterion Collection](#criterion-collection) | [AV1](#av1)                                           | [Remux Tier 02](#remux-tier-02)           |
| [Hybrid](#hybrid)                             | [Bad Dual Groups](#bad-dual-groups)                   | [Remux Tier 03](#remux-tier-03)           |
| [IMAX](#imax)                                 | [Black and White Editions](#black-and-white-editions) | [UHD Bluray Tier 01](#uhd-bluray-tier-01) |
| [IMAX Enhanced](#imax-enhanced)               | [BR-DISK](#br-disk)                                   | [UHD Bluray Tier 02](#uhd-bluray-tier-02) |
| [Masters of Cinema](#masters-of-cinema)       | [Extras](#extras)                                     | [UHD Bluray Tier 03](#uhd-bluray-tier-03) |
| [Open Matte](#open-matte)                     | [Generated Dynamic HDR](#generated-dynamic-hdr)       | [HD Bluray Tier 01](#hd-bluray-tier-01)   |
| [Remaster](#remaster)                         | [Line/Mic Dubbed](#linemic-dubbed)                    | [HD Bluray Tier 02](#hd-bluray-tier-02)   |
| [Special Edition](#special-edition)           | [LQ](#lq)                                             | [HD Bluray Tier 03](#hd-bluray-tier-03)   |
| [Theatrical Cut](#theatrical-cut)             | [LQ (Release Title)](#lq-release-title)               | [WEB Tier 01](#web-tier-01)               |
| [Vinegar Syndrome](#vinegar-syndrome)         | [No-RlsGroup](#no-rlsgroup)                           | [WEB Tier 02](#web-tier-02)               |
|                                               | [Obfuscated](#obfuscated)                             | [WEB Tier 03](#web-tier-03)               |
|                                               | [Retags](#retags)                                     |                                           |
|                                               | [Scene](#scene)                                       |                                           |
|                                               | [Sing-Along Versions](#sing-along-versions)           |                                           |
|                                               | [Upscaled](#upscaled)                                 |                                           |

---

| Repacks/Proper (Required)      | Golden Rule (Optional)             | Miscellaneous (Optional)      | Resolution (Optional) |
|--------------------------------|------------------------------------|-------------------------------|-----------------------|
| [Repack/Proper](#repackproper) | [x265 (no HDR/DV)](#x265-no-hdrdv) | [FreeLeech](#freeleech)       | [720p](#720p)         |
| [Repack2](#repack2)            | [x265 (HD)](#x265-hd)              | [HFR](#hfr)                   | [1080p](#1080p)       |
| [Repack3](#repack3)            |                                    | [Internal](#internal)         | [2160p](#2160p)       |
|                                |                                    | [MPEG2](#mpeg2)               |                       |
|                                |                                    | [Multi](#multi)               |                       |
|                                |                                    | [P2P Internal](#p2p-internal) |                       |
|                                |                                    | [VC-1](#vc-1)                 |                       |
|                                |                                    | [VP9](#vp9)                   |                       |
|                                |                                    | [x264](#x264)                 |                       |
|                                |                                    | [x265](#x265)                 |                       |
|                                |                                    | [x266](#x266)                 |                       |

---

| Language profiles (Optional)                                                                       | Accessibility (Optional) |
|----------------------------------------------------------------------------------------------------|--------------------------|
| [German](#german)                                                                                  | [WiTH AD](#with-ad)      |
| [German DL](#german-dl)                                                                            | [WiTH ASL](#with-asl)    |
| [German DL (undefined)](#german-dl-undefined)                                                      | [WiTH BASL](#with-basl)  |
| [Language: Not English (English Only)](#language-not-english)                                      | [WiTH BSL](#with-bsl)    |
| [Language: Not French (French Only)](#language-not-french)                                         |                          |
| [Language: Not Original (Original Only)](#language-not-original)                                   |                          |
| [Language: Original + French](#language-original-plus-french)                                      |                          |
| [Not German or English](#not-german-or-english)                                                    |                          |
| [Not German, Japanese or English](#not-german-japanese-or-english)                                 |                          |
| [Not German, Japanese, Korean, Chinese or English](#not-german-japanese-korean-chinese-or-english) |                          |
| [Wrong Language](#wrong-language)                                                                  |                          |

---

| Anime Release Groups                  | Anime Release Groups                    | Anime Versions | Anime Optional                        |
|---------------------------------------|-----------------------------------------|----------------|---------------------------------------|
| [Anime BD Tier 01](#anime-bd-tier-01) | [Anime Web Tier 01](#anime-web-tier-01) | [v0](#v0)      | [10bit](#10bit)                       |
| [Anime BD Tier 02](#anime-bd-tier-02) | [Anime Web Tier 02](#anime-web-tier-02) | [v1](#v1)      | [Anime Dual Audio](#anime-dual-audio) |
| [Anime BD Tier 03](#anime-bd-tier-03) | [Anime Web Tier 03](#anime-web-tier-03) | [v2](#v2)      | [Dubs Only](#dubs-only)               |
| [Anime BD Tier 04](#anime-bd-tier-04) | [Anime Web Tier 04](#anime-web-tier-04) | [v3](#v3)      | [Uncensored](#uncensored)             |
| [Anime BD Tier 05](#anime-bd-tier-05) | [Anime Web Tier 05](#anime-web-tier-05) | [v4](#v4)      |                                       |
| [Anime BD Tier 06](#anime-bd-tier-06) | [Anime Web Tier 06](#anime-web-tier-06) |                |                                       |
| [Anime BD Tier 07](#anime-bd-tier-07) | [Anime Raws](#anime-raws)               |                |                                       |
| [Anime BD Tier 08](#anime-bd-tier-08) | [Anime LQ Groups](#anime-lq-groups)     |                |                                       |

---

| German Release Groups                           | German Anime Release Groups                                 | German Miscellaneous                          | German Unwanted                                       |
|-------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------------|
| [German Remux Tier 01](#german-remux-tier-01)   | [German Anime Bluray Tier 01](#german-anime-bluray-tier-01) | [German 1080p Booster](#german-1080p-booster) | [German LQ](#german-lq)                               |
| [German Remux Tier 02](#german-remux-tier-02)   | [German Anime Bluray Tier 02](#german-anime-bluray-tier-02) | [German 2160p Booster](#german-2160p-booster) | [German LQ (Release Title)](#german-lq-release-title) |
| [German Bluray Tier 01](#german-bluray-tier-01) | [German Anime Bluray Tier 03](#german-anime-bluray-tier-03) | [German Subbed](#german-subbed)               | [German Microsized](#german-microsized)               |
| [German Bluray Tier 02](#german-bluray-tier-02) | [German Anime Web Tier 01](#german-anime-web-tier-01)       |                                               |                                                       |
| [German Bluray Tier 03](#german-bluray-tier-03) | [German Anime Web Tier 02](#german-anime-web-tier-02)       |                                               |                                                       |
| [German Web Tier 01](#german-web-tier-01)       | [German Anime Web Tier 03](#german-anime-web-tier-03)       |                                               |                                                       |
| [German Web Tier 02](#german-web-tier-02)       | [German Anime Scene](#german-anime-scene)                   |                                               |                                                       |
| [German Web Tier 03](#german-web-tier-03)       |                                                             |                                               |                                                       |
| [German Scene](#german-scene)                   |                                                             |                                               |                                                       |

---

| French Release Groups                           | French Anime Release Groups             | French Audio Version |
|-------------------------------------------------|-----------------------------------------|----------------------|
| [FR Remux Tier 01](#fr-remux-tier-01)           | [FR Anime Tier 01](#fr-anime-tier-01)   | [VFF](#vff)          |
| [FR Remux Tier 02](#fr-remux-tier-02)           | [FR Anime Tier 02](#fr-anime-tier-02)   | [VOF](#vof)          |
| [FR UHD Bluray Tier 01](#fr-uhd-bluray-tier-01) | [FR Anime Tier 03](#fr-anime-tier-03)   | [VFI](#vfi)          |
| [FR UHD Bluray Tier 02](#fr-uhd-bluray-tier-02) | [FR Anime FanSub](#fr-anime-fansub)     | [VF2](#vf2)          |
| [FR HD Bluray Tier 01](#fr-hd-bluray-tier-01)   |                                         | [VFQ](#vfq)          |
| [FR HD Bluray Tier 02](#fr-hd-bluray-tier-02)   |                                         | [VOQ](#voq)          |
| [FR WEB Tier 01](#fr-web-tier-01)               |                                         | [VQ](#vq)            |
| [FR WEB Tier 02](#fr-web-tier-02)               |                                         | [VFB](#vfb)          |
| [FR Scene Groups](#fr-scene-groups)             |                                         | [VOSTFR](#vostfr)    |
| [FR LQ](#fr-lq)                                 |                                         | [FanSUB](#fansub)    |
|                                                 |                                         | [FastSUB](#fastsub)  |

---

## Audio Formats

---

### TrueHD ATMOS

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/truehd-atmos.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/truehd-atmos.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS X

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dts-x.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dts-x.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### ATMOS (undefined)

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/atmos-undefined.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/atmos-undefined.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DDPlus ATMOS

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/ddplus-atmos.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/ddplus-atmos.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### TrueHD

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/truehd.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/truehd.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-HD MA

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dts-hd-ma.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dts-hd-ma.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FLAC

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/flac.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/flac.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### PCM

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/pcm.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/pcm.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-HD HRA

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dts-hd-hra.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dts-hd-hra.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DDPlus

<sub>Dolby Digital Plus = DD+ = DDPlus</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/ddplus.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/ddplus.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS-ES

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dts-es.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dts-es.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DTS

<sub>DTS = Basic DTS</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dts.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dts.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### AAC

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/aac.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/aac.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DD

<sub>(Basic) Dolby Digital = DD</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dd.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dd.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### MP3

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/mp3.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/mp3.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Opus

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/opus.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/opus.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Audio Channels

---

### 1.0 Mono

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/10-mono.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 2.0 Stereo

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/20-stereo.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 3.0 Sound

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/30-sound.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 4.0 Sound

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/40-sound.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 5.1 Surround

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/51-surround.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 6.1 Surround

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/61-surround.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 7.1 Surround

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/71-surround.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## HDR Formats

---

### HDR

<sub>HDR</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hdr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hdr.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DV-Boost

<sub>DV = DoVi = Dolby Vision</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dv-boost.md-->

:::

<!-- the reason why we didn't use here `include-markdown` is because all the headers when using `include-markdown` will be looking in `/includes` and not the current markdown file, in this case, the pointer to `#dv-wo-hdr-fallback` in `includes/dv.md` -->

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dv-boost.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### HDR10Plus Boost

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hdr10plus-boost.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hdr10plus-boost.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## HDR Optional

---

### DV (Disk)

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dv-disk.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dv-disk.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### DV (w/o HDR fallback)

<sub>DV = DoVi = Dolby Vision</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dv-wo-hdr-fallback.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dv-wo-hdr-fallback.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### SDR

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/sdr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/sdr.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### SDR (no WEBDL)

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/sdr-no-webdl-radarr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/sdr-no-webdl.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### HLG

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hlg.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hlg.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Streaming Services

---

### Streaming Services General

#### AMZN

<sub>Amazon Prime Video</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/amzn.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/amzn.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### ATV

<sub>Apple TV</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/atv.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/atv.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### ATVP

<sub>Apple TV+</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/atvp.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/atvp.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### BCORE

<sub>Bravia Core</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/bcore.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/bcore.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### CRiT

<sub>Criterion Channel</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/crit.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/crit.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### DSNP

<sub>Disney+</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dsnp.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dsnp.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### PLAY

<sub>Google Play</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/play.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/play.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### HBO

<sub>HBO</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hbo.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hbo.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### HMAX

<sub>HBO Max</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hmax.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hmax.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Hulu

<sub>Hulu</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hulu.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hulu.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### IT

<sub>iTunes</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/it.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/it.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Max

<sub>Max (streaming service)</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hmax.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/max.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### MA

<sub>Movies Anywhere</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/ma.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/ma.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### NF

<sub>Netflix</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/nf.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/nf.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### PMTP

<sub>Paramount+</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/pmtp.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/pmtp.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### PCOK

<sub>Peacock TV</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/pcok.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/pcok.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### ROKU

<sub>ROKU</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/roku.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/roku.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### STAN

<sub>Stan</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/stan.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/stan.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Asian Streaming Services

---

#### CPNG

<sub>Coupang Play</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/cpng.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/cpng.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### HTSR

<sub>Disney+ Hotstar</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/htsr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/htsr.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### friDay

<sub>friDay Video</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/friday.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/friday.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### FOD

<sub>Fuji Television On Demand aka Fuji TV On Demand</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/fod.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/fod.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Hami

<sub>Hami Video</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hami.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hami.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### iQIY

<sub>iQIYI</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/iqiy.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/iqiy.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### KKTV

<sub>KKTV</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/kktv.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/kktv.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### KCW

<sub>KOCOWA</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/kcw.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/kcw.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### LINETV

<sub>LINE TV</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/linetv.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/linetv.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### myTVSUPER

<sub>myTV SUPER</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/mytvsuper.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/mytvsuper.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### TVING

<sub>TVING</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/tving.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/tving.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### TVer

<sub>TVer</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/tver.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/tver.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### U-NEXT

<sub>U-NEXT</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/u-next.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/u-next.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Viki

<sub>Rakuten Viki</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/viki.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/viki.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### VIU

<sub>VIU</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/viu.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/viu.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Wavve

<sub>Wavve</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/wavve.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/wavve.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### WeTV

<sub>WeTV</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/wetv.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/wetv.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Youku

<sub>Youku</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/youku.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/youku.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Dutch Streaming Services

---

#### Pathe

<sub>Pathé Thuis</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/pathe.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/pathe.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### VDL

<sub>Videoland</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/vdl.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/vdl.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Misc Streaming Services

---

#### AUBC

<sub>Australian Broadcasting Corporation</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/aubc.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/aubc.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### CNLP

<sub>Canal+</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/cnlp.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/cnlp.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### CBC

<sub>CBC</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/cbc.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/cbc.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### Crav

<sub>Crave</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/crav.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/crav.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### FAH

<sub>Fandango</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/fah.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/fah.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### OViD

<sub>OViD</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/ovid.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/ovid.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### STRP

<sub>Star+</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/strp.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/strp.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### UK Streaming Services

---

#### iP

<sub>BBC iPlayer aka iP</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/ip.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/ip.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### ITVX

<sub>ITVX aka ITV</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/itvx.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/itvx.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### MY5

<sub>MY5 aka Channel 5</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/my5.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/my5.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### NOW

<sub>NOW</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/now.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/now.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Streaming Services

---

#### FUNI

<sub>Funimation</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/funi.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/funi.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

#### VRV

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/vrv.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/vrv.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Movie Versions

---

### 4K Remaster

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/4k-remaster.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/4k-remaster.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Criterion Collection

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/criterion-collection.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/criterion-collection.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Hybrid

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hybrid.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hybrid.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### IMAX

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/imax.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/imax.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### IMAX Enhanced

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/imax-enhanced.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/imax-enhanced.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Masters of Cinema

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/masters-of-cinema.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/masters-of-cinema.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Open Matte

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/open-matte.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/open-matte.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Remaster

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/remaster.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/remaster.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Special Edition

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/special-edition.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/special-edition.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Theatrical Cut

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/theatrical-cut.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/theatrical-cut.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Vinegar Syndrome

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/vinegar-syndrome.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/vinegar-syndrome.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Unwanted Formats

---

### 3D

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/3d.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/3d.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### AV1

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/av1.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/av1.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Bad Dual Groups

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/bad-dual-groups.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/bad-dual-groups.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Black and White Editions

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/black-and-white-editions.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/black-and-white-editions.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### BR-DISK

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/br-disk.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/br-disk.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Extras

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/extras.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/extras.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Generated Dynamic HDR

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/generated-dynamic-hdr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/generated-dynamic-hdr.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Line/Mic Dubbed

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/line-mic-dubbed.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/line-mic-dubbed.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### LQ

<sub>Low-Quality Releases = LQ</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/lq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/lq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### LQ (Release Title)

<sub>Low-Quality Releases = LQ</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/lq-release-title.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/lq-release-title.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### No-RlsGroup

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/no-rlsgroup.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/no-rlsgroup.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Obfuscated

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/obfuscated.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/obfuscated.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Retags

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/retags.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/retags.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Scene

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/scene.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/scene.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Sing-Along Versions

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/sing-along-versions.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/sing-along-versions.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Upscaled

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/upscaled.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/upscaled.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## HQ Release Groups

---

### Remux Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/remux-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/remux-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Remux Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/remux-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/remux-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Remux Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/remux-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/remux-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### UHD Bluray Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/uhd-bluray-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/uhd-bluray-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### UHD Bluray Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/uhd-bluray-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/uhd-bluray-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### UHD Bluray Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/uhd-bluray-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/uhd-bluray-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hd-bluray-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hd-bluray-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hd-bluray-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hd-bluray-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### HD Bluray Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hd-bluray-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hd-bluray-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/web-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/web-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/web-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/web-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### WEB Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/web-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/web-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Repacks/Proper (Required)

---

### Repack/Proper

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/repack-proper.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/repack-proper.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack2

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/repack2.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/repack2.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Repack3

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/repack3.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/repack3.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Golden Rule (Optional)

::: details Why block 720/1080p encodes in x265? - [Click to show/hide]

<!--@include: ../../includes/docker/x265.md-->

---

### x265 (no HDR/DV)

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/x265-no-hdrdv-radarr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/x265-no-hdrdv.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### x265 (HD)

<sub>720/1080p no x265 = x265 (720/1080p) = x265 (HD)</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/x265-hd-radarr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/x265-hd.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Miscellaneous (Optional)

---

### FreeLeech

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/freeleech.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/freeleech.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### HFR

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/hfr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/hfr.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Internal

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/internal.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/internal.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### MPEG2

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/mpeg2.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/mpeg2.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Multi

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/multi.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/multi.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### P2P Internal

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/p2p-internal.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/p2p-internal.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VC-1

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/vc-1.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/vc-1.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VP9

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/vp9.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/vp9.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### x264

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/x264.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/x264.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### x265

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/x265.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/x265.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### x266

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/x266.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/x266.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Resolution (Optional)

---

### 720p

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/720p.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/720p.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 1080p

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/1080p.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/1080p.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### 2160p

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/2160p.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/2160p.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Language Profiles

---

### German

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German DL

<sub>Language: German + Original</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-dl.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-dl.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German DL (undefined)

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-dl-undefined.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-dl-undefined.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not English

<sub>Language: English Only</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/language-not-english.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/language-not-english.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not French

<sub>Language: French Only</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/language-not-french.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/language-not-french.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Not Original

<sub>Language: Original Only</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/language-not-original.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/language-not-original.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Language: Original Plus French

<sub>Language: Original + French</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/language-original-plus-french.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/language-original-plus-french.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Not German or English

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/not-german-or-english.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/not-german-or-english.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Not German, Japanese or English

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/not-german-japanese-or-english.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/not-german-japanese-or-english.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Not German, Japanese, Korean, Chinese or English

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/not-german-japanese-korean-chinese-or-english.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/not-german-japanese-korean-chinese-or-english.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Wrong Language

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/wrong-language.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/wrong-language.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Accessibility (Optional)

---

### WiTH AD

<sub>Audio Description</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/with-ad.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/with-ad.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### WiTH ASL

<sub>American Sign Language</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/with-asl.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/with-asl.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### WiTH BASL

<sub>Black American Sign Language</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/with-basl.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/with-basl.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### WiTH BSL

<sub>British Sign Language</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/with-bsl.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/with-bsl.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Anime Release Groups

---

### Anime BD Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 04

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-04.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-04.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 05

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-05.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-05.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 06

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-06.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-06.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 07

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-07.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-07.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime BD Tier 08

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-bd-tier-08.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-bd-tier-08.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-web-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-web-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-web-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-web-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-web-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-web-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 04

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-web-tier-04.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-web-tier-04.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 05

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-web-tier-05.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-web-tier-05.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Web Tier 06

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-web-tier-06.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-web-tier-06.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Raws

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-raws.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-raws.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime LQ Groups

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-lq-groups.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-lq-groups.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Anime Versions

---

### v0

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/v0.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/v0.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### v1

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/v1.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/v1.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### v2

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/v2.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/v2.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### v3

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/v3.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/v3.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### v4

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/v4.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/v4.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Anime Optional

---

### 10bit

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/10bit.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/10bit.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Anime Dual Audio

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/anime-dual-audio.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/anime-dual-audio.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Dubs Only

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/dubs-only.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/dubs-only.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Uncensored

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/uncensored.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/uncensored.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## German Release Groups

---

### German Remux Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-remux-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-remux-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Remux Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-remux-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-remux-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Bluray Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-bluray-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-bluray-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Bluray Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-bluray-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-bluray-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Bluray Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-bluray-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-bluray-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Web Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-web-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-web-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Web Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-web-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-web-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Web Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-web-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-web-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Scene

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-scene.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-scene.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## German Anime Release Groups

---

### German Anime Bluray Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-bluray-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-bluray-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Anime Bluray Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-bluray-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-bluray-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Anime Bluray Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-bluray-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-bluray-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Anime Web Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-web-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-web-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Anime Web Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-web-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-web-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Anime Web Tier 03

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-web-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-web-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Anime Scene

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-anime-scene.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-anime-scene.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## German Miscellaneous

---

### German 1080p Booster

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-1080p-booster.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-1080p-booster.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German 2160p Booster

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-2160p-booster.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-2160p-booster.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German LQ

<sub>German Low-Quality Releases = German LQ</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-lq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-lq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German LQ (Release Title)

<sub>Low-Quality Releases = LQ</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-lq-release-title.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-lq-release-title.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Microsized

<sub>German Microsized Releases = German Microsized</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-microsized.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-microsized.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### German Subbed

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/german-subbed.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/german-subbed.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## French Release Groups

---

### FR Remux Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-remux-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-remux-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Remux Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-remux-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-remux-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR UHD Bluray Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-uhd-bluray-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-uhd-bluray-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR UHD Bluray Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-uhd-bluray-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-uhd-bluray-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR HD Bluray Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-hd-bluray-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-hd-bluray-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR HD Bluray Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-hd-bluray-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-hd-bluray-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 01

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-web-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-web-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR WEB Tier 02

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-web-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-web-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Scene Groups

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-scene.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-scene.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR LQ

<sub>French Low-Quality Releases = FR LQ</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-lq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-lq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## French Anime Release Groups

---

### FR Anime Tier 01

::: details FR Anime Tier 01 - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-anime-tier-01.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-anime-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 02

::: details FR Anime Tier 02 - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-anime-tier-02.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-anime-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime Tier 03

::: details FR Anime Tier 03 - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-anime-tier-03.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-anime-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FR Anime FanSub

::: details FR Anime FanSub - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-anime-fansub.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-anime-fansub.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## French Audio Version

---

### VFF

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vff.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vff.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VOF

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vof.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vof.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VFI

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vfi.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vfi.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VF2

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vf2.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vf2.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VFQ

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vfq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vfq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VOQ

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-voq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-voq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VQ

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VFB

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vfb.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vfb.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### VOSTFR

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/french-vostfr.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/french-vostfr.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FanSUB

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/fansub.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/fansub.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### FastSUB

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/fastsub.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/fastsub.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

## Asian Release Groups
<!-- markdownlint-disable MD052-->
{{ radarr['cf-groups']['release-groups-asian']['trash_description'] }}
<!-- markdownlint-enable MD052-->
---

### Asian Tier 01

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/asian-tier-01.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Asian Tier 02

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/asian-tier-02.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Asian Tier 03

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/asian-tier-03.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

### Asian LQ

<sub>Asian Low-Quality Releases = Asian LQ</sub>

::: details Description - [Click to show/hide]

<!--@include: ../../includes/cf-descriptions/asian-lq.md-->

:::

::: details JSON - [Click to show/hide]

```json
<!--@include: @/json/radarr/cf/asian-lq.json-->
```

:::

<sub><sup>[TOP](#index)</sup></sub>

---

<!-- END OF THE COLLECTION LIST -->
