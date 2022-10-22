If you prefer 2160p Remuxes (Remux-2160p)

{! include-markdown "../../includes/french-guide/radarr-french-releases-information.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-hdr-formats.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

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

Use the following main settings in your profile:

![!cf-profile-encodes](/Radarr/images/cf-french-profile-2160p-remuxes.png)

!!! attention "Make sure you don't check the BR-DISK."

??? example "Workflow - [CLICK TO EXPAND]"

    - It will download WEB-DL 2160p for the streaming movies you see more often lately.
    - It will upgrade to Remux-2160p when available.
    - It will fallback to the 1080p Remuxes profile if no 2160p are available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.
