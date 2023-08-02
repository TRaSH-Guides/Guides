??? abstract "Misc - [Click to show/hide]"
    | Custom Format                                                                                            |                             Score                              | Trash ID                                        |
    | -------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
    | [{{ radarr['cf']['repack-proper']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#repackproper) | {{ radarr['cf']['repack-proper']['trash_scores']['default'] }} | {{ radarr['cf']['repack-proper']['trash_id'] }} |
    | [{{ radarr['cf']['repack2']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#repack2)            |    {{ radarr['cf']['repack2']['trash_scores']['default'] }}    | {{ radarr['cf']['repack2']['trash_id'] }}       |

    ??? tip "Proper and Repacks - [Click to show/hide]"

        I also suggest to change the Propers and Repacks settings in Radarr

        `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Radarr/Radarr-collection-of-custom-formats/#repackproper) Custom Format.

        ![!cf-mm-propers-repacks-disable](/Radarr/images/cf-mm-propers-repacks-disable.png)

        This way you make sure the Custom Formats preferences will be used and not ignored.
