This blocks most 720/1080p (HD) releases that are encoded in x265, **But it will allow 720/1080p x265 releases if they have HDR and/or DV**

*Since some NF releases won't be released as 4k, this allows you to still have the DV/HDR releases.*

In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}`

??? question "Why block 720/1080p encodes in x265? - [Click to show/hide]"

    --8<-- "includes/docker/x265.md"

{! include-markdown "../../includes/cf-descriptions/x265-no-hdrdv-radarr-warning.md" !}
