??? abstract "Miscellaneous (Required) - [Click to show/hide]"

    | Custom Format                                                                                            |                                Score                                | Trash ID                                        |
    |----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------:|-------------------------------------------------|
    | [{{ sonarr['cf']['repack-proper']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#repackproper) | {{ sonarr['cf']['repack-proper']['trash_scores']['anime-sonarr'] }} | {{ sonarr['cf']['repack-proper']['trash_id'] }} |
    | [{{ sonarr['cf']['repack-v2']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#repack-v2)        |   {{ sonarr['cf']['repack-v2']['trash_scores']['anime-sonarr'] }}   | {{ sonarr['cf']['repack-v2']['trash_id'] }}     |
    | [{{ sonarr['cf']['repack-v3']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#repack-v3)        |   {{ sonarr['cf']['repack-v3']['trash_scores']['anime-sonarr'] }}   | {{ sonarr['cf']['repack-v3']['trash_id'] }}     |

    ??? tip "Proper and Repacks - [Click to show/hide]"

        We also suggest changing the Propers and Repacks settings in Sonarr.

        `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Sonarr/sonarr-collection-of-custom-formats/#repackproper) Custom Format.

        ![!cf-mm-propers-repacks-disable](/Sonarr/images/cf-mm-propers-repacks-disable.png)

        This way you make sure the Custom Formats preferences will be used and not ignored.
