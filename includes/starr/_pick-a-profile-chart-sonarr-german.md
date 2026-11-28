<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START(["Start: pick a [German] Sonarr profile"]) --> KIND{"<span style='color:#1f2937'>Content kind?</span>"}
    KIND -->|German live-action TV| RES{"<span style='color:#1f2937'>Display + player<br/>resolution?</span>"}
    KIND -->|German anime TV| P_ANIME(["<span style='color:#fff'>[German] Anime HD Bluray + WEB</span>"])

    RES -->|1080p only| HD_SRC{"<span style='color:#1f2937'>Source<br/>preference?</span>"}
    HD_SRC -->|Encode / WEB| P_DE_HD(["<span style='color:#fff'>[German] HD Bluray + WEB</span>"])
    HD_SRC -->|Remux| P_DE_HDR(["<span style='color:#fff'>[German] HD Remux + WEB</span>"])
    RES -->|2160p / 4K| UHD_SRC{"<span style='color:#1f2937'>Source<br/>preference?</span>"}
    UHD_SRC -->|Encode<br/>default scoring| P_DE_UHD(["<span style='color:#fff'>[German] UHD Bluray + WEB</span>"])
    UHD_SRC -->|Encode<br/>alternative scoring| P_DE_UHD_ALT(["<span style='color:#fff'>[German] UHD Bluray + WEB (Alternative)</span>"])
    UHD_SRC -->|Remux| P_DE_UHDR(["<span style='color:#fff'>[German] UHD Remux + WEB</span>"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#1f2937;
    class P_ANIME,P_DE_HD,P_DE_HDR,P_DE_UHD,P_DE_UHD_ALT,P_DE_UHDR leaf;
    class KIND,RES,HD_SRC,UHD_SRC decision;
```
<!-- markdownlint-enable MD041-->
