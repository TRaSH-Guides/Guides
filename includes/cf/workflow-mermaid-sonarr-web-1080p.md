<!-- markdownlint-disable MD041-->
??? abstract "Workflow Logic - [Click to show/hide]"

    ```mermaid
    flowchart LR
        S([Search]) --> W{WEB-DL 1080p<br/>available?}
        W -- Yes --> DW[Download<br/>WEB-DL 1080p]
        DW --> ALT{WEB-720p / HDTV-1080p<br/>also enabled?}
        ALT -- Yes --> UP[Upgrade until<br/>cutoff is reached]
        ALT -- No --> CF{CF score<br/>&lt; 10000?}
        UP --> CF
        CF -- Yes --> CFU[Keep upgrading<br/>via Custom Formats]
        CF -- No --> STOP([Cutoff reached])
        CFU -. loop .-> CF
    ```

    - It will download WEB-DL 1080p. (If you also enabled `WEB 720p` and/or `HDTV 1080p` it will upgrade until `Upgrade Until`)
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`? We're too lazy to calculate the maximum for every Quality Profile we provide, and we want it to upgrade to the highest possible score anyway to result in the highest possible quality release.
<!-- markdownlint-enable MD041-->
