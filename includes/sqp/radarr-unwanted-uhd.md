??? abstract "Unwanted - [Click to show/hide]"
    | Custom Format                                                                                   |                           Score                           | Trash ID                                   |
    | ----------------------------------------------------------------------------------------------- | :-------------------------------------------------------: | ------------------------------------------ |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)   | {{ radarr['cf']['br-disk']['trash_scores']['default'] }}  | {{ radarr['cf']['br-disk']['trash_id'] }}  |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)             |    {{ radarr['cf']['lq']['trash_scores']['default'] }}    | {{ radarr['cf']['lq']['trash_id'] }}       |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)             |    {{ radarr['cf']['3d']['trash_scores']['default'] }}    | {{ radarr['cf']['3d']['trash_id'] }}       |
    | [{{ radarr['cf']['upscaled']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#upscaled) | {{ radarr['cf']['upscaled']['trash_scores']['default'] }} | {{ radarr['cf']['upscaled']['trash_id'] }} |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['upscaled']['name'] }}:** A custom format to prevent Radarr from grabbing upscaled releases.
