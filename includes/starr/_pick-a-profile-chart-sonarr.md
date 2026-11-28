<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START([Start: pick a Sonarr profile]) --> KIND{"<span style='color:#1f2937'>Audience?</span>"}
    KIND -->|Standard TV library| RES{"<span style='color:#1f2937'>Display + player<br/>resolution?</span>"}

    RES -->|1080p only| HD_KIND{"<span style='color:#1f2937'>Need older /<br/>HDTV sources?</span>"}
    HD_KIND -->|No - WEB only| P_WEB_1080(["<span style='color:#fff'>WEB-1080p</span>"])
    HD_KIND -->|Yes - WEB + HDTV / Bluray| P_WEB_1080_ALT(["<span style='color:#fff'>WEB-1080p Alternative</span>"])
    RES -->|2160p / 4K| UHD_KIND{"<span style='color:#1f2937'>Combine with<br/>1080p?</span>"}
    UHD_KIND -->|No - pure 2160p| P_WEB_2160(["<span style='color:#fff'>WEB-2160p</span>"])
    UHD_KIND -->|Yes - upgrade chain<br/>from 1080p| P_WEB_2160_COMB(["<span style='color:#fff'>WEB-2160p Combined</span>"])
    UHD_KIND -->|Yes - older / HDTV sources too| P_WEB_2160_ALT(["<span style='color:#fff'>WEB-2160p Alternative</span>"])

    ANIME[Anime shows?] -.-> ANIME_LINK[/"See the Anime guide<br/>for [Anime] Remux-1080p"/]
    DE[German TV?] -.-> DE_LINK[/"See the German guide<br/>for [German] profiles"/]
    FR[French TV?] -.-> FR_LINK[/"See the French guide<br/>for [French] profiles"/]

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#1f2937;
    classDef pointer fill:none,stroke:#9ca3af,stroke-dasharray:4 3,color:#6b7280;
    class P_WEB_1080,P_WEB_1080_ALT,P_WEB_2160,P_WEB_2160_COMB,P_WEB_2160_ALT leaf;
    class KIND,RES,HD_KIND,UHD_KIND decision;
    class ANIME,ANIME_LINK,DE,DE_LINK,FR,FR_LINK pointer;
```
<!-- markdownlint-enable MD041-->
