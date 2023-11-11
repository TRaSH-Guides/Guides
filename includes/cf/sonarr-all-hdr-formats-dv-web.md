??? abstract "All HDR Formats + DV (WEBDL) - [Click to show/hide]"

    **Why would i choose this HDR formats ?**

    - Not all devices in your chain support Dolby Vision.
    - You share your media library with other family members that don't have Dolby Vision compatible devices.

    {! include-markdown "../../includes/cf/dv-info.md" !}

    | Custom Format                                                                                             |                             Score                              | Trash ID                                        |
    | --------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
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
    | [{{ sonarr['cf']['dv-webdl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-webdl)           |   {{ sonarr['cf']['dv-webdl']['trash_scores']['default'] }}    | {{ sonarr['cf']['dv-webdl']['trash_id'] }}      |

    {! include-markdown "../../includes/cf/sonarr-dv-tip-dv-webdl.md" !}
