<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START([Start: pick a Radarr profile]) --> KIND{Audience?}
    KIND -->|Standard movie library| RES{Display + player<br/>resolution?}

    RES -->|1080p only| HD_SRC{Source<br/>preference?}
    HD_SRC -->|Encode<br/>smaller / cheaper| P_HD([HD Bluray + WEB])
    HD_SRC -->|Remux<br/>untouched stream| P_R1080([Remux + WEB 1080p])

    RES -->|2160p / 4K<br/>HDR-capable player| UHD_SRC{Source<br/>preference?}
    UHD_SRC -->|Encode<br/>x265 acceptable| P_UHD([UHD Bluray + WEB])
    UHD_SRC -->|Remux<br/>maximum quality| P_R2160([Remux + WEB 2160p])
    UHD_SRC -->|Combined<br/>Remux + WEB tiers| P_R2160_COMB([Remux 2160p Combined])
    UHD_SRC -->|Alternative scoring| P_R2160_ALT([Remux 2160p Alternative])

    ANIME[Anime movies?] -.-> ANIME_LINK[/"See the Anime guide<br/>for [Anime] Remux-1080p"/]
    DE[German movies?] -.-> DE_LINK[/"See the German guide<br/>for [German] profiles"/]
    FR[French movies?] -.-> FR_LINK[/"See the French guide<br/>for [French] profiles"/]
    SQP[Power user /<br/>custom SQP rules?] -.-> SQP_LINK[/"See the SQP guide<br/>for [SQP] profiles"/]

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    classDef pointer fill:none,stroke:#9ca3af,stroke-dasharray:4 3,color:#6b7280;
    class P_HD,P_R1080,P_UHD,P_R2160,P_R2160_COMB,P_R2160_ALT leaf;
    class KIND,RES,HD_SRC,UHD_SRC decision;
    class ANIME,ANIME_LINK,DE,DE_LINK,FR,FR_LINK,SQP,SQP_LINK pointer;
```
<!-- markdownlint-enable MD041-->
