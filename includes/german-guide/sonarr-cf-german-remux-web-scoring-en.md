<!-- markdownlint-disable MD041-->
??? abstract "HQ Source Groups - [Click to show/hide]"

    | Custom Format                                                                                                           |                                  Score                                  | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ------------------------------------------------------ |
    | [{{ sonarr['cf']['german-remux-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-remux-tier-01) |  {{ sonarr['cf']['german-remux-tier-01']['trash_scores']['default'] }}  | {{ sonarr['cf']['german-remux-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['german-remux-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-remux-tier-02) |  {{ sonarr['cf']['german-remux-tier-02']['trash_scores']['default'] }}  | {{ sonarr['cf']['german-remux-tier-02']['trash_id'] }} |
    | [{{ sonarr['cf']['german-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-web-tier-01)     |   {{ sonarr['cf']['german-web-tier-01']['trash_scores']['default'] }}   | {{ sonarr['cf']['german-web-tier-01']['trash_id'] }}   |
    | [{{ sonarr['cf']['german-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-web-tier-02)     |   {{ sonarr['cf']['german-web-tier-02']['trash_scores']['default'] }}   | {{ sonarr['cf']['german-web-tier-02']['trash_id'] }}   |
    | [{{ sonarr['cf']['german-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-web-tier-03)     |   {{ sonarr['cf']['german-web-tier-03']['trash_scores']['default'] }}   | {{ sonarr['cf']['german-web-tier-03']['trash_id'] }}   |
    | [{{ sonarr['cf']['german-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-scene)                 | :warning: {{ sonarr['cf']['german-scene']['trash_scores']['default'] }} | {{ sonarr['cf']['german-scene']['trash_id'] }}         |
    | [{{ sonarr['cf']['web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-01)                   |      {{ sonarr['cf']['web-tier-01']['trash_scores']['default'] }}       | {{ sonarr['cf']['web-tier-01']['trash_id'] }}          |
    | [{{ sonarr['cf']['web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-02)                   |      {{ sonarr['cf']['web-tier-02']['trash_scores']['default'] }}       | {{ sonarr['cf']['web-tier-02']['trash_id'] }}          |
    | [{{ sonarr['cf']['web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-03)                   |      {{ sonarr['cf']['web-tier-03']['trash_scores']['default'] }}       | {{ sonarr['cf']['web-tier-03']['trash_id'] }}          |

    !!! tip

        :warning: German Scene groups are included as a fallback if you really want their release despite a potential loss in quality. Either score the CF to `{{ sonarr['cf']['german-scene']['trash_scores']['default'] }}` (default) or `0`, depending on what you want to achieve.

    Note: Bluray Custom Formats are not included as the main fallback for this profile is WEB. However, feel free to add them if needed.
<!-- markdownlint-enable MD041-->
