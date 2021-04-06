# Collection of Custom Formats

Here I will try to collect a collection of the most needed and commonly used Custom Formats.
These have been collected from either discussions on discord or that I created with help from others.
Special thanks to [rg9400](https://github.com/rg9400), [bakerboy448](https://github.com/bakerboy448) and Team Radarr.

!!! warning "Important"
    Keep in mind Custom Formats are made to fine tune your Quality Profile

    **Quality Profile trumps Custom Formats**

With Radarr V3, Custom Formats are much more advanced/powerful than with v0.2, although this also means a Custom Format is much more complicated to setup.

After requesting at Team Radarr we now have the options to import/export the Custom Formats in a JSON format that we can use here what makes it easier to share the different kind of Custom Formats.

I also made 2 guides related to this one.

- [How to import Custom Formats](/Radarr/V3/Radarr-import-custom-formats){:target="_blank" rel="noopener noreferrer"}. Where I will try to explain how to import the Custom Formats.
- [How to setup Custom Formats](/Radarr/V3/Radarr-setup-custom-formats){:target="_blank" rel="noopener noreferrer"} Where I will try to explain how to make the most use of Custom Formats and show some personal examples that I'm using. That you can use to get a idea how to setup yours.

!!! tip

    I also suggest to change the Propers and Repacks settings in Radarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](#repack-proper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Formats preferences will be used and not ignored.

------

## INDEX

------

| Audio                                    | Audio Advanced #1                             | Audio Advanced #2                           | Audio Channels               |
| :--------------------------------------- | --------------------------------------------- | ------------------------------------------- | ---------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [TrueHD ATMOS](#truehd-atmos)                 | [FLAC](#flac)                               | [1.0 Mono](#10-mono)         |
| [DTS-HD/DTS:X](#dts-hddtsx)              | [DTS X](#dts-x)                               | [PCM](#pcm)                                 | [2.0 Stereo](#20-stereo)     |
| [Surround Sound](#surround-sound)      | [ATMOS (undefined)](#atmos-undefined) | [DTS-HD HRA](#dts-hd-hra)                   | [3.0 Sound](#30-sound)       |
|                                          | [DD+ ATMOS](#dd-atmos)          | [AAC](#aac)                                 | [4.0 Sound](#40-sound)       |
|                                          | [TrueHD](#truehd)       | [Basic Dolby Digital](#basic-dolby-digital) | [5.1 Surround](#51-surround) |
|                                          | [DTS-HD MA](#dts-hd-ma)                       | [MP3](#mp3)                                 | [6.1 Surround](#61-surround) |
|                                          | [Dolby Digital Plus](#dolby-digital-plus)     | [Opus](#opus)                               | [7.1 Surround](#71-surround) |
|                                          | [DTS-ES](#dts-es)                             |                                             | [9.1 Surround](#91-surround) |
|                                          | [Basic DTS](#basic-dts)                       |                                             |                              |

------

| HDR Metadata                                              | Movie Versions                                | Misc (-1000)                                  | Misc                                      |
| --------------------------------------------------------- | --------------------------------------------- | --------------------------------------------- | ----------------------------------------- |
| [Dolby Vision](#dolby-vision)                             | [Hybrid](#hybrid)                             | [BR-DISK](#br-disk)                           | [Repack/Proper](#repack-proper)           |
| [Dolby Vision (Single Layer)](#dolby-vision-single-layer) | [Remaster](#remaster)                         | [EVO except WEB-DL](#evo-except-web-dl)       | [Streaming Services](#streaming-services) |
| [HDR](#hdr)                                               | [4K Remaster](#4k-remaster)                   | [Low Quality Releases](#lq-releases) | [High Quality Releases](#hq-releases)                         |
| [HDR (undefined)](#hdr-undefined)                         | [Special Editions](#special-edition)          | [720/1080p no x265](#7201080p-no-x265)        | [x264](#x264)                             |
| [10 Bit](#10-bit)                                         | [Criterion Collection](#criterion-collection) | [3D](#3d)                                     | [x265](#x265)                             |
|                                                           | [Theatrical Cut](#theatrical-cut)             |                                               | [MPEG2](#mpeg2)                           |
|                                                           | [IMAX](#imax)                                 |                                               | [FreeLeech](#freeleech)                   |
|                                                           |                                               |                                               | [Dutch Groups](#dutch-groups)             |
|                                                           |                                               |                                               | [Anime Dual Audio](#anime-dual-audio)     |
|                                                           |                                               |                                               | [Multi](#multi)                           |
|                                                           |                                               |                                               |                                           |

## Audio

------

### Dolby TrueHD/ATMOS

>If you prefer TrueHD|Atmos audio tracks.

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    {
        "trash_id": "060059fc2b8759d9f314e1f18c76fd4a",
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

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD/DTS:X

>If you prefer DTS-HD/DTS:X audio tracks.

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    {
        "trash_id": "4eb3c272d48db8ab43c2c85283b69744",
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

<sub><sup>[TOP](#index)</sup>

------

### Surround Sound

>If you prefer all kind of surround sounds

!!! warning

    Don't use this Custom Format in combination with the `Audio Advanced` CF if you want to fine tune your audio formats or else it will add up the scores.

??? example "json"

    ```json
    {
        "trash_id": "43bb5f09c79641e7a22e48d440bd8868",
        "name": "Surround Sound",
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

<sub><sup>[TOP](#index)</sup>

------

## Audio Advanced

------

### TrueHD ATMOS

<sub><sub><sub>Score [500]</sub>

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Atmos){:target="_blank" rel="noopener noreferrer"}
>
>Dolby Atmos is a surround sound technology developed by Dolby Laboratories. It expands on existing surround sound systems by adding height channels, allowing sounds to be interpreted as three-dimensional objects.

??? example "json"

    ```json
    {
        "trash_id": "496f355514737f7d83bf7aa4d24f8169",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### DTS X

<sub><sub><sub>Score [490]</sub>

>DTS:X is an object-based audio codec, which aims to create a multi-dimensional sound that “moves around you like it would in real life”

??? example "json"

    ```json
    {
        "trash_id": "2f22d89048b01681dde8afe203bf2e95",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### ATMOS (undefined)

<sub><sub><sub>Score [480]</sub>

>Handles cases where only Atmos is specified in title but not DD+ or TrueHD (Where it is not specified if it is Lossy or Lossless)

!!! note
    Give this the same score as Lossy Atmos, and then on import, it will get changed to either lossy or lossless based on mediainfo.

??? example "json"

    ```json
    {
        "trash_id": "417804f7f2c4308c1f4c5d380d4c4475",
        "name": "ATMOS (undefined)",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### DD+ ATMOS

<sub><sub><sub>Score [480]</sub>

>Atmos via UHD Blu-ray will be lossless, or lossy via streaming services so in this case it will be lossy + Atmos

??? example "json"

    ```json
    {
        "trash_id": "1af239278386be2919e1bcee0bde047e",
        "name": "DD+ ATMOS",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### TrueHD

<sub><sub><sub>Score [470]</sub>

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_TrueHD){:target="_blank" rel="noopener noreferrer"}
>
>Dolby TrueHD is a lossless, multi-channel audio codec developed by Dolby Laboratories for home video, used principally in Blu-ray Disc and compatible hardware.

??? example "json"

    ```json
    {
        "trash_id": "3cafb66171b47f226146a0770576870f",
        "name": "TrueHD",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD MA

<sub><sub><sub>Score [460]</sub>

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/DTS-HD_Master_Audio){:target="_blank" rel="noopener noreferrer"}
>
>DTS-HD Master Audio is a multi-channel, lossless audio codec developed by DTS as an extension of the lossy DTS Coherent Acoustics codec (DTS CA; usually itself referred to as just DTS). Rather than being an entirely new coding mechanism, DTS-HD MA encodes an audio master in lossy DTS first, then stores a concurrent stream of supplementary data representing whatever the DTS encoder discarded. This gives DTS-HD MA a lossy "core" able to be played back by devices that cannot decode the more complex lossless audio. DTS-HD MA's primary application is audio storage and playback for Blu-ray Disc media.

??? example "json"

    ```json
    {
        "trash_id": "dcf3ec6938fa32445f590a4da84256cd",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### FLAC

<sub><sub><sub>Score [450]</sub>

>FLAC stands for Free Lossless Audio Codec, an audio format similar to MP3, but lossless, meaning that audio is compressed in FLAC without any loss in quality. This is similar to how Zip works, except with FLAC you will get much better compression because it is designed specifically for audio

??? example "json"

    ```json
    {
        "trash_id": "a570d4a0e56a2874b64e5bfa55202a1b",
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
                    "value": "[^-]dd[p+]|eac3"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### PCM

<sub><sub><sub>Score [450]</sub>

>PCM is the method of encoding typically used for uncompressed digital audio

??? example "json"

    ```json
    {
        "trash_id": "e7c2fcae07cbada050a0af3357491d7b",
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
                    "value": "[^-]dd[p+]|eac3"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### DTS-HD HRA

<sub><sub><sub>Score [440]</sub>

>Description placeholder

??? example "json"

    ```json
    {
        "trash_id": "8e109e50e0a0b83a5098b056e13bf6db",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### Dolby Digital Plus

<sub><sub><sub>Score [430]</sub>

<sub>Dolby Digital Plus = DD+</sub>
>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital_Plus){:target="_blank" rel="noopener noreferrer"}
>
>Dolby Digital Plus, also known as Enhanced AC-3 (and commonly abbreviated as DD+ or E-AC-3, or EC-3) is a digital audio compression scheme developed by Dolby Labs for transport and storage of multi-channel digital audio. It is a successor to Dolby Digital (AC-3).

??? example "json"

    ```json
    {
        "trash_id": "185f1dd7264c4562b9022d963ac37424",
        "name": "DD+",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
                "name": "Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### DTS-ES

<sub><sub><sub>Score [420]</sub>

>DTS-ES (DTS Extended Surround) includes two variants, DTS-ES Discrete 6.1, and DTS-ES Matrix 5.1, depending on how the sound was originally mastered and stored.

??? example "json"

    ```json
    {
        "trash_id": "f9f847ac70a0af62ea4a08280b859636",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### Basic DTS

<sub><sub><sub>Score [410]</sub>

<sub>Basic DTS = DTS</sub>
>Description placeholder

??? example "json"

    ```json
    {
        "trash_id": "1c1a4c5e823891c75bc50380a6866f73",
        "name": "DTS",
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
                    "value": "dts.?(hd|ma|es|hi|hr)"
                }
            },
            {
                "name": "Not Dolby Digital Plus",
                "implementation": "ReleaseTitleSpecification",
                "negate": true,
                "required": true,
                "fields": {
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### AAC

<sub><sub><sub>Score [400]</sub>

Advanced Audio Coding
>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
>Advanced Audio Coding (AAC) is an audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves higher sound quality than MP3 at the same bit rate.

??? example "json"

    ```json
    {
        "trash_id": "240770601cc226190c367ef59aba7463",
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
                    "value": "[^-]dd[p+]|eac3"
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

<sub><sup>[TOP](#index)</sup>

------

### Basic Dolby Digital

<sub><sub><sub>Score [390]</sub>

<sub>Basic Dolby Digital = DD</sub>
>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dolby_Digital){:target="_blank" rel="noopener noreferrer"}
>
>Dolby Digital, also known as Dolby AC-3, the audio compression is lossy.

??? example "json"

    ```json
    {
        "trash_id": "c2998bd0d90ed5621d8df281e839436e",
        "name": "DD",
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

<sub><sup>[TOP](#index)</sup>

------

### MP3

>Description placeholder

??? example "json"

    ```json
    {
        "trash_id": "6ba9033150e7896bdc9ec4b44f2b230f",
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

<sub><sup>[TOP](#index)</sup>

------

### Opus

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}
>
>Opus is a lossy audio coding format developed by the Xiph.Org Foundation and standardized by the Internet Engineering Task Force, designed to efficiently code speech and general audio in a single format, while remaining low-latency enough for real-time interactive communication and low-complexity enough for low-end embedded processors.Opus replaces both Vorbis and Speex for new applications, and several blind listening tests have ranked it higher-quality than any other standard audio format at any given bitrate until transparency is reached, including MP3, AAC, and HE-AAC

??? example "json"

    ```json
    {
        "trash_id": "a061e2e700f81932daf888599f8a8273",
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

<sub><sup>[TOP](#index)</sup>

------

## Audio Channels

------

### 1.0 Mono

??? example "json"

    ```json
    {
        "trash_id": "b124be9b146540f8e62f98fe32e49a2a",
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

<sub><sup>[TOP](#index)</sup>

------

### 2.0 Stereo

??? example "json"

    ```json
    {
        "trash_id": "89dac1be53d5268a7e10a19d3c896826",
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

<sub><sup>[TOP](#index)</sup>

------

### 3.0 Sound

??? example "json"

    ```json
    {
        "trash_id": "205125755c411c3b8622ca3175d27b37",
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

<sub><sup>[TOP](#index)</sup>

------

### 4.0 Sound

??? example "json"

    ```json
    {
        "trash_id": "373b58bd188fc00c817bd8c7470ea285",
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

<sub><sup>[TOP](#index)</sup>

------

### 5.1 Surround

??? example "json"

    ```json
    {
        "trash_id": "77ff61788dfe1097194fd8743d7b4524",
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

<sub><sup>[TOP](#index)</sup>

------

### 6.1 Surround

??? example "json"

    ```json
    {
        "trash_id": "6fd7b090c3f7317502ab3b63cc7f51e3",
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

<sub><sup>[TOP](#index)</sup>

------

### 7.1 Surround

??? example "json"

    ```json
    {
        "trash_id": "e77382bcfeba57cb83744c9c5449b401",
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

<sub><sup>[TOP](#index)</sup>

------

### 9.1 Surround

??? example "json"

    ```json
    {
        "trash_id": "f2aacebe2c932337fe352fa6e42c1611",
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

<sub><sup>[TOP](#index)</sup>

------

## HDR metadata

------

### Dolby Vision

<sub><sub><sub>Score [300]</sub>

<sub>Dolby Vision = DoVi</sub>
>Dolby Vision is a content mastering and delivery format similar to the HDR10 media profile.
>
>Dolby Vision is a proprietary, dynamic HDR format developed by Dolby Labs. By adjusting the picture on a scene-by-scene (and even frame-by-frame) basis, it lets you see more detail with better color accuracy. It is constantly making adjustments so that each image on the screen is optimized.

??? example "json"

    ```json
    {
        "trash_id": "5d96ce331b98e077abb8ceb60553aa16",
      "name": "DoVi",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Dolby Vision",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": "\\b(dv|dovi|dolby[ .]vision)\\b"
          }
        },
        {
          "name": "DoVi-SL: Dolby Vision (Single Layer)",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "\\b(sl[ .]dv|single[ .]layer[ .]dovi)\\b"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

#### Dolby Vision (no WEB-DL)

!!! NOTE

    **You shouldn't use both but choose which one you want to use for your use case !!!**

    Use the same scoring that you would use for Dolby Vision normally.

<sub>Dolby Vision = DoVi</sub>
>This is a special Custom Format that ignores DV for WEB-DL but allows for other sources.
>
>WEB-DL from Streaming Services don't have the fallback to HDR(10), What can results in weird playback issues like weird colors if you want to play it on a not DoVi compatible setup.
>Remuxes and Bluray have a fallback to HDR(10).

??? example "json"

    ```json
    {
        "trash_id": "923b6abef9b17f937fab56cfcf89e1f1",
      "name": "DoVi",
      "includeCustomFormatWhenRenaming": true,
      "specifications": [
        {
          "name": "Dolby Vision",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": "\\b(dv|dovi|dolby[ .]vision)\\b"
          }
        },
        {
          "name": "WEBDL",
          "implementation": "SourceSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": 7
          }
        },
        {
          "name": "WEBRIP",
          "implementation": "SourceSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": 8
          }
        },
        {
          "name": "Dolby Vision (Single Layer)",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "\\b(sl[ .]dv|single[ .]layer[ .]dovi)\\b"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### Dolby Vision (Single Layer)

<sub><sub><sub>Score [295]</sub>

<sub>Dolby Vision (Single Layer) = DoVi (SL)</sub>
>Custom Format for Single Layer Dolby Vision releases.

!!! note

    This used to be the the preferred option for PLeX with a Shield 2019 model that supports DV.

    But now DV is part of the MKV spec and ExoPlayer added native support.

??? example "json"

    ```json
    {
        "trash_id": "462c511637953269a9053d1ed1ffc3a5",
        "name": "DoVi (SL)",
        "includeCustomFormatWhenRenaming": true,
        "specifications": [{
                "name": "Dolby Vision (Single Layer)",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": true,
                "fields": {
                    "value": "\\b(sl[ .]dv|single[ .]layer[ .]dovi)\\b"
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

<sub><sup>[TOP](#index)</sup>

------

### HDR

<sub><sub><sub>Score [290]</sub>

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}
>
>High-dynamic-range video (HDR video) is video having a dynamic range greater than that of standard-dynamic-range video (SDR video).HDR video involves capture, production, content/encoding, and display. HDR capture and displays are capable of brighter whites and deeper blacks. To accommodate this, HDR encoding standards allow for a higher maximum luminance and use at least a 10-bit dynamic range (color depth, compared to 8-bit for non-professional and 10-bit for professional SDR video) in order to maintain precision across this extended range.

??? example "json"

    ```json
    {
        "trash_id": "e61e28db95d22bedcadf030b8f156d96",
      "name": "HDR",
      "includeCustomFormatWhenRenaming": false,
      "specifications": [
        {
          "name": "HDR",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": "\\bHDR(\\b|\\d)"
          }
        },
        {
          "name": "DoVi",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "\\b(dv|dovi|dolby[ .]vision)\\b"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### HDR (undefined)

<sub><sub><sub>Score [290]</sub>

>Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.
>
>For now it's only FraMeSToR that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "json"

    ```json
    {
        "trash_id": "2a4d9069cc1fe3242ff9bdaebed239bb",
      "name": "HDR (undefined)",
      "includeCustomFormatWhenRenaming": false,
      "specifications": [
        {
          "name": "FraMeSToR",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": "\\bFraMeSToR\\b"
          }
        },
        {
          "name": "2160p",
          "implementation": "ResolutionSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": 2160
          }
        },
        {
          "name": "HDR: HDR",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "\\bHDR(\\b|\\d)"
          }
        },
        {
          "name": "DoVi: Dolby Vision",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "\\b(dv|dovi)\\b|dolby.?vision"
          }
        },
        {
          "name": "SDR: SDR",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "\\bSDR(\\b|\\d)"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### 10 Bit

??? example "json"

    ```json
    {
        "trash_id": "e114f2f915fa2414b60683cd73c554f3",
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

<sub><sup>[TOP](#index)</sup>

------

## Movie Versions

------

### Hybrid

<sub><sub><sub>Score [200]</sub>

>A hybrid release means any combination of sources (video + audio) and not a direct encode of a single source. Generally you can be sure that any hybrid that has been put together is the best quality release of a particular title.

??? example "json"

    ```json
    {
        "trash_id": "0f12c086e289cf966fa5948eac571f44",
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

<sub><sup>[TOP](#index)</sup>

------

### Remaster

<sub><sub><sub>Score [190]</sub>

>[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}
>
>For the software term, see Software remastering.
Remaster (also digital remastering and digitally remastered) refers to changing the quality of the sound or of the image, or both, of previously created recordings, either audiophonic, cinematic, or videographic.

??? example "json"

    ```json
    {
        "trash_id": "570bc9ebecd92723d2d21500f4be314c",
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

<sub><sup>[TOP](#index)</sup>

------

### 4K Remaster

<sub><sub><sub>Score [190]</sub>

>A remastered or mastered in 4K should give you usually the best picture and audio currently for the movie. Both are just names to describe the best possible currently for the movie.
>
>To be clear, the final digital films on the Mastered in 4K Blu-rays still only have the same 1920 x 1080 pixels of actual resolution as normal Blu-rays. But the argument goes that because these full HD files were derived from higher-resolution masters, their images will be more precise, with better colours, less noise, and enhanced sharpness and detail. Not least because the higher-resolution mastering process will provide more detail from the original print for the Blu-ray masters to draw on when going through their (hopefully…) frame-by-frame compression process.
>
>Another important element of the Mastered in 4K discs is that they’re all mastered with ‘x.v.YCC’ colour specification. This delivers an expanded colour range closer to that contained in original source material.

??? example "json"

    ```json
    {
        "trash_id": "eca37840c13c6ef2dd0262b141a5482f",
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

<sub><sup>[TOP](#index)</sup>

------

### Criterion Collection

<sub><sub><sub>Score [170]</sub>

>The Criterion Collection, Inc. (or simply Criterion) is an American home video distribution company which focuses on licensing "important classic and contemporary films" and selling them to film aficionados.Criterion has helped to standardize characteristics of home video such as film restoration, using the letterbox format for widescreen films, and adding bonus features and commentary tracks.

??? example "json"

    ```json
    {
        "trash_id": "e0c07d59beb37348e975a930d5e50319",
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

<sub><sup>[TOP](#index)</sup>

------

### Theatrical Cut

>The Theatrical Cut is the version of the film that was shown at cinemas.

??? example "json"

    ```json
    {
        "trash_id": "e9001909a4c88013a359d0b9920d7bea",
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

<sub><sup>[TOP](#index)</sup>

------

### Special Edition

<sub><sub><sub>Score [180]</sub>

>Custom format for several Special Editions
>
> - The Director's Cut is the version edited by the Director, usually for additional home media releases.
> - An Extended Cut is usually any version of the film which is longer than the theatrical cut (though in very rare cases, its shorter).

??? example "json"

    ```json
    {
        "trash_id": "957d0f44b592285f26449575e8b1167e",
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

<sub><sup>[TOP](#index)</sup>

------

### IMAX

<sub><sub><sub>Score [190]</sub>

>Description placeholder

??? example "json"

    ```json
    {
        "trash_id": "eecf3a857724171f968a66cb5719e152",
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

<sub><sup>[TOP](#index)</sup>

------

## Misc (-1000)

------

### BR-DISK

<sub><sub><sub>Score [-9999]</sub>

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
    {
        "trash_id": "ed38b889b31be83fda192888e2286d83",
      "name": "BR-DISK",
      "includeCustomFormatWhenRenaming": false,
      "specifications": [
        {
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
          "required": true,
          "fields": {
            "value": 5
          }
        },
        {
          "name": "WEBDL",
          "implementation": "SourceSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": 7
          }
        },
        {
          "name": "WEBRIP",
          "implementation": "SourceSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": 8
          }
        },
        {
          "name": "x265/HEVC",
          "implementation": "ReleaseTitleSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": "[xh]\\.?265|\\bHEVC(\\b|\\d)"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### EVO except WEB-DL

<sub><sub><sub>Score [-9999]</sub>

<sub>EVO except WEB-DL = EVO (no WEB-DL)</sub>
>This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
>
>You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000` or even `-9999`

??? example "json"

    ```json
    {
        "trash_id": "90cedc1fea7ea5d11298bebd3d1d3223",
      "name": "EVO (no WEB-DL)",
      "includeCustomFormatWhenRenaming": false,
      "specifications": [
        {
          "name": "EVO",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": true,
          "fields": {
            "value": "\\bEVO\\b"
          }
        },
        {
          "name": "WEBDL",
          "implementation": "SourceSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": 7
          }
        },
        {
          "name": "WEBRIP",
          "implementation": "SourceSpecification",
          "negate": true,
          "required": true,
          "fields": {
            "value": 8
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### LQ-Releases

<sub><sub><sub>Score [-9999]</sub>

<sub>Low Quality Releases = LQ</sub>
>A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality.

!!! note

    You might want to add the following also [EVO except WEB-DL](#evo-except-web-dl)

    - BLOCK1 = Low-Quality Releases (often banned groups)
    - BLOCK2 = Another Small list of often banned groups.
    - BLOCK3 = And Another list.
    - BLOCK4 = Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.
    - BLOCK5 = RiffTrax is an American company that produces scripted humorous audio commentary tracks intended to be played in unison with particular television programs and films, In short just annoying !!!

??? example "json"

    ```json
    {
        "trash_id": "90a6f9a284dff5103f6346090e6280c8",
      "name": "LQ",
      "includeCustomFormatWhenRenaming": false,
      "specifications": [
        {
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
            "value": "\\bRARBG\\b|\\bFGT\\b|-BReWeRS|-Grym|-LiGaS|-Zeus|-Tigole"
          }
        },
        {
          "name": "[BLOCK4]",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": "-beAst|\\bCHD\\b|-HDWinG|\\bMTeam\\b|-MySiLU|-WiKi"
          }
        },
        {
          "name": "[BLOCK5]",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": "\\bRifftrax\\b|\\bRU4HD\\b"
          }
        }
      ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### 720/1080p no x265

<sub><sub><sub>Score [-9999]</sub>

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
    {
        "trash_id": "dc98083864ea246d05a42df0d05f81cc",
     "name": "x265 (720/1080p)",
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

<sub><sup>[TOP](#index)</sup>

------

### 3D

<sub><sub><sub>Score [-9999]</sub>

>If you prefer or not prefer 3D.
>
>You can use Custom Format or use Restrictions (`Settings` => `Indexers` => `Restrictions`) what ever you prefer.

??? example "json"

    ```json
    {
        "trash_id": "b8cd450cbfa689c0259a01d9e29ba3d6",
        "name": "3D",
        "includeCustomFormatWhenRenaming": false,
        "specifications": [{
            "name": "3D",
            "implementation": "ReleaseTitleSpecification",
            "negate": false,
            "required": true,
            "fields": {
                "value": "\\b3d\\b|\\bsbs\\b|half[ .]ou"
            }
        }]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

## Misc

------

### HQ-Releases

<sub><sub><sub>Score [100]</sub>

<sub>HQ-Releases = HQ</sub>
>A collection of P2P groups that are known for their high quality releases.

??? example "json"

    ```json
    {
        "trash_id": "1c7d7b04b15cc53ea61204bebbcc1ee2",
        "name": "HQ",
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
                "name": "[BLOCK4]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "\\bBHDStudio\\b"
                }
            },
            {
                "name": "[Remux Groups]",
                "implementation": "ReleaseTitleSpecification",
                "negate": false,
                "required": false,
                "fields": {
                    "value": "-FraMeSToR|-EPSiLON|\\bKRaLiMaRKo\\b|-PmP|-BLURANiUM|-SiCFoI|-SURFINBIRD"
                }
            }
        ]
    }
    ```

<sub><sup>[TOP](#index)</sup>

------

### Repack Proper

<sub><sub><sub>Score [1]</sub>

??? example "json"

    ```json
    {
        "trash_id": "e7718d7a3ce595f289bfee26adc178f5",
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

<sub><sup>[TOP](#index)</sup>

------

### Streaming Services

>Collection of Streaming Services

!!! attention

    This CF only prefers the known streaming services and doesn't work the same way like the release profile that can be used in Sonarr to include the streaming service name in your renaming scheme when using `{[Custom Formats]}` !!!
    If you want to have this option then you need to add them all separate.

??? example "json"

    ```json
    {
        "trash_id": "fd7da02c647dd3f1b6757e150fffc5ff",
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

<sub><sup>[TOP](#index)</sup>

------

### x264

>x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

If you want maximum compatibility and have much better direct play support then use x264 for 720p/1080p

??? example "json"

    ```json
    {
        "trash_id": "2899d84dc9372de3408e6d8cc18e9666",
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

<sub><sup>[TOP](#index)</sup>

------

### x265

>x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

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

That's why I created my own golden rule.

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
        "trash_id": "9170d55c319f4fe40da8711ba9d8050d",
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

<sub><sup>[TOP](#index)</sup>

------

### FreeLeech

<sub><sub><sub>Score [5]</sub>

>Sometimes, torrent sites set a torrent to be freeleech. This means, that the download of this torrent will not count towards your download quota or ratio. This is really useful, if you do not have the best ratio yet.

!!! attention
    Keep in mind not all trackers support this option.

??? example "json"

    ```json
    {
        "trash_id": "0d91270a7255a1e388fa85e959f359d8",
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

<sub><sup>[TOP](#index)</sup>

------

### Dutch Groups

>If you prefer movies with also a Dutch audio track.

??? example "json"

    ```json
    {
        "trash_id": "9de657fd3d327ecf144ec73dfe3a3e9a",
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

<sub><sup>[TOP](#index)</sup>

------

### Anime Dual Audio

??? example "json"

    ```json
    {
        "trash_id": "4a3b087eea2ce012fcc1ce319259a3be",
      "name": "Anime Dual Audio",
      "includeCustomFormatWhenRenaming": false,
      "specifications": [
        {
          "name": "Dual Audio",
          "implementation": "ReleaseTitleSpecification",
          "negate": false,
          "required": false,
          "fields": {
            "value": "dual.?audio"
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

<sub><sup>[TOP](#index)</sup>

------

### MPEG2

??? example "json"

    ```json
    {
        "trash_id": "ff86c4326018682f817830ced463332b",
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

<sub><sup>[TOP](#index)</sup>

------

### Multi

??? example "json"

    ```json
    {
        "trash_id": "4b900e171accbfb172729b63323ea8ca",
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

<sub><sup>[TOP](#index)</sup>
