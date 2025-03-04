??? abstract "Miscellaneous (Required) - [Click to show/hide]"

    | Custom Format                                                                                            |                                Score                                | Trash ID                                        |
    |----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------:|-------------------------------------------------|
    | [{{ radarr['cf']['repack-proper']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#repackproper) | {{ radarr['cf']['repack-proper']['trash_scores']['anime-radarr'] }} | {{ radarr['cf']['repack-proper']['trash_id'] }} |
    | [{{ radarr['cf']['repack2']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#repack-v2)          |    {{ radarr['cf']['repack2']['trash_scores']['anime-radarr'] }}    | {{ radarr['cf']['repack2']['trash_id'] }}       |
    | [{{ radarr['cf']['repack3']['name'] }}](/Radarr/radarr-collection-of-custom-formats/#repack-v3)          |    {{ radarr['cf']['repack3']['trash_scores']['anime-radarr'] }}    | {{ radarr['cf']['repack3']['trash_id'] }}       |

    ??? tip "Proper and Repacks - [Click to show/hide]"

        We also suggest changing the Propers and Repacks settings in Radarr.

        `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Radarr/radarr-collection-of-custom-formats/#repackproper) Custom Format.

        ![!cf-mm-propers-repacks-disable](/Radarr/images/cf-mm-propers-repacks-disable.png)

        This way you make sure the Custom Formats preferences will be used and not ignored.
