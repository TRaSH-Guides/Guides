<!-- markdownlint-disable MD041-->
```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 80, "rankSpacing": 110, "padding": 20}, "themeVariables": {"fontSize": "22px"}}}%%
flowchart TD
    START(["Start: pick a [French] Sonarr profile"]) --> VAR{"<span style='color:#1f2937'>Audio variant?</span>"}

    VAR -->|MULTi.VO<br/>original audio + French| VO_RES{"<span style='color:#1f2937'>Target resolution?</span>"}
    VAR -->|MULTi.VF<br/>French audio only| VF_RES{"<span style='color:#1f2937'>Target resolution?</span>"}
    VAR -->|VOSTFR<br/>original audio + French subs| VOS_RES{"<span style='color:#1f2937'>Target resolution?</span>"}

    VO_RES -->|1080p| P_VO_1080(["<span style='color:#fff'>[French MULTi.VO]<br/>HD Bluray + WEB (1080p)</span>"])
    VO_RES -->|2160p| P_VO_2160(["<span style='color:#fff'>[French MULTi.VO]<br/>UHD Bluray + WEB (2160p)</span>"])

    VF_RES -->|1080p| P_VF_1080(["<span style='color:#fff'>[French MULTi.VF]<br/>HD Bluray + WEB (1080p)</span>"])
    VF_RES -->|2160p| P_VF_2160(["<span style='color:#fff'>[French MULTi.VF]<br/>UHD Bluray + WEB (2160p)</span>"])

    VOS_RES -->|1080p| P_VOS_1080(["<span style='color:#fff'>[French VOSTFR]<br/>HD Bluray + WEB (1080p)</span>"])
    VOS_RES -->|2160p| P_VOS_2160(["<span style='color:#fff'>[French VOSTFR]<br/>UHD Bluray + WEB (2160p)</span>"])

    classDef leaf fill:#1f2937,stroke:#4051B5,stroke-width:2px,color:#fff;
    classDef decision fill:#fef3c7,stroke:#ca8a04,color:#1f2937;
    class P_VO_1080,P_VO_2160,P_VF_1080,P_VF_2160,P_VOS_1080,P_VOS_2160 leaf;
    class VAR,VO_RES,VF_RES,VOS_RES decision;
```
<!-- markdownlint-enable MD041-->
