*This Custom Format will only match on* `DV` **NOT** *on* `DV HDR10` *etc*.

Depending on the source (WEB-DL, Bluray, or Remux) this format will match the following:

- With Remuxes, it means that it will have `DV HDR10`.
- With Bluray encodes, it means it will have `DV HDR10`.
- With WEB-DL, it means 99% it will only support Dolby Vision without `HDR10` fallback (Incompatible devices will playback with blown out pinks and greens, if you have this issue always make sure you also add the following [Custom Format](#dv-webdl) with a score of `-10000`)
