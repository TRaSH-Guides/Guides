<!-- markdownlint-disable MD041-->
??? abstract "German Anime Audio - [Click to show/hide]"

    | Custom Format                                                                                                                            | Score                                                                         | Trash ID                                                       |
    | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
    | [{{ sonarr['cf']['language-german']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#language-german)                            | {{ sonarr['cf']['language-german']['trash_scores']['default'] }}              | {{ sonarr['cf']['language-german']['trash_id'] }}              |
    | [{{ sonarr['cf']['language-german-dl']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#language-german-dl)                      | {{ sonarr['cf']['language-german-dl']['trash_scores']['german-anime'] }}            | {{ sonarr['cf']['language-german-dl']['trash_id'] }}           |
    | [{{ sonarr['cf']['language-german-dl-undefined']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#language-german-dl-undefined)  | {{ sonarr['cf']['language-german-dl-undefined']['trash_scores']['default'] }} | {{ sonarr['cf']['language-german-dl-undefined']['trash_id'] }} |
    | [{{ sonarr['cf']['language-not-german-japanese-or-english']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#language-not-german-japanese-or-english) | {{ sonarr['cf']['language-not-german-japanese-or-english']['trash_scores']['default'] }}  | {{ sonarr['cf']['language-not-german-japanese-or-english']['trash_id'] }}  |
    | [{{ sonarr['cf']['german-anime-subbed']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#german-anime-subbed) | {{ sonarr['cf']['german-anime-subbed']['trash_scores']['default'] }}  | {{ sonarr['cf']['german-anime-subbed']['trash_id'] }}  |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['language-german-dl']['name'] }}:** This custom format helps Radarr recognize German Dual Language audio releases. It will add `German DL` to your filename.
    - **{{ sonarr['cf']['language-german-dl-undefined']['name'] }}:** This Custom Format is mainly used to fix files that are wrongly named after import. For example, suppose the filename suggests it is only German but actually contains German and English audio. It is also useful for users who use a non-optimal file naming that does not follow suggested naming schemes, example: `John Wick Kapitel 2 (2017) [2160p] [HDR] [7.1, 7.1] [ger, eng] [Vio]`
    - **{{ sonarr['cf']['language-german']['name'] }}:** This custom format helps Radarr recognize German audio releases that contain only a German language track and no others. It will add `German` to your filename.
    - **{{ sonarr['cf']['language-not-german-japanese-or-english']['name'] }}:** This custom format is used to avoid releases which do not contain German, Japanese or English audio.
    - **{{ sonarr['cf']['german-anime-subbed']['name'] }}:** Used to recognize German (and possibly english) subtitles.
<!-- markdownlint-enable MD041-->
