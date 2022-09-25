| Custom Format                                                                                                                   | Score                                                                         | Trash ID                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [{{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-audio)   | {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_score'] }}    | {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_id'] }}   |
| [{{ radarr['user-radarr-cf']['french-cfs']['french-audio']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#french-audio) | {{ radarr['user-radarr-cf']['french-cfs']['french-audio']['trash_score'] }}   | {{ radarr['user-radarr-cf']['french-cfs']['french-audio']['trash_id'] }}  |
| [{{ radarr['user-radarr-cf']['french-cfs']['multi-french']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi-french) | 0                                                                             | {{ radarr['user-radarr-cf']['french-cfs']['multi-french']['trash_id'] }}  |

??? summary "Breakdown and Why - [CLICK TO EXPAND]"

    - **{{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['name'] }}:** This is a custom format to help Radarr recognise MULTi audio release.

        !!! Info "You can safely replace the original [{{ radarr['cf']['multi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#multi) Custom Format from the Guide with it."

    - **{{ radarr['user-radarr-cf']['french-cfs']['french-audio']['name'] }}:** This is a custom format to help Radarr recognise release with French audio. It is optional and only give a small boost if the release indeed possess a French audio.
    - **{{ radarr['user-radarr-cf']['french-cfs']['multi-french']['name'] }}:** This is a custom format that will rename your file with 'Multi-French'.

    **How it works**
    When Radarr find a release with 'MULTi' in, it will allocate a {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_score'] }} score on it thanks to the **{{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['name'] }}** custom format. If the release indeed possess at least the original audio and French audio, it will be renamed by the **{{ radarr['user-radarr-cf']['french-cfs']['multi-french']['name'] }}**. Allowing the release to keep the {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_score'] }} score from the {{ radarr['user-radarr-cf']['french-cfs']['multi-audio']['trash_score'] }}.
