<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis"}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TD
    START([Start: pick a [French] Radarr profile]) --> VAR{Audio variant?}

    VAR -->|MULTi.VO<br/>original audio + French| VO_RES{Resolution + source?}
    VAR -->|MULTi.VF<br/>French audio only| VF_RES{Resolution + source?}
    VAR -->|VOSTFR<br/>original audio + French subs| VOS_RES{Resolution + source?}

    VO_RES -->|HD Bluray + WEB| P_VO_HD(["[French MULTi.VO]<br/>HD Bluray + WEB"])
    VO_RES -->|HD Remux 1080p| P_VO_HDR(["[French MULTi.VO]<br/>HD Remux (1080p)"])
    VO_RES -->|UHD Bluray + WEB| P_VO_UHD(["[French MULTi.VO]<br/>UHD Bluray + WEB"])
    VO_RES -->|UHD Remux 2160p| P_VO_UHDR(["[French MULTi.VO]<br/>UHD Remux (2160p)"])

    VF_RES -->|HD Bluray + WEB| P_VF_HD(["[French MULTi.VF]<br/>HD Bluray + WEB"])
    VF_RES -->|HD Remux 1080p| P_VF_HDR(["[French MULTi.VF]<br/>HD Remux (1080p)"])
    VF_RES -->|UHD Bluray + WEB| P_VF_UHD(["[French MULTi.VF]<br/>UHD Bluray + WEB"])
    VF_RES -->|UHD Remux 2160p| P_VF_UHDR(["[French MULTi.VF]<br/>UHD Remux (2160p)"])

    VOS_RES -->|HD Bluray + WEB| P_VOS_HD(["[French VOSTFR]<br/>HD Bluray + WEB"])
    VOS_RES -->|HD Remux 1080p| P_VOS_HDR(["[French VOSTFR]<br/>HD Remux (1080p)"])
    VOS_RES -->|UHD Bluray + WEB| P_VOS_UHD(["[French VOSTFR]<br/>UHD Bluray + WEB"])
    VOS_RES -->|UHD Remux 2160p| P_VOS_UHDR(["[French VOSTFR]<br/>UHD Remux (2160p)"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    class P_VO_HD,P_VO_HDR,P_VO_UHD,P_VO_UHDR,P_VF_HD,P_VF_HDR,P_VF_UHD,P_VF_UHDR,P_VOS_HD,P_VOS_HDR,P_VOS_UHD,P_VOS_UHDR leaf;
    class VAR,VO_RES,VF_RES,VOS_RES decision;
```
<!-- markdownlint-enable MD041-->
