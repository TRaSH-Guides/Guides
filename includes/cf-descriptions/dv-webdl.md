<!-- markdownlint-disable MD041-->
**DV (WEBDL)**<br>

This is a special Custom Format that blocks WEBDLs **WITH** Dolby Vision but **WITHOUT** HDR10 fallback.

You will need to add the following as a new Custom Format, and when created adjust the scoring in your Quality Profile (`Settings` => `Profiles`) to `-10000`.

This Custom Format works together with the normal DV Custom Format that you would use to prefer Dolby Vision.

Most WEBDL from Streaming Services **DO NOT** have the fallback to HDR10. During playback, issues with weird colors (typically a green hue) can result when you attempt to play it on a non-Dolby Vision-compatible setup.

Remuxes and Bluray have a fallback to HDR10.
<!-- markdownlint-enable MD041-->
