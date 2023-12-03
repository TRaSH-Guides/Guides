??? abstract "Unwanted - [Click to show/hide]"
    | Custom Format                                                                                                  |                               Score                               | Trash ID                                           |
    | -------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------: | -------------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)                  |     {{ radarr['cf']['br-disk']['trash_scores']['default'] }}      | {{ radarr['cf']['br-disk']['trash_id'] }}          |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                            |        {{ radarr['cf']['lq']['trash_scores']['default'] }}        | {{ radarr['cf']['lq']['trash_id'] }}               |
    | [{{ radarr['cf']['lq-release-title']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq-release-title) | {{ radarr['cf']['lq-release-title']['trash_scores']['default'] }} | {{ radarr['cf']['lq-release-title']['trash_id'] }} |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning:        |     {{ radarr['cf']['x265-hd']['trash_scores']['default'] }}      | {{ radarr['cf']['x265-hd']['trash_id'] }}          |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                            |        {{ radarr['cf']['3d']['trash_scores']['default'] }}        | {{ radarr['cf']['3d']['trash_id'] }}               |
    | [{{ radarr['cf']['upscaled']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#upscaled)                |     {{ radarr['cf']['upscaled']['trash_scores']['default'] }}     | {{ radarr['cf']['upscaled']['trash_id'] }}         |
    | [{{ radarr['cf']['extras']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#extras)                    |      {{ radarr['cf']['extras']['trash_scores']['default'] }}      | {{ radarr['cf']['extras']['trash_id'] }}           |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['lq-release-title']['name'] }}:** A collection of terms seen in the titles of Low Quality releases that are not captured by using a release group name.
    - **{{ radarr['cf']['x265-hd']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        !!! Danger "Don't use this together with [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv), Only ever include one of them :warning:"

    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['upscaled']['name'] }}:** A custom format to prevent Radarr from grabbing upscaled releases.
    - **{{ radarr['cf']['extras']['name'] }}:** Blocks releases that only contain extras
