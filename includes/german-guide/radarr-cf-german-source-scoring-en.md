??? abstract "Source - [Click to show/hide]"

    | Custom Format                                                                                                                     |                                  Score                                     | Trash ID                                |
    | --------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------: | --------------------------------------- |
    | [{{ radarr['cf']['web']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/web.json)          | {{ radarr['cf']['web']['trash_scores']['default'] }}                       | {{ radarr['cf']['web']['trash_id'] }}  |
    | [{{ radarr['cf']['bluray']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/bluray.json)    | {{ radarr['cf']['bluray']['trash_scores']['default'] }}                    | {{ radarr['cf']['bluray']['trash_id'] }} |

    ---

    Breakdown and Why

    - Since we are merging all qualities into a single group we need to add scores for different sources to allow upgrades between them.
