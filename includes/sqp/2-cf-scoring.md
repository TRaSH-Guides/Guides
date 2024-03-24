#### Custom Formats and scores

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-all-hdr-formats.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe.md" !}

??? abstract "HQ Release Groups - [Click to show/hide]"
    | Custom Format                                                                                                       |                                         Score                                         | Trash ID                                             |
    | ------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------: | ---------------------------------------------------- |
    | [{{ radarr['cf']['remux-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remux-tier-01)           |            {{ radarr['cf']['remux-tier-01']['trash_scores']['default'] }}             | {{ radarr['cf']['remux-tier-01']['trash_id'] }}      |
    | [{{ radarr['cf']['remux-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remux-tier-02)           |            {{ radarr['cf']['remux-tier-02']['trash_scores']['default'] }}             | {{ radarr['cf']['remux-tier-02']['trash_id'] }}      |
    | [{{ radarr['cf']['remux-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remux-tier-03)           |            {{ radarr['cf']['remux-tier-03']['trash_scores']['default'] }}             | {{ radarr['cf']['remux-tier-03']['trash_id'] }}      |
    | [{{ radarr['cf']['uhd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-01) | :warning: {{ radarr['cf']['uhd-bluray-tier-01']['trash_scores']['sqp-2'] }} :warning: | {{ radarr['cf']['uhd-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['uhd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-02) | :warning: {{ radarr['cf']['uhd-bluray-tier-02']['trash_scores']['sqp-2'] }} :warning: | {{ radarr['cf']['uhd-bluray-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['uhd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-03) | :warning: {{ radarr['cf']['uhd-bluray-tier-03']['trash_scores']['sqp-2'] }} :warning: | {{ radarr['cf']['uhd-bluray-tier-03']['trash_id'] }} |
    | [{{ radarr['cf']['web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-01)               |             {{ radarr['cf']['web-tier-01']['trash_scores']['default'] }}              | {{ radarr['cf']['web-tier-01']['trash_id'] }}        |
    | [{{ radarr['cf']['web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-02)               |             {{ radarr['cf']['web-tier-02']['trash_scores']['default'] }}              | {{ radarr['cf']['web-tier-02']['trash_id'] }}        |
    | [{{ radarr['cf']['web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-03)               |             {{ radarr['cf']['web-tier-03']['trash_scores']['default'] }}              | {{ radarr['cf']['web-tier-03']['trash_id'] }}        |

    !!! warning "Scores marked with a :warning: warning :warning: are different to those used in the main guide"

{! include-markdown "../../includes/sqp/uhd-radarr-misc.md" !}

{! include-markdown "../../includes/cf/radarr-unwanted-uhd.md" !}

{! include-markdown "../../includes/sqp/uhd-radarr-optional.md" !}

{! include-markdown "../../includes/sqp/uhd-radarr-resolution.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}
