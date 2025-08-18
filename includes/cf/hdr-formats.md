<!-- markdownlint-disable MD041 MD036-->
**HDR Formats Setup**

**HDR**

All users with HDR-capable equipment must add the `HDR` and `DV (WEBDL)` custom formats. This configuration ensures that the most compatible HDR formats are prioritized while excluding WEB-sourced Dolby Vision releases that lack an HDR base layer.

--8<-- "includes/cf-descriptions/dv-boost.md"

--8<-- "includes/cf-descriptions/hdr10plus-boost.md"

---

??? question "Why do I need `DV (WEBDL)`? - [Click to show/hide]"

    The `DV (WEBDL)` custom format serves two important purposes:

    - It ensures that the most compatible HDR formats are prioritized
    - It excludes WEB-sourced Dolby Vision releases without an HDR base layer (Profile 5)

    **When to use:** If not every device accessing your media server supports Dolby Vision, you should add the `DV (WEBDL)` custom format to prevent compatibility issues.
<!-- markdownlint-enable MD041 MD036-->
