??? abstract "Multi Audio - [Click to show/hide]"
    | Custom Format                                                                                           |                             Score                             | Trash ID                                       |
    | ------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------: | ---------------------------------------------- |
    | [{{ sonarr['cf']['multi-audio']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#multi-audio)   | {{ sonarr['cf']['multi-audio']['trash_scores']['default'] }}  | {{ sonarr['cf']['multi-audio']['trash_id'] }}  |
    | [{{ sonarr['cf']['french-audio']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#french-audio) | {{ sonarr['cf']['french-audio']['trash_scores']['default'] }} | {{ sonarr['cf']['french-audio']['trash_id'] }} |
    | [{{ sonarr['cf']['multi-french']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#multi-french) |                               0                               | {{ sonarr['cf']['multi-french']['trash_id'] }} |

    ??? info "Breakdown and Why - [Click to show/hide]"

        - **{{ sonarr['cf']['multi-audio']['name'] }}:** This is a custom format to help Sonarr recognize MULTi audio releases.

            !!! tip
                You can safely replace the original [{{ sonarr['cf']['multi']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#multi) Custom Format from the Guide with it.

        - **{{ sonarr['cf']['french-audio']['name'] }}:** This is a custom format to help Sonarr recognize release with French audio. It is optional and only gives a small boost if the release indeed possesses French audio.
        - **{{ sonarr['cf']['multi-french']['name'] }}:** This is a custom format that will rename your file with `Multi-French`.

        !!! question "How it works"
            When Sonarr finds a release with `MULTi`, it will allocate a {{ sonarr['cf']['multi-audio']['trash_scores']['default'] }} score to it thanks to the **{{ sonarr['cf']['multi-audio']['name'] }}** custom format. If the release contains at least both the original audio and French audio, it will be renamed by the **{{ sonarr['cf']['multi-french']['name'] }}**. Allowing the release to keep the {{ sonarr['cf']['multi-audio']['trash_scores']['default'] }} score from the {{ sonarr['cf']['multi-audio']['name'] }} Custom Format.
