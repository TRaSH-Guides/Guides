<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis"}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TD
    START([Start: pick a Sonarr profile]) --> KIND{What kind of<br/>content?}
    KIND -->|TV shows| MAIN_LANG{Primary audio<br/>language?}
    KIND -->|Anime shows| ANIME_LANG{Anime audio<br/>language?}

    MAIN_LANG -->|English / international| EN_RES{Display + player<br/>resolution?}
    MAIN_LANG -->|German| DE_RES{Display + player<br/>resolution?}
    MAIN_LANG -->|French| FR_VAR{French audio<br/>variant?}

    EN_RES -->|1080p only| EN_HD_KIND{Need older /<br/>HDTV sources?}
    EN_HD_KIND -->|No - WEB only| P_WEB_1080([WEB-1080p])
    EN_HD_KIND -->|Yes - WEB + HDTV / Bluray| P_WEB_1080_ALT([WEB-1080p Alternative])
    EN_RES -->|2160p / 4K| EN_UHD_KIND{Combine with<br/>1080p?}
    EN_UHD_KIND -->|No - pure 2160p| P_WEB_2160([WEB-2160p])
    EN_UHD_KIND -->|Yes - upgrade chain<br/>from 1080p| P_WEB_2160_COMB([WEB-2160p Combined])
    EN_UHD_KIND -->|Yes - older / HDTV sources too| P_WEB_2160_ALT([WEB-2160p Alternative])

    DE_RES -->|1080p only| DE_HD_SRC{Source<br/>preference?}
    DE_HD_SRC -->|Encode / WEB| P_DE_HD(["[German] HD Bluray + WEB"])
    DE_HD_SRC -->|Remux| P_DE_HDR(["[German] HD Remux + WEB"])
    DE_RES -->|2160p / 4K| DE_UHD_SRC{Source<br/>preference?}
    DE_UHD_SRC -->|Encode / WEB| P_DE_UHD(["[German] UHD Bluray + WEB"])
    DE_UHD_SRC -->|Encode alternative| P_DE_UHD_ALT(["[German] UHD Bluray + WEB Alt"])
    DE_UHD_SRC -->|Remux| P_DE_UHDR(["[German] UHD Remux + WEB"])

    FR_VAR -->|MULTi.VO<br/>original + French| FR_VO_RES{Target resolution?}
    FR_VAR -->|MULTi.VF<br/>French audio only| FR_VF_RES{Target resolution?}
    FR_VAR -->|VOSTFR<br/>French subtitles| FR_VOSTFR_RES{Target resolution?}

    FR_VO_RES -->|1080p| P_FR_VO_1080(["[French MULTi.VO]<br/>HD Bluray + WEB (1080p)"])
    FR_VO_RES -->|2160p| P_FR_VO_2160(["[French MULTi.VO]<br/>UHD Bluray + WEB (2160p)"])

    FR_VF_RES -->|1080p| P_FR_VF_1080(["[French MULTi.VF]<br/>HD Bluray + WEB (1080p)"])
    FR_VF_RES -->|2160p| P_FR_VF_2160(["[French MULTi.VF]<br/>UHD Bluray + WEB (2160p)"])

    FR_VOSTFR_RES -->|1080p| P_FR_VOS_1080(["[French VOSTFR]<br/>HD Bluray + WEB (1080p)"])
    FR_VOSTFR_RES -->|2160p| P_FR_VOS_2160(["[French VOSTFR]<br/>UHD Bluray + WEB (2160p)"])

    ANIME_LANG -->|EN / JP| P_ANIME(["[Anime] Remux-1080p"])
    ANIME_LANG -->|German| P_DE_ANIME(["[German] Anime HD Bluray + WEB"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    class P_WEB_1080,P_WEB_1080_ALT,P_WEB_2160,P_WEB_2160_COMB,P_WEB_2160_ALT,P_DE_HD,P_DE_HDR,P_DE_UHD,P_DE_UHD_ALT,P_DE_UHDR,P_FR_VO_1080,P_FR_VO_2160,P_FR_VF_1080,P_FR_VF_2160,P_FR_VOS_1080,P_FR_VOS_2160,P_ANIME,P_DE_ANIME leaf;
    class KIND,MAIN_LANG,ANIME_LANG,EN_RES,EN_HD_KIND,EN_UHD_KIND,DE_RES,DE_HD_SRC,DE_UHD_SRC,FR_VAR,FR_VO_RES,FR_VF_RES,FR_VOSTFR_RES decision;
```
<!-- markdownlint-enable MD041-->
