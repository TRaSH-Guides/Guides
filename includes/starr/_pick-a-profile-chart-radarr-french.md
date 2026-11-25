<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START(["Start: pick a [French] Radarr profile"]) --> VAR{"<span style='color:#1f2937'>Audio variant?</span>"}

    VAR -->|MULTi.VO<br/>original audio + French| VO_RES{"<span style='color:#1f2937'>Resolution + source?</span>"}
    VAR -->|MULTi.VF<br/>French audio only| VF_RES{"<span style='color:#1f2937'>Resolution + source?</span>"}
    VAR -->|VOSTFR<br/>original audio + French subs| VOS_RES{"<span style='color:#1f2937'>Resolution + source?</span>"}

    VO_RES -->|HD Bluray + WEB| P_VO_HD(["<span style='color:#fff'>[French MULTi.VO]<br/>HD Bluray + WEB</span>"])
    VO_RES -->|HD Remux 1080p| P_VO_HDR(["<span style='color:#fff'>[French MULTi.VO]<br/>HD Remux (1080p)</span>"])
    VO_RES -->|UHD Bluray + WEB| P_VO_UHD(["<span style='color:#fff'>[French MULTi.VO]<br/>UHD Bluray + WEB</span>"])
    VO_RES -->|UHD Remux 2160p| P_VO_UHDR(["<span style='color:#fff'>[French MULTi.VO]<br/>UHD Remux (2160p)</span>"])

    VF_RES -->|HD Bluray + WEB| P_VF_HD(["<span style='color:#fff'>[French MULTi.VF]<br/>HD Bluray + WEB</span>"])
    VF_RES -->|HD Remux 1080p| P_VF_HDR(["<span style='color:#fff'>[French MULTi.VF]<br/>HD Remux (1080p)</span>"])
    VF_RES -->|UHD Bluray + WEB| P_VF_UHD(["<span style='color:#fff'>[French MULTi.VF]<br/>UHD Bluray + WEB</span>"])
    VF_RES -->|UHD Remux 2160p| P_VF_UHDR(["<span style='color:#fff'>[French MULTi.VF]<br/>UHD Remux (2160p)</span>"])

    VOS_RES -->|HD Bluray + WEB| P_VOS_HD(["<span style='color:#fff'>[French VOSTFR]<br/>HD Bluray + WEB</span>"])
    VOS_RES -->|HD Remux 1080p| P_VOS_HDR(["<span style='color:#fff'>[French VOSTFR]<br/>HD Remux (1080p)</span>"])
    VOS_RES -->|UHD Bluray + WEB| P_VOS_UHD(["<span style='color:#fff'>[French VOSTFR]<br/>UHD Bluray + WEB</span>"])
    VOS_RES -->|UHD Remux 2160p| P_VOS_UHDR(["<span style='color:#fff'>[French VOSTFR]<br/>UHD Remux (2160p)</span>"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#1f2937;
    class P_VO_HD,P_VO_HDR,P_VO_UHD,P_VO_UHDR,P_VF_HD,P_VF_HDR,P_VF_UHD,P_VF_UHDR,P_VOS_HD,P_VOS_HDR,P_VOS_UHD,P_VOS_UHDR leaf;
    class VAR,VO_RES,VF_RES,VOS_RES decision;
```
<!-- markdownlint-enable MD041-->
