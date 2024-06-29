??? abstract "Explanation - [Click to show/hide]"

    !!! tip "MULTi definition per indexers"

        Some Indexers in **Radarr** will let you choose which audio is normally included inside a `MULTi` release as an option. You should choose only `Original` and `German` if you decide to use it.
        This option should only be used for German indexers where you are sure that `MULTi` does include both `Original` and `German` audio. Doing so in more "international" indexers can create to false positive with the German Audio CFs.

??? abstract "German Audio - [Click to show/hide]"

    | Custom Format                                                                                                                             | Score                                                                | Trash ID                                             |
    | ------------------------------------------------------------------------------------------------------------------------------------------| ---------------------------------------------------------------------|----------------------------------------------------- |
    | [{{ radarr['cf']['german']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-only)                                          | {{ radarr['cf']['german']['trash_scores']['default'] }}              |{{ radarr['cf']['german']['trash_id'] }}              |
    | [{{ radarr['cf']['german-dl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-and-original-language)                      | {{ radarr['cf']['german-dl']['trash_scores']['default'] }}           |{{ radarr['cf']['german-dl']['trash_id'] }}           |
    | [{{ radarr['cf']['german-dl-fallback']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-and-original-language-fallback)    | {{ radarr['cf']['german-dl-fallback']['trash_scores']['default'] }}  |{{ radarr['cf']['german-dl-fallback']['trash_id'] }}  |
    | [{{ radarr['cf']['original-language']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#original-language)                         | {{ radarr['cf']['original-language']['trash_scores']['default'] }}   |{{ radarr['cf']['original-language']['trash_id'] }}   |

   ??? info "Breakdown and Why - [Click to show/hide]"

        - **{{ radarr['cf']['multi-audio']['name'] }}:** This is a custom format to help Radarr recognize MULTi audio releases.

            !!! tip

                You can safely replace the original [{{ radarr['cf']['multi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi) Custom Format from the Guide with it.

        - **{{ radarr['cf']['french-audio']['name'] }}:** This is a custom format to help Radarr recognize release with French audio. It is optional and only gives a small boost if the release indeed possesses French audio.
        - **{{ radarr['cf']['multi-french']['name'] }}:** This is a custom format that will rename your file with `Multi-French`.

        !!! question "How it works"

            When Radarr finds a release with `MULTi`, it will allocate a {{ radarr['cf']['multi-audio']['trash_scores']['default'] }} score to it thanks to the **{{ radarr['cf']['multi-audio']['name'] }}** custom format. If the release contains at least both the original audio and French audio, it will be renamed by the **{{ radarr['cf']['multi-french']['name'] }}**. Allowing the release to keep the {{ radarr['cf']['multi-audio']['trash_scores']['default'] }} score from the {{ radarr['cf']['multi-audio']['name'] }} Custom Format.
