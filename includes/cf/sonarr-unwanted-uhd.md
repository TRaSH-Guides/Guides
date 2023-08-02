??? abstract "Unwanted (UHD) - [Click to show/hide]"
    | Custom Format                                                                                 |                          Score                           | Trash ID                                  |
    | --------------------------------------------------------------------------------------------- | :------------------------------------------------------: | ----------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk) | {{ sonarr['cf']['br-disk']['trash_scores']['default'] }} | {{ sonarr['cf']['br-disk']['trash_id'] }} |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq)           |   {{ sonarr['cf']['lq']['trash_scores']['default'] }}    | {{ sonarr['cf']['lq']['trash_id'] }}      |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#extras)   | {{ sonarr['cf']['extras']['trash_scores']['default'] }}  | {{ sonarr['cf']['extras']['trash_id'] }}  |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }} :** This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ sonarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ sonarr['cf']['extras']['name'] }}:** This blocks/ignores extras
