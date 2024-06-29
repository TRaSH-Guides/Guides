??? abstract "HQ Source Groups - [Click to show/hide]"

    | Custom Format                                                                                                               |                                   Score                                         | Trash ID                                                   |
    | --------------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------: | ---------------------------------------------------------- |
    | [{{ radarr['cf']['german-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-tier-01)                 | {{ radarr['cf']['german-tier-01']['trash_scores']['default'] }}                 | {{ radarr['cf']['german-tier-01']['trash_id'] }}           |
    | [{{ radarr['cf']['german-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-tier-02)                 | {{ radarr['cf']['german-tier-02']['trash_scores']['default'] }}                 | {{ radarr['cf']['german-tier-02']['trash_id'] }}           |
    | [{{ radarr['cf']['german-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-tier-03)                 | {{ radarr['cf']['german-tier-03']['trash_scores']['default'] }}                 | {{ radarr['cf']['german-tier-03']['trash_id'] }}           |
    | [{{ radarr['cf']['german-scene-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-scene-tier-01)     | :warning: {{ radarr['cf']['german-scene-tier-01']['trash_scores']['default'] }} | {{ radarr['cf']['german-scene-tier-01']['trash_id'] }}     |
    | [{{ radarr['cf']['german-scene-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-scene-tier-02)     | :warning: {{ radarr['cf']['german-scene-tier-02']['trash_scores']['default'] }} | {{ radarr['cf']['german-scene-tier-02']['trash_id'] }}     |

    !!! tip

        :warning: German Scene groups are included as a fallback if you really want their release despite a potential loss in quality. Either score the CF to `{{ radarr['cf']['german-scene-tier-01']['trash_scores']['default'] }}` / `{{ radarr['cf']['german-scene-tier-02']['trash_scores']['default'] }}` (default) or `0` depending on what you want to achieve.

    ??? info "Original mix (optional)"

        {! include-markdown "../../includes/cf/radarr-cf-hd-bluray-web-scoring.md" !}
