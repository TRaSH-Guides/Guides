# Collection of Custom Formats for Radarr V3

Here I will try to collect a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on discord or that I created with help from others.
Special thanks to [rg9400](https://github.com/rg9400){:target="_blank"}, [bakerboy448](https://github.com/bakerboy448){:target="_blank"} and Team Radarr.

!!! warning "Important"
    Keep in mind Custom Formats are made to fine tune your Quality Profile

    **Quality Profile trumps Custom Formats**

With Radarr V3, Custom Formats are much more advanced/powerful than with v0.2, although this also means a Custom Format is much more complicated to setup.

After requesting at Team Radarr we now have the options to import/export the Custom Formats in a JSON format that we can use here what makes it easier to share the different kind of Custom Formats.

I also made a [Guide](How-to-importexport-Custom-Formats-and-truly-make-use-of-it.md) on how to import/export the Custom Formats and how to truly make use of it.

------

## INDEX

------

| Audio                                    | Audio Advanced #1                             | Audio Advanced #2                           | Audio Channels               |
| :--------------------------------------- | --------------------------------------------- | ------------------------------------------- | ---------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [TrueHD ATMOS](#truehd-atmos)                 | [FLAC](#flac)                               | [1.0 Mono](#10-mono)         |
| [DTS-HD/DTS:X](#dts-hddtsx)              | [DTS X](#dts-x)                               | [PCM](#pcm)                                 | [2.0 Stereo](#20-stereo)     |
| [Surround Sounds](#surround-sounds)      | [ATMOS (indeterminate)](#atmos-indeterminate) | [DTS-HD HRA](#dts-hd-hra)                   | [3.0 Sound](#30-sound)       |
|                                          | [DD+ ATMOS (lossy)](#dd-atmos-lossy)          | [AAC](#aac)                                 | [4.0 Sound](#40-sound)       |
|                                          | [TrueHD (not ATMOS)](#truehd-not-atmos)       | [Basic Dolby Digital](#basic-dolby-digital) | [5.1 Surround](#51-surround) |
|                                          | [DTS-HD MA](#dts-hd-ma)                       | [MP3](#mp3)                                 | [6.1 Surround](#61-surround) |
|                                          | [Dolby Digital Plus](#dolby-digital-plus)     | [Opus](#opus)                               | [7.1 Surround](#71-surround) |
|                                          | [DTS-ES](#dts-es)                             |                                             | [9.1 Surround](#91-surround) |
|                                          | [Basic DTS](#basic-dts)                       |                                             |                              |

------

| HDR Metadata                                              | Movie Versions                                | Misc (-1000)                                  | Misc                                      |
| --------------------------------------------------------- | --------------------------------------------- | --------------------------------------------- | ----------------------------------------- |
| [Dolby Vision](#dolby-vision)                             | [Hybrid](#hybrid)                             | [BR-DISK](#br-disk)                           | [Repack/Proper](#repack-proper)           |
| [Dolby Vision (Single Layer)](#dolby-vision-single-layer) | [Remaster](#remaster)                         | [EVO except WEB-DL](#evo-except-web-dl)       | [Streaming Services](#streaming-services) |
| [HDR](#hdr)                                               | [4K Remaster](#4k-remaster)                   | [Low Quality Releases](#low-quality-releases) | [HQ-P2P](#hq-p2p)                         |
| [10 Bit](#10-bit)                                         | [Special Editions](#special-edition)          | [720/1080p no x265](#7201080p-no-x265)        | [x264](#x264)                             |
|                                                           | [Criterion Collection](#criterion-collection) | [3D](#3d)                                     | [x265](#x265)                             |
|                                                           | [Theatrical Cut](#theatrical-cut)             |                                               | [MPEG2](#mpeg2)                           |
|                                                           | [IMAX](#imax)                                 |                                               | [FreeLeech](#freeleech)                   |
|                                                           |                                               |                                               | [Dutch Groups](#dutch-groups)             |
|                                                           |                                               |                                               | [Anime Dual Audio](#anime-dual-audio)     |
|                                                           |                                               |                                               | [Multi](#multi)                           |
|                                                           |                                               |                                               | [FraMeSToR](#framestor)                   |

## Audio

------

### Dolby TrueHD/ATMOS

If you prefer TrueHD|Atmos audio tracks.

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    {
        "name": "Dolby TrueHD/ATMOS",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "truehd|atmos",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": false,
            "fields": {
                "value": "truehd|atmos"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### DTS-HD/DTS:X

If you prefer DTS-HD/DTS:X audio tracks.

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    {
        "name": "DTS-HD/DTS:X",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "dts.?(hd|es|x(?!\\d))",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": false,
            "fields": {
                "value": "dts.?(hd|es|x(?!\\d))"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Surround Sounds

If you prefer all kind of surround sounds

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    {
        "name": "Surround Sounds",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "dts\\-?(hd|x)|truehd|atmos|dd(\\+|p)(5|7)",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": false,
            "fields": {
                "value": "dts\\-?(hd|x)|truehd|atmos|dd(\\+|p)(5|7)"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

## Audio Advanced

------

### TrueHD ATMOS

??? example "json"

    ```json
    {
        "name": "TrueHD ATMOS",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "TrueHD",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "TrueHD"
                }
            },
            {
                "name": "ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Dolby Digital Plus ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### DTS X

??? example "json"

    ```json
    {
        "name": "DTS X",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "DTS X",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "dts[-. ]?x(?!\\d)"
                }
            },
            {
                "name": "Not Basic DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "DTS[ .]?[1-9]"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDD(\\b|\\d)|(?<!e)ac3"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### ATMOS (indeterminate)

Handles cases where only Atmos is specified in title but not DD+ or TrueHD (Where it is not specified if it is Lossy or Lossless)

Give this the same score as Lossy Atmos, and then on import, it will get changed to either lossy or lossless based on mediainfo.

??? example "json"

    ```json
    {
        "name": "ATMOS (indeterminate)",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not TrueHD",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### DD+ ATMOS (lossy)

??? example "json"

    ```json
    {
        "name": "DD+ ATMOS (lossy)",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not TrueHD",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### TrueHD (not ATMOS)

??? example "json"

    ```json
    {
        "name": "TrueHD (not ATMOS)",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "TrueHD",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "TrueHD"
                }
            },
            {
                "name": "ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### DTS-HD MA

??? example "json"

    ```json
    {
        "name": "DTS-HD MA",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "DTS-HD MA",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "dts.?(ma|hd.?ma)"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not Basic DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "DTS[ .]?[1-9]"
                }
            },
            {
                "name": "Not Basic Dolby Digital ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDD(\\b|\\d)|(?<!e)ac3"
                }
            },
            {
                "name": "Not DTS X",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts[-. ]?x(?!\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS-HD HRA/ES",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts.?(es|(hd.?)?(hr|hi))"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### FLAC

FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "json"

    ```json
    {
        "name": "FLAC",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not Dolby Digital Plus ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### PCM

??? example "json"

    ```json
    {
        "name": "PCM",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not Dolby Digital Plus ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### DTS-HD HRA

??? example "json"

    ```json
    {
        "name": "DTS-HD HRA",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "DTS-HD HRA",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "dts.?(hd.?)?(hr|hi)"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not Basic DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "DTS[ .]?[1-9]"
                }
            },
            {
                "name": "Not Basic Dolby Digital ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDD(\\b|\\d)|(?<!e)ac3"
                }
            },
            {
                "name": "Not DTS X",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts[-. ]?x(?!\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS-ES",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts.?es"
                }
            },
            {
                "name": "Not 6.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]6\\.[0-1]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Dolby Digital Plus

??? example "json"

    ```json
    {
        "name": "Dolby Digital Plus",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### DTS-ES

??? example "json"

    ```json
    {
        "name": "DTS-ES",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "DTS-ES",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "dts.?(es|(hd.?)?(hr|hi))"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not Basic DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "DTS[ .]?[1-9]"
                }
            },
            {
                "name": "Not Basic Dolby Digital ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDD(\\b|\\d)|(?<!e)ac3"
                }
            },
            {
                "name": "Not DTS X",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts[-. ]?x(?!\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            },
            {
                "name": "6.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]6\\.[0-1]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Basic DTS

??? example "json"

    ```json
    {
        "name": "Basic DTS",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Basic DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS-HD",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts.?(hd|ma|es|hi)"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDD(\\b|\\d)|(?<!e)ac3"
                }
            },
            {
                "name": "Not DTS X",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dts[-. ]?x(?!\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### AAC

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank"}

Advanced Audio Coding

Advanced Audio Coding (AAC) is an audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves higher sound quality than MP3 at the same bit rate.

??? example "json"

    ```json
    {
        "name": "AAC",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not Dolby Digital Plus ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "dd[p+]|eac3"
                }
            },
            {
                "name": "Not Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!e)ac3"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Basic Dolby Digital

??? example "json"

    ```json
    {
        "name": "Basic Dolby Digital",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Basic Dolby Digital",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bDD[^a-z+]|(?<!e)ac3"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "eac3"
                }
            },
            {
                "name": "Not TrueHD/ATMOS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "TrueHD|\\bATMOS(\\b|\\d)"
                }
            },
            {
                "name": "Not DTS",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bDTS(\\b|\\d)"
                }
            },
            {
                "name": "Not FLAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bFLAC(\\b|\\d)"
                }
            },
            {
                "name": "Not AAC",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\bAAC(\\b|\\d)"
                }
            },
            {
                "name": "Not PCM",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "\\b(l?)PCM(\\b|\\d)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### MP3

??? example "json"

    ```json
    {
        "name": "MP3",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "MP3",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "mp3"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Opus

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank"}

Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "json"

    ```json
    {
        "name": "Opus",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "Opus",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "\\bOPUS(\\b|\\d)"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

## Audio Channels

------

### 1.0 Mono

??? example "json"

    ```json
    {
        "name": "1.0 Mono",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Mono",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]1\\.0|\\bMono\\b|\\[PCM \\]"
                }
            },
            {
                "name": "Not Stereo",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9]2\\.0|\\bStereo\\b"
                }
            },
            {
                "name": "Not 3.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]3\\.0"
                }
            },
            {
                "name": "Not 4.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]4\\.0"
                }
            },
            {
                "name": "Not High Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][5-9]\\.[0-1]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 2.0 Stereo

??? example "json"

    ```json
    {
        "name": "2.0 Stereo",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Stereo",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9]2\\.0|\\bStereo\\b"
                }
            },
            {
                "name": "Not 3.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]3\\.0"
                }
            },
            {
                "name": "Not 4.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]4\\.0"
                }
            },
            {
                "name": "Not High Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][5-9]\\.[0-1]"
                }
            },
            {
                "name": "Not Mono",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]1\\.0|\\bMono\\b|\\[PCM \\]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 3.0 Sound

??? example "json"

    ```json
    {
        "name": "3.0 Sound",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "3.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]3\\.0"
                }
            },
            {
                "name": "Not Mono",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]1\\.0|\\bMono\\b|\\[PCM \\]"
                }
            },
            {
                "name": "Not Stereo",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9]2\\.0|\\bStereo\\b"
                }
            },
            {
                "name": "Not 4.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]4\\.0"
                }
            },
            {
                "name": "Not High Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][5-9]\\.[0-1]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 4.0 Sound

??? example "json"

    ```json
    {
        "name": "4.0 Sound",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "4.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]4\\.0"
                }
            },
            {
                "name": "Not Mono",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]1\\.0|\\bMono\\b|\\[PCM \\]"
                }
            },
            {
                "name": "Not Stereo",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9]2\\.0|\\bStereo\\b"
                }
            },
            {
                "name": "Not 3.0ch",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]3\\.0"
                }
            },
            {
                "name": "Not High Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][5-9]\\.[0-1]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 5.1 Surround

??? example "json"

    ```json
    {
        "name": "5.1 Surround",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "5.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]5\\.[0-1]"
                }
            },
            {
                "name": "Not 7.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][7-8]\\.[0-1]"
                }
            },
            {
                "name": "Not 9.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]9\\.[0-1]"
                }
            },
            {
                "name": "Not Low Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9][1-4]\\.[0-1]|\\b(Stereo|Mono)\\b"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 6.1 Surround

??? example "json"

    ```json
    {
        "name": "6.1 Surround",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "6.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]6\\.[0-1]"
                }
            },
            {
                "name": "Not 7.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][7-8]\\.[0-1]"
                }
            },
            {
                "name": "Not 9.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]9\\.[0-1]"
                }
            },
            {
                "name": "Not Low Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9][1-4]\\.[0-1]|\\b(Stereo|Mono)\\b"
                }
            },
            {
                "name": "Not 5.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]5\\.[0-1]"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 7.1 Surround

??? example "json"

    ```json
    {
        "name": "7.1 Surround",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "7.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9][7-8]\\.[0-1]"
                }
            },
            {
                "name": "Not 9.1  Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9]9\\.[0-1]"
                }
            },
            {
                "name": "Not Low Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9][1-4]\\.[0-1]|\\b(Stereo|Mono)\\b"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 9.1 Surround

??? example "json"

    ```json
    {
        "name": "9.1 Surround",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "9.1  Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^0-9]9\\.[0-1]"
                }
            },
            {
                "name": "Not 7.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][7-8]\\.[0-1]"
                }
            },
            {
                "name": "Not 5.1 Surround",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^0-9][5-6]\\.[0-1]"
                }
            },
            {
                "name": "Not Low Channel Count",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "(?<!repac)[^0-9][1-4]\\.[0-1]|\\b(Stereo|Mono)\\b"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

## HDR metadata

------

### Dolby Vision

Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.

Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "json"

    ```json
    {
        "name": "DoVi",
        "includeCustomFormatWhenRenaming": true,
        "specifications": [{
            "name": "Dolby Vision",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "\\b(DV|dovi)\\b|dolby.?vision"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Dolby Vision (Single Layer)

Custom Format for Single Layer Dolby Vision releases.

!!! note

    This used to be the the preferred option for PLeX with a Shield 2019 model that supports DV.

    But now DV is part of the MKV spec and ExoPlayer added native support.

??? example "json"

    ```json
    {
        "name": "Dolby Vision (Single Layer)",
        "includeCustomFormatWhenRenaming": true,
        "specifications": [{
                "name": "Dolby Vision (Single Layer)",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "sl.?dv|single.?layer.?dovi"
                }
            },
            {
                "name": "Remux",
                "implementation": "QualityModifierSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": 5
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### HDR

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank"}

High-dynamic-range video (HDR video) is video having a dynamic range greater than that of standard-dynamic-range video (SDR video).HDR video involves capture, production, content/encoding, and display. HDR capture and displays are capable of brighter whites and deeper blacks. To accommodate this, HDR encoding standards allow for a higher maximum luminance and use at least a 10-bit dynamic range (color depth, compared to 8-bit for non-professional and 10-bit for professional SDR video) in order to maintain precision across this extended range.

??? example "json"

    ```json
    {
        "name": "HDR",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "HDR",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "\\bHDR(\\b|\\d)"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 10 Bit

??? example "json"

    ```json
    {
        "name": "10 Bit",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "10 Bit",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "\\b10bit(\\b|\\d)"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

## Movie Versions

------

### Hybrid

A hybrid release means any combination of sources (video + audio) and not a direct encode of a single source. Generally you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "json"

    ```json
    {
        "name": "Hybrid",
        "includeCustomFormatWhenRenaming": true,
        "specifications": [{
                "name": "Hybrid",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\bhybrid(\\b|\\d)"
                }
            },
            {
                "name": "Not Hybrid Release Group",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "-HYBRID"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Remaster

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank"}

For the software term, see Software remastering.
Remaster (also digital remastering and digitally remastered) refers to changing the quality of the sound or of the image, or both, of previously created recordings, either audiophonic, cinematic, or videographic.

??? example "json"

    ```json
    {
        "name": "Remaster",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Remaster",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "Remaster"
                }
            },
            {
                "name": "Not 4K Remaster",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "4K"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 4K Remaster

A remastered or mastered in 4K should give you usually the best picture and audio currently for the movie. Both are just names to describe the best possible currently for the movie.

To be clear, the final digital films on the Mastered in 4K Blu-rays still only have the same 1920 x 1080 pixels of actual resolution as normal Blu-rays. But the argument goes that because these full HD files were derived from higher-resolution masters, their images will be more precise, with better colours, less noise, and enhanced sharpness and detail. Not least because the higher-resolution mastering process will provide more detail from the original print for the Blu-ray masters to draw on when going through their (hopefully…) frame-by-frame compression process.

Another important element of the Mastered in 4K discs is that they’re all mastered with ‘x.v.YCC’ colour specification. This delivers an expanded colour range closer to that contained in original source material.

??? example "json"

    ```json
    {
        "name": "4K Remaster",
        "includeCustomFormatWhenRenaming": true,
        "specifications": [{
                "name": "Remaster",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "Remaster"
                }
            },
            {
                "name": "4K",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "4k"
                }
            },
            {
                "name": "Not 4K Resolution",
                "implementation": "ResolutionSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": 2160
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Criterion Collection

The Criterion Collection, Inc. (or simply Criterion) is an American home video distribution company which focuses on licensing "important classic and contemporary films" and selling them to film aficionados.Criterion has helped to standardize characteristics of home video such as film restoration, using the letterbox format for widescreen films, and adding bonus features and commentary tracks.

??? example "json"

    ```json
    {
        "name": "Criterion Collection",
        "includeCustomFormatWhenRenaming": true,
        "specifications": [{
                "name": "Criterion",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "criterion"
                }
            },
            {
                "name": "CC",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "\\bCC\\b"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Theatrical Cut

The Theatrical Cut is the version of the film that was shown at cinemas.

??? example "json"

    ```json
    {
        "name": "Theatrical Cut",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "Theatrical",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "Theatrical"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Special Edition

Custom format for several Special Editions

- The Director's Cut is the version edited by the Director, usually for additional home media releases.
- An Extended Cut is usually any version of the film which is longer than the theatrical cut (though in very rare cases, its shorter).

??? example "json"

    ```json
    {
        "name": "Special Edition",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Special Edition ",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "(?<!^)\\b(extended|uncut|director|special|unrated|uncensored|cut|version|edition)(\\b|\\d)"
                }
            },
            {
                "name": "Not Theatrical ",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "Theatrical"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### IMAX

??? example "json"

    ```json
    {
      "name": "IMAX",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "IMAX",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": "\\bIMAX\\b"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

## Misc (-1000)

------

### BR-DISK

This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

!!! note

    Depending on your renaming scheme it could happen that Radarr will match renamed files after they are downloaded and imported as `BR-DISK`,
    This is a cosmetic annoyance till I come up for another way to solve this,
    being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
    Several reasons why this is happening:

    - Blame the often wrongly used naming of x265 encodes.
    - Radarr v3 uses dynamic custom formats.

??? example "json"

    ```json
    {
        "name": "BR-DISK",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "avc|vc-1|hevc",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "avc|vc-1|hevc"
                }
            },
            {
                "name": "Remux",
                "implementation": "QualityModifierSpecification",
                "negate": true,
                "required": false,
                "fields": {
                    "value": 5
                }
            },
            {
                "name": "WEBDL",
                "implementation": "SourceSpecification",
                "negate": true,
                "required": false,
                "fields": {
                    "value": 7
                }
            },
            {
                "name": "^((?!x265).)*$",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "^((?!x265).)*$"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### EVO except WEB-DL

This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

??? example "json"

    ```json
    {
        "name": "EVO (except WEB-DL)",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "EVO",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "\\bEVO\\b"
                }
            },
            {
                "name": "WEBDL",
                "implementation": "SourceSpecification",
                "negate": true,
                "required": false,
                "fields": {
                    "value": 7
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Low Quality Releases

A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality.

!!! note

    You might want to add the following also [EVO except WEB-DL](#evo-except-web-dl)

    - BLOCK1 = Low-Quality Releases (often banned groups)
    - BLOCK2 = Another Small list of often banned groups.
    - BLOCK3 = And Another list.
    - BLOCK4 = Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.

??? example "json"

    ```json
    {
        "name": "Low Quality Releases",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "[BLOCK1]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-aXXo|-CrEwSaDe|-DEViSE|-FaNGDiNG0|-FLAWL3SS|-FZHD|-FRDS|-HDTime|-IMAGINE|-iPlanet|-KingBen|-KiNGDOM|-KLAXXON|-Leffe|-LTRG|-mHD|-mSD|-NhaNc3|-nHD|-nikt0|-nSD|-PrisM|-PRODJi|-Rx|-RDN|-SANTi|-ViSION|-WAF|-WHiiZz|-x0r|\\bYIFY\\b|\\bYTS\\b|-STUTTERSHIT"
                }
            },
            {
                "name": "[BLOCK2]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-CDDHD|-EuReKA|-DDR|-DNL|-BARC0DE"
                }
            },
            {
                "name": "[BLOCK3]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "\\bRARBG\\b|-FGT|-BReWeRS|-Grym|-LiGaS|-Zeus|-Tigole"
                }
            },
            {
                "name": "[BLOCK4]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-beAst|-CHD|-HDWinG|-MTeam|-MySiLU|-WiKi"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 720/1080p no x265

This blocks/ignores 720/1080p releases that are encoded in x265

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

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

So I created my own golden rule.

- 720/1080p => x264
- 2160p/4k => x265

??? example "json"

    ```json
    {
     "name": "720/1080p != x265",
     "includeCustomFormatWhenRenaming": false,
     "specifications": [
       {
         "name": "720p",
         "implementation": "ResolutionSpecification",
         "negate": false,
         "required": false,
         "fields": {
           "value": 720
         }
       },
       {
         "name": "1080p",
         "implementation": "ResolutionSpecification",
         "negate": false,
         "required": false,
         "fields": {
           "value": 1080
         }
       },
       {
         "name": "x265/HEVC",
         "implementation": "ReleaseTitleSpecification",
         "negate": false,
         "required": true,
         "fields": {
           "value": "[xh]\\.?265|\\bHEVC(\\b|\\d)"
         }
       }
     ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### 3D

If you prefer or not prefer 3D.

You can use Custom Format or use Restrictions (`Settings` => `Indexers` => `Restrictions`) what ever you prefer.

??? example "json"

    ```json
    {
        "name": "3D",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "3d|sbs|half-ou",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "3d|sbs|half.?ou"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

## Misc

------

### HQ-P2P

A collection of P2P groups that are known for their high quality releases

??? example "json"

    ```json
    {
        "name": "HQ-P2P",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "[BLOCK1]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-BMF|-decibeL|\\bD-Z0N3\\b|\\bFTW-HD\\b|-HiFi|-NCmt|-OISTiLe|-TDD|\\bZQ\\b"
                }
            },
            {
                "name": "[BLOCK2]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-HiSD|-NTb|-ift|-geek|-tnp|-ncmt|-pter|-bbq"
                }
            },
            {
                "name": "[BLOCK3]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-CRiSC|-CtrlHD|-DON|\\b-EA\\b|-EbP|-LolHD|-SbR|-TayTo|-VietHD"
                }
            },
            {
                "name": "[Remux Groups]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-FraMeSToR|-EPSiLON|//bKRaLiMaRKo//b"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Repack Proper

??? example "json"

    ```json
    {
        "name": "Repack/Proper",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Repack",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "Repack"
                }
            },
            {
                "name": "Proper",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "Proper"
                }
            },
            {
                "name": "Rerip",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "Rerip"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Streaming Services

Collection of Streaming Services

!!! attention

    This CF only prefers the known streaming services and doesn't work the same way like the release profile that can be used in Sonarr to include the streaming service name in your renaming scheme when using `{[Custom Formats]}` !!!
    If you want to have this option then you need to add them all separate.

??? example "json"

    ```json
    {
        "name": "Streaming Services",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Amazon",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(amzn|amazon).?web.?(dl|rip)"
                }
            },
            {
                "name": "Netflix",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(nf|netflix).?web.?(dl|rip)"
                }
            },
            {
                "name": "AppleTV+",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(atvp).?web.?(dl|rip)"
                }
            },
            {
                "name": "Disney+",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(dsnp|dsny|disney).?web.?(dl|rip)"
                }
            },
            {
                "name": "DCU",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(dcu).?web.?(dl|rip)"
                }
            },
            {
                "name": "HBO Max",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(hmax).?web.?(dl|rip)"
                }
            },
            {
                "name": "HBO",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(hbo).?web.?(dl|rip)"
                }
            },
            {
                "name": "Youtube Red",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(red).?web.?(dl|rip)"
                }
            },
            {
                "name": "Quibi",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(qibi).?web.?(dl|rip)"
                }
            },
            {
                "name": "iTunes",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(it).?web.?(dl|rip)"
                }
            },
            {
                "name": "Hulu",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "(hulu).?web.?(dl|rip)"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### x264

x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank"}.

If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p

??? example "json"

    ```json
    {
        "name": "x264",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "x264",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[xh]\\.?264|\\bAVC(\\b|\\d)"
                }
            },
            {
                "name": "Remux",
                "implementation": "QualityModifierSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": 5
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### x265

x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank"}.

!!! quote
    x265 is good for for 4k stuff or 1080p if they used the the remuxes as source.
    If the media isn't source quality/remux, then there will be a loss of quality every time.

    Something like 95% of video files are x264 and have much better direct play support.
    If you have more than a couple users, you will notice much more transcoding.
    Just depends on your priorities.

    So basically if you are storage poor and just need to save space, use x265.
    The catch is if you want best quality x265, you need source quality files, so you still have huge file sizes.
    If you want maximum compatibility and the option to change your files to something else later, then x264.
    It's all really dependent on specific situations for different people

It's a shame that most x265 groups microsize the releases or use the x264 as source what results in low quality releases. And the few groups that do use the correct source suffer from it.

So I created my own golden rule.

- 720/1080p => x264
- 2160p/4k => x265

> If you want to make use of the Golden Rule you could make use of the following Custom Format [720/1080p no x265](#7201080p-no-x265)

Some extra info about 4K/X265

[4k, transcoding, and you - aka the rules of 4k - a FAQ](https://forums.plex.tv/t/plex-4k-transcoding-and-you-aka-the-rules-of-4k-a-faq/378203) - Plex.tv

1. Don’t bother transcoding 4k
1. If you cannot direct play 4k, then perhaps you should not even be collecting 4k.
1. If you don’t have the storage space for a copy of both 4k and 1080/720, then perhaps you should not even be collecting 4k.
1. To avoid transcoding for remote and non-4k clients, keep your 4k content in separate plex libraries.

??? example "json"

    ```json
    {
        "name": "x265",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "x265",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[xh]\\.?265|\\bHEVC(\\b|\\d)"
                }
            },
            {
                "name": "Remux",
                "implementation": "QualityModifierSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": 5
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### FreeLeech

Sometimes, torrent sites set a torrent to be freeleech. This means, that the download of this torrent will not count towards your download quota or ratio. This is really useful, if you do not have the best ratio yet.

!!! attention
    Keep in mind not all trackers support this option.

??? example "json"

    ```json
    {
        "name": "FreeLeech",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "FreeLeech",
            "implementation": "IndexerFlagSpecification",
            "negate": false,
            "required": false,
            "fields": {
                "value": 1
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Dutch Groups

If you prefer movies with also a Dutch audio track.

??? example "json"

    ```json
    {
        "name": "Dutch Groups",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "Dutch Groups",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "-CyTSuNee|-SHiTSoNy|-QoQ"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Anime Dual Audio

??? example "json"

    ```json
    {
        "name": "Anime Dual Audio",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dual Audio",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "dual\\.audio"
                }
            },
            {
                "name": "BluDragon",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "bludragon"
                }
            },
            {
                "name": "EN+JA",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "EN\\+JA|JA\\+EN"
                }
            },
            {
                "name": "ZR",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "\\bZR\\b"
                }
            },
            {
                "name": "Japanese Language",
                "implementation": "LanguageSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": 8
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### MPEG2

??? example "json"

    ```json
    {
        "name": "MPEG2",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "MPEG2",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "MPEG-?2"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### Multi

??? example "json"

    ```json
    {
        "name": "Multi",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "Multi",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "\\bMulti(\\b|\\d)"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>

------

### FraMeSToR

If you prefer FraMeSToR releases.

Also FraMeSToR doesn't add HDR to their release name so I suggest to add them at the same score as you add one of your HDR Custom Formats.

??? example "json"

    ```json
    {
        "name": "FraMeSToR",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "FraMeSToR",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
              "value": "\\bFraMeSToR\\b"
         }
       }]
    }
    ```

<sub><sup>[TOP](#index)</sup></sub>
