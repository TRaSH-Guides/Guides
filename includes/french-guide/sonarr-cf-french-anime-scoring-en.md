??? abstract "HQ Source Groups - [Click to show/hide]"
    | Custom Format                                                                                                               |                                           Score                                           | Trash ID                                                   |
    | --------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------: | ---------------------------------------------------------- |
    | [{{ sonarr['cf']['french-anime-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-01)         |           {{ sonarr['cf']['french-anime-tier-01']['trash_scores']['default'] }}           | {{ sonarr['cf']['french-anime-tier-01']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-anime-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-02)         |           {{ sonarr['cf']['french-anime-tier-02']['trash_scores']['default'] }}           | {{ sonarr['cf']['french-anime-tier-02']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-anime-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-03)         |           {{ sonarr['cf']['french-anime-tier-03']['trash_scores']['default'] }}           | {{ sonarr['cf']['french-anime-tier-03']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)                  |               {{ sonarr['cf']['french-scene']['trash_scores']['default'] }}               | {{ sonarr['cf']['french-scene']['trash_id'] }}             |
    | [{{ sonarr['cf']['french-anime-fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-fansub)           |      {{ sonarr['cf']['french-anime-fansub']['trash_scores']['default'] }} or `1000`       | {{ sonarr['cf']['french-anime-fansub']['trash_id'] }}      |
    | [{{ sonarr['cf']['french-hd-bluray-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-hd-bluray-tier-01) | (optional) {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_scores']['french-anime'] }} | {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01)             |    (optional) {{ sonarr['cf']['french-web-tier-01']['trash_scores']['french-anime'] }}    | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02)             |    (optional) {{ sonarr['cf']['french-web-tier-02']['trash_scores']['french-anime'] }}    | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03)             |    (optional) {{ sonarr['cf']['french-web-tier-03']['trash_scores']['french-anime'] }}    | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }}       |

    !!! tip
        French Scene groups are included and should be always added as some of the biggest releaser of French subbed and/or dubbed are from the French Scene.

        FanSUB groups can either be scored either {{ sonarr['cf']['french-anime-fansub']['trash_scores']['default'] }} (default) or `1000` depending if you want to prefer FanSUB or SeaDex releases.

    !!! tip "Original French Bluray/Web Tiers"
        They are optional and can be included or not. This is due because some of them tend to release some animes.
