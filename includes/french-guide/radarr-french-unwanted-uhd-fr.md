??? abstract "Indésirable - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                   |                           Score                            | Trash ID                                    |
    | ------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------: | ------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)           |  {{ radarr['cf']['br-disk']['trash_scores']['default'] }}  | {{ radarr['cf']['br-disk']['trash_id'] }}   |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                     |    {{ radarr['cf']['3d']['trash_scores']['default'] }}     | {{ radarr['cf']['3d']['trash_id'] }}        |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                     |    {{ radarr['cf']['lq']['trash_scores']['default'] }}     | {{ radarr['cf']['lq']['trash_id'] }}        |
    | [{{ radarr['cf']['french-lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-lq)           | {{ radarr['cf']['french-lq']['trash_scores']['default'] }} | {{ radarr['cf']['french-lq']['trash_id'] }} |
    | [{{ radarr['cf']['upscaled']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#upscaled)         | {{ radarr['cf']['upscaled']['trash_scores']['default'] }}  | {{ radarr['cf']['upscaled']['trash_id'] }}  |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning: |  {{ radarr['cf']['x265-hd']['trash_scores']['default'] }}  | {{ radarr['cf']['x265-hd']['trash_id'] }}   |

    ------

    Description et objectifs

    - **{{ radarr['cf']['br-disk']['name'] }} :** Il s'agit d'un Format Personnalisé qui permet à Radarr de reconnaître et d'ignorer les BR-DISK (ISO et structure de dossier Blu-ray) en plus de la qualité standard des BR-DISK.
    - **{{ radarr['cf']['3d']['name'] }}:** La 3D convient-elle encore pour les particuliers ?
    - **{{ radarr['cf']['lq']['name'] }}:** Une collection de groupes P2P anglais qui sont souvent bannis des meilleurs trackers en raison de leur manque de qualité ou pour d'autres raisons.
    - **{{ radarr['cf']['french-lq']['name'] }}:** Une collection de groupes P2P français qui sont souvent bannis des meilleurs trackers en raison de leur manque de qualité ou pour d'autres raisons.
    - **{{ radarr['cf']['upscaled']['name'] }}:** Ceci permets de bloquer les versions upscalées en 4K.
    - **{{ radarr['cf']['x265-hd']['name'] }}:** Ceci bloque/ignore les sorties 720/1080p (HD) qui sont encodées en x265. - Plus d'informations [ICI](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"} (en anglais).

        !!! Danger "Ne l'utilisez pas avec le Format Personnalisé [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning:"

    ??? note "Optionnel - [Cliquer pour afficher/masquer]"

        Cela inclut les Formats Personnalisés optionnels créés par TRaSH pour le guide original. Assurez-vous de bien comprendre ce qu'ils impliquent avant de les intégrer. En outre, deux Formats Personnalisés peuvent créer des problèmes si vous voulez du MULTi :

        - [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups) : ce dernier peut être sujet à controverse pour les personnes recherchant une version MULTi. Il est recommandé de ne pas l'utiliser.
        - [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene), il peut inclure des groupes Scene déjà dans le Format Personnalisé [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups). Qui est utilisé comme substitut afin d'augmenter les chances d'obtenir une version MULTi.

        {! include-markdown "../../includes/cf/radarr-optional.md" !}
