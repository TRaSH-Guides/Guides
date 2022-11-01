??? summary "Unwanted - [CLICK TO EXPAND]"
    | Custom Format                                                                                 | Score                                        | Trash ID                                  |
    | --------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk) | {{ radarr['cf']['br-disk']['trash_score'] }} | {{ radarr['cf']['br-disk']['trash_id'] }} |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)           | {{ radarr['cf']['lq']['trash_score'] }}      | {{ radarr['cf']['lq']['trash_id'] }}      |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)           | {{ radarr['cf']['3d']['trash_score'] }}      | {{ radarr['cf']['3d']['trash_id'] }}      |
    | [{{ radarr['cf']['sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#sdr)         | {{ radarr['cf']['sdr']['trash_score'] }}     | {{ radarr['cf']['sdr']['trash_id'] }}     |

    ------
    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['sdr']['name'] }}:** This will help to prevent to grab UHD/4k releases without HDR Formats.
