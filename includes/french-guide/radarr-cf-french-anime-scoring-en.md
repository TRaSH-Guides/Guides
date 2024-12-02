??? abstract "HQ Source Groups - [Click to show/hide]"

    | Custom Format                                                                                                                   | Trash ID                                                   | VOSTFR Profile Score                                                                  | MULTi.VO Profile Score                                                               |
    | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
    | [{{ radarr['cf']['language-original-french']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#language-original-french) | {{ radarr['cf']['language-original-french']['trash_id'] }} | {{ radarr['cf']['language-original-french']['trash_scores']['french-anime-vostfr'] }} | {{ radarr['cf']['language-original-french']['trash_scores']['french-anime-multi'] }} |
    | [{{ radarr['cf']['language-not-original']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#language-not-original)       | {{ radarr['cf']['language-not-original']['trash_id'] }}    | {{ radarr['cf']['language-not-original']['trash_scores']['french-anime-vostfr'] }}    | {{ radarr['cf']['language-not-original']['trash_scores']['french-anime-multi'] }}    |
    | [{{ radarr['cf']['language-not-french']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#language-not-french)           | {{ radarr['cf']['language-not-french']['trash_id'] }}      | {{ radarr['cf']['language-not-french']['trash_scores']['french-anime-vostfr'] }}      | {{ radarr['cf']['language-not-french']['trash_scores']['french-anime-multi'] }}      |
    | [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#vostfr)                              | {{ radarr['cf']['french-vostfr']['trash_id'] }}            | {{ radarr['cf']['french-vostfr']['trash_scores']['french-anime-vostfr'] }}            | {{ radarr['cf']['french-vostfr']['trash_scores']['french-anime-multi'] }}            |
    | [{{ radarr['cf']['french-anime-tier-01']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-anime-tier-01)             | {{ radarr['cf']['french-anime-tier-01']['trash_id'] }}     | {{ radarr['cf']['french-anime-tier-01']['trash_scores']['french-anime-vostfr'] }}     | {{ radarr['cf']['french-anime-tier-01']['trash_scores']['french-anime-multi'] }}     |
    | [{{ radarr['cf']['french-anime-tier-02']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-anime-tier-02)             | {{ radarr['cf']['french-anime-tier-02']['trash_id'] }}     | {{ radarr['cf']['french-anime-tier-02']['trash_scores']['french-anime-vostfr'] }}     | {{ radarr['cf']['french-anime-tier-02']['trash_scores']['french-anime-multi'] }}     |
    | [{{ radarr['cf']['french-anime-tier-03']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-anime-tier-03)             | {{ radarr['cf']['french-anime-tier-03']['trash_id'] }}     | {{ radarr['cf']['french-anime-tier-03']['trash_scores']['french-anime-vostfr'] }}     | {{ radarr['cf']['french-anime-tier-03']['trash_scores']['french-anime-multi'] }}     |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-scene-groups)                      | {{ radarr['cf']['french-scene']['trash_id'] }}             | {{ radarr['cf']['french-scene']['trash_scores']['french-anime-vostfr'] }}             | {{ radarr['cf']['french-scene']['trash_scores']['french-anime-multi'] }}             |
    | [{{ radarr['cf']['french-anime-fansub']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-anime-fansub)               | {{ radarr['cf']['french-anime-fansub']['trash_id'] }}      | {{ radarr['cf']['french-anime-fansub']['trash_scores']['french-anime-vostfr'] }}      | {{ radarr['cf']['french-anime-fansub']['trash_scores']['french-anime-multi'] }}      |
    | [{{ radarr['cf']['french-hd-bluray-tier-01']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-hd-bluray-tier-01)     | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_id'] }} | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_scores']['french-anime-vostfr'] }} | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_scores']['french-anime-multi'] }} |
    | [{{ radarr['cf']['french-hd-bluray-tier-02']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-hd-bluray-tier-02)     | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_id'] }} | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_scores']['french-anime-vostfr'] }} | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_scores']['french-anime-multi'] }} |
    | [{{ radarr['cf']['french-web-tier-01']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-web-tier-01)                 | {{ radarr['cf']['french-web-tier-01']['trash_id'] }}       | {{ radarr['cf']['french-web-tier-01']['trash_scores']['french-anime-vostfr'] }}       | {{ radarr['cf']['french-web-tier-01']['trash_scores']['french-anime-multi'] }}       |
    | [{{ radarr['cf']['french-web-tier-02']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-web-tier-02)                 | {{ radarr['cf']['french-web-tier-02']['trash_id'] }}       | {{ radarr['cf']['french-web-tier-02']['trash_scores']['french-anime-vostfr'] }}       | {{ radarr['cf']['french-web-tier-02']['trash_scores']['french-anime-multi'] }}       |

    !!! tip

        French Scene groups are included and should always be added, as some of the biggest releasers of French subbed and/or dubbed content are from the French Scene.

        FanSUB groups can be scored either {{ radarr['cf']['french-anime-fansub']['trash_scores']['default'] }} (default) or `1000`, depending on whether you prefer FanSUB or SeaDex releases.

    !!! tip "Original French Blu-ray/Web Tiers"

        They are optional and can be included or not. This is because some of them tend to release some anime.

    !!! tip "VOSTFR Profile Score"

        If you want the VOSTFR profile to also accept MULTI releases when no VOSTFR release is available, you need to set the value of [{{ radarr['cf']['language-original-french']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#language-original-french) to `0` instead of `{{ radarr['cf']['language-original-french']['trash_scores']['french-anime-vostfr'] }}`

    !!! tip "Prefer the FanSub version to others"

        For this example, if you prefer FanSub to any FR Anime Tiers, you should score the [{{ radarr['cf']['french-anime-fansub']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#fr-anime-fansub) to `1700` instead of `{{ radarr['cf']['french-anime-fansub']['trash_scores']['default'] }}`
