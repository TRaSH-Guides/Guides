??? abstract "Multi audio - [Click to show/hide]"
    | Custom Format                                                                                           |                             Score                             | Trash ID                                       |
    | ------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: | ---------------------------------------------- |
    | [{{ radarr['cf']['multi-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-audio)   | {{ radarr['cf']['multi-audio']['trash_scores']['default'] }}  | {{ radarr['cf']['multi-audio']['trash_id'] }}  |
    | [{{ radarr['cf']['french-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#french-audio) | {{ radarr['cf']['french-audio']['trash_scores']['default'] }} | {{ radarr['cf']['french-audio']['trash_id'] }} |
    | [{{ radarr['cf']['multi-french']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-french) |                               0                               | {{ radarr['cf']['multi-french']['trash_id'] }} |

    ??? info "Breakdown and Why - [Click to show/hide]"

        - **{{ radarr['cf']['multi-audio']['name'] }}:** This is a custom format to help Radarr recognize MULTi audio releases.

            !!! tip
                You can safely replace the original [{{ radarr['cf']['multi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi) Custom Format from the Guide with it.

        - **{{ radarr['cf']['french-audio']['name'] }}:** This is a custom format to help Radarr recognize release with French audio. It is optional and only gives a small boost if the release indeed possesses French audio.
        - **{{ radarr['cf']['multi-french']['name'] }}:** This is a custom format that will rename your file with `Multi-French`.

        !!! question "How it works"
            When Radarr finds a release with `MULTi`, it will allocate a {{ radarr['cf']['multi-audio']['trash_scores']['default'] }} score to it thanks to the **{{ radarr['cf']['multi-audio']['name'] }}** custom format. If the release contains at least both the original audio and French audio, it will be renamed by the **{{ radarr['cf']['multi-french']['name'] }}**. Allowing the release to keep the {{ radarr['cf']['multi-audio']['trash_scores']['default'] }} score from the {{ radarr['cf']['multi-audio']['name'] }} Custom Format.
