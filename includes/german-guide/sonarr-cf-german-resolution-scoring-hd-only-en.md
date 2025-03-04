<!-- markdownlint-disable MD041-->
??? abstract "German Resolution - [Click to show/hide]"

    | Custom Format                                                                                                           |                                 Score                                 | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------: | ------------------------------------------------------ |
    | [{{ sonarr['cf']['german-1080p-booster']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#german-1080p-booster) | {{ sonarr['cf']['german-1080p-booster']['trash_scores']['default'] }} | {{ sonarr['cf']['german-1080p-booster']['trash_id'] }} |
    | [{{ sonarr['cf']['720p']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#720p)                                 |         {{ sonarr['cf']['720p']['trash_scores']['default'] }}         | {{ sonarr['cf']['720p']['trash_id'] }}                 |
    | [{{ sonarr['cf']['1080p']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#1080p)                               |        {{ sonarr['cf']['1080p']['trash_scores']['default'] }}         | {{ sonarr['cf']['1080p']['trash_id'] }}                |

    ---

    Breakdown and Why

    - Since we are merging all qualities into a single group, we need to add scores for different resolutions to allow upgrades between them.
    - As the scores for German groups are higher, we need to introduce resolution boosters to ensure upgradability between resolutions, allowing for upgrades from English to German.
<!-- markdownlint-enable MD041-->
