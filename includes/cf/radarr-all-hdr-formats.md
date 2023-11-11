??? abstract "All HDR Formats - [Click to show/hide]"

    **Why would i choose this HDR formats ?**

    - You have a setup that supports Dolby Vision.
    - You share your media library with other family members that also have have Dolby Vision compatible devices.

    {! include-markdown "../../includes/cf/dv-info.md" !}

    | Custom Format                                                                                             |                             Score                              | Trash ID                                        |
    | --------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
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

    {! include-markdown "../../includes/cf/dv-tip-dv-webdl.md" !}
