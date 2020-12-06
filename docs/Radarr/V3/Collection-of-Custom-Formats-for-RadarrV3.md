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

| Audio                                    | Audio Channels               | Audio Advanced                                | Video                                                     | Video Advanced                                | Misc                                          |
| :--------------------------------------- | ---------------------------- | --------------------------------------------- | --------------------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [1.0 Mono](#10-mono)         | [ATMOS (indeterminate)](#atmos-indeterminate) | [3D](#3d)                                                 | [Remaster](#remaster)                         | [BR-DISK](#br-disk)                           |
| [DTS-HD/DTS:X](#dts-hddtsx)              | [2.0 Stereo](#20-stereo)     | [Basic Dolby Digital](#basic-dolby-digital)   | [x264](#x264)                                             | [4K Remaster](#4k-remaster)                   | [EVO except WEB-DL](#evo-except-web-dl)       |
| [Surround Sounds](#surround-sounds)      | [3.0 Sound](#30-sound)       | [Basic DTS](#basic-dts)                       | [x265](#x265)                                             | [Criterion Collection](#criterion-collection) | [Low Quality Releases](#low-quality-releases) |
|                                          | [4.0 Sound](#40-sound)       | [DD+ ATMOS (lossy)](#dd-atmos-lossy)          | [Dolby Vision](#dolby-vision)                             | [Theatrical Cut](#theatrical-cut)             | [Repack/Proper](#repack-proper)               |
| [AAC](#aac)                              | [5.1 Surround](#51-surround) | [Dolby Digital Plus](#dolby-digital-plus)     | [Dolby Vision (Single Layer)](#dolby-vision-single-layer) | [Special Editions](#special-edition)          | [Anime Dual Audio](#anime-dual-audio)         |
| [FLAC](#flac)                            | [6.1 Surround](#61-surround) | [DTS X](#dts-x)                               | [HDR](#hdr)                                               |                                               | [Hybrid](#hybrid)                             |
| [MP3](#mp3)                              | [7.1 Surround](#71-surround) | [DTS-ES](#dts-es)                             | [10 Bit](#10-bit)                                         | [Streaming Services](#streaming-services)     | [Multi](#multi)                               |
| [PCM](#pcm)                              | [9.1 Surround](#91-surround) | [DTS-HD HRA](#dts-hd-hra)                     | [MPEG2](#mpeg2)                                           | [Dutch Groups](#dutch-groups)                 | [FreeLeech](#freeleech)                       |
| [Opus](#opus)                            |                              | [DTS-HD MA](#dts-hd-ma)                       |                                                           | [HQ-P2P](#hq-p2p)                             |                                               |
|                                          |                              | [TrueHD (not ATMOS)](#truehd-not-atmos)       |                                                           |                                               |                                               |
|                                          |                              | [TrueHD ATMOS](#truehd-atmos)                 |                                                           |                                               |                                               |

------

## BR-DISK

This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

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

!!! note

    Depending on your renaming scheme it could happen that Radarr will match renamed files after they are downloaded and imported as `BR-DISK`,
    This is a cosmetic annoyance till I come up for another way to solve this,
    being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
    Several reasons why this is happening:

    - Blame the often wrongly used naming of x265 encodes.
    - Radarr v3 uses dynamic custom formats.

------

## Dolby TrueHD/ATMOS

If you prefer TrueHD|Atmos audio tracks.

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

------

## DTS-HD/DTS:X

If you prefer DTS-HD/DTS:X audio tracks.

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

------

## Dolby Vision (Single Layer)

Custom Format for Single Layer Dolby Vision releases.

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

!!! note

    This seems the preferred option for PLeX with a Shield 2019 model that supports DV.

    But keep in mind it also depends on how the releaser names the files!
    Shield can play any Single Layer DV in a .ts container via Plex natively.  It can also play most Single Layer in .mkv but only via PlexForKodi with a modded version of exoplayer.

    An incompatible variant should still play as HDR10 in most clients.

    **UPDATE:** DV is part of the MKV spec now and ExoPlayer added native support so hopefully coming soon.

------

## Special Edition

Custom format for several Special Editions

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

------

## HDR

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

------

## x264

x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264) compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

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

------

## x265

x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265) compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

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

### Some extra info about 4K/X265

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

------

## Low Quality Releases

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

!!! note

    You might want to add the following also [EVO except WEB-DL](#evo-except-web-dl)

    - BLOCK1 = Low-Quality Releases (often banned groups)
    - BLOCK2 = Another Small list of often banned groups.
    - BLOCK3 = And Another list.
    - BLOCK4 = Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.

------

## EVO except WEB-DL

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

------

## 3D

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

------

## 4K Remaster

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

------

## Anime Dual Audio

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

------

## ATMOS (indeterminate)

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

------

## Basic Dolby Digital

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

------

## Basic DTS

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

------

## Criterion Collection

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

------

## DD+ ATMOS (lossy)

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

------

## Dolby Digital Plus

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

------

## Dolby Vision

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

------

## DTS X

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

------

## DTS-ES

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

------

## DTS-HD HRA

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

------

## DTS-HD MA

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

------

## Hybrid

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

------

## Multi

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

------

## Remaster

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

------

## Repack Proper

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

------

## Surround Sounds

If you prefer all kind of surround sounds

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

------

## Theatrical Cut

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

------

## TrueHD (not ATMOS)

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

------

## TrueHD ATMOS

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

------

## FreeLeech

Sometimes, torrent sites set a torrent to be freeleech. This means, that the download of this torrent will not count towards your download quota or ratio. This is really useful, if you do not have the best ratio yet.

!!! warning
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

------

## 1.0 Mono

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

------

## 2.0 Stereo

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

------

## 3.0 Sound

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

------

## 4.0 Sound

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

------

## 5.1 Surround

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

------

## 6.1 Surround

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

------

## 7.1 Surround

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

------

## 9.1 Surround

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

------

## AAC

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

------

## FLAC

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

------

## MP3

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

------

## MPEG2

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

------

## Opus

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

------

## PCM

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

------

## 10 Bit

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

------

## Dutch Groups

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

------

## Streaming Services

Collection of Streaming Services

??? example "json"

    ```json
    {
        "name": "Streaming Services",
        "includeCustomFormatWhenRenaming": true,
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

------

## HQ-P2P

A collection of P2P groups that are knows for their high quality releases

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
