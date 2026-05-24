<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis"}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TD
    START([Start: pick a Sonarr profile]) --> KIND{Audience?}
    KIND -->|Standard TV library| RES{Display + player<br/>resolution?}

    RES -->|1080p only| HD_KIND{Need older /<br/>HDTV sources?}
    HD_KIND -->|No - WEB only| P_WEB_1080([WEB-1080p])
    HD_KIND -->|Yes - WEB + HDTV / Bluray| P_WEB_1080_ALT([WEB-1080p Alternative])
    RES -->|2160p / 4K| UHD_KIND{Combine with<br/>1080p?}
    UHD_KIND -->|No - pure 2160p| P_WEB_2160([WEB-2160p])
    UHD_KIND -->|Yes - upgrade chain<br/>from 1080p| P_WEB_2160_COMB([WEB-2160p Combined])
    UHD_KIND -->|Yes - older / HDTV sources too| P_WEB_2160_ALT([WEB-2160p Alternative])

    ANIME[Anime shows?] -.-> ANIME_LINK[/See the Anime guide<br/>for [Anime] Remux-1080p/]
    DE[German TV?] -.-> DE_LINK[/See the German guide<br/>for [German] profiles/]
    FR[French TV?] -.-> FR_LINK[/See the French guide<br/>for [French] profiles/]

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    classDef pointer fill:none,stroke:#9ca3af,stroke-dasharray:4 3,color:#6b7280;
    class P_WEB_1080,P_WEB_1080_ALT,P_WEB_2160,P_WEB_2160_COMB,P_WEB_2160_ALT leaf;
    class KIND,RES,HD_KIND,UHD_KIND decision;
    class ANIME,ANIME_LINK,DE,DE_LINK,FR,FR_LINK pointer;
```
<!-- markdownlint-enable MD041-->
