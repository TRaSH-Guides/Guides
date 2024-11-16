??? abstract "Indésirable - [Cliquer pour afficher/masquer]"

    | Formats Personnalisés                                                                                           |                               Score                               | Trash ID                                           |
    |-----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------:|----------------------------------------------------|
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)                   |     {{ radarr['cf']['br-disk']['trash_scores']['default'] }}      | {{ radarr['cf']['br-disk']['trash_id'] }}          |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                             |        {{ radarr['cf']['lq']['trash_scores']['default'] }}        | {{ radarr['cf']['lq']['trash_id'] }}               |
    | [{{ radarr['cf']['lq-release-title']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq-release-title) | {{ radarr['cf']['lq-release-title']['trash_scores']['default'] }} | {{ radarr['cf']['lq-release-title']['trash_id'] }} |
    | [{{ radarr['cf']['french-lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-lq)                   |    {{ radarr['cf']['french-lq']['trash_scores']['default'] }}     | {{ radarr['cf']['french-lq']['trash_id'] }}        |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning:         |     {{ radarr['cf']['x265-hd']['trash_scores']['default'] }}      | {{ radarr['cf']['x265-hd']['trash_id'] }}          |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                             |        {{ radarr['cf']['3d']['trash_scores']['default'] }}        | {{ radarr['cf']['3d']['trash_id'] }}               |
    | [{{ radarr['cf']['upscaled']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#upscaled)                 |     {{ radarr['cf']['upscaled']['trash_scores']['default'] }}     | {{ radarr['cf']['upscaled']['trash_id'] }}         |
    | [{{ radarr['cf']['extras']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#extras)                     |      {{ radarr['cf']['extras']['trash_scores']['default'] }}      | {{ radarr['cf']['extras']['trash_id'] }}           |
    | [{{ radarr['cf']['av1']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#av1)                           |       {{ radarr['cf']['av1']['trash_scores']['default'] }}        | {{ radarr['cf']['av1']['trash_id'] }}              |

    ---

    Détail et Pourquoi

    - **{{ radarr['cf']['br-disk']['name'] }} :** Format Personnalisé qui aides Radarr à reconnaître et ignorer les BR-DISK (ISO et structure de dossier Blu-ray) en plus de la qualité standard BR-DISK.
    - **{{ radarr['cf']['lq']['name'] }} :** Une collection de groupes connus qui sont souvent bannis en raison du manque de qualité de leurs releases ou pour d'autres raisons.
    - **{{ radarr['cf']['lq-release-title']['name'] }} :** Une collection de termes trouvés dans les titres de release de faible qualité.
    - **{{ radarr['cf']['french-lq']['name'] }} :** Une collection de groupes français connus qui sont souvent bannis en raison du manque de qualité de leurs releases ou pour d'autres raisons.
    - **{{ radarr['cf']['x265-hd']['name'] }} :** Bloque les release 720/1080p (HD) qui sont encodées en x265..

        {! include-markdown "../../includes/cf-descriptions/x265-hd-radarr-warning.md" !}

    - **{{ radarr['cf']['3d']['name'] }} :** La 3D est-elle encore d'actualité ?
    - **{{ radarr['cf']['upscaled']['name'] }} :** Un Format Personnalisé pour empêcher Radarr de récupérer des versions upscalées (amélioré via IA).
    - **{{ radarr['cf']['extras']['name'] }} :** Bloque les publications qui ne contiennent que des extras
    - **{{ radarr['cf']['av1']['name'] }} :** Cela bloque toutes les publications encodées en AV1.

        {! include-markdown "../../includes/cf-descriptions/av1.md" !}
