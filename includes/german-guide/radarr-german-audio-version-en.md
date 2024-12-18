??? abstract "German Audio - [Click to show/hide]"

    | Custom Format                                                                                                                             | Score                                                                | Trash ID                                             |
    | ------------------------------------------------------------------------------------------------------------------------------------------| ---------------------------------------------------------------------|----------------------------------------------------- |
    | [{{ radarr['cf']['german']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-only)                                          | {{ radarr['cf']['german']['trash_scores']['default'] }}              |{{ radarr['cf']['german']['trash_id'] }}              |
    | [{{ radarr['cf']['german-dl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-and-original-language)                      | {{ radarr['cf']['german-dl']['trash_scores']['default'] }}           |{{ radarr['cf']['german-dl']['trash_id'] }}           |
    | [{{ radarr['cf']['german-dl-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-and-original-language-undefined)  | {{ radarr['cf']['german-dl-undefined']['trash_scores']['default'] }} |{{ radarr['cf']['german-dl-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['original-language']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#original-language)                         | 0                                                                    |{{ radarr['cf']['original-language']['trash_id'] }}   |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['german-dl']['name'] }}:** This is a custom format to help Radarr recognize German Dual Language audio releases. This custom format will rename your file with `German.DL`.
    - **{{ radarr['cf']['german-dl-undefined']['name'] }}:** This is a custom format to help Radarr recognize German Dual Language releases where the indexer does provide wrong language information (e.g. German only even though the release title suggests it's dual language), or where existing files have a weird naming scheme  (e.g. `John Wick Kapitel 2 (2017) [2160p] [HDR] [7.1, 7.1] [ger, eng] [Vio]`)
    - **{{ radarr['cf']['german']['name'] }}:** This is a custom format to help Radarr recognize German audio releases which do only contain a german language track and no other.
    - **{{ radarr['cf']['original-language']['name'] }}:** This is a custom format to help Radarr recognize releases containing the original language track but not the German audio.
