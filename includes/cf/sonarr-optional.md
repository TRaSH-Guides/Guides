??? abstract "Optional (UHD) - [Click to show/hide]"
    | Custom Format                                                                               |                          Score                          | Trash ID                                 |
    | ------------------------------------------------------------------------------------------- | :-----------------------------------------------------: | ---------------------------------------- |
    | [{{ sonarr['cf']['retags']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#retags) | {{ sonarr['cf']['retags']['trash_scores']['default'] }} | {{ sonarr['cf']['retags']['trash_id'] }} |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['retags']['name'] }}:** This will help avoid retagged releases that may no longer meet the quality of the original group (e.g. TGx downsampling a NTb release from 5.1 audio to 2.0 audio yet maintain the NTb naming)
