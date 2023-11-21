??? abstract "Optional UHD - [Click to show/hide]"
    | Custom Format                                                                         |                        Score                         | Trash ID                              |
    | ------------------------------------------------------------------------------------- | :--------------------------------------------------: | ------------------------------------- |
    | [{{ radarr['cf']['sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#sdr) | {{ radarr['cf']['sdr']['trash_scores']['default'] }} | {{ radarr['cf']['sdr']['trash_id'] }} |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['sdr']['name'] }}:** This will prevent grabbing UHD/4k releases without HDR Formats.
