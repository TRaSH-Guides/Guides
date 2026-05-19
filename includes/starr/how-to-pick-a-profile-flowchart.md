<!-- markdownlint-disable MD041-->
!!! abstract "Pick a profile - decision flowchart"

    Use this as a starting point. The right profile depends on your hardware,
    bandwidth, and language preference — the chart collapses each branch onto
    a single quality-profile family; pick the specific tier (1080p vs 2160p,
    Bluray vs Remux) once you've narrowed the branch.

    ```mermaid
    flowchart TD
        START([Start: pick a profile]) --> ANIME{Anime only?}

        ANIME -- Yes --> ANIME_LANG{Audio language?}
        ANIME_LANG -- EN/JP --> P_ANIME[Anime Remux-1080p]
        ANIME_LANG -- German --> P_GANIME[German Anime HD Bluray + WEB]
        ANIME_LANG -- French --> P_FRANIME[French Anime profiles]

        ANIME -- No --> LANG{Primary language?}
        LANG -- English --> EN{4K display + HDR-capable player?}
        LANG -- German --> DE{4K display + HDR-capable player?}
        LANG -- French --> FR{Variant?}

        EN -- No --> EN_HD{Bandwidth / storage limited?}
        EN_HD -- Limited --> P_HD[HD Bluray + WEB]
        EN_HD -- Plenty --> P_R1080[Remux + WEB 1080p]
        EN -- Yes --> EN_UHD{Encode or Remux?}
        EN_UHD -- Encode --> P_UHD[UHD Bluray + WEB]
        EN_UHD -- Remux --> P_R2160[Remux + WEB 2160p]

        DE -- No --> P_DE_HD[German HD Bluray + WEB<br/>or HD Remux + WEB]
        DE -- Yes --> P_DE_UHD[German UHD Bluray + WEB<br/>or UHD Remux + WEB]

        FR -- VO --> P_FR_VO[French MULTi.VO profiles]
        FR -- VF --> P_FR_VF[French MULTi.VF profiles]
        FR -- VOSTFR --> P_FR_VOSTFR[French VOSTFR profiles]

        START -.advanced.-> P_SQP(SQP-1 ... SQP-5<br/>see SQP guide)

        classDef leaf fill:#1f2937,stroke:#4051B5,color:#fff;
        class P_ANIME,P_GANIME,P_FRANIME,P_HD,P_R1080,P_UHD,P_R2160,P_DE_HD,P_DE_UHD,P_FR_VO,P_FR_VF,P_FR_VOSTFR,P_SQP leaf;
    ```

    !!! tip "Combine profiles for upgrade chains"

        The chart picks one starting profile. You can combine HD/UHD profiles
        into a single profile if you want to start with 1080p and upgrade to
        2160p once a 4K release shows up. See the per-profile sections below.
<!-- markdownlint-enable MD041-->
