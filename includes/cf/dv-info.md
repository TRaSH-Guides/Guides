??? info "Why am i getting purple or green colors - [Click to show/hide]"

    Why am i getting purple or green colors?

    There could be several reasons why your TV shows purple or green colors when playing Dolby Vision content. Here are some possible explanations:

    1. Unsupported Hardware: Your TV or hardware media player device (Roku, AppleTV, etc) doesn't support Dolby Vision. Or your hardware media player device doesn't support all the Dolby Vision Profiles. As a result, the device might struggle to produce accurate colors, leading to a purple or green tint.

    1. Incorrect Display Settings: Dolby Vision content often requires specific settings on the TV or display device to be enabled in order to deliver the intended visual experience. If these settings are not configured correctly, it can result in the device showing distorted colors, including purple or green hues.

    1. HDMI Compatibility Issues: Sometimes, HDMI cables or ports may not be fully compatible with Dolby Vision. If the media player device is not recognizing the Dolby Vision signal properly, it may fail to process the content correctly, resulting in abnormal color rendering.

    To resolve the purple or green color issues when playing Dolby Vision content, you can try the following troubleshooting steps:

    1. Ensure your TV or hardware media player device is Dolby Vision compatible and up-to-date with the latest firmware.
    1. Verify that your TV or display device is set up correctly and has the necessary Dolby Vision settings enabled.
    1. Check the HDMI cables and ensure they are capable of transmitting Dolby Vision signals.

??? info "Dolby Vision Profiles - [Click to show/hide]"

    Dolby Vision Profiles

    - **Profile 5** <sup>(*1*)</sup> - This is what comes with WEB-DL Dolby Vision release without HDR10 fallback.<br>(*Incompatible devices will playback with blown out pinks and greens*)
    - **Profile 7** <sup>(*2*)</sup> - This is what comes with UHD Bluray Remuxes and UHD BluRay releases.<br>*These files will play on an Nvidia Shield Pro (2019), but on most other players will revert to the HDR10 fallback.*
    - **Profile 8** <sup>(*3*)</sup> - This is what comes with (Hybrid) WEB-DL releases (HULU), Hybrid UHD Remux and UHD BluRay releases all of which have HDR10 fallback.<br>*This works with several mainstream media players.*<br>
    ------
    - <sup>(*1*) *On PLEX for AppleTV, It has been confirmed that with the latest build of Plex, Profile 5 MKV files now play correctly!*<br>*On an AppleTV 4K 1st gen and up, files are direct streamed (not transcoded) to an MP4 container and play using the native AVPlayer instead of Plex’s MPV.*</sup>
    - <sup>(*2*) *Neither Infuse nor PLEX for AppleTV will deliver real Dolby Vision with Profile 7.*</sup>
    - <sup>(*3*) *On PLEX for AppleTV it won't deliver real Dolby Vision with Profile 8, And will only play the HDR10 fallback.*<br>***“although your TV will incorrectly say that it is playing DV”***.<br>*With infuse it will convert it on the fly to Profile 5 and deliver real Dolby Vision.*<br>***“Make sure you set the Extended Dolby Vision settings to Limited (prefer accuracy) - Convert P8 to P5 (when possible), and play other P8 as HDR (output will switch to either DoVi or HDR depending on the video)”***</sup>

??? question "Which HDR Format should I choose? - [Click to show/hide]"

    ![!HDR Formats Flowchart](/Radarr/images/flowchart-hdr-formats.png)
