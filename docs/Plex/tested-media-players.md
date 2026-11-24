---
hide:
    - navigation
    - toc
---

# Tested Media Players

| Symbol | Meaning |
| :---: | --- |
| :white_check_mark: | Yes |
| :x: | No |
| :grey_question: | No Test Results |
| *Empty* | No result yet |
| <sup>1</sup> | Notes/Extra Info: hover the number to read the note, or click it to jump to the note |
| <abbr title="Column description">DV P5</abbr> | Column names with a dotted underline have a description: hover them to read it |
| Row / Column | Click a row, or the name of a format column, to highlight it so you don't lose your place, click it again to remove the highlight |

<div class="media-players" markdown>

| Device | Player/Product | DV P5 | DV P7 | DV P8 | FEL | MEL | HDR10 | <abbr title="HDR10+ content backward compatible with non-HDR10+ TVs/Devices. HDR10+ metadata is ignored by devices that do not support the format and video is played back in HDR10.">HDR10+</abbr> | TrueHD<br>ATMOS | DTS X | DD+<br>ATMOS | TrueHD | DTS-HD<br>MA | FLAC/PCM | DD+/E-AC3 | DTS | AAC | DD/AC3 | Hi10 | ASS/SSA | PGS |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| AFTKM (Amazon Fire TV Stick 4K (Gen 2))[^firestick-tested] | Plex for Android (TV) | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | :white_check_mark: | :white_check_mark:[^firestick-hdr10plus] | :white_check_mark: | :x:[^firestick-dts] | :white_check_mark: | :white_check_mark: | :x:[^firestick-dts] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| Apple TV (4K)[^atv4k-tested] | Plex for Apple TV | :white_check_mark: | :x:[^atv-dv-profile] | :x:[^atv-dv-profile] | | | :white_check_mark: | :x:[^hdr10-fallback] | :x:[^atv-truehd-opus] | :x:[^dts-core-lpcm] | :x:[^atv-ddp-atmos-pcm] | :x:[^atv-truehd-opus] | :x:[^dts-core-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | :x:[^dts-core-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | | | |
| Apple TV (4K)[^atv4k-tested] | Infuse | :white_check_mark: | :x:[^atv-infuse-p7] | :white_check_mark: | | | :white_check_mark: | :x:[^hdr10-fallback] | :x:[^infuse-lpcm] | :x:[^infuse-lpcm] | :white_check_mark: | :x:[^infuse-lpcm] | :x:[^infuse-lpcm] | :white_check_mark: | :white_check_mark: | :x:[^decodes-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | | | |
| Apple TV (4K) 2nd Gen | Plex for Apple TV | :white_check_mark: | :x:[^atv-dv-profile] | :x:[^atv-dv-profile] | | | :white_check_mark: | :x:[^hdr10-fallback] | :x:[^atv-truehd-opus] | :x:[^dts-core-lpcm] | :x:[^atv-ddp-atmos-pcm] | :x:[^atv-truehd-opus] | :x:[^dts-core-lpcm] | :white_check_mark: | :white_check_mark: | :x:[^dts-core-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | | | |
| Apple TV (4K) 2nd Gen | Infuse | :white_check_mark: | :x:[^atv-infuse-p7] | :white_check_mark: | | | :white_check_mark: | :x:[^hdr10-fallback] | :x:[^infuse-lpcm] | :x:[^infuse-lpcm] | :white_check_mark: | :x:[^infuse-lpcm] | :x:[^infuse-lpcm] | :white_check_mark: | :white_check_mark: | :x:[^decodes-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | | | |
| Apple TV (4K) 3rd Gen | Plex for Apple TV | :white_check_mark: | :x:[^atv-dv-profile] | :x:[^atv-dv-profile] | | | :white_check_mark: | :white_check_mark: | :x:[^atv-truehd-opus] | :x:[^dts-core-lpcm] | :x:[^atv-ddp-atmos-pcm] | :x:[^atv-truehd-opus] | :x:[^dts-core-lpcm] | :white_check_mark: | :white_check_mark: | :x:[^dts-core-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | | | |
| Apple TV (4K) 3rd Gen | Infuse | :white_check_mark: | :x:[^atv-infuse-p7] | :white_check_mark: | | | :white_check_mark: | :white_check_mark: | :x:[^infuse-lpcm] | :x:[^infuse-lpcm] | :white_check_mark: | :x:[^infuse-lpcm] | :x:[^infuse-lpcm] | :white_check_mark: | :white_check_mark: | :x:[^decodes-lpcm] | :white_check_mark: | :x:[^decodes-lpcm] | | | |
| Chromecast Google TV[^chromecast-tested] | Plex for Android (TV) | :white_check_mark: | :x:[^hdr10-fallback] | :white_check_mark: | | | :white_check_mark: | :grey_question:[^hdr10plus-untested] | :x:[^chromecast-truehd] | :x:[^chromecast-dtsx] | :white_check_mark: | :x:[^chromecast-truehd] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| Homatics R 4k Plus[^homatics-tested] | PlexKodiConnect | :white_check_mark: | :white_check_mark:[^dv-p7-fel-mel] | :white_check_mark: | :white_check_mark:[^dv-p7-fel-mel] | :white_check_mark:[^dv-p7-fel-mel] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| Kodi LG webOSTV[^kodi-webos-tested] | PlexKodiConnect | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | :white_check_mark: | :x:[^hdr10-fallback] | :white_check_mark: | :grey_question: | :white_check_mark: | :grey_question: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :grey_question: | :white_check_mark: | :grey_question: | | | |
| LG OLED65CX6LA[^lg-cx-tested] | Plex for LG | :x:[^lg-cx-dv-p5] | :x:[^hdr10-fallback] | :x:[^hdr10-fallback] | | | :white_check_mark: | :x:[^hdr10-fallback] | :x:[^lg-cx-truehd-atmos] | :x:[^lg-cx-dts-7-1] | :white_check_mark: | :white_check_mark:[^lg-cx-truehd] | :x:[^lg-cx-dts-7-1] | :white_check_mark:[^lg-cx-flac-pcm] | :white_check_mark: | :x:[^lg-cx-dts] | :white_check_mark: | :white_check_mark: | | | |
| Roku Ultra 4640x[^roku-tested] | Plex for Roku | :x: | :x:[^hdr10-fallback] | :x:[^hdr10-fallback] | | | :white_check_mark: | :grey_question:[^hdr10plus-untested] | :x:[^roku-eac3] | :grey_question: | :white_check_mark: | :x:[^roku-eac3] | :x:[^roku-dts-hd-ma] | :grey_question: | :white_check_mark: | :grey_question: | :white_check_mark: | :white_check_mark: | | | |
| SHIELD Android TV (2015) | Plex for Android (TV) | :x: | :x: | :x: | | | :white_check_mark: | :x:[^hdr10-fallback] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| SHIELD Android TV (2017) | Plex for Android (TV) | :x: | :x: | :x: | | | :white_check_mark: | :x:[^hdr10-fallback] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| SHIELD Android TV (2019) (Pro)[^shield-pro-plex-tested] | Plex for Android (TV) | :white_check_mark: | :white_check_mark:[^shield-pro-plex-dv-p7] | :white_check_mark: | | | :white_check_mark: | :x:[^hdr10-fallback] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| SHIELD Android TV (2019) (Pro)[^shield-pro-pkc-tested] | PlexKodiConnect | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | :white_check_mark: | :x:[^hdr10-fallback] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| Ugoos AM6B+[^ugoos-tested] | Kodi (PM4K) | :white_check_mark: | :white_check_mark:[^dv-p7-fel-mel] | :white_check_mark: | :white_check_mark:[^dv-p7-fel-mel] | :white_check_mark:[^dv-p7-fel-mel] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |
| Zidoo/Z9X PRO[^zidoo-tested] | plex2zidoo (PM4K) | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | :white_check_mark: | :white_check_mark: | :white_check_mark:[^zidoo-edid] | :white_check_mark:[^zidoo-edid] | :white_check_mark: | :white_check_mark:[^zidoo-edid] | :white_check_mark:[^zidoo-edid] | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | | | |

</div>

///Footnotes Go Here///

[^firestick-tested]: Test Result Provided by: DoonGuy<br>
    Test Result: <https://discord.com/channels/492590071455940612/1242251198673846442>
[^firestick-hdr10plus]: HDR10+ video files with a height NOT divisible by 16 will not decode correctly.<br>
    <https://www.amazonforum.com/s/question/0D56Q0000CLUXxzSQH/hdr10-video-files-with-a-height-not-divisible-by-16-will-not-decode-correctly>
[^firestick-dts]: FIRE STICK ITSELF TRANSCODES TO DTS 5.1! I would consider this format unsupported!
[^atv4k-tested]: Test results provided by: MvB<br>
    Test Results: <https://discord.com/channels/492590071455940612/1227314280857342023><br>
    Date of Test: April 2024

    other sources:<br>
    Infuse forum, and several other sources like reddit and plex forum
[^atv-dv-profile]: Doesn't support this Dolby Vision profile, according to several sources including the Infuse forum. They mention that it actually falls back to HDR10, but your TV will trigger Dolby Vision (DV). This is often referred to as fake DV.<br>
    Fake DV = Triggers DV on your devices but you're actually playing the HDR10 base layer.

    However, one of our team members tested it and his setup triggered DV on his TV and his AVR. We can't say for sure if this is fake DV or real DV.
[^hdr10-fallback]: Will fallback to HDR10
[^atv-truehd-opus]: TrueHD is transcoded to Opus/FLAC (Atmos metadata is discarded)
[^dts-core-lpcm]: Decodes DTS Core to LPCM
[^atv-ddp-atmos-pcm]: Decodes to PCM (Atmos metadata is discarded)
[^decodes-lpcm]: Decodes to LPCM
[^atv-infuse-p7]: The Apple TV doesn't support Profile 7, according to several sources including the Infuse forum. They mention that it actually falls back to HDR10
[^infuse-lpcm]: Audio is converted losslessly to LPCM, but spatial metadata (i.e. Atmos or DTS:X) is discarded. No audio fidelity loss compared to source audio.
[^chromecast-tested]: Test Result Provided by: TRaSH<br>
    Test Result: <https://discord.com/channels/492590071455940612/1238791066786857041>
[^hdr10plus-untested]: No HDR10+ test result yet. It will fallback to HDR10; HDR10+ support is unknown until someone can test it.
[^chromecast-truehd]: AUDIO: Transcode (TrueHD 7.1  => OPUS 7.1)<br>
    Plex Playback Info: Transcode Reason TrueHD audio is not supported by the device
[^chromecast-dtsx]: Direct Play (DCA 7.1)<br>
    Plex Playback Info: Direct Play (DTS-HD 7.1)
[^homatics-tested]: Test results provided by: sek<br>
    Test Results: <https://discord.com/channels/492590071455940612/1293673285527011388><br>
    Date of Test: October 2024

    Suppose you want a box that can run premium Android applications and CoreELEC. In that case, the best overall device is the Homatics Box R 4k Plus with its support for Dolby Vision including FEL and AV1 with a certified Android TV box. However, CoreELEC will run slower than the Ugoos and may not be able to decode some older Blu-ray movies as it does not support the VC1 codec.
[^dv-p7-fel-mel]: Can play both FEL and MEL DV P7 as well as Single Track and Dual Track
[^kodi-webos-tested]: Test Result Provided by: Jimbo<br>
    Test Result: <https://discord.com/channels/492590071455940612/1237182040319987784><br>
    TV: LG C3
[^lg-cx-tested]: Test Result Provided by: TRaSH<br>
    Test Result: <https://discord.com/channels/492590071455940612/1235664786717671545>
[^lg-cx-dv-p5]: TV triggers DV, but picture is Purple and green
[^lg-cx-truehd-atmos]: Transcode (TrueHD 7.1 => EAC3 7.1)
[^lg-cx-dts-7-1]: Transcode (DCA 7.1 => AAC 5.1)<br>
    Plex LG Video Settings Force Direct Play Disabled else no audio
[^lg-cx-truehd]: Plex LG Video Settings Force Direct Play Enabled if disabled Transcodes (TrueHD 7.1 => EAC3 7.1)
[^lg-cx-flac-pcm]: Plex LG Video Settings Force Direct Play Enabled if disabled Transcodes to AAC Stereo
[^lg-cx-dts]: Transcodes (DCA 5.1 => AAC 5.1)<br>
    Plex LG Video Settings Force Direct Play Disabled else no audio
[^roku-tested]: Test Result Provided by: BeyondBroke<br>
    Test Result: <https://discord.com/channels/492590071455940612/1231867264010289163>
[^roku-eac3]: Audio is transcoded to E-AC3/DD+
[^roku-dts-hd-ma]: Audio is transcoded to AC3/DD
[^shield-pro-plex-tested]: Test results provided by: TRaSH and several others<br>
    Date of Test: April 2024
[^shield-pro-plex-dv-p7]: It should play Profile 7 releases without issues.<br>
    But:<br>
    FEL/MEL  will be played as single layer.<br>
    MEL means, the EL is just empty, so Profile 7 BL+MEL+RPU is totally identical to Profile 8 BL+RPU
[^shield-pro-pkc-tested]: Test results provided by: Jimbo<br>
    Test Results: <https://discord.com/channels/492590071455940612/1226612112730882100><br>
    Date of Test: April 2024
[^ugoos-tested]: Supports Dolby Vision including FEL and 3D on CoreELEC -ng. They can decode 24fps VC-1 content using a software decoding. Somewhat faster than S905X4-J devices, but more expensive and lack hardware support for AV1. CoreELEC can be installed on the emmc and HS400 enabled which greatly reduces boot time and speeds up the interface making it feel significantly faster than the S905X4.

    If you want the best media box to only run CoreELEC, then the Ugoos AM6b+ is the best box with its faster processor and the ability to install COREelec to the emmc with HS400, but it runs an older version of Android and sacrifices support for certified apps including Netflix and AV1. However, only the Ugoos AM6b+ can fully replace a disc-based player.
[^zidoo-tested]: Test results provided by: Chris.dc<br>
    Date of Test: April 2024<br>
    Test Result Provided by: ANIMATEK<br>
    Test Result: <https://discord.com/channels/492590071455940612/1228243671200043018><br>
    Date of Test: April 2024
[^zidoo-edid]: There are special considerations, where the audio setup will modify the EDID profile that gets sent from the TV to the Zidoo, cutting some framerate/resolution combinations. In some cases this leads to a frame or two skipping every now and then, because the framerate of the video didn't match the TV.<br>
    See this thread on how to get the best EDID for your setup (even if this is not an issue for you, as there are other benefits):  <https://forum.zidoo.tv/index.php?threads/edid-thread-rtd1619bpd-players.96829/>

*[DV P5]: DV Profile 5. This is what comes with WEB-DL Dolby Vision releases without HDR10 fallback. (Incompatible devices will playback with blown out pinks and greens)
*[DV P7]: DV Profile 7. This is what comes with UHD Bluray Remuxes and UHD BluRay releases. These files will play on an Nvidia Shield Pro (2019), but on most other players will revert to the HDR10 fallback.
*[DV P8]: DV Profile 8. This is what comes with (Hybrid) WEB-DL (HULU), Hybrid UHD Remux, and UHD BluRay releases (all of which have HDR10 fallback). This works with several mainstream media players.
*[FEL]: DV Profile 7 with a Full Enhancement Layer. Found on many UHD BluRay Remuxes. Players that play DV P7 without FEL support ignore the enhancement layer and play the base layer with the DV metadata. Some DV P8 releases have the FEL baked into the video, those play as normal DV P8 and don't need FEL support.
*[MEL]: DV Profile 7 with a Minimal Enhancement Layer. The enhancement layer is empty, so the picture is the same as DV Profile 8.
*[Hi10]: H.264 (AVC) High 10 profile, also called Hi10P. 10-bit H.264, common in older anime releases. Most hardware decoders can't play it, so it needs software decoding or a transcode.
*[ASS/SSA]: Advanced SubStation Alpha / SubStation Alpha subtitles, common in anime releases. Styled subtitles with fonts, colors and positioning. If the player can't render them, Plex burns them into the video, which forces a video transcode.
*[PGS]: Presentation Graphic Stream subtitles, found on Blu-ray and UHD BluRay releases. Image-based, so the player can't restyle them. If the player can't render them, Plex burns them into the video, which forces a video transcode.
