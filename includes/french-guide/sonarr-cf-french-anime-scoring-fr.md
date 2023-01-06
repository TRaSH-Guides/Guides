??? summary "HQ Source Groups - [CLIQUEZ POUR AFFICHER]"
    | Formats Personnalisés                                                                                               | Score                                                     | Trash ID                                               |
    | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
    | [{{ sonarr['cf']['french-anime-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-01) | {{ sonarr['cf']['french-anime-tier-01']['trash_score'] }}       | {{ sonarr['cf']['french-anime-tier-01']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-anime-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-tier-02) | {{ sonarr['cf']['french-anime-tier-02']['trash_score'] }}       | {{ sonarr['cf']['french-anime-tier-02']['trash_id'] }}       |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)          | {{ sonarr['cf']['french-scene']['trash_score'] }}               | {{ sonarr['cf']['french-scene']['trash_id'] }}               |
    | [{{ sonarr['cf']['french-anime-fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-anime-fansub)   | {{ sonarr['cf']['french-anime-fansub']['trash_score'] }}        | {{ sonarr['cf']['french-anime-fansub']['trash_id'] }}        |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01)     | (optionnel) `1100`                                              | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }}         |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02)     | (optionnel) `1100`                                              | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }}         |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03)     | (optionnel) `1100`                                              | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }}         |
    | :warning: {{ sonarr['cf']['french-anime-tier-optional']['name'] }} :warning:                                        | {{ sonarr['cf']['french-anime-tier-optional']['trash_score'] }} | {{ sonarr['cf']['french-anime-tier-optional']['trash_id'] }} |

    !!! tip
        Les groupes de la scène française sont inclus et devraient toujours être ajoutés car certains des principaux groupes qui publient des versions sous-titrées et/ou doublées en français en sont issus.

        Les groupes FanSUB peuvent être notés soit {{ sonarr['cf']['french-anime-fansub']['trash_score'] }} (par défaut) soit `1000` selon que vous souhaitez privilégier les sorties FanSUB ou SeaDex.

    !!! tip "Original French Web Tiers"
        Ils sont optionnels et peuvent être inclus ou non. Cela est dû au fait que certains d'entre eux ont tendance à publier des anime doublés. Ajoutez-les uniquement si vous recherchez des sorties MULTi, car leurs sorties VOSTFR sont facilement supplantées.

    !!! danger ":warning: {{ sonarr['cf']['french-anime-tier-optional']['name'] }}"
        Ce tier ne doit être ajouté à votre configuration que si vous n'utilisez pas le score original du Anime Guide (les tiers Seadex). Sinon, vous doublerez le score pour ces groupes.
