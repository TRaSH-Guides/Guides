<!-- markdownlint-disable MD041-->
??? abstract "German Audio - [Click to show/hide]"

    | Custom Format                                                                                                                            | Score                                                                         | Trash ID                                                       |
    | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
    | [{{ radarr['cf']['language-german']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#language-german)                            | {{ radarr['cf']['language-german']['trash_scores']['default'] }}              | {{ radarr['cf']['language-german']['trash_id'] }}              |
    | [{{ radarr['cf']['language-german-dl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#language-german-dl)                      | {{ radarr['cf']['language-german-dl']['trash_scores']['german'] }}            | {{ radarr['cf']['language-german-dl']['trash_id'] }}           |
    | [{{ radarr['cf']['language-german-dl-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#language-german-dl-undefined)  | {{ radarr['cf']['language-german-dl-undefined']['trash_scores']['default'] }} | {{ radarr['cf']['language-german-dl-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['language-not-german-english']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#language-not-german-or-english) | {{ radarr['cf']['language-not-german-english']['trash_scores']['default'] }}  | {{ radarr['cf']['language-not-german-english']['trash_id'] }}  |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['language-german-dl']['name'] }}:** This custom format helps Radarr recognize German Dual Language audio releases. It will add `German DL` to your filename.
    - **{{ radarr['cf']['language-german-dl-undefined']['name'] }}:** This Custom Format is mainly used to fix files that are wrongly named after import. For example, suppose the filename suggests it is only German but actually contains German and English audio. It is also useful for users who use a non-optimal file naming that does not follow suggested naming schemes, example: `John Wick Kapitel 2 (2017) [2160p] [HDR] [7.1, 7.1] [ger, eng] [Vio]`
    - **{{ radarr['cf']['language-german']['name'] }}:** This custom format helps Radarr recognize German audio releases that contain only a German language track and no others. It will add `German` to your filename.
    - **{{ radarr['cf']['language-not-german-english']['name'] }}:** This custom format is used to avoid releases which do not contain German or English audio.
<!-- markdownlint-enable MD041-->
