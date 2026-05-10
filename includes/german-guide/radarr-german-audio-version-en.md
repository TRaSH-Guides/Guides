<!-- markdownlint-disable MD041-->
??? abstract "German Audio - [Click to show/hide]"

    | Custom Format                                                                                                                            | Score                                                                         | Trash ID                                                       |
    | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
    | [{{ radarr['cf']['german']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german)                            | {{ radarr['cf']['german']['trash_scores']['default'] }}              | {{ radarr['cf']['german']['trash_id'] }}              |
    | [{{ radarr['cf']['german-dl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-dl)                      | {{ radarr['cf']['german-dl']['trash_scores']['german'] }}            | {{ radarr['cf']['german-dl']['trash_id'] }}           |
    | [{{ radarr['cf']['german-dl-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-dl-undefined)  | {{ radarr['cf']['german-dl-undefined']['trash_scores']['default'] }} | {{ radarr['cf']['german-dl-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['not-german-or-english']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#not-german-or-english) | {{ radarr['cf']['not-german-or-english']['trash_scores']['default'] }}  | {{ radarr['cf']['not-german-or-english']['trash_id'] }}  |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['german-dl']['name'] }}:** This custom format helps Radarr recognize German Dual Language audio releases. It will add `German DL` to your filename.
    - **{{ radarr['cf']['german-dl-undefined']['name'] }}:** This Custom Format is mainly used to fix files that are wrongly named after import. For example, suppose the filename suggests it is only German but actually contains German and English audio. It is also useful for users who use a non-optimal file naming that does not follow suggested naming schemes, example: `John Wick Kapitel 2 (2017) [2160p] [HDR] [7.1, 7.1] [ger, eng] [Vio]`
    - **{{ radarr['cf']['german']['name'] }}:** This custom format helps Radarr recognize German audio releases that contain only a German language track and no others. It will add `German` to your filename.
    - **{{ radarr['cf']['not-german-or-english']['name'] }}:** This custom format is used to avoid releases which do not contain German or English audio.
<!-- markdownlint-enable MD041-->
