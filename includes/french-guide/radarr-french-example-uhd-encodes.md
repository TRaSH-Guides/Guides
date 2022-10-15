If you prefer UHD Encodes (Bluray-2160p)

{! include-markdown "../../includes/cf/radarr-hdr-formats.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

{! include-markdown "../../includes/french-guide/radarr-movie-versions.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                                                                 | Score                                                          | Trash ID                                                    |
    | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- |
    | [{{ radarr['cf']['french-uhd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-uhd-bluray-tier-01) | {{ radarr['cf']['french-uhd-bluray-tier-01']['trash_score'] }} | {{ radarr['cf']['french-uhd-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['french-uhd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-uhd-bluray-tier-02) | {{ radarr['cf']['french-uhd-bluray-tier-02']['trash_score'] }} | {{ radarr['cf']['french-uhd-bluray-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['french-hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hd-bluray-tier-01)   | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_score'] }}  | {{ radarr['cf']['french-hd-bluray-tier-01']['trash_id'] }}  |
    | [{{ radarr['cf']['french-hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hd-bluray-tier-02)   | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_score'] }}  | {{ radarr['cf']['french-hd-bluray-tier-02']['trash_id'] }}  |
    | [{{ radarr['cf']['french-web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-web-tier-01)               | {{ radarr['cf']['french-web-tier-01']['trash_score'] }}        | {{ radarr['cf']['french-web-tier-01']['trash_id'] }}        |
    | [{{ radarr['cf']['french-web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-web-tier-02)               | {{ radarr['cf']['french-web-tier-02']['trash_score'] }}        | {{ radarr['cf']['french-web-tier-02']['trash_id'] }}        |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups)                    | ??????                                                         | {{ radarr['cf']['french-scene']['trash_id'] }}              |

    !!! tip
        French Scene groups are included as a fallback if you really want MULTi release despite a potential loss in quality. Either score the CF to `{{ radarr['cf']['french-scene']['trash_score'] }}` or `0` depending on what you want to achieve.

    ??? info "Original mix (optional)"
        | Custom Format                                                                                                          | Score                                                   | Trash ID                                             |
        | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------- |
        | [{{ radarr['cf']['uhd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-uhd-bluray-tier-01) | {{ radarr['cf']['uhd-bluray-tier-01']['trash_score'] }} | {{ radarr['cf']['uhd-bluray-tier-01']['trash_id'] }} |
        | [{{ radarr['cf']['uhd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-uhd-bluray-tier-02) | {{ radarr['cf']['uhd-bluray-tier-02']['trash_score'] }} | {{ radarr['cf']['uhd-bluray-tier-02']['trash_id'] }} |
        | [{{ radarr['cf']['uhd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-uhd-bluray-tier-03) | {{ radarr['cf']['uhd-bluray-tier-03']['trash_score'] }} | {{ radarr['cf']['uhd-bluray-tier-03']['trash_id'] }} |
        | [{{ radarr['cf']['hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-01)      | {{ radarr['cf']['hd-bluray-tier-01']['trash_score'] }}  | {{ radarr['cf']['hd-bluray-tier-01']['trash_id'] }}  |
        | [{{ radarr['cf']['hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-02)      | {{ radarr['cf']['hd-bluray-tier-02']['trash_score'] }}  | {{ radarr['cf']['hd-bluray-tier-02']['trash_id'] }}  |
        | [{{ radarr['cf']['web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-01)                  | {{ radarr['cf']['web-tier-01']['trash_score'] }}        | {{ radarr['cf']['web-tier-01']['trash_id'] }}        |
        | [{{ radarr['cf']['web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-02)                  | {{ radarr['cf']['web-tier-02']['trash_score'] }}        | {{ radarr['cf']['web-tier-02']['trash_id'] }}        |
        | [{{ radarr['cf']['web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-03)                  | {{ radarr['cf']['web-tier-03']['trash_score'] }}        | {{ radarr['cf']['web-tier-03']['trash_id'] }}        |

!!! tip
    `Audio Advanced` Custom Formats are not included, being with encodes higher video quality is preferred. If you also want HD audio formats I would suggest to go for the Remuxes.

    {! include-markdown "../../includes/french-guide/radarr-french-releases-information.md" !}

Use the following main settings in your profile.

![!cf-profile-encodes](images/cf-french-profile-2160p-encodes.png)

!!! attention "Make sure you don't check the BR-DISK."

??? example "Workflow - [CLICK TO EXPAND]"

    - It will download WEB-DL 2160p for the streaming movies you see more often lately.
    - It will upgrade till Bluray-2160p when available.
    - It will fallback to the HQ Encodes (720/1080p) profile if no 2160p are available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.
