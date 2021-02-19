# Radarr-CF-Movie-Versions

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

[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Remaster){:target="_blank" rel="noopener noreferrer"}

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
