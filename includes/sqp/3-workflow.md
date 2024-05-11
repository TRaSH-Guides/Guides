## Workflow Logic

??? abstract "Workflow Logic - [Click to show/hide]"

    **Depending on what's released first and available the following Workflow Logic will be used:**

    - When the 4k WEB-DL is released it will download the 4k WEB-DL. (streaming services)
    - When the 4k Remux is released it will upgrade to the 4k Remux.
    - When the IMAX-E is released it will upgrade to the IMAX-E. (*optional, see below*)

    ---

    *Possible Variables*

    **When no 4k release exists, it will grab the following:**

    - 1080p WEB-DL with DV/HDR (*optional also 1080p WEBDL without DV/HDR*)
    - 1080p Remux

    !!! info "[*Optional*] IMAX Enhanced (IMAX-E)<br>- When an IMAX Enhanced exists it will upgrade/downgrade to IMAX Enhanced.<br>- IMAX Enhanced will **ONLY** be chosen if it has the same **AUDIO** and **HDR Metadata**<br>- It won't downgrade from a `TrueHD Atmos` to a `DD+ Atmos` or from a `DV` to a `HDR`."
