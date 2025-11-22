<!-- markdownlint-disable MD041-->
??? abstract "Miscellaneous Anime (Optional) - [Click to show/hide]"

    | Custom Format                                                                                                             |                                  Score                                  | Trash ID                                                |
    | ------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------: | ------------------------------------------------------- |
    | [{{ sonarr['cf']['uncensored']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#uncensored)                                                 |                                            0                                            | {{ sonarr['cf']['uncensored']['trash_id'] }}                         |
    | [{{ sonarr['cf']['10bit']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#10bit)                                                           |                                            0                                            | {{ sonarr['cf']['10bit']['trash_id'] }}                              |
    | [{{ sonarr['cf']['anime-dual-audio']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#anime-dual-audio)                                     |                                            0                                            | {{ sonarr['cf']['anime-dual-audio']['trash_id'] }}                   |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['uncensored']['name'] }}:** [*Optional*] This Custom Format covers releases that are uncensored. If you want to prefer `uncensored` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of e.g. `101`, and if you want to prefer it over any tiers give the `CF` a score of `3000`.
    - **{{ sonarr['cf']['10bit']['name'] }}:** [*Optional*] This Custom Format covers releases that are 10bit. If you want to prefer `10bit` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of e.g. `101`, and if you want to prefer it over any tiers give the `CF` a score of `3000`.
    - **{{ sonarr['cf']['anime-dual-audio']['name'] }}:** [*Optional*] This Custom Format covers releases that have Dual Audio. If you want to prefer `Dual Audio` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of e.g. `101`, and if you want to prefer it over any tiers give the `CF` a score of `3000`. :warning: This affects only the English tiers for fallback.
<!-- markdownlint-enable MD041-->
