<!-- markdownlint-disable MD041-->
??? abstract "Workflow Logic - [Click to show/hide]"

    ```mermaid
    flowchart LR
        S([Search]) --> W{WEB-1080p<br/>available?}
        S --> R{Remux-1080p<br/>available?}
        W -- Yes --> DW[Download<br/>WEB-1080p]
        R -- Yes --> DR[Download<br/>Remux-1080p]
        DW -. upgrade .-> DR
        DR --> CF{CF score<br/>&lt; 10000?}
        DW --> CF
        CF -- Yes --> CFU[Keep upgrading<br/>via Custom Formats]
        CF -- No --> STOP([Cutoff reached])
        CFU -. loop .-> CF
    ```

    - When the WEB-1080p is released it will download the WEB-1080p. (streaming services)
    - When the REMUX-1080p is released it will upgrade to the REMUX-1080p.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of `10000`.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `500`? We're too lazy to calculate the maximum for every Quality Profile we provide, and we want it to upgrade to the highest possible score anyway to result in the highest possible quality release.
<!-- markdownlint-enable MD041-->
