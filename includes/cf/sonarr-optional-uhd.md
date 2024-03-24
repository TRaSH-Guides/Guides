??? abstract "Optional (UHD) - [Click to show/hide]"
    | Custom Format                                                                                                     |                             Score                             | Trash ID                                       |
    | ----------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: | ---------------------------------------------- |
    | [{{ sonarr['cf']['sdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sdr)                             |     {{ sonarr['cf']['sdr']['trash_scores']['default'] }}      | {{ sonarr['cf']['sdr']['trash_id'] }}          |
    | [{{ sonarr['cf']['sdr-no-webdl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sdr-no-webdl) :warning: | {{ sonarr['cf']['sdr-no-webdl']['trash_scores']['default'] }} | {{ sonarr['cf']['sdr-no-webdl']['trash_id'] }} |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['sdr']['name'] }}:** {! include-markdown "../../includes/cf-descriptions/sdr.md" !}
    - **{{ sonarr['cf']['sdr-no-webdl']['name'] }}:** This will prevent grabbing UHD/4k Remux and Bluray encode releases without HDR Formats. - i.e., SDR WEB releases will still be allowed. 4K SDR WEB releases can look better than the 1080p version, owing to improved bitrate.

        !!! Danger "Don't use this together with [{{ sonarr['cf']['sdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sdr), Only ever include one of them :warning:"
