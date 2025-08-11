<!-- markdownlint-disable MD041-->
**HDR**

All users with HDR-capable equipment must add the `HDR` and `DV (WEBDL)` custom formats. This ensures that the most compatible HDR formats are prioritized, while WEB-sourced Dolby Vision releases *without* an HDR base layer are excluded.

**DV**

Users with equipment that supports Dolby Vision should add the `DV` custom format so that releases containing Dolby Vision are prioritized over standard HDR releases.

{==

If *everyone* who uses your media server has equipment that fully supports Dolby Vision, then you can remove the `DV (WEBDL)` custom format. In any other circumstances removing the  `DV (WEBDL)` custom format will lead to playback issues.

==}

**HDR10+**

If you prefer HDR10+ releases and you have equipment that supports HDR10+, then you should add the `HDR10+` custom format, so that releases containing HDR10+ are prioritized over standard HDR releases.

??? question "Why do I need `DV (WEBDL)`? - [Click to show/hide]"

    - This ensures that the most compatible HDR formats are prioritized, while WEB-sourced Dolby Vision releases without an HDR base layer are excluded.(Profile 5)
    - If NOT every device accessing your media server supports Dolby Vision, then you should add the `DV (WEBDL)` custom format.
<!-- markdownlint-enable MD041-->
