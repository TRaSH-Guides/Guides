<!-- markdownlint-disable MD041-->
??? abstract "HQ Source Groups - [Click to show/hide]"

    | Custom Format                                                                                                             |                                  Score                                  | Trash ID                                                |
    | ------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ------------------------------------------------------- |
    | [{{ sonarr['cf']['german-bluray-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-bluray-tier-01) | {{ sonarr['cf']['german-bluray-tier-01']['trash_scores']['default'] }}  | {{ sonarr['cf']['german-bluray-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['german-bluray-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-bluray-tier-02) | {{ sonarr['cf']['german-bluray-tier-02']['trash_scores']['default'] }}  | {{ sonarr['cf']['german-bluray-tier-02']['trash_id'] }} |
    | [{{ sonarr['cf']['german-bluray-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-bluray-tier-03) | {{ sonarr['cf']['german-bluray-tier-03']['trash_scores']['default'] }}  | {{ sonarr['cf']['german-bluray-tier-03']['trash_id'] }} |
    | [{{ sonarr['cf']['german-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-web-tier-01)       |   {{ sonarr['cf']['german-web-tier-01']['trash_scores']['default'] }}   | {{ sonarr['cf']['german-web-tier-01']['trash_id'] }}    |
    | [{{ sonarr['cf']['german-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-web-tier-02)       |   {{ sonarr['cf']['german-web-tier-02']['trash_scores']['default'] }}   | {{ sonarr['cf']['german-web-tier-02']['trash_id'] }}    |
    | [{{ sonarr['cf']['german-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-web-tier-03)       |   {{ sonarr['cf']['german-web-tier-03']['trash_scores']['default'] }}   | {{ sonarr['cf']['german-web-tier-03']['trash_id'] }}    |
    | [{{ sonarr['cf']['german-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-scene)                   | :warning: {{ sonarr['cf']['german-scene']['trash_scores']['default'] }} | {{ sonarr['cf']['german-scene']['trash_id'] }}          |
    | [{{ sonarr['cf']['web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-01)                     |      {{ sonarr['cf']['web-tier-01']['trash_scores']['default'] }}       | {{ sonarr['cf']['web-tier-01']['trash_id'] }}           |
    | [{{ sonarr['cf']['web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-02)                     |      {{ sonarr['cf']['web-tier-02']['trash_scores']['default'] }}       | {{ sonarr['cf']['web-tier-02']['trash_id'] }}           |
    | [{{ sonarr['cf']['web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-03)                     |      {{ sonarr['cf']['web-tier-03']['trash_scores']['default'] }}       | {{ sonarr['cf']['web-tier-03']['trash_id'] }}           |

    !!! tip

        :warning: German Scene groups are included as a fallback if you really want their release despite a potential loss in quality. Either score the CF to `{{ sonarr['cf']['german-scene']['trash_scores']['default'] }}` (default) or `0`, depending on what you want to achieve.

    !!! tip "Custom Formats for the Alternative Quality Profile"

        In case you went for the alternative quality profile (including 720p/1080p qualities) you will need to add the following custom formats.

        | Custom Format                                                                                                     |                               Score                                | Trash ID                                            |
        | ----------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------: | --------------------------------------------------- |
        | [{{ sonarr['cf']['hd-bluray-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hd-bluray-tier-01) | {{ sonarr['cf']['hd-bluray-tier-01']['trash_scores']['default'] }} | {{ sonarr['cf']['hd-bluray-tier-01']['trash_id'] }} |
        | [{{ sonarr['cf']['hd-bluray-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hd-bluray-tier-02) | {{ sonarr['cf']['hd-bluray-tier-02']['trash_scores']['default'] }} | {{ sonarr['cf']['hd-bluray-tier-02']['trash_id'] }} |

<!-- markdownlint-enable MD041-->
