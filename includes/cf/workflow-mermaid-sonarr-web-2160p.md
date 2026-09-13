<!-- markdownlint-disable MD041-->
??? abstract "Workflow Logic - [Click to show/hide]"

    ```mermaid
    flowchart LR
        S([Search]) --> W{WEB-DL 2160p<br/>with HDR/DV?}
        W -- Yes --> DW[Download<br/>WEB-2160p]
        DW --> CF{CF score<br/>&lt; 10000?}
        CF -- Yes --> CFU[Keep upgrading<br/>via Custom Formats]
        CF -- No --> STOP([Cutoff reached])
        CFU -. loop .-> CF
    ```

    - This will download WEB-2160p with HDR/DV.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`? We're too lazy to calculate the maximum for every Quality Profile we provide, and we want it to upgrade to the highest possible score anyway to result in the highest possible quality release.
<!-- markdownlint-enable MD041-->
