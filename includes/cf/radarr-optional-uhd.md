??? abstract "Optional UHD - [Click to show/hide]"

    | Custom Format                                                                                                     |                             Score                             | Trash ID                                       |
    | ----------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: | ---------------------------------------------- |
    | [{{ radarr['cf']['sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#sdr)                             |     {{ radarr['cf']['sdr']['trash_scores']['default'] }}      | {{ radarr['cf']['sdr']['trash_id'] }}          |
    | [{{ radarr['cf']['sdr-no-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#sdr-no-webdl) :warning: | {{ radarr['cf']['sdr-no-webdl']['trash_scores']['default'] }} | {{ radarr['cf']['sdr-no-webdl']['trash_id'] }} |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['sdr']['name'] }}:** {! include-markdown "../../includes/cf-descriptions/sdr.md" !}
    - **{{ radarr['cf']['sdr-no-webdl']['name'] }}:** This will prevent grabbing UHD/4k Remux and Bluray encode releases without HDR Formats. - i.e., SDR WEB releases will still be allowed since 4K SDR WEB releases can often look better than the 1080p version due to the improved bitrate.

        !!! Danger "Don't use this together with [{{ radarr['cf']['sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#sdr), Only ever include one of them :warning:"
