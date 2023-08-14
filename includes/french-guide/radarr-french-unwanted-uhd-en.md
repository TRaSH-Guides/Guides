??? abstract "Unwanted - [Click to show/hide]"
    | Custom Format                                                                                           |                           Score                            | Trash ID                                    |
    | ------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------: | ------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)           |  {{ radarr['cf']['br-disk']['trash_scores']['default'] }}  | {{ radarr['cf']['br-disk']['trash_id'] }}   |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                     |    {{ radarr['cf']['3d']['trash_scores']['default'] }}     | {{ radarr['cf']['3d']['trash_id'] }}        |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                     |    {{ radarr['cf']['lq']['trash_scores']['default'] }}     | {{ radarr['cf']['lq']['trash_id'] }}        |
    | [{{ radarr['cf']['french-lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-lq)           | {{ radarr['cf']['french-lq']['trash_scores']['default'] }} | {{ radarr['cf']['french-lq']['trash_id'] }} |
    | [{{ radarr['cf']['upscaled']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#upscaled)         | {{ radarr['cf']['upscaled']['trash_scores']['default'] }}  | {{ radarr['cf']['upscaled']['trash_id'] }}  |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning: |  {{ radarr['cf']['x265-hd']['trash_scores']['default'] }}  | {{ radarr['cf']['x265-hd']['trash_id'] }}   |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['french-lq']['name'] }}:** A collection of known Low Quality French groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['upscaled']['name'] }}:** A custom format to prevent Radarr from grabbing 4K upscaled releases.
    - **{{ radarr['cf']['x265-hd']['name'] }}:** This blocks/ignores 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        !!!! Danger "Don't use this together with [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv), only ever include one of them :warning:"

    ??? note "Optional - [Click to show/hide]"

        This includes optional Custom Formats made by Trash for the original guide. Please be sure to understand what those do before adding them. Moreover, it includes two Custom Formats you may use at your own risk if you want MULTi:

        - [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups), which can be controversial for people looking for MULTi release. I encourage you to not use it.
        - [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene), it may include Scene groups already in [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups) Custom Format. Which is used for fallback to be sure to get a MULTi release.

        {! include-markdown "../../includes/cf/radarr-optional.md" !}
