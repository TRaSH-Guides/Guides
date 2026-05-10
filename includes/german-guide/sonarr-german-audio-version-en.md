<!-- markdownlint-disable MD041-->
??? abstract "German Audio - [Click to show/hide]"

    | Custom Format                                                                                                                            | Score                                                                         | Trash ID                                                       |
    | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
    | [{{ sonarr['cf']['german']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german)                            | {{ sonarr['cf']['german']['trash_scores']['default'] }}              | {{ sonarr['cf']['german']['trash_id'] }}              |
    | [{{ sonarr['cf']['german-dl']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-dl)                      | {{ sonarr['cf']['german-dl']['trash_scores']['german'] }}            | {{ sonarr['cf']['german-dl']['trash_id'] }}           |
    | [{{ sonarr['cf']['german-dl-undefined']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-dl-undefined)  | {{ sonarr['cf']['german-dl-undefined']['trash_scores']['default'] }} | {{ sonarr['cf']['german-dl-undefined']['trash_id'] }} |
    | [{{ sonarr['cf']['not-german-or-english']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#not-german-or-english) | {{ sonarr['cf']['not-german-or-english']['trash_scores']['default'] }}  | {{ sonarr['cf']['not-german-or-english']['trash_id'] }}  |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['german-dl']['name'] }}:** This custom format helps Sonarr recognize German Dual Language audio releases. It will add `German DL` to your filename.
    - **{{ sonarr['cf']['german-dl-undefined']['name'] }}:** This Custom Format is mainly used to fix files that are wrongly named after import. For example, suppose the filename suggests it is only German but actually contains German and English audio. It is also useful for users who use a non-optimal file naming that does not follow suggested naming schemes, example: `John Wick Kapitel 2 (2017) [2160p] [HDR] [7.1, 7.1] [ger, eng] [Vio]`
    - **{{ sonarr['cf']['german']['name'] }}:** This custom format helps Sonarr recognize German audio releases that contain only a German language track and no others. It will add `German` to your filename.
    - **{{ sonarr['cf']['not-german-or-english']['name'] }}:** This custom format is used to avoid releases which do not contain German or English audio.
<!-- markdownlint-enable MD041-->
