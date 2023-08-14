??? abstract "HQ Source Groups - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                                       |                                           Score                                           | Trash ID                                                   |
    | --------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------: | ---------------------------------------------------------- |
    | [{{ sonarr['cf']['french-anime-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-01)         |           {{ sonarr['cf']['french-anime-tier-01']['trash_scores']['default'] }}           | {{ sonarr['cf']['french-anime-tier-01']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-anime-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-02)         |           {{ sonarr['cf']['french-anime-tier-02']['trash_scores']['default'] }}           | {{ sonarr['cf']['french-anime-tier-02']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-anime-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-03)         |           {{ sonarr['cf']['french-anime-tier-03']['trash_scores']['default'] }}           | {{ sonarr['cf']['french-anime-tier-03']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)                  |               {{ sonarr['cf']['french-scene']['trash_scores']['default'] }}               | {{ sonarr['cf']['french-scene']['trash_id'] }}             |
    | [{{ sonarr['cf']['french-anime-fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-fansub)           |      {{ sonarr['cf']['french-anime-fansub']['trash_scores']['default'] }} ou `1000`       | {{ sonarr['cf']['french-anime-fansub']['trash_id'] }}      |
    | [{{ sonarr['cf']['french-hd-bluray-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-hd-bluray-tier-01) | (optional) {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_scores']['french-anime'] }} | {{ sonarr['cf']['french-hd-bluray-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01)             |    (optional) {{ sonarr['cf']['french-web-tier-01']['trash_scores']['french-anime'] }}    | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02)             |    (optional) {{ sonarr['cf']['french-web-tier-02']['trash_scores']['french-anime'] }}    | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03)             |    (optional) {{ sonarr['cf']['french-web-tier-03']['trash_scores']['french-anime'] }}    | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }}       |

    !!! tip
        Les groupes de la scène française sont inclus et devraient toujours être ajoutés car certains des principaux groupes qui publient des versions sous-titrées et/ou doublées en français en sont issus.

        Les groupes FanSUB peuvent être notés soit {{ sonarr['cf']['french-anime-fansub']['trash_scores']['default'] }} (par défaut) soit `1000` selon que vous souhaitez privilégier les sorties FanSUB ou SeaDex.

    !!! tip "Original French Bluray/Web Tiers"
        Ils sont optionnels et peuvent être inclus ou non. Cela est dû au fait que certains d'entre eux ont tendance à publier des animes.
