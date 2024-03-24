??? abstract "Optional (UHD) - [Click to show/hide]"
    | Custom Format                                                                               |                          Score                          | Trash ID                                 |
    | ------------------------------------------------------------------------------------------- | :-----------------------------------------------------: | ---------------------------------------- |
    | [{{ sonarr['cf']['sdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sdr)       |  {{ sonarr['cf']['sdr']['trash_scores']['default'] }}   | {{ sonarr['cf']['sdr']['trash_id'] }}    |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['sdr']['name'] }}:** This will prevent the grabbing of UHD/4K releases that do not contain HDR.
