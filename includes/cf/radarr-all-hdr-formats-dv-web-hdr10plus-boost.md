??? abstract "All HDR Formats + DV (WEBDL) + HDR10+ Boost - [Click to show/hide]"

    **Why would i choose this HDR formats ?**

    - Not all devices in your chain support Dolby Vision.
    - You share your media library with other family members that don't have Dolby Vision compatible devices.
    - You have a (Samsung) TV that supports HDR10+.

    {! include-markdown "../../includes/cf/dv-info.md" !}

    | Custom Format                                                                                                 |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['dv-hdr10']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10)               |    {{ radarr['cf']['dv-hdr10']['trash_scores']['default'] }}     | {{ radarr['cf']['dv-hdr10']['trash_id'] }}        |
    | [{{ radarr['cf']['dv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv)                           |       {{ radarr['cf']['dv']['trash_scores']['default'] }}        | {{ radarr['cf']['dv']['trash_id'] }}              |
    | [{{ radarr['cf']['dv-hlg']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hlg)                   |     {{ radarr['cf']['dv-hlg']['trash_scores']['default'] }}      | {{ radarr['cf']['dv-hlg']['trash_id'] }}          |
    | [{{ radarr['cf']['dv-sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-sdr)                   |     {{ radarr['cf']['dv-sdr']['trash_scores']['default'] }}      | {{ radarr['cf']['dv-sdr']['trash_id'] }}          |
    | [{{ radarr['cf']['hdr10plus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus)             |    {{ radarr['cf']['hdr10plus']['trash_scores']['default'] }}    | {{ radarr['cf']['hdr10plus']['trash_id'] }}       |
    | [{{ radarr['cf']['hdr10']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10)                     |      {{ radarr['cf']['hdr10']['trash_scores']['default'] }}      | {{ radarr['cf']['hdr10']['trash_id'] }}           |
    | [{{ radarr['cf']['hdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr)                         |       {{ radarr['cf']['hdr']['trash_scores']['default'] }}       | {{ radarr['cf']['hdr']['trash_id'] }}             |
    | [{{ radarr['cf']['hdr-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr-undefined)     |  {{ radarr['cf']['hdr-undefined']['trash_scores']['default'] }}  | {{ radarr['cf']['hdr-undefined']['trash_id'] }}   |
    | [{{ radarr['cf']['pq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pq)                           |       {{ radarr['cf']['pq']['trash_scores']['default'] }}        | {{ radarr['cf']['pq']['trash_id'] }}              |
    | [{{ radarr['cf']['hlg']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hlg)                         |       {{ radarr['cf']['hlg']['trash_scores']['default'] }}       | {{ radarr['cf']['hlg']['trash_id'] }}             |
    | [{{ radarr['cf']['dv-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl)               |    {{ radarr['cf']['dv-webdl']['trash_scores']['default'] }}     | {{ radarr['cf']['dv-webdl']['trash_id'] }}        |
    | [{{ radarr['cf']['hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus-boost) | {{ radarr['cf']['hdr10plus-boost']['trash_scores']['default'] }} | {{ radarr['cf']['hdr10plus-boost']['trash_id'] }} |

    {! include-markdown "../../includes/cf/radarr-dv-tip-dv-webdl.md" !}
