??? summary "All HDR Formats + DV (WEBDL) + HDR10+ Boost - [CLICK TO EXPAND]"

    {! include-markdown "../../includes/cf/dv-info.md" !}

    ![!HDR Formats Flowchart](/Radarr/images/flowchart-hdr-formats.png){ data-title="Follow the flowchart, continue till you hit finished." data-description="- The yellow boxes match the Quality Profile on the right side of the Guide.<br>- If the Guide says <b>ALL</b> it means <b>ALL</b>. (<u>Even if you have a TV/Hardware Media Player that can't handle for example DV or HDR10+</u>, else you will limit yourself what you're able to get or get download loops, this also counts for the audio formats).<br><br><b>All the used scores and combination of Custom Formats in this Guide are tested to get the desired results and prevent download loops as much as possible.</b>" }


    | Custom Format                                                                                                 | Score                                                | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
    | [{{ sonarr['cf']['dv-hdr10']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-hdr10)               | {{ sonarr['cf']['dv-hdr10']['trash_score'] }}        | {{ sonarr['cf']['dv-hdr10']['trash_id'] }}        |
    | [{{ sonarr['cf']['dv']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv)                           | {{ sonarr['cf']['dv']['trash_score'] }}              | {{ sonarr['cf']['dv']['trash_id'] }}              |
    | [{{ sonarr['cf']['dv-hlg']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-hlg)                   | {{ sonarr['cf']['dv-hlg']['trash_score'] }}          | {{ sonarr['cf']['dv-hlg']['trash_id'] }}          |
    | [{{ sonarr['cf']['dv-sdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-sdr)                   | {{ sonarr['cf']['dv-sdr']['trash_score'] }}          | {{ sonarr['cf']['dv-sdr']['trash_id'] }}          |
    | [{{ sonarr['cf']['hdr10plus']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr10plus)             | {{ sonarr['cf']['hdr10plus']['trash_score'] }}       | {{ sonarr['cf']['hdr10plus']['trash_id'] }}       |
    | [{{ sonarr['cf']['hdr10']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr10)                     | {{ sonarr['cf']['hdr10']['trash_score'] }}           | {{ sonarr['cf']['hdr10']['trash_id'] }}           |
    | [{{ sonarr['cf']['hdr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr)                         | {{ sonarr['cf']['hdr']['trash_score'] }}             | {{ sonarr['cf']['hdr']['trash_id'] }}             |
    | [{{ sonarr['cf']['hdr-undefined']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr-undefined)     | {{ sonarr['cf']['hdr-undefined']['trash_score'] }}   | {{ sonarr['cf']['hdr-undefined']['trash_id'] }}   |
    | [{{ sonarr['cf']['pq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#pq)                           | {{ sonarr['cf']['pq']['trash_score'] }}              | {{ sonarr['cf']['pq']['trash_id'] }}              |
    | [{{ sonarr['cf']['hlg']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hlg)                         | {{ sonarr['cf']['hlg']['trash_score'] }}             | {{ sonarr['cf']['hlg']['trash_id'] }}             |
    | [{{ sonarr['cf']['dv-webdl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-webdl)               | {{ sonarr['cf']['dv-webdl']['trash_score'] }}        | {{ sonarr['cf']['dv-webdl']['trash_id'] }}        |
    | [{{ sonarr['cf']['hdr10plus-boost']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hdr10plus-boost) | {{ sonarr['cf']['hdr10plus-boost']['trash_score'] }} | {{ sonarr['cf']['hdr10plus-boost']['trash_id'] }} |


    !!! hint
        If you (or family members you share your collection with) have a setup that doesn't support Dolby Vision then it's best to add **ALL** the HDR Formats listed above (including **ALL** the DV ones (with and without HDR in it), It is important to also add the [{{ sonarr['cf']['dv-webdl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dv-webdl) Custom Format with a score of {{ sonarr['cf']['dv-webdl']['trash_score'] }}
