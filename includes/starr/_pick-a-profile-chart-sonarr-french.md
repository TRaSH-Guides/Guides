<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START(["Start: pick a [French] Sonarr profile"]) --> VAR{Audio variant?}

    VAR -->|MULTi.VO<br/>original audio + French| VO_RES{Target resolution?}
    VAR -->|MULTi.VF<br/>French audio only| VF_RES{Target resolution?}
    VAR -->|VOSTFR<br/>original audio + French subs| VOS_RES{Target resolution?}

    VO_RES -->|1080p| P_VO_1080(["[French MULTi.VO]<br/>HD Bluray + WEB (1080p)"])
    VO_RES -->|2160p| P_VO_2160(["[French MULTi.VO]<br/>UHD Bluray + WEB (2160p)"])

    VF_RES -->|1080p| P_VF_1080(["[French MULTi.VF]<br/>HD Bluray + WEB (1080p)"])
    VF_RES -->|2160p| P_VF_2160(["[French MULTi.VF]<br/>UHD Bluray + WEB (2160p)"])

    VOS_RES -->|1080p| P_VOS_1080(["[French VOSTFR]<br/>HD Bluray + WEB (1080p)"])
    VOS_RES -->|2160p| P_VOS_2160(["[French VOSTFR]<br/>UHD Bluray + WEB (2160p)"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff,font-weight:bold;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#000;
    class P_VO_1080,P_VO_2160,P_VF_1080,P_VF_2160,P_VOS_1080,P_VOS_2160 leaf;
    class VAR,VO_RES,VF_RES,VOS_RES decision;
```
<!-- markdownlint-enable MD041-->
