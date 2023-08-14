??? abstract "HQ Source Groups - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                                       |                                   Score                                   | Trash ID                                                   |
    | --------------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------: | ---------------------------------------------------------- |
    | [{{ radarr['cf']['french-hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hd-bluray-tier-01) | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_scores']['default'] }} | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['french-hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hd-bluray-tier-02) | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_scores']['default'] }} | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['french-web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-web-tier-01)             |    {{ radarr['cf']['french-web-tier-01']['trash_scores']['default'] }}    | {{ radarr['cf']['french-web-tier-01']['trash_id'] }}       |
    | [{{ radarr['cf']['french-web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-web-tier-02)             |    {{ radarr['cf']['french-web-tier-02']['trash_scores']['default'] }}    | {{ radarr['cf']['french-web-tier-02']['trash_id'] }}       |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups)                  |  :warning: {{ radarr['cf']['french-scene']['trash_scores']['default'] }}  | {{ radarr['cf']['french-scene']['trash_id'] }}             |

    !!! tip
        :warning: Les groupes de la Scène française sont inclus comme substitut si vous voulez vraiment une version MULTi malgré une éventuelle perte de qualité. Vous pouvez lui attribuer un score de `{{ radarr['cf']['french-scene']['trash_scores']['default'] }}` (par défaut) ou de `0` selon ce que vous voulez obtenir.

    ??? info "Mix original (optionnel)"
        {! include-markdown "../../includes/cf/radarr-cf-hd-bluray-web-scoring.md" !}
