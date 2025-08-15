<!-- markdownlint-disable MD041-->
**DV**<br>

This Custom Format serves as a catch-all for all Dolby Vision–related formats.

Depending on the source (WEB-DL, Blu-ray, or Remux), it matches the following formats:

- **Remuxes:** Include `DV HDR10` or `DV HDR10+`
- **Blu-ray encodes:** Include `DV HDR10` or `DV HDR10+`
- **WEB-DL:** In most cases, only Dolby Vision is present without an `HDR10` fallback. On incompatible devices, this can cause severe color issues such as blown-out pinks and greens. If you encounter this issue, make sure to also add the `DV (WEBDL)` format with a score of `-10000`
<!-- markdownlint-enable MD041-->
