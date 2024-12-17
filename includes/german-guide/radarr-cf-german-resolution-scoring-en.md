??? abstract "Resolution - [Click to show/hide]"

    | Custom Format                                                                                                                                                 |                                  Score                                                                      | Trash ID                |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------: | -------------------------------------------------------- |
    | [{{ radarr['cf']['german-1080p-booster']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/1080p.json)                   | {{ radarr['cf']['german-1080p-booster']['trash_scores']['default'] }}      | {{ radarr['cf']['german-1080p-booster']['trash_id'] }}   |
    | [{{ radarr['cf']['german-2160p-booster']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/german-2160p-booster.json)    | {{ radarr['cf']['german-2160p-booster']['trash_scores']['default'] }}      | {{ radarr['cf']['german-2160p-booster']['trash_id'] }}   |
    | [{{ radarr['cf']['720p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/720p.json)                                    | {{ radarr['cf']['720p']['trash_scores']['default'] }}                      | {{ radarr['cf']['720p']['trash_id'] }}                   |
    | [{{ radarr['cf']['1080p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/1080p.json)                                  | {{ radarr['cf']['1080p']['trash_scores']['default'] }}                     | {{ radarr['cf']['1080p']['trash_id'] }}                  |
    | [{{ radarr['cf']['2160p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/2160p.json)                                  | {{ radarr['cf']['2160p']['trash_scores']['default'] }}                     | {{ radarr['cf']['2160p']['trash_id'] }}                  |

    ---

    Breakdown and Why

    - Since we are merging all qualities into a single group we need to add scores for different sources to allow upgrades between them.
    - As the scores for german groups are higher, to allow for upgrades from english to german, we need to introduce resolution boosters to not loose upgradability between resolutions.
