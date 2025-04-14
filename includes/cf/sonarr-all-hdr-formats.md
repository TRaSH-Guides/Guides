??? abstract "All HDR Formats - [Click to show/hide]"

    **Why would I choose All HDR formats ?**

    - You have a 4K/2160p TV and a hardware media player device (such as Roku, AppleTV, Shield, SmartTV App, etc.) that supports several HDR formats (such as Dolby Vision, HDR10, HDR10+, etc.).

        {! include-markdown "../../includes/cf/dv-limitations-atv.md" !}

    - You've chosen a profile that includes 4K/2160p releases. You must use all the HDR formats with 4k/2160p profiles.
    - You must add **ALL** the HDR formats - don't leave any of them out!

    {! include-markdown "../../includes/cf/dv-info-green-purple.md" !}

    {! include-markdown "../../includes/cf/dv-info-profiles.md" !}

    {! include-markdown "../../includes/cf/which-hdr-formats-should-i-choose.md" !}

    | Custom Format                                                                                             |                             Score                              | Trash ID                                        |
    | --------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
    | [{{ sonarr['cf']['dv-hdr10plus']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-hdr10plus)   | {{ sonarr['cf']['dv-hdr10plus']['trash_scores']['default'] }}  | {{ sonarr['cf']['dv-hdr10plus']['trash_id'] }}  |
    | [{{ sonarr['cf']['dv-hdr10']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-hdr10)           |   {{ sonarr['cf']['dv-hdr10']['trash_scores']['default'] }}    | {{ sonarr['cf']['dv-hdr10']['trash_id'] }}      |
    | [{{ sonarr['cf']['dv']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv)                       |      {{ sonarr['cf']['dv']['trash_scores']['default'] }}       | {{ sonarr['cf']['dv']['trash_id'] }}            |
    | [{{ sonarr['cf']['dv-hlg']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-hlg)               |    {{ sonarr['cf']['dv-hlg']['trash_scores']['default'] }}     | {{ sonarr['cf']['dv-hlg']['trash_id'] }}        |
    | [{{ sonarr['cf']['dv-sdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-sdr)               |    {{ sonarr['cf']['dv-sdr']['trash_scores']['default'] }}     | {{ sonarr['cf']['dv-sdr']['trash_id'] }}        |
    | [{{ sonarr['cf']['hdr10plus']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr10plus)         |   {{ sonarr['cf']['hdr10plus']['trash_scores']['default'] }}   | {{ sonarr['cf']['hdr10plus']['trash_id'] }}     |
    | [{{ sonarr['cf']['hdr10']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr10)                 |     {{ sonarr['cf']['hdr10']['trash_scores']['default'] }}     | {{ sonarr['cf']['hdr10']['trash_id'] }}         |
    | [{{ sonarr['cf']['hdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr)                     |      {{ sonarr['cf']['hdr']['trash_scores']['default'] }}      | {{ sonarr['cf']['hdr']['trash_id'] }}           |
    | [{{ sonarr['cf']['hdr-undefined']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr-undefined) | {{ sonarr['cf']['hdr-undefined']['trash_scores']['default'] }} | {{ sonarr['cf']['hdr-undefined']['trash_id'] }} |
    | [{{ sonarr['cf']['pq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#pq)                       |      {{ sonarr['cf']['pq']['trash_scores']['default'] }}       | {{ sonarr['cf']['pq']['trash_id'] }}            |
    | [{{ sonarr['cf']['hlg']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hlg)                     |      {{ sonarr['cf']['hlg']['trash_scores']['default'] }}      | {{ sonarr['cf']['hlg']['trash_id'] }}           |

    ??? abstract "Add Custom Format `DV (WEBDL)` with a score of `-10000` - [Click to show/hide]"

        **Why would I add this Custom Format?**

        - Not all devices in your chain support Dolby Vision.
        - You share your media library with other family members that don't have Dolby Vision compatible devices.
        - According the flowchart I should add this Custom Format

        <p align="center">![Flowchart](/Radarr/images/flowchart-hdr-dv-webdl.png){ width="20%" height="20%" }

        | Custom Format                                                                                   |                           Score                           | Trash ID                                   |
        | ----------------------------------------------------------------------------------------------- | :-------------------------------------------------------: | ------------------------------------------ |
        | [{{ sonarr['cf']['dv-webdl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-webdl) | {{ sonarr['cf']['dv-webdl']['trash_scores']['default'] }} | {{ sonarr['cf']['dv-webdl']['trash_id'] }} |

    ??? abstract "Add the Custom Formats `DV HDR10+ Boost` and `HDR10+ Boost` - [Click to show/hide]"

        **Why would I add this Custom Format?**

        - You have a (Samsung) TV that supports HDR10+.
        - According the flowchart I should add this Custom Format

        <p align="center">![Flowchart](/Radarr/images/flowchart-hdr10plus-boost.png){ width="20%" height="20%" }

        !!! warning "If you use this Custom Format then 99% of the time you also need to add the following Custom Format `DV (WEBDL)` with a score of `-10000`"

        | Custom Format                                                                                                       |                                Score                                | Trash ID                                             |
        | ------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------: | ---------------------------------------------------- |
        | [{{ sonarr['cf']['hdr10plus-boost']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr10plus-boost)       |  {{ sonarr['cf']['hdr10plus-boost']['trash_scores']['default'] }}   | {{ sonarr['cf']['hdr10plus-boost']['trash_id'] }}    |
        | [{{ sonarr['cf']['dv-hdr10plus-boost']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-hdr10plus-boost) | {{ sonarr['cf']['dv-hdr10plus-boost']['trash_scores']['default'] }} | {{ sonarr['cf']['dv-hdr10plus-boost']['trash_id'] }} |
