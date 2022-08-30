??? summary "Misc - [CLICK TO EXPAND]"
    | Custom Format                                                                                       | Score                                        | Trash ID                                  |
    | --------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- |
    | [{{ radarr['cf']['repack-proper']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#repack-proper) | {{ radarr['cf']['repack-proper']['trash_score'] }} | {{ radarr['cf']['repack-proper']['trash_id'] }} |
    | [{{ radarr['cf']['repack2']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#repack2)             | {{ radarr['cf']['repack2']['trash_score'] }}       | {{ radarr['cf']['repack2']['trash_id'] }}       |

    ??? tip "Proper and Repacks - [CLICK TO EXPAND]"

        I also suggest to change the Propers and Repacks settings in Radarr

        `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Radarr/Radarr-collection-of-custom-formats/#repack-proper) Custom Format.

        ![!cf-mm-propers-repacks-disable](/Radarr/images/cf-mm-propers-repacks-disable.png)

        This way you make sure the Custom Formats preferences will be used and not ignored.
