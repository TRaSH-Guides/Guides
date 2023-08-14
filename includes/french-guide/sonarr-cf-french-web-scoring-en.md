??? abstract "HQ Source Groups - [Click to show/hide]"
    | Custom Format                                                                                                   |                                  Score                                  | Trash ID                                             |
    | --------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ---------------------------------------------------- |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01) |   {{ sonarr['cf']['french-web-tier-01']['trash_scores']['default'] }}   | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02) |   {{ sonarr['cf']['french-web-tier-02']['trash_scores']['default'] }}   | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }} |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03) |   {{ sonarr['cf']['french-web-tier-03']['trash_scores']['default'] }}   | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }} |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)      | :warning: {{ sonarr['cf']['french-scene']['trash_scores']['default'] }} | {{ sonarr['cf']['french-scene']['trash_id'] }}       |

    !!! tip
        :warning: French Scene groups are included as a fallback if you really want MULTi release despite a potential loss in quality. Either score the CF to `{{ sonarr['cf']['french-scene']['trash_scores']['default'] }}` (default) or `0` depending on what you want to achieve.

    ??? info "Original mix (optional)"
        {! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}
