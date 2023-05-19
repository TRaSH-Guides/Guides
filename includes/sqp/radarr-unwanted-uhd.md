??? abstract "Unwanted - [CLICK TO EXPAND]"
    | Custom Format                                                                                                       | Score                                              | Trash ID                                        |
    | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)                       | {{ radarr['cf']['br-disk']['trash_score'] }}       | {{ radarr['cf']['br-disk']['trash_id'] }}       |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                                 | {{ radarr['cf']['lq']['trash_score'] }}            | {{ radarr['cf']['lq']['trash_id'] }}            |
    | [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning: | {{ radarr['cf']['x265-no-hdrdv']['trash_score'] }} | {{ radarr['cf']['x265-no-hdrdv']['trash_id'] }} |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                                 | {{ radarr['cf']['3d']['trash_score'] }}            | {{ radarr['cf']['3d']['trash_id'] }}            |
    | [{{ radarr['cf']['upscaled']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#upscaled)                     | {{ radarr['cf']['upscaled']['trash_score'] }}      | {{ radarr['cf']['upscaled']['trash_id'] }}      |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['x265-no-hdrdv']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265, But it will allow 720/1080p x265 releases if they have HDR and/or DV. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        !!! Danger "Don't use this together with [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"

    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['upscaled']['name'] }}:** A custom format to prevent Radarr from grabbing upscaled releases.
