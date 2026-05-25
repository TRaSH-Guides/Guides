<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START([Start: pick a Radarr profile]) --> KIND{Audience?}
    KIND -->|Standard movie library| RES{Display + player<br/>resolution?}
    KIND -->|Power user /<br/>custom SQP rules| SQP_RES{SQP - target<br/>resolution?}

    RES -->|1080p only| HD_SRC{Source<br/>preference?}
    HD_SRC -->|Encode<br/>smaller / cheaper| P_HD([HD Bluray + WEB])
    HD_SRC -->|Remux<br/>untouched stream| P_R1080([Remux + WEB 1080p])

    RES -->|2160p / 4K<br/>HDR-capable player| UHD_SRC{Source<br/>preference?}
    UHD_SRC -->|Encode<br/>x265 acceptable| P_UHD([UHD Bluray + WEB])
    UHD_SRC -->|Remux<br/>maximum quality| P_R2160([Remux + WEB 2160p])
    UHD_SRC -->|Combined<br/>Remux + WEB tiers| P_R2160_COMB([Remux 2160p Combined])
    UHD_SRC -->|Alternative scoring| P_R2160_ALT([Remux 2160p Alternative])

    SQP_RES -->|1080p only| SQP_1080_WEB{WEB-only?}
    SQP_1080_WEB -->|No| P_SQP_1_1080(["[SQP] SQP-1 (1080p)"])
    SQP_1080_WEB -->|Yes| P_SQP_1_W1080(["[SQP] SQP-1 WEB (1080p)"])
    SQP_RES -->|2160p only| SQP_2160_WEB{WEB-only?}
    SQP_2160_WEB -->|No| P_SQP_1_2160(["[SQP] SQP-1 (2160p)"])
    SQP_2160_WEB -->|Yes| P_SQP_1_W2160(["[SQP] SQP-1 WEB (2160p)"])
    SQP_RES -->|Tiered multi-profile setup<br/>see SQP guide| SQP_TIER{Which tier?}
    SQP_TIER -->|Strict block-list| P_SQP_2(["[SQP] SQP-2"])
    SQP_TIER -->|Streaming-focused| P_SQP_3(["[SQP] SQP-3"])
    SQP_TIER -->|Streaming + audio priority| P_SQP_3A(["[SQP] SQP-3 (Audio)"])
    SQP_TIER -->|Encodes + Remux hybrid| P_SQP_4(["[SQP] SQP-4"])
    SQP_TIER -->|MA-hybrid Remux variant| P_SQP_4M(["[SQP] SQP-4 (MA Hybrid)"])
    SQP_TIER -->|Hardlinked-store optimised| P_SQP_5(["[SQP] SQP-5"])

    ANIME[Anime movies?] -.-> ANIME_LINK[/"See the Anime guide<br/>for [Anime] Remux-1080p"/]
    DE[German movies?] -.-> DE_LINK[/"See the German guide<br/>for [German] profiles"/]
    FR[French movies?] -.-> FR_LINK[/"See the French guide<br/>for [French] profiles"/]

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    classDef sqp fill:#312e81,stroke:#a5b4fc,color:#fff;
    classDef pointer fill:none,stroke:#9ca3af,stroke-dasharray:4 3,color:#6b7280;
    class P_HD,P_R1080,P_UHD,P_R2160,P_R2160_COMB,P_R2160_ALT leaf;
    class P_SQP_1_1080,P_SQP_1_W1080,P_SQP_1_2160,P_SQP_1_W2160,P_SQP_2,P_SQP_3,P_SQP_3A,P_SQP_4,P_SQP_4M,P_SQP_5 sqp;
    class KIND,RES,HD_SRC,UHD_SRC,SQP_RES,SQP_1080_WEB,SQP_2160_WEB,SQP_TIER decision;
    class ANIME,ANIME_LINK,DE,DE_LINK,FR,FR_LINK pointer;
```
<!-- markdownlint-enable MD041-->
