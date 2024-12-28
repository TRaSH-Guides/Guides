??? abstract "HQ Source Groups - [Click to show/hide]"

    | Custom Format                                                                                                                   | Trash ID                                                   |                                 VOSTFR Profile Score                                  |                                MULTi.VO Profile Score                                |
    |---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|:-------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
    | [{{ sonarr['cf']['language-original-plus-french']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#language-original-plus-french) | {{ sonarr['cf']['language-original-plus-french']['trash_id'] }} | {{ sonarr['cf']['language-original-plus-french']['trash_scores']['french-anime-vostfr'] }} | {{ sonarr['cf']['language-original-plus-french']['trash_scores']['french-anime-multi'] }} |
    | [{{ sonarr['cf']['language-not-original']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#language-not-original)       | {{ sonarr['cf']['language-not-original']['trash_id'] }}    |  {{ sonarr['cf']['language-not-original']['trash_scores']['french-anime-vostfr'] }}   |  {{ sonarr['cf']['language-not-original']['trash_scores']['french-anime-multi'] }}   |
    | [{{ sonarr['cf']['language-not-french']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#language-not-french)           | {{ sonarr['cf']['language-not-french']['trash_id'] }}      |   {{ sonarr['cf']['language-not-french']['trash_scores']['french-anime-vostfr'] }}    |   {{ sonarr['cf']['language-not-french']['trash_scores']['french-anime-multi'] }}    |
    | [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr)                              | {{ sonarr['cf']['french-vostfr']['trash_id'] }}            |      {{ sonarr['cf']['french-vostfr']['trash_scores']['french-anime-vostfr'] }}       |      {{ sonarr['cf']['french-vostfr']['trash_scores']['french-anime-multi'] }}       |
    | [{{ sonarr['cf']['french-anime-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-01)             | {{ sonarr['cf']['french-anime-tier-01']['trash_id'] }}     |   {{ sonarr['cf']['french-anime-tier-01']['trash_scores']['french-anime-vostfr'] }}   |   {{ sonarr['cf']['french-anime-tier-01']['trash_scores']['french-anime-multi'] }}   |
    | [{{ sonarr['cf']['french-anime-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-02)             | {{ sonarr['cf']['french-anime-tier-02']['trash_id'] }}     |   {{ sonarr['cf']['french-anime-tier-02']['trash_scores']['french-anime-vostfr'] }}   |   {{ sonarr['cf']['french-anime-tier-02']['trash_scores']['french-anime-multi'] }}   |
    | [{{ sonarr['cf']['french-anime-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-03)             | {{ sonarr['cf']['french-anime-tier-03']['trash_id'] }}     |   {{ sonarr['cf']['french-anime-tier-03']['trash_scores']['french-anime-vostfr'] }}   |   {{ sonarr['cf']['french-anime-tier-03']['trash_scores']['french-anime-multi'] }}   |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)                      | {{ sonarr['cf']['french-scene']['trash_id'] }}             |       {{ sonarr['cf']['french-scene']['trash_scores']['french-anime-vostfr'] }}       |       {{ sonarr['cf']['french-scene']['trash_scores']['french-anime-multi'] }}       |
    | [{{ sonarr['cf']['french-anime-fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-fansub)               | {{ sonarr['cf']['french-anime-fansub']['trash_id'] }}      |   {{ sonarr['cf']['french-anime-fansub']['trash_scores']['french-anime-vostfr'] }}    |   {{ sonarr['cf']['french-anime-fansub']['trash_scores']['french-anime-multi'] }}    |
    | [{{ sonarr['cf']['french-hd-bluray-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-hd-bluray-tier-01)     | {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_id'] }} | {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_scores']['french-anime-vostfr'] }} | {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_scores']['french-anime-multi'] }} |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01)                 | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }}       |    {{ sonarr['cf']['french-web-tier-01']['trash_scores']['french-anime-vostfr'] }}    |    {{ sonarr['cf']['french-web-tier-01']['trash_scores']['french-anime-multi'] }}    |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02)                 | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }}       |    {{ sonarr['cf']['french-web-tier-02']['trash_scores']['french-anime-vostfr'] }}    |    {{ sonarr['cf']['french-web-tier-02']['trash_scores']['french-anime-multi'] }}    |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03)                 | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }}       |    {{ sonarr['cf']['french-web-tier-03']['trash_scores']['french-anime-vostfr'] }}    |    {{ sonarr['cf']['french-web-tier-03']['trash_scores']['french-anime-multi'] }}    |

    !!! tip

        French Scene groups are included and should always be added, as some of the biggest releasers of French subbed and/or dubbed content are from the French Scene.

        FanSUB groups can be scored either {{ sonarr['cf']['french-anime-fansub']['trash_scores']['default'] }} (default) or `1000`, depending on whether you prefer FanSUB or SeaDex releases.

    !!! tip "Original French Blu-ray/Web Tiers"

        They are optional and can be included or not. This is because some of them tend to release some anime.

    !!! tip "VOSTFR Profile Score"

        If you want the VOSTFR profile to also accept MULTI releases when no VOSTFR release is available, you need to set the value of [{{ sonarr['cf']['language-original-plus-french']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#language-original-plus-french) to `0` instead of `{{ sonarr['cf']['language-original-plus-french']['trash_scores']['french-anime-vostfr'] }}`

    !!! tip "Prefer the FanSub version to others"

        For this example, if you prefer FanSub to any FR Anime Tiers, you should score the [{{ sonarr['cf']['french-anime-fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-fansub) to `1700` instead of `{{ sonarr['cf']['french-anime-fansub']['trash_scores']['default'] }}`
