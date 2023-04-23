!!! info "Dolby Vision is available in several profiles"

    - **Profile 5** <sup>(*1*)</sup> - This is what comes with WEB-DL Dolby Vision release without HDR10 fallback.<br>(*Incompatible devices will playback with blown out pinks and greens*)
    - **Profile 7** <sup>(*2*)</sup> - This is what comes with UHD Bluray Remuxes and UHD BluRay releases.<br>*These files will play on an Nvidia Shield Pro (2019), but on most other players will revert to the HDR10 fallback.*
    - **Profile 8** <sup>(*3*)</sup> - This is what comes with (Hybrid) WEB-DL releases (HULU), Hybrid UHD Remux and UHD BluRay releases all of which have HDR10 fallback.<br>*This works with several mainstream media players.*<br>
    ------
    - <sup>(*1*) *On PLEX for AppleTV, It has been confirmed that with the latest build of Plex, Profile 5 MKV files now play correctly!*<br>*On an AppleTV 4K 1st gen and up, files are direct streamed (not transcoded) to an MP4 container and play using the native AVPlayer instead of Plex’s MPV.*</sup>
    - <sup>(*2*) *Neither Infuse nor PLEX for AppleTV will deliver real Dolby Vision with Profile 7.*</sup>
    - <sup>(*3*) *On PLEX for AppleTV it won't deliver real Dolby Vision with Profile 8, And will only play the HDR10 fallback.*<br>***“although your TV will incorrectly say that it is playing DV”***.<br>*With infuse it will convert it on the fly to Profile 5 and deliver real Dolby Vision.*<br>***“Make sure you set the Extended Dolby Vision settings to Limited (prefer accuracy) - Convert P8 to P5 (when possible), and play other P8 as HDR (output will switch to either DoVi or HDR depending on the video)”***</sup>
