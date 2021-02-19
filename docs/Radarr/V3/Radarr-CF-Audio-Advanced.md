# Radarr-CF-Audio-Advanced

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

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}

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

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Opus_(audio_format)){:target="_blank" rel="noopener noreferrer"}

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
