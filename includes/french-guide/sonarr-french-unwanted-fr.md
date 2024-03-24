??? abstract "Indésirable - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                   |                           Score                            | Trash ID                                    |
    | ------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------: | ------------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk)           |  {{ sonarr['cf']['br-disk']['trash_scores']['default'] }}  | {{ sonarr['cf']['br-disk']['trash_id'] }}   |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq)                     |    {{ sonarr['cf']['lq']['trash_scores']['default'] }}     | {{ sonarr['cf']['lq']['trash_id'] }}        |
    | [{{ sonarr['cf']['french-lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-lq)           | {{ sonarr['cf']['french-lq']['trash_scores']['default'] }} | {{ sonarr['cf']['french-lq']['trash_id'] }} |
    | [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd) :warning: |  {{ sonarr['cf']['x265-hd']['trash_scores']['default'] }}  | {{ sonarr['cf']['x265-hd']['trash_id'] }}   |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#extras)             |  {{ sonarr['cf']['extras']['trash_scores']['default'] }}   | {{ sonarr['cf']['extras']['trash_id'] }}    |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }} :** Il s'agit d'un format personnalisé pour aider Sonarr à reconnaître et à ignorer les BR-DISK (ISO et structure de dossier Blu-ray) en plus de la qualité standard des BR-DISK.
    - **{{ sonarr['cf']['lq']['name'] }}:** Une collection de groupes P2P anglais qui sont souvent bannis des meilleurs trackers en raison de leur manque de qualité ou pour d'autres raisons.
    - **{{ sonarr['cf']['french-lq']['name'] }}:** Une collection de groupes P2P français qui sont souvent bannis des meilleurs trackers en raison de leur manque de qualité ou pour d'autres raisons.
    - **{{ sonarr['cf']['x265-hd']['name'] }}:** Ceci bloque/ignore les sorties 720/1080p (HD) qui sont encodées en x265. - Plus d'informations [ICI](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"} (en anglais).

        !!! Danger "Ne l'utilisez pas avec le Format Personnalisé [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning:"

    - **{{ sonarr['cf']['extras']['name'] }}:** Bloque les extras

    ??? warning "Type de FanSubs - [Cliquer pour afficher/masquer]"
        Ces Formats Personnalisés sont optionnels et permettent de savoir quel type de FanSubs vos versions possèdent. Seul le FastSub n'est pas souhaité car il est souvent fait trop rapidement et reste peu soigné. Si vous ne voulez pas de FanSub non plus, vous devez aussi lui donner un score de {{ sonarr['cf']['fastsub']['trash_scores']['default'] }}.

        | Formats Personnalisés                                                                         |                          Score                           | Trash ID                                  |
        | --------------------------------------------------------------------------------------------- | :------------------------------------------------------: | ----------------------------------------- |
        | [{{ sonarr['cf']['fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fansub)   |                            0                             | {{ sonarr['cf']['fansub']['trash_id'] }}  |
        | [{{ sonarr['cf']['fastsub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fastsub) | {{ sonarr['cf']['fastsub']['trash_scores']['default'] }} | {{ sonarr['cf']['fastsub']['trash_id'] }} |
