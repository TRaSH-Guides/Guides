??? abstract "Miscellaneous UHD (Optional) - [Click to show/hide]"

    !!! tip "I recommend using the following Custom Formats"

        - **For details on "Why" and a potential warning :warning: please see the notes below.**
        - `x265 (no HDR/DV)` over the `x265 (HD)`
        - `SDR (no WEBDL)` over the `SDR`

    | Custom Format                                                                                                       |                             Score                              | Trash ID                                        |
    | ------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
    | [{{ sonarr['cf']['sdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sdr)                               |      {{ sonarr['cf']['sdr']['trash_scores']['default'] }}      | {{ sonarr['cf']['sdr']['trash_id'] }}           |
    | [{{ sonarr['cf']['sdr-no-webdl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sdr-no-webdl) :warning:   | {{ sonarr['cf']['sdr-no-webdl']['trash_scores']['default'] }}  | {{ sonarr['cf']['sdr-no-webdl']['trash_id'] }}  |
    | [{{ sonarr['cf']['x265-no-hdrdv']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-no-hdrdv) :warning: | {{ sonarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }} | {{ sonarr['cf']['x265-no-hdrdv']['trash_id'] }} |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['sdr']['name'] }}:** This will prevent grabbing UHD/4k releases without HDR Formats.
    - **{{ sonarr['cf']['sdr-no-webdl']['name'] }}:** This will prevent grabbing UHD/4k Remux and Bluray encode releases without HDR Formats. - i.e., SDR WEB releases will still be allowed since 4K SDR WEB releases can often look better than the 1080p version due to the improved bitrate.

        {! include-markdown "../../includes/cf-descriptions/sdr-no-webdl-sonarr-warning.md" !}

    - **{{ sonarr['cf']['x265-no-hdrdv']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265, **But it will allow x265 releases if they have HDR and/or DV**

        {! include-markdown "../../includes/cf-descriptions/x265-no-hdrdv-sonarr-warning.md" !}
