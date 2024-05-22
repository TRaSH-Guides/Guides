This blocks all 720/1080p (HD) releases that are encoded in x265.

In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-hd']['trash_scores']['default'] }}`

??? question "Why block 720/1080p encodes in x265? - [Click to show/hide]"

    --8<-- "includes/docker/x265.md"

{! include-markdown "../../includes/cf-descriptions/x265-hd-radarr-warning.md" !}
