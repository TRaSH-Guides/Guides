# Radarr-CF-Misc

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
                    "value": "-FraMeSToR|-EPSiLON|\\bKRaLiMaRKo\\b"
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

x264 is a *free software library* and *application* for encoding video streams into the [H.264/MPEG-4 AVC](https://en.wikipedia.org/wiki/H.264){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

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

x265 is a *free software library* and *application* for encoding video streams into the [H.265/MPEG-H HEVC](http://en.wikipedia.org/wiki/H.265){:target="_blank" rel="noopener noreferrer"} compression format, and is released under the terms of the [GNU GPL](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html){:target="_blank" rel="noopener noreferrer"}.

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
