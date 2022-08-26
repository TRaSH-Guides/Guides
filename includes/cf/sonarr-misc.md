??? summary "Misc - [CLICK TO EXPAND]"
    | Custom Format                                                                                             | Score                                              | Trash ID                                        |
    | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------- |
    | [{{ sonarr['cf']['repack-proper']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#repack-proper) | {{ sonarr['cf']['repack-proper']['trash_score'] }} | {{ sonarr['cf']['repack-proper']['trash_id'] }} |
    | [{{ sonarr['cf']['repack-v2']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#repack-v2)             | {{ sonarr['cf']['repack-v2']['trash_score'] }}       | {{ sonarr['cf']['repack-v2']['trash_id'] }}       |
    | [{{ sonarr['cf']['repack-v3']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#repack-v3)             | {{ sonarr['cf']['repack-v3']['trash_score'] }}       | {{ sonarr['cf']['repack-v3']['trash_id'] }}       |

    ??? tip "Proper and Repacks - [CLICK TO EXPAND]"

        I also suggest to change the Propers and Repacks settings in Sonarr

        `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Sonarr/Sonarr-collection-of-custom-formats/#repack-proper) Custom Format.

        ![!cf-mm-propers-repacks-disable](/Sonarr/images/cf-mm-propers-repacks-disable.png)

        This way you make sure the Custom Formats preferences will be used and not ignored.
