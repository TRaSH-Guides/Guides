<!-- markdownlint-disable MD041-->
**HDR Setup**

All users with HDR-capable equipment must add the `HDR` and `DV (WEBDL)` custom formats. This configuration ensures that the most compatible HDR formats are prioritized while excluding WEB-sourced Dolby Vision releases that lack an HDR base layer.

**Dolby Vision (DV)**

Users with Dolby Vision-compatible equipment should add the `DV` custom format. This prioritizes releases containing Dolby Vision over standard HDR releases.

{==

**Important:** If *everyone* who uses your media server has equipment that fully supports Dolby Vision, you can safely remove the `DV (WEBDL)` custom format. However, in all other circumstances, removing the `DV (WEBDL)` custom format will cause playback issues.

==}

**HDR10+ Boost**

If you prefer HDR10+ releases and have compatible equipment, add the `HDR10+ Boost` custom format. This prioritizes releases containing HDR10+ over standard HDR releases.

??? question "Why do I need `DV (WEBDL)`? - [Click to show/hide]"

    The `DV (WEBDL)` custom format serves two important purposes:

    - It ensures that the most compatible HDR formats are prioritized
    - It excludes WEB-sourced Dolby Vision releases without an HDR base layer (Profile 5)

    **When to use:** If not every device accessing your media server supports Dolby Vision, you should add the `DV (WEBDL)` custom format to prevent compatibility issues.
<!-- markdownlint-enable MD041-->
