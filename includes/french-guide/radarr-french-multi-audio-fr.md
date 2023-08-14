??? abstract "Multi audio - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                   |                             Score                             | Trash ID                                       |
    | ------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: | ---------------------------------------------- |
    | [{{ radarr['cf']['multi-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-audio)   | {{ radarr['cf']['multi-audio']['trash_scores']['default'] }}  | {{ radarr['cf']['multi-audio']['trash_id'] }}  |
    | [{{ radarr['cf']['french-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#french-audio) | {{ radarr['cf']['french-audio']['trash_scores']['default'] }} | {{ radarr['cf']['french-audio']['trash_id'] }} |
    | [{{ radarr['cf']['multi-french']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-french) |                               0                               | {{ radarr['cf']['multi-french']['trash_id'] }} |

    ??? info "Description et objectifs - [Cliquer pour afficher/masquer]"

        - **{{ radarr['cf']['multi-audio']['name'] }}:** Il s'agit d'un Format Personnalisé pour aider Radarr à reconnaître les releases aved plusieurs audios (MULTi).

            !!! tip
                Vous pouvez remplacer sans problème le Format Personnalisé [{{ radarr['cf']['multi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi) du Guide par celui-ci.

        - **{{ radarr['cf']['french-audio']['name'] }}:** Il s'agit d'un Format Personnalisé pour aider Radarr à reconnaître les versions ayant un audio francophone. Il est facultatif et ne donne un léger bonus que si la version possède effectivement un audio français.
        - **{{ radarr['cf']['multi-french']['name'] }}:** Il s'agit d'un Format Personnalisé qui renommera votre fichier avec `Multi-French`..

        !!! question "Comment fonctionne cette méthode"
            Lorsque Radarr trouve une version avec `MULTi`, il lui attribue le score de {{ radarr['cf']['multi-audio']['trash_scores']['default'] }} grâce au Format Personnalisé **{{ radarr['cf']['multi-audio']['name'] }}**. Si la version contient au moins l'audio original et l'audio français, elle sera renommée par le Format Personnalisé **{{ radarr['cf']['multi-french']['name'] }}**. Ce qui permet à la version de conserver le score de {{ radarr['cf']['multi-audio']['trash_scores']['default'] }} du Format Personnalisé {{ radarr['cf']['multi-audio']['name'] }}.
