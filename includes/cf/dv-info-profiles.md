<!-- markdownlint-disable MD041-->
??? info "Dolby Vision Profiles - [Click to show/hide]"

    Dolby Vision Profiles

    - **Profile 5** <sup>(*1*)</sup> - This is what comes with WEB-DL Dolby Vision releases without HDR10 fallback.<br>(*Incompatible devices will playback with blown out pinks and greens*)
    - **Profile 7** <sup>(*2*)</sup> - This is what comes with UHD Bluray Remuxes and UHD BluRay releases.<br>*These files will play on an Nvidia Shield Pro (2019), but on most other players will revert to the HDR10 fallback.*
    - **Profile 8** <sup>(*3*)</sup> - This is what comes with (Hybrid) WEB-DL (HULU), Hybrid UHD Remux, and UHD BluRay releases (all of which have HDR10 fallback).<br>*This works with several mainstream media players.*<br>

    ---

    {! include-markdown "../../includes/cf/dv-limitations-atv.md" !}

    - <sup>(*1*) *PLEX for AppleTV and Plex with Infuse will only play profile 5 correctly if CMv2.9 is used*</sup>
    - <sup>(*2*) *Neither Infuse nor PLEX for AppleTV will deliver real Dolby Vision with Profile 7.*</sup>
    - <sup>(*3*) *On PLEX for AppleTV, it won't deliver real Dolby Vision with Profile 8 and will only play the HDR10 fallback if CM2.9 is used. Otherwise, you will end up with a black screen*<br>***“although your TV will incorrectly say that it is playing DV”***.<br>*With infuse, it will convert it on the fly to Profile 5, and deliver real Dolby Vision if CMv2.9 is used. Otherwise, you will end up with a black screen*<br>***“Make sure you set the Extended Dolby Vision settings to Limited (prefer accuracy), Convert P8 to P5 (when possible), and play other P8 as HDR (output will switch to either DoVi or HDR depending on the video)”***</sup>

??? info "Dolby Vision Versions - CMv2.9 and CMv4.0 - [Click to show/hide]"

    !!! bug "It is too technical to explain in detail, so I'll keep it short with tested facts: <br>PLEX for AppleTV and Plex with Infuse only support CMv2.9."

    There are two versions of Dolby Vision, namely CMv2.9 and CMv4.0. CMv4.0 uses an improved algorithm and a superior tone curve, allowing for better mapping and more controls during the Dolby Vision trim pass process.

    More info about the different Dolby Vision Versions: [Dolby Vision Versions - CMv2.9 vs. CMv4.0](https://professionalsupport.dolby.com/s/article/When-should-I-use-CM-v2-9-or-CM-v4-0-and-can-I-convert-between-them?language=en_US)
<!-- markdownlint-enable MD041-->
