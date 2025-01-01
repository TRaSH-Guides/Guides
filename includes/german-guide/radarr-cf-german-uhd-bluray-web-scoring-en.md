<!-- markdownlint-disable MD041-->
??? abstract "HQ Source Groups - [Click to show/hide]"

    | Custom Format                                                                                                             |                                  Score                                  | Trash ID                                                |
    | ------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ------------------------------------------------------- |
    | [{{ radarr['cf']['german-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-bluray-tier-01) | {{ radarr['cf']['german-bluray-tier-01']['trash_scores']['default'] }}  | {{ radarr['cf']['german-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['german-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-bluray-tier-02) | {{ radarr['cf']['german-bluray-tier-02']['trash_scores']['default'] }}  | {{ radarr['cf']['german-bluray-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['german-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-bluray-tier-03) | {{ radarr['cf']['german-bluray-tier-03']['trash_scores']['default'] }}  | {{ radarr['cf']['german-bluray-tier-03']['trash_id'] }} |
    | [{{ radarr['cf']['german-web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-web-tier-01)       |   {{ radarr['cf']['german-web-tier-01']['trash_scores']['default'] }}   | {{ radarr['cf']['german-web-tier-01']['trash_id'] }}    |
    | [{{ radarr['cf']['german-web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-web-tier-02)       |   {{ radarr['cf']['german-web-tier-02']['trash_scores']['default'] }}   | {{ radarr['cf']['german-web-tier-02']['trash_id'] }}    |
    | [{{ radarr['cf']['german-web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-web-tier-03)       |   {{ radarr['cf']['german-web-tier-03']['trash_scores']['default'] }}   | {{ radarr['cf']['german-web-tier-03']['trash_id'] }}    |
    | [{{ radarr['cf']['german-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-scene)                   | :warning: {{ radarr['cf']['german-scene']['trash_scores']['default'] }} | {{ radarr['cf']['german-scene']['trash_id'] }}          |
    | [{{ radarr['cf']['uhd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-01)       |   {{ radarr['cf']['uhd-bluray-tier-01']['trash_scores']['default'] }}   | {{ radarr['cf']['uhd-bluray-tier-01']['trash_id'] }}    |
    | [{{ radarr['cf']['uhd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-02)       |   {{ radarr['cf']['uhd-bluray-tier-02']['trash_scores']['default'] }}   | {{ radarr['cf']['uhd-bluray-tier-02']['trash_id'] }}    |
    | [{{ radarr['cf']['uhd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-03)       |   {{ radarr['cf']['uhd-bluray-tier-03']['trash_scores']['default'] }}   | {{ radarr['cf']['uhd-bluray-tier-03']['trash_id'] }}    |
    | [{{ radarr['cf']['web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-01)                     |      {{ radarr['cf']['web-tier-01']['trash_scores']['default'] }}       | {{ radarr['cf']['web-tier-01']['trash_id'] }}           |
    | [{{ radarr['cf']['web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-02)                     |      {{ radarr['cf']['web-tier-02']['trash_scores']['default'] }}       | {{ radarr['cf']['web-tier-02']['trash_id'] }}           |
    | [{{ radarr['cf']['web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-03)                     |      {{ radarr['cf']['web-tier-03']['trash_scores']['default'] }}       | {{ radarr['cf']['web-tier-03']['trash_id'] }}           |

    !!! tip

        :warning: German Scene groups are included as a fallback if you really want their release despite a potential loss in quality. Either score the CF to `{{ radarr['cf']['german-scene']['trash_scores']['default'] }}` (default) or `0`, depending on what you want to achieve.

    !!! tip "Custom Formats for the Alternative Quality Profile"

        In case you went for the alternative quality profile (including 720p/1080p qualities) you will need to add the following custom formats.

        | Custom Format                                                                                                             |                                  Score                                  | Trash ID                                                |
        | ------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ------------------------------------------------------- |
        | [{{ radarr['cf']['hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-01)         |   {{ radarr['cf']['hd-bluray-tier-01']['trash_scores']['default'] }}    | {{ radarr['cf']['hd-bluray-tier-01']['trash_id'] }}     |
        | [{{ radarr['cf']['hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-02)         |   {{ radarr['cf']['hd-bluray-tier-02']['trash_scores']['default'] }}    | {{ radarr['cf']['hd-bluray-tier-02']['trash_id'] }}     |
        | [{{ radarr['cf']['hd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-03)         |   {{ radarr['cf']['hd-bluray-tier-03']['trash_scores']['default'] }}    | {{ radarr['cf']['hd-bluray-tier-03']['trash_id'] }}     |

<!-- markdownlint-enable MD041-->
