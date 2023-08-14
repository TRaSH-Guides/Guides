??? abstract "Multi Audio - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                                   |                             Score                             | Trash ID                                       |
    | ------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: | ---------------------------------------------- |
    | [{{ sonarr['cf']['multi-audio']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#multi-audio)   | {{ sonarr['cf']['multi-audio']['trash_scores']['default'] }}  | {{ sonarr['cf']['multi-audio']['trash_id'] }}  |
    | [{{ sonarr['cf']['french-audio']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#french-audio) | {{ sonarr['cf']['french-audio']['trash_scores']['default'] }} | {{ sonarr['cf']['french-audio']['trash_id'] }} |
    | [{{ sonarr['cf']['multi-french']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#multi-french) |                               0                               | {{ sonarr['cf']['multi-french']['trash_id'] }} |

    ??? info "Description et objectifs - [Cliquer pour afficher/masquer]"

        - **{{ sonarr['cf']['multi-audio']['name'] }}:** Il s'agit d'un Format Personnalisé pour aider Sonarr à reconnaître les releases aved plusieurs audios (MULTi).

            !!! tip
                Vous pouvez remplacer sans problème le Format Personnalisé [{{ sonarr['cf']['multi']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#multi) du Guide par celui-ci.

        - **{{ sonarr['cf']['french-audio']['name'] }}:** Il s'agit d'un Format Personnalisé pour aider Sonarr à reconnaître les versions ayant un audio francophone. Il est facultatif et ne donne un léger bonus que si la version possède effectivement un audio français.
        - **{{ sonarr['cf']['multi-french']['name'] }}:** Il s'agit d'un Format Personnalisé qui renommera votre fichier avec `Multi-French`..

        !!! question "Comment fonctionne cette méthode"
            Lorsque Sonarr trouve une version avec `MULTi`, il lui attribue le score de {{ sonarr['cf']['multi-audio']['trash_scores']['default'] }} grâce au Format Personnalisé **{{ sonarr['cf']['multi-audio']['name'] }}**. Si la version contient au moins l'audio original et l'audio français, elle sera renommée par le Format Personnalisé **{{ sonarr['cf']['multi-french']['name'] }}**. Ce qui permet à la version de conserver le score de {{ sonarr['cf']['multi-audio']['trash_scores']['default'] }} du Format Personnalisé {{ sonarr['cf']['multi-audio']['name'] }}.
