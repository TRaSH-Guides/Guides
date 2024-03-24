??? abstract "All HDR Formats - [Click to show/hide]"

    **Why would I choose All HDR formats?**

    - You have a 4K/2160p TV and a hardware media player device (such as Roku, AppleTV, Shield, SmartTV App, etc.) that supports several HDR formats (such as Dolby Vision, HDR10, HDR10+, etc.).

        {! include-markdown "../../includes/cf/dv-limitations-atv.md" !}

    - You've chosen a profile that includes 4K/2160p releases. You must use all the HDR formats with 4k/2160p profiles.
    - You must add **ALL** the HDR formats - don't leave any of them out!

    {! include-markdown "../../includes/cf/dv-info-green-purple.md" !}

    {! include-markdown "../../includes/cf/dv-info-profiles.md" !}

    {! include-markdown "../../includes/cf/which-hdr-formats-should-i-choose.md" !}

    | Custom Format                                                                                             |                             Score                              | Trash ID                                        |
    | --------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
    | [{{ radarr['cf']['dv-hdr10plus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10plus)   | {{ radarr['cf']['dv-hdr10plus']['trash_scores']['default'] }}  | {{ radarr['cf']['dv-hdr10plus']['trash_id'] }}  |
    | [{{ radarr['cf']['dv-hdr10']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10)           |   {{ radarr['cf']['dv-hdr10']['trash_scores']['default'] }}    | {{ radarr['cf']['dv-hdr10']['trash_id'] }}      |
    | [{{ radarr['cf']['dv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv)                       |      {{ radarr['cf']['dv']['trash_scores']['default'] }}       | {{ radarr['cf']['dv']['trash_id'] }}            |
    | [{{ radarr['cf']['dv-hlg']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hlg)               |    {{ radarr['cf']['dv-hlg']['trash_scores']['default'] }}     | {{ radarr['cf']['dv-hlg']['trash_id'] }}        |
    | [{{ radarr['cf']['dv-sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-sdr)               |    {{ radarr['cf']['dv-sdr']['trash_scores']['default'] }}     | {{ radarr['cf']['dv-sdr']['trash_id'] }}        |
    | [{{ radarr['cf']['hdr10plus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus)         |   {{ radarr['cf']['hdr10plus']['trash_scores']['default'] }}   | {{ radarr['cf']['hdr10plus']['trash_id'] }}     |
    | [{{ radarr['cf']['hdr10']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10)                 |     {{ radarr['cf']['hdr10']['trash_scores']['default'] }}     | {{ radarr['cf']['hdr10']['trash_id'] }}         |
    | [{{ radarr['cf']['hdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr)                     |      {{ radarr['cf']['hdr']['trash_scores']['default'] }}      | {{ radarr['cf']['hdr']['trash_id'] }}           |
    | [{{ radarr['cf']['hdr-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr-undefined) | {{ radarr['cf']['hdr-undefined']['trash_scores']['default'] }} | {{ radarr['cf']['hdr-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['pq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pq)                       |      {{ radarr['cf']['pq']['trash_scores']['default'] }}       | {{ radarr['cf']['pq']['trash_id'] }}            |
    | [{{ radarr['cf']['hlg']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hlg)                     |      {{ radarr['cf']['hlg']['trash_scores']['default'] }}      | {{ radarr['cf']['hlg']['trash_id'] }}           |

    ??? abstract "Add Custom Format `DV (WEBDL)` with a score of `-10000` - [Click to show/hide]"

        **Why would I add this Custom Format?**

        - Not all devices in your chain support Dolby Vision.
        - You share your media library with other family members that don't have Dolby Vision compatible devices.
        - According the flowchart I should add this Custom Format

        <p align="center">![Flowchart](/Radarr/images/flowchart-hdr-dv-webdl.png){ width="20%" height="20%" }

        | Custom Format                                                                                   |                           Score                           | Trash ID                                   |
        | ----------------------------------------------------------------------------------------------- | :-------------------------------------------------------: | ------------------------------------------ |
        | [{{ radarr['cf']['dv-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl) | {{ radarr['cf']['dv-webdl']['trash_scores']['default'] }} | {{ radarr['cf']['dv-webdl']['trash_id'] }} |

    ??? abstract "Add the Custom Formats `DV HDR10+ Boost` and `HDR10+ Boost` - [Click to show/hide]"

        **Why would I add this Custom Format?**

        - You have a (Samsung) TV that supports HDR10+.
        - According the flowchart I should add this Custom Format

        <p align="center">![Flowchart](/Radarr/images/flowchart-hdr10plus-boost.png){ width="20%" height="20%" }

        !!! warning "If you use this Custom Format then 99% of the time you also need to add the following Custom Format `DV (WEBDL)` with a score of `-10000`"

        | Custom Format                                                                                                       |                                Score                                | Trash ID                                             |
        | ------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------: | ---------------------------------------------------- |
        | [{{ radarr['cf']['hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus-boost)       |  {{ radarr['cf']['hdr10plus-boost']['trash_scores']['default'] }}   | {{ radarr['cf']['hdr10plus-boost']['trash_id'] }}    |
        | [{{ radarr['cf']['dv-hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10plus-boost) | {{ radarr['cf']['dv-hdr10plus-boost']['trash_scores']['default'] }} | {{ radarr['cf']['dv-hdr10plus-boost']['trash_id'] }} |
