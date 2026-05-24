<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis"}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TD
    START([Start: pick a [German] Sonarr profile]) --> KIND{Content kind?}
    KIND -->|German live-action TV| RES{Display + player<br/>resolution?}
    KIND -->|German anime TV| P_ANIME(["[German] Anime HD Bluray + WEB"])

    RES -->|1080p only| HD_SRC{Source<br/>preference?}
    HD_SRC -->|Encode / WEB| P_DE_HD(["[German] HD Bluray + WEB"])
    HD_SRC -->|Remux| P_DE_HDR(["[German] HD Remux + WEB"])
    RES -->|2160p / 4K| UHD_SRC{Source<br/>preference?}
    UHD_SRC -->|Encode<br/>default scoring| P_DE_UHD(["[German] UHD Bluray + WEB"])
    UHD_SRC -->|Encode<br/>alternative scoring| P_DE_UHD_ALT(["[German] UHD Bluray + WEB (Alternative)"])
    UHD_SRC -->|Remux| P_DE_UHDR(["[German] UHD Remux + WEB"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    class P_ANIME,P_DE_HD,P_DE_HDR,P_DE_UHD,P_DE_UHD_ALT,P_DE_UHDR leaf;
    class KIND,RES,HD_SRC,UHD_SRC decision;
```
<!-- markdownlint-enable MD041-->
