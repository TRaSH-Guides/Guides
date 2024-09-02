??? abstract "Resolution - [Click to show/hide]"

    | Custom Format                                                                                                                |                                  Score                                     | Trash ID                                |
    | ---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------: | --------------------------------------- |
    | [{{ radarr['cf']['720p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/720p.json)   | :warning: 0                      | {{ radarr['cf']['720p']['trash_id'] }}  |
    | [{{ radarr['cf']['1080p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/1080p.json) | :warning: 290                    | {{ radarr['cf']['1080p']['trash_id'] }} |
    | [{{ radarr['cf']['2160p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/2160p.json) | :warning: 300                    | {{ radarr['cf']['2160p']['trash_id'] }} |

    ---

    Breakdown and Why

    - Since we are merging all qualities into a single group we need to add scores for different sources to allow upgrades between them.
