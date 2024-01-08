??? abstract "Misc - [Click to show/hide]"
    | Custom Format                                                                                     |                           Score                            | Trash ID                                    |
    | ------------------------------------------------------------------------------------------------- | :--------------------------------------------------------: | ------------------------------------------- |
    | [{{ sonarr['cf']['proper']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#proper)       |  {{ sonarr['cf']['proper']['trash_scores']['default'] }}   | {{ sonarr['cf']['proper']['trash_id'] }}    |
    | [{{ sonarr['cf']['repack']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#repack)       |  {{ sonarr['cf']['repack']['trash_scores']['default'] }}   | {{ sonarr['cf']['repack']['trash_id'] }}    |
    | [{{ sonarr['cf']['repack-v2']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#repack-v2) | {{ sonarr['cf']['repack-v2']['trash_scores']['default'] }} | {{ sonarr['cf']['repack-v2']['trash_id'] }} |
    | [{{ sonarr['cf']['repack-v3']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#repack-v3) | {{ sonarr['cf']['repack-v3']['trash_scores']['default'] }} | {{ sonarr['cf']['repack-v3']['trash_id'] }} |

    ??? tip "Proper and Repacks - [Click to show/hide]"

        I also suggest changing the Propers and Repacks settings in Sonarr

        `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack](/Sonarr/sonarr-collection-of-custom-formats/#repack) and [Proper](/Sonarr/sonarr-collection-of-custom-formats/#proper) Custom Formats.

        ![!cf-mm-propers-repacks-disable](/Sonarr/images/cf-mm-propers-repacks-disable.png)

        This way you make sure the Custom Formats preferences will be used and not ignored.
