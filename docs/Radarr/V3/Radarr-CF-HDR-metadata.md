# Radarr-CF-HDR-metadata

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

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding){:target="_blank" rel="noopener noreferrer"}

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

### HDR (indeterminate)

Some groups don't add HDR to their 4K release name so I suggest to add this Custom Format at the same score as you add one of your HDR Custom Formats.

For now it's only FraMeSToR that doesn't add HDR to their release name but in the feature we can add more to it if needed.

??? example "json"

    ```json
    {
      "name": "HDR (indeterminate)",
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
            "value": "\\b(DV|dovi)\\b|dolby.?vision"
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
