??? summary "Multi audio - [CLICK TO EXPAND]"
    | Custom Format                                                                                           | Score                                             | Trash ID                                       |
    | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------- |
    | [{{ radarr['cf']['multi-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-audio)   | {{ radarr['cf']['multi-audio']['trash_score'] }}  | {{ radarr['cf']['multi-audio']['trash_id'] }}  |
    | [{{ radarr['cf']['french-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#french-audio) | {{ radarr['cf']['french-audio']['trash_score'] }} | {{ radarr['cf']['french-audio']['trash_id'] }} |
    | [{{ radarr['cf']['multi-french']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-french) | 0                                                 | {{ radarr['cf']['multi-french']['trash_id'] }} |

    ??? info "Breakdown and Why - [CLICK TO EXPAND]"

        - **{{ radarr['cf']['multi-audio']['name'] }}:** This is a custom format to help Radarr recognise MULTi audio release.

            !!! tip
                You can safely replace the original [{{ radarr['cf']['multi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi) Custom Format from the Guide with it.

        - **{{ radarr['cf']['french-audio']['name'] }}:** This is a custom format to help Radarr recognise release with French audio. It is optional and only give a small boost if the release indeed possess a French audio.
        - **{{ radarr['cf']['multi-french']['name'] }}:** This is a custom format that will rename your file with 'Multi-French'.

        !!! question "How it works"
            When Radarr find a release with 'MULTi' in, it will allocate a {{ radarr['cf']['multi-audio']['trash_score'] }} score on it thanks to the **{{ radarr['cf']['multi-audio']['name'] }}** custom format. If the release indeed possess at least the original audio and French audio, it will be renamed by the **{{ radarr['cf']['multi-french']['name'] }}**. Allowing the release to keep the {{ radarr['cf']['multi-audio']['trash_score'] }} score from the {{ radarr['cf']['multi-audio']['name'] }}.
