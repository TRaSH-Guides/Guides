<!-- markdownlint-disable MD041-->
??? abstract "Miscellaneous Anime (Optional) - [Click to show/hide]"

    | Custom Format                                                                                                             |                                  Score                                  | Trash ID                                                |
    | ------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ------------------------------------------------------- |
    | [{{ radarr['cf']['uncensored']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uncensored)                                                 |                                            0                                            | {{ radarr['cf']['uncensored']['trash_id'] }}                         |
    | [{{ radarr['cf']['10bit']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#10bit)                                                           |                                            0                                            | {{ radarr['cf']['10bit']['trash_id'] }}                              |
    | [{{ radarr['cf']['anime-dual-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#anime-dual-audio)                                     |                                            0                                            | {{ radarr['cf']['anime-dual-audio']['trash_id'] }}                   |
    | [{{ radarr['cf']['language-not-german-japanese-korean-chinese-or-english']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#language-not-german-japanese-korean-chinese-or-english)      |             {{ radarr['cf']['language-not-german-japanese-korean-chinese-or-english']['trash_scores']['default'] }}                  | {{ radarr['cf']['language-not-german-japanese-korean-chinese-or-english']['trash_id'] }}                   |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['uncensored']['name'] }}:** [*Optional*] This Custom Format covers releases that are uncensored. If you want to prefer `uncensored` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of e.g. `101`, and if you want to prefer it over any tiers give the `CF` a score of `3000`.
    - **{{ radarr['cf']['10bit']['name'] }}:** [*Optional*] This Custom Format covers releases that are 10bit. If you want to prefer `10bit` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of e.g. `101`, and if you want to prefer it over any tiers give the `CF` a score of `3000`.
    - **{{ radarr['cf']['anime-dual-audio']['name'] }}:** [*Optional*] This Custom Format covers releases that have Dual Audio. If you want to prefer `Dual Audio` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of e.g. `101`, and if you want to prefer it over any tiers give the `CF` a score of `3000`. :warning: This affects only the English tiers for fallback.
    - **{{ radarr['cf']['language-not-german-japanese-korean-chinese-or-english']['name'] }}:** [*Optional*] This custom format is used to avoid releases which do not contain German, Japanese, Korean, Chinese or English audio. You can utilize it to get animated media from other East Asian countries. :warning: If this `CF` is used, `{{ radarr['cf']['language-not-german-japanese-or-english']['name'] }}` must be `0`.
<!-- markdownlint-enable MD041-->
