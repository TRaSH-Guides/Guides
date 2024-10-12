??? abstract "Unwanted - [Click to show/hide]"

    | Custom Format                                                                                                   |                               Score                               | Trash ID                                           |
    |-----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------:|----------------------------------------------------|
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk)                   |     {{ sonarr['cf']['br-disk']['trash_scores']['default'] }}      | {{ sonarr['cf']['br-disk']['trash_id'] }}          |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq)                             |        {{ sonarr['cf']['lq']['trash_scores']['default'] }}        | {{ sonarr['cf']['lq']['trash_id'] }}               |
    | [{{ sonarr['cf']['lq-release-title']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq-release-title) | {{ sonarr['cf']['lq-release-title']['trash_scores']['default'] }} | {{ sonarr['cf']['lq-release-title']['trash_id'] }} |
    | [{{ sonarr['cf']['french-lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-lq)                   |    {{ sonarr['cf']['french-lq']['trash_scores']['default'] }}     | {{ sonarr['cf']['french-lq']['trash_id'] }}        |
    | [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd) :warning:         |     {{ sonarr['cf']['x265-hd']['trash_scores']['default'] }}      | {{ sonarr['cf']['x265-hd']['trash_id'] }}          |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#extras)                     |      {{ sonarr['cf']['extras']['trash_scores']['default'] }}      | {{ sonarr['cf']['extras']['trash_id'] }}           |
    | [{{ sonarr['cf']['av1']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#av1)                           |       {{ sonarr['cf']['av1']['trash_scores']['default'] }}        | {{ sonarr['cf']['av1']['trash_id'] }}              |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }} :** This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ sonarr['cf']['lq']['name'] }}:** A collection of known low-quality groups that are often banned from the top trackers due to their releases' lack of quality or other reasons.
    - **{{ sonarr['cf']['lq-release-title']['name'] }}:** A collection of terms seen in the titles of low-quality releases that are not captured by using a release group name.
    - **{{ sonarr['cf']['french-lq']['name'] }}:** A collection of known low-quality French groups that are often banned from the top trackers due to their releases' lack of quality or other reasons.
    - **{{ sonarr['cf']['x265-hd']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265.

        {! include-markdown "../../includes/cf-descriptions/x265-hd-sonarr-warning.md" !}

    - **{{ sonarr['cf']['extras']['name'] }}:** This blocks/ignores extras
    - **{{ sonarr['cf']['av1']['name'] }}:** This blocks all releases encoded in AV1.

        {! include-markdown "../../includes/cf-descriptions/av1.md" !}

    ??? warning "Type of FanSubs - [Click to show/hide]"

        Those Custom Formats are optionals and allow to know which type of FanSubs your releases have. Only the `FastSub` is not wanted as it is often done too quickly and are often not well done. If you do not want FanSub either you should also score it to {{ sonarr['cf']['fastsub']['trash_scores']['default'] }}.

        | Custom Format                                                                                 |                          Score                           | Trash ID                                  |
        |-----------------------------------------------------------------------------------------------|:--------------------------------------------------------:|-------------------------------------------|
        | [{{ sonarr['cf']['fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fansub)   |                            0                             | {{ sonarr['cf']['fansub']['trash_id'] }}  |
        | [{{ sonarr['cf']['fastsub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fastsub) | {{ sonarr['cf']['fastsub']['trash_scores']['default'] }} | {{ sonarr['cf']['fastsub']['trash_id'] }} |
