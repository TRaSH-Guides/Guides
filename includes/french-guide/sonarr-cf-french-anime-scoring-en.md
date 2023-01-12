??? abstract "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                                                       | Score                                                     | Trash ID                                               |
    | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
    | [{{ sonarr['cf']['french-anime-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-01) | {{ sonarr['cf']['french-anime-tier-01']['trash_score'] }}       | {{ sonarr['cf']['french-anime-tier-01']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-anime-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-02) | {{ sonarr['cf']['french-anime-tier-02']['trash_score'] }}       | {{ sonarr['cf']['french-anime-tier-02']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)          | {{ sonarr['cf']['french-scene']['trash_score'] }}               | {{ sonarr['cf']['french-scene']['trash_id'] }}               |
    | [{{ sonarr['cf']['french-anime-fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-fansub)   | {{ sonarr['cf']['french-anime-fansub']['trash_score'] }} or `1000` | {{ sonarr['cf']['french-anime-fansub']['trash_id'] }}        |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01)     | (optional) `1100`                                               | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }}         |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02)     | (optional) `1100`                                               | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }}         |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03)     | (optional) `1100`                                               | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }}         |
    | :warning: {{ sonarr['cf']['french-anime-tier-optional']['name'] }} :warning:                                        | {{ sonarr['cf']['french-anime-tier-optional']['trash_score'] }} | {{ sonarr['cf']['french-anime-tier-optional']['trash_id'] }} |

    !!! tip
        French Scene groups are included and should be always added as some of the biggest releaser of French subbed and/or dubbed are from the French Scene.

        FanSUB groups can either be scored either {{ sonarr['cf']['french-anime-fansub']['trash_score'] }} (default) or `1000` depending if you want to prefer FanSUB or SeaDex releases.

    !!! tip "Original French Web Tiers"
        French Web tiers are optional and can be included or not. This is due because some of them tend to release some Dubbed anime. Only add them if you are looking for MULTi releases as their VOSTFR releases are easily trumped by either the original Anime guide or by the French Anime tiers.

    !!! danger ":warning: {{ sonarr['cf']['french-anime-tier-optional']['name'] }}"
        This tier should only be added to your setup if you are not using the orginal anime guide score (the Seadex anime tiers). Otherwise, you will end with double scoring on those groups.
