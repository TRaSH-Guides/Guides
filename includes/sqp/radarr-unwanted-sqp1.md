??? abstract "Unwanted - [Click to show/hide]"

    | Custom Format                                                                                                             |                                 Score                                  | Trash ID                                                |
    | ------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------: | ------------------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)                             |        {{ radarr['cf']['br-disk']['trash_scores']['default'] }}        | {{ radarr['cf']['br-disk']['trash_id'] }}               |
    | [{{ radarr['cf']['generated-dynamic-hdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#generated-dynamic-hdr) | {{ radarr['cf']['generated-dynamic-hdr']['trash_scores']['default'] }} | {{ radarr['cf']['generated-dynamic-hdr']['trash_id'] }} |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                                       |          {{ radarr['cf']['lq']['trash_scores']['default'] }}           | {{ radarr['cf']['lq']['trash_id'] }}                    |
    | [{{ radarr['cf']['lq-release-title']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq-release-title)           |   {{ radarr['cf']['lq-release-title']['trash_scores']['default'] }}    | {{ radarr['cf']['lq-release-title']['trash_id'] }}      |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning:                   |        {{ radarr['cf']['x265-hd']['trash_scores']['default'] }}        | {{ radarr['cf']['x265-hd']['trash_id'] }}               |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                                       |          {{ radarr['cf']['3d']['trash_scores']['default'] }}           | {{ radarr['cf']['3d']['trash_id'] }}                    |
    | [{{ radarr['cf']['extras']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#extras)                               |        {{ radarr['cf']['extras']['trash_scores']['default'] }}         | {{ radarr['cf']['extras']['trash_id'] }}                |
    | [{{ radarr['cf']['10bit']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#10bit)                                 |       {{ radarr['cf']['10bit']['trash_scores']['sqp-1-1080p'] }}       | {{ radarr['cf']['10bit']['trash_id'] }}                 |
    | [{{ radarr['cf']['av1']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#av1)                                     |          {{ radarr['cf']['av1']['trash_scores']['default'] }}          | {{ radarr['cf']['av1']['trash_id'] }}                   |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['generated-dynamic-hdr']['name'] }} :** A collection of groups who are known to generate their own dynamic HDR metadata - Dolby Vision and/or HDR10+.
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known low-quality groups that are often banned from the top trackers due to their releases' lack of quality or other reasons.
    - **{{ radarr['cf']['lq-release-title']['name'] }}:** A collection of terms seen in the titles of low-quality releases that are not captured by using a release group name.
    - **{{ radarr['cf']['x265-hd']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265.

        {! include-markdown "../../includes/cf-descriptions/x265-hd-radarr-warning.md" !}

    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['extras']['name'] }}:** Blocks releases that only contain extras
    - **{{ radarr['cf']['10bit']['name'] }}:** Blocks releases that use Hi10P
    - **{{ radarr['cf']['av1']['name'] }}:** This blocks all releases encoded in AV1.

        {! include-markdown "../../includes/cf-descriptions/av1.md" !}
