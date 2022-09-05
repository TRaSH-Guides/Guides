| Custom Format                                                                                                                   | Score                                                                         | Trash ID                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [{{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['name'] }}](/Radarr/radarr-setup-custom-format-french/#multi-audio)   | {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_score'] }}    | {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_id'] }}   |
| [{{ radarr['user-radarr-cf']['french-cfs']['french-audio']['name'] }}](/Radarr/radarr-setup-custom-format-french/#french-audio) | {{ radarr['user-radarr-cf']['french-cfs']['french-audio']['trash_score'] }}   | {{ radarr['user-radarr-cf']['french-cfs']['french-audio']['trash_id'] }}  |
| [{{ radarr['user-radarr-cf']['french-cfs']['multi-french']['name'] }}](/Radarr/radarr-setup-custom-format-french/#multi-french) | {{ radarr['user-radarr-cf']['french-cfs']['multi-french']['trash_score'] }}   | {{ radarr['user-radarr-cf']['french-cfs']['multi-french']['trash_id'] }}  |

??? summary "Breakdown and Why - [CLICK TO EXPAND]"

    - **{{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['name'] }}:** This is a custom format to help Radarr recognise MULTi audio release.

        !!! Info "You can safely replace the original [{{ radarr['cf']['multi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi) Custom Format from the Guide with it."

    - **{{ radarr['user-radarr-cf']['french-cfs']['french-audio']['name'] }}:** This is a custom format to help Radarr recognise release with French audio.
    - **{{ radarr['user-radarr-cf']['french-cfs']['multi-french']['name'] }}:** This is a custom format that will rename your file with 'Multi-French' in order to avoid download loop in Radarr.
