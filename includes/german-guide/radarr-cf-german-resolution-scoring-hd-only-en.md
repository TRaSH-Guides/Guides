<!-- markdownlint-disable MD041-->
??? abstract "German Resolution - [Click to show/hide]"

    | Custom Format                                                                                                           |                                 Score                                 | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------: | ------------------------------------------------------ |
    | [{{ radarr['cf']['german-1080p-booster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#german-1080p-booster) | {{ radarr['cf']['german-1080p-booster']['trash_scores']['default'] }} | {{ radarr['cf']['german-1080p-booster']['trash_id'] }} |
    | [{{ radarr['cf']['720p']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#720p)                                 |         {{ radarr['cf']['720p']['trash_scores']['default'] }}         | {{ radarr['cf']['720p']['trash_id'] }}                 |
    | [{{ radarr['cf']['1080p']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#1080p)                               |        {{ radarr['cf']['1080p']['trash_scores']['default'] }}         | {{ radarr['cf']['1080p']['trash_id'] }}                |

    ---

    Breakdown and Why

    - Since we are merging all qualities into a single group, we need to add scores for different resolutions to allow upgrades between them.
    - As the scores for German groups are higher, we need to introduce resolution boosters to ensure upgradability between resolutions, allowing for upgrades from English to German.
<!-- markdownlint-enable MD041-->
