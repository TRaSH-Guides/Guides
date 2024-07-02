??? abstract "Unwanted - [Click to show/hide]"

    | Custom Format                                                                                           |                           Score                            | Trash ID                                    |
    | ------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------: | ------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)           |  {{ radarr['cf']['br-disk']['trash_scores']['default'] }}  | {{ radarr['cf']['br-disk']['trash_id'] }}   |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                     |    {{ radarr['cf']['3d']['trash_scores']['default'] }}     | {{ radarr['cf']['3d']['trash_id'] }}        |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                     |    {{ radarr['cf']['lq']['trash_scores']['default'] }}     | {{ radarr['cf']['lq']['trash_id'] }}        |
    | [{{ radarr['cf']['german-lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-lq)           | {{ radarr['cf']['german-lq']['trash_scores']['default'] }} | {{ radarr['cf']['german-lq']['trash_id'] }} |
    | [{{ radarr['cf']['german-micro']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-micro)        | {{ radarr['cf']['german-micro']['trash_scores']['default'] }} | {{ radarr['cf']['german-micro']['trash_id'] }} |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning: |  :warning: 0  | {{ radarr['cf']['x265-hd']['trash_id'] }}   |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['german-lq']['name'] }}:** A collection of known Low Quality German groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['german-micro']['name'] }}:** A collection of German groups producing low quality micro-sized releases.
    - :warning: **{{ radarr['cf']['x265-hd']['name'] }}:** This blocks/ignores 720/1080p (HD) releases that are encoded in x265. However as there are certain german groups (ZeroTwo, VECTOR, ...) which produce high bitrate 1080p x265 encodes we recommend setting the score of this custom format to 0.

    ??? note "Optional - [Click to show/hide]"

        This includes optional Custom Formats made by Trash for the original guide. Please be sure to understand what those do before adding them. Moreover, it includes two Custom Formats you may use at your own risk if you want Dual Language:

        - [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups), which can be controversial for people looking for Dual Language release. I encourage you to not use it.
        - [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene), it may include Scene groups already in [{{ radarr['cf']['german-scene-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-scene-tier-01) and [{{ radarr['cf']['german-scene-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-scene-tier-02) Custom Format. Which is used for fallback to be sure to get a Dual Language release.

        {! include-markdown "../../includes/cf/radarr-optional.md" !}
