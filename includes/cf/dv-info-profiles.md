<!-- markdownlint-disable MD041-->
??? info "Dolby Vision Profiles - [Click to show/hide]"

    Dolby Vision Profiles

    - **Profile 5** <sup>(*1*)</sup> - This is what comes with WEB-DL Dolby Vision releases without HDR10 fallback.<br>(*Incompatible devices will playback with blown out pinks and greens*)
    - **Profile 7** <sup>(*2*)</sup> - This is what comes with UHD Bluray Remuxes and UHD BluRay releases.<br>*These files will play on an Nvidia Shield Pro (2019), but on most other players will revert to the HDR10 fallback.*
    - **Profile 8** <sup>(*3*)</sup> - This is what comes with (Hybrid) WEB-DL (HULU), Hybrid UHD Remux, and UHD BluRay releases (all of which have HDR10 fallback).<br>*This works with several mainstream media players.*<br>

    ---

    {! include-markdown "../../includes/cf/dv-limitations-atv.md" !}

    - <sup>(*1*) *PLEX for Apple TV and Plex with Infuse will only play profile 5 correctly if CMv2.9 is used.*</sup>
    - <sup>(*2*) *Neither Infuse nor PLEX for Apple TV will deliver real Dolby Vision with Profile 7.*</sup>
    - <sup>(*3*) *PLEX for Apple TV will only play profile 8 correctly if CMv2.9 is used. However, we have also received reports that in some cases, it will fall back to HDR10, or you may encounter a black screen.*<br><br>To prevent your TV from incorrectly indicating that it is playing DV follow the steps provided by an Infuse user:**<br>“With Infuse ensure you set the Extended Dolby Vision settings to Limited (prefer accuracy), convert P8 to P5 (when possible), and play other P8 as HDR (output will switch to either DoVi or HDR depending on the video)”**</sup>

??? info "Dolby Vision Versions - CMv2.9 and CMv4.0 - [Click to show/hide]"

    There are two versions of Dolby Vision, namely CMv2.9 and CMv4.0. CMv4.0 uses an improved algorithm and a superior tone curve, allowing for better mapping and more controls during the Dolby Vision trim pass process.

    More info about the different Dolby Vision Versions: [Dolby Vision Versions - CMv2.9 vs. CMv4.0](https://professionalsupport.dolby.com/s/article/When-should-I-use-CM-v2-9-or-CM-v4-0-and-can-I-convert-between-them?language=en_US){:target="\_blank" rel="noopener noreferrer"}
<!-- markdownlint-enable MD041-->
