<!-- markdownlint-disable MD041-->
??? abstract "HDR Formats - [Click to show/hide]"

    {! include-markdown "../../includes/cf/hdr-formats.md" !}

    | Custom Format                                                                                                       |                                Score                                | Trash ID                                             |
    | ------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------: | ---------------------------------------------------- |
    | [{{ radarr['cf']['hdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr)                               |        {{ radarr['cf']['hdr']['trash_scores']['default'] }}         | {{ radarr['cf']['hdr']['trash_id'] }}                |
    | [{{ radarr['cf']['dv-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-boost)                     |      {{ radarr['cf']['dv-boost']['trash_scores']['default'] }}      | {{ radarr['cf']['dv-boost']['trash_id'] }}           |
    | [{{ radarr['cf']['hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus-boost)       |  {{ radarr['cf']['hdr10plus-boost']['trash_scores']['default'] }}   | {{ radarr['cf']['hdr10plus-boost']['trash_id'] }}    |
    | [{{ radarr['cf']['dv-wo-hdr-fallback']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-wo-hdr-fallback) | {{ radarr['cf']['dv-wo-hdr-fallback']['trash_scores']['default'] }} | {{ radarr['cf']['dv-wo-hdr-fallback']['trash_id'] }} |

    ---

    {! include-markdown "../../includes/cf/dv-info-green-purple.md" !}

    {! include-markdown "../../includes/cf/dv-info-profiles.md" !}
<!-- markdownlint-enable MD041-->
