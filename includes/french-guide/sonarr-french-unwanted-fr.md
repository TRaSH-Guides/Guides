??? abstract "Indésirable - [Cliquer pour afficher/masquer]"

    | Formats Personnalisés                                                                                           |                               Score                               | Trash ID                                           |
    |-----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------:|----------------------------------------------------|
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk)                   |     {{ sonarr['cf']['br-disk']['trash_scores']['default'] }}      | {{ sonarr['cf']['br-disk']['trash_id'] }}          |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq)                             |        {{ sonarr['cf']['lq']['trash_scores']['default'] }}        | {{ sonarr['cf']['lq']['trash_id'] }}               |
    | [{{ sonarr['cf']['lq-release-title']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq-release-title) | {{ sonarr['cf']['lq-release-title']['trash_scores']['default'] }} | {{ sonarr['cf']['lq-release-title']['trash_id'] }} |
    | [{{ sonarr['cf']['french-lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-lq)                   |    {{ sonarr['cf']['french-lq']['trash_scores']['default'] }}     | {{ sonarr['cf']['french-lq']['trash_id'] }}        |
    | [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd) :warning:         |     {{ sonarr['cf']['x265-hd']['trash_scores']['default'] }}      | {{ sonarr['cf']['x265-hd']['trash_id'] }}          |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#extras)                     |      {{ sonarr['cf']['extras']['trash_scores']['default'] }}      | {{ sonarr['cf']['extras']['trash_id'] }}           |
    | [{{ sonarr['cf']['av1']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#av1)                           |       {{ sonarr['cf']['av1']['trash_scores']['default'] }}        | {{ sonarr['cf']['av1']['trash_id'] }}              |

    ---

    Détail et Pourquoi

    - **{{ sonarr['cf']['br-disk']['name'] }} :** Format Personnalisé qui aides Radarr à reconnaître et ignorer les BR-DISK (ISO et structure de dossier Blu-ray) en plus de la qualité standard BR-DISK.
    - **{{ sonarr['cf']['lq']['name'] }} :** Une collection de groupes connus qui sont souvent bannis en raison du manque de qualité de leurs releases ou pour d'autres raisons.
    - **{{ sonarr['cf']['lq-release-title']['name'] }} :** Une collection de termes trouvés dans les titres de release de faible qualité.
    - **{{ sonarr['cf']['french-lq']['name'] }} :** Une collection de groupes français connus qui sont souvent bannis en raison du manque de qualité de leurs releases ou pour d'autres raisons.
    - **{{ sonarr['cf']['x265-hd']['name'] }} :** Bloque les release 720/1080p (HD) qui sont encodées en x265.

        {! include-markdown "../../includes/cf-descriptions/x265-hd-sonarr-warning.md" !}

    - **{{ sonarr['cf']['extras']['name'] }} :** Bloque les publications qui ne contiennent que des extras
    - **{{ sonarr['cf']['av1']['name'] }} :** Cela bloque toutes les publications encodées en AV1.

        {! include-markdown "../../includes/cf-descriptions/av1.md" !}

    ??? warning "Type de FanSubs - [Cliquer pour afficher/masquer]"

        Ces Formats Personnalisés sont optionnels et permettent de savoir quel type de FanSubs vos versions possèdent. Seul le `FastSub` n'est pas souhaité car il est souvent fait trop rapidement et reste peu soigné. Si vous ne voulez pas de FanSub non plus, vous devez aussi lui donner un score de {{ sonarr['cf']['fastsub']['trash_scores']['default'] }}.

        | Formats Personnalisés                                                                         |                          Score                           | Trash ID                                  |
        |-----------------------------------------------------------------------------------------------|:--------------------------------------------------------:|-------------------------------------------|
        | [{{ sonarr['cf']['fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fansub)   |                            0                             | {{ sonarr['cf']['fansub']['trash_id'] }}  |
        | [{{ sonarr['cf']['fastsub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fastsub) | {{ sonarr['cf']['fastsub']['trash_scores']['default'] }} | {{ sonarr['cf']['fastsub']['trash_id'] }} |
