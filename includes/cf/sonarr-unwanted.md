??? abstract "Unwanted - [Click to show/hide]"

    | Custom Format                                                                                                   |                               Score                               | Trash ID                                           |
    | --------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------: | -------------------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk)                   |     {{ sonarr['cf']['br-disk']['trash_scores']['default'] }}      | {{ sonarr['cf']['br-disk']['trash_id'] }}          |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq)                             |        {{ sonarr['cf']['lq']['trash_scores']['default'] }}        | {{ sonarr['cf']['lq']['trash_id'] }}               |
    | [{{ sonarr['cf']['lq-release-title']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq-release-title) | {{ sonarr['cf']['lq-release-title']['trash_scores']['default'] }} | {{ sonarr['cf']['lq-release-title']['trash_id'] }} |
    | [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd) :warning:         |     {{ sonarr['cf']['x265-hd']['trash_scores']['default'] }}      | {{ sonarr['cf']['x265-hd']['trash_id'] }}          |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#extras)                     |      {{ sonarr['cf']['extras']['trash_scores']['default'] }}      | {{ sonarr['cf']['extras']['trash_id'] }}           |
    | [{{ sonarr['cf']['av1']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#av1)                           |       {{ sonarr['cf']['av1']['trash_scores']['default'] }}        | {{ sonarr['cf']['av1']['trash_id'] }}              |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }} :** This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ sonarr['cf']['lq']['name'] }}:** A collection of known low-quality groups that are often banned from the top trackers due to their releases' lack of quality or other reasons.
    - **{{ sonarr['cf']['lq-release-title']['name'] }}:** A collection of terms seen in the titles of low-quality releases that are not captured by using a release group name.
    - **{{ sonarr['cf']['x265-hd']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265.

        {! include-markdown "../../includes/cf-descriptions/x265-hd-sonarr-warning.md" !}

    - **{{ sonarr['cf']['extras']['name'] }}:** This blocks/ignores extras
    - **{{ sonarr['cf']['av1']['name'] }}:** This blocks all releases encoded in AV1.

        {! include-markdown "../../includes/cf-descriptions/av1.md" !}
