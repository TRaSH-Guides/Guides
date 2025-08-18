<!-- markdownlint-disable MD041 MD036-->
**DV Boost**<br>

If you prefer Dolby Vision and have compatible equipment, add the `DV Boost` custom format. This prioritizes releases containing Dolby Vision over standard HDR releases.

{==

>**Important:** If *everyone* who uses your media server has equipment that fully supports Dolby Vision, you can safely remove the `DV (WEBDL)` custom format. However, in all other circumstances, removing the `DV (WEBDL)` custom format will cause playback issues.

==}

Depending on the source (WEB-DL, Blu-ray, or Remux), it will prefer the following Dolby Vision formats:

- **Remuxes:** Prefers `DV HDR10` or `DV HDR10+` over standard HDR releases.
- **Blu-ray encodes:** Prefers `DV HDR10` or `DV HDR10+` over standard HDR releases.
- **WEB-DL:** Prefers `DV HDR10` or `DV HDR10+` and `DV P5`:circle-question:{ title="WEB-sourced Dolby Vision releases without an HDR base layer<br>(DV Profile 5)" } over standard HDR releases, but still prioritizes `DV HDR10` or `DV HDR10+` over `DV P5`:circle-question:{ title="WEB-sourced Dolby Vision releases without an HDR base layer<br>(DV Profile 5)" }. Adding the `DV (WEBDL)` format excludes `DV P5`:circle-question:{ title="WEB-sourced Dolby Vision releases without an HDR base layer<br>(DV Profile 5)" }.
<!-- markdownlint-enable MD041 MD036-->
