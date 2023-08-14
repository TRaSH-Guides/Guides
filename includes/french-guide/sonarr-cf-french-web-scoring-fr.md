??? abstract "HQ Source Groups - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                           |                                  Score                                  | Trash ID                                             |
    | --------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ---------------------------------------------------- |
    | [{{ sonarr['cf']['french-web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-01) |   {{ sonarr['cf']['french-web-tier-01']['trash_scores']['default'] }}   | {{ sonarr['cf']['french-web-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['french-web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-02) |   {{ sonarr['cf']['french-web-tier-02']['trash_scores']['default'] }}   | {{ sonarr['cf']['french-web-tier-02']['trash_id'] }} |
    | [{{ sonarr['cf']['french-web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-web-tier-03) |   {{ sonarr['cf']['french-web-tier-03']['trash_scores']['default'] }}   | {{ sonarr['cf']['french-web-tier-03']['trash_id'] }} |
    | [{{ sonarr['cf']['french-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-scene-groups)      | :warning: {{ sonarr['cf']['french-scene']['trash_scores']['default'] }} | {{ sonarr['cf']['french-scene']['trash_id'] }}       |

    !!! tip
        :warning: Les groupes de la Scène française sont inclus comme substitut si vous voulez vraiment une version MULTi malgré une éventuelle perte de qualité. Vous pouvez lui attribuer un score de `{{ radarr['cf']['french-scene']['trash_scores']['default'] }}` (par défaut) ou de `0` selon ce que vous voulez obtenir.

    ??? info "Mix original (optionnel)"
        {! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}
