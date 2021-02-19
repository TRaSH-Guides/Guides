# Radarr-CF-Misc-1000

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

That's why I created my own golden rule.

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
