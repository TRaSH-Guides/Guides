??? abstract "Unwanted - [Click to show/hide]"
    | Custom Format                                                                                 |                           Score                            | Trash ID                                    |
    | --------------------------------------------------------------------------------------------- | :--------------------------------------------------------: | ------------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#br-disk) |  {{ sonarr['cf']['br-disk']['trash_scores']['default'] }}  | {{ sonarr['cf']['br-disk']['trash_id'] }}   |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#lq)           |    {{ sonarr['cf']['lq']['trash_scores']['default'] }}     | {{ sonarr['cf']['lq']['trash_id'] }}        |
    | [{{ sonarr['cf']['french-lq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fr-lq) | {{ sonarr['cf']['french-lq']['trash_scores']['default'] }} | {{ sonarr['cf']['french-lq']['trash_id'] }} |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#extras)   |  {{ sonarr['cf']['extras']['trash_scores']['default'] }}   | {{ sonarr['cf']['extras']['trash_id'] }}    |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }} :** This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ sonarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ sonarr['cf']['french-lq']['name'] }}:** A collection of known Low Quality French groups that are often banned from the top trackers because the lack of quality or other reasons.
    - **{{ sonarr['cf']['extras']['name'] }}:** This blocks/ignores extras

    ??? warning "Type of FanSubs - [Click to show/hide]"
        Those Custom Formats are optionals and allow to know which type of FanSubs your releases have. Only the FastSub is not wanted as it is often done too quickly and are often not well done. If you do not want FanSub either you should also score it to {{ sonarr['cf']['fastsub']['trash_scores']['default'] }}.

        | Custom Format                                                                                 |                          Score                           | Trash ID                                  |
        | --------------------------------------------------------------------------------------------- | :------------------------------------------------------: | ----------------------------------------- |
        | [{{ sonarr['cf']['fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fansub)   |                            0                             | {{ sonarr['cf']['fansub']['trash_id'] }}  |
        | [{{ sonarr['cf']['fastsub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fastsub) | {{ sonarr['cf']['fastsub']['trash_scores']['default'] }} | {{ sonarr['cf']['fastsub']['trash_id'] }} |
