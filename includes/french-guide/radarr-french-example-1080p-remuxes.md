If you prefer 1080p Remuxes (Remux-1080p)

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

??? summary "Movie Versions - [CLICK TO EXPAND]"
    | Custom Format                                                                                                 | Score                                                | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
    | [{{ radarr['cf']['hybrid']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hybrid)                   | {{ radarr['cf']['hybrid']['trash_score'] }}          | {{ radarr['cf']['hybrid']['trash_id'] }}          |
    | [{{ radarr['cf']['remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remaster)               | {{ radarr['cf']['remaster']['trash_score'] }}        | {{ radarr['cf']['remaster']['trash_id'] }}        |
    | [{{ radarr['cf']['special-edition']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#special-edition) | {{ radarr['cf']['special-edition']['trash_score'] }} | {{ radarr['cf']['special-edition']['trash_id'] }} |
    | [{{ radarr['cf']['imax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax)                       | {{ radarr['cf']['imax']['trash_score'] }}            | {{ radarr['cf']['imax']['trash_id'] }}            |

{! include-markdown "../../includes/cf/radarr-misc.md" !}

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                                                       | Score                                                     | Trash ID                                               |
    | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
    | [{{ radarr['cf']['french-remux-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-remux-tier-01) | {{ radarr['cf']['french-remux-tier-01']['trash_score'] }} | {{ radarr['cf']['french-remux-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['french-remux-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-remux-tier-02) | {{ radarr['cf']['french-remux-tier-02']['trash_score'] }} | {{ radarr['cf']['french-remux-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['french-web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-web-tier-01)     | {{ radarr['cf']['french-web-tier-01']['trash_score'] }}   | {{ radarr['cf']['french-web-tier-01']['trash_id'] }}   |
    | [{{ radarr['cf']['french-web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-web-tier-02)     | {{ radarr['cf']['french-web-tier-02']['trash_score'] }}   | {{ radarr['cf']['french-web-tier-02']['trash_id'] }}   |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups)          | ??????                                                    | {{ radarr['cf']['french-scene']['trash_id'] }}         |

    !!! tip
        French Scene groups are included as a fallback if you really want MULTi release despite a potential loss in quality. Either score the CF to `{{ radarr['cf']['french-scene']['trash_score'] }}` or `0` depending on what you want to achieve.

    ??? info "Original mix (optional)"
        {! include-markdown "../../includes/cf/radarr-cf-remux-web-scoring.md" !}

Use the following main settings in your profile.

![!cf-profile-encodes](/Radarr/images/cf-french-profile-1080p-remuxes.png)

!!! attention "Make sure you don't check the BR-DISK."

??? example "Workflow - [CLICK TO EXPAND]"

    - It will download WEB-DL 1080p for the streaming movies you see more often lately.
    - It will upgrade till Remux-1080p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.
