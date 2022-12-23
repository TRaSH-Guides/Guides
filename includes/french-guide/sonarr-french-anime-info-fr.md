!!! info "Important"
    Dans un premier temps, vous devez suivre les sections suivantes du Guide Anime original (en anglais uniquemment) :

    - [How to setup Quality Profiles Anime | Media Management](/Sonarr/sonarr-setup-quality-profiles-anime/#media-management){:target="_blank" rel="noopener noreferrer"}.
    - [How to setup Quality Profiles Anime | Quality Settings](/Sonarr/sonarr-setup-quality-profiles-anime/#quality-settings){:target="_blank" rel="noopener noreferrer"}.
    - [How to setup Quality Profiles Anime | Quality Profile](/Sonarr/sonarr-setup-quality-profiles-anime/#quality-profile){:target="_blank" rel="noopener noreferrer"}.

    Ne continuez pas avant d'avoir lu ces trois sections et d'avoir suivi leurs instructions.

    !!! info "Original Scoring"
        Il s'agit de la notation originale du Guide Anime et elle doit être suivie en fonction de ce que vous voulez obtenir. Ainsi vous ne trouvez pas de version VOSTFR ou MULTi, vous aurez toujours une version de bonne qualité :

        - [Default Scoring](/Sonarr/sonarr-setup-quality-profiles-anime/#default-scoring){:target="_blank" rel="noopener noreferrer"}: La configuration par défaut qui garantit que vous aurez au minimum une bonne version sous-titrée en anglais. *Rappelez-vous que si vous ne voulez que des versions sous-titrées, cela devrait être le choix idéal et vous devriez essayer de configurer [Bazarr](/Bazarr/Setup-Guide){:target="_blank" rel="noopener noreferrer"} pour obtenir la VOSTFR.*
        - [Dual Audio](/Sonarr/sonarr-setup-quality-profiles-anime/#dual-audio-scoring){:target="_blank" rel="noopener noreferrer"}: Si vous voulez avoir des versions Dual Audio (audio original et anglais) au cas où Sonarr ne trouve pas de sortie VOSTFR ou MULTi.
        - [Uncensored Scoring](/Sonarr/sonarr-setup-quality-profiles-anime/#uncensored-scoring){:target="_blank" rel="noopener noreferrer"}: Si vous préférez les versions non censurées (les Bluray sont le plus souvent non-censurées).

    ??? warning "Type de FanSubs - [CLIQUEZ POUR AFFICHER]"
        Ces Formats Personnalisés sont optionnels et permettent de savoir quel type de FanSubs vos versions possèdent. Seul le FastSub n'est pas souhaité car il est souvent fait trop rapidement et reste peu soigné.

        | Formats Personnalisés                                                                         | Score                                        | Trash ID                                  |
        | --------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- |
        | [{{ sonarr['cf']['fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fansub)   | {{ sonarr['cf']['multi-audio']['fansub'] }}  | {{ sonarr['cf']['fansub']['trash_id'] }} |
        | [{{ sonarr['cf']['fastsub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fastsub) | {{ sonarr['cf']['fastsub']['trash_score'] }} | {{ sonarr['cf']['fastsub']['trash_id'] }} |
