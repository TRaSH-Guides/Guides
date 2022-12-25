??? summary "Indésirable - [CLIQUEZ POUR AFFICHER]"
    | Formats Personnalisés                                                                                               | Score                                                | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk)                       | {{ sonarr['cf']['br-disk']['trash_score'] }}         | {{ sonarr['cf']['br-disk']['trash_id'] }}         |
    | [{{ sonarr['cf']['french-lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-lq)                       | {{ sonarr['cf']['french-lq']['trash_score'] }}       | {{ sonarr['cf']['french-lq']['trash_id'] }}       |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }} :** Il s'agit d'un format personnalisé pour aider Sonarr à reconnaître et à ignorer les BR-DISK (ISO et structure de dossier Blu-ray) en plus de la qualité standard des BR-DISK.
    - **{{ sonarr['cf']['french-lq']['name'] }}:** Une collection de groupes P2P français qui sont souvent bannis des meilleurs trackers en raison de leur manque de qualité ou pour d'autres raisons.
