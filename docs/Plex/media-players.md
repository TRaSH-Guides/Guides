# Media Players

We've created a excel sheet with several tested Media Player devices with info that has been provided by our community.

Do you see a missing Player/Product ? and are you able to provide the needed info please join [TRaSH Guides Discord](https://trash-guides.info/discord){:target="_blank" rel="noopener noreferrer"}

We hope this excel sheet will be a helpful resource for those looking for a reliable Media Player device.

!!! info "A lot of results have a comment added that provides extra information, such as fallback HDR or audio formats, as well as other information that we've gathered from several sources."

## What does it cover

This sheet will only covers Player/Product that can run the Plex client direct/in-direct (JF/Emby isn't covered **yet** in this sheet because of the lack of proper tautulli app, and feedback/info from users).

The following aspects are covered

### Does it support the most common HDR formats

The sheet also has comments added for extra info

- Dolby Vision Profile 5 (*does not have a HDR10 baselayer, so cannot fallback to HDR10*)
- Dolby Vision Profile 7 (*DV + HDR10 baselayer, so it can fallback to HDR10*)
- Dolby Vision Profile 8 (*DV + HDR10 baselayer, so it can fallback to HDR10*)
- HDR10
- HDR10+ (*HDR10+ has also a HDR10 baselayer, so it can fallback to HDR10*)

!!! info "Which profile is used by what"

    - Profile 5 => WEBDL (Streaming Services)
    - Profile 7 => Untouched Remuxes and BR-DISK
    - Profile 8 => Encodes, Hybrid Remuxes, Hybrid WEBDL

#### How to make use of HDR Formats for Radarr

- [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most use of Custom Formats and shows some specifics of my configuration. You can use

- You have a 4K TV and a hardware media player device (such as Roku, AppleTV, Shield, SmartTV App, etc.) that supports several HDR formats (such as Dolby Vision, HDR10, HDR10+, etc.).

{! include-markdown "../../includes/cf/radarr-all-hdr-formats.md" !}

#### How to make use of HDR Formats for Sonarr

- [How to setup Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most use of Custom Formats and shows some specifics of my configuration. You can use these examples to get an idea of how to set up your preferences.

- You have a 4K TV and a hardware media player device (such as Roku, AppleTV, Shield, SmartTV App, etc.) that supports several HDR formats (such as Dolby Vision, HDR10, HDR10+, etc.).

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

### Does it passthrough the most common audio formats

This allows for the best audio quality as the audio signal is not altered or compressed in any way before reaching the AV receiver or soundbar. This is especially important for high-quality audio formats such as Dolby TrueHD or DTS-HD Master Audio.

By using audio passthrough, you can ensure that you are getting the best audio experience possible when watching movies or listening to music through your home theater system. It allows you to take full advantage of the capabilities of your AVR/Soundbar and ensures that you are hearing the audio as it was intended to be heard by the content creators.

Overall, audio passthrough is the ideal way to send audio from your media server to your AV receiver or soundbar for the highest quality audio experience.

- TrueHD Atmos
- DTS X
- DD+ Atmos
- TrueHD
- DTS-HD MA
- FLAC/PCM
- DD+ (E-AC3)
- DTS
- AAC
- DD (AC3)

#### How to make use of Audio Formats for Radarr

- [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most use of Custom Formats and shows some specifics of my configuration. You can use

- You have an audio setup that supports all HD Audio (TrueHD, DTS-X, DTS-HD, etc).
- You have a media player (hardware devices) that can passthrough HD audio.
- You don't have an AppleTV (Being it can't passthrough untouched HD audio).

*The reason that I score lossy Atmos higher than lossless DTS-HD MA is that I prefer having the object metadata (Atmos) over lossless audio.*

{! include-markdown "../../includes/cf/radarr-audio.md" !}

#### How to make use of Audio Formats for Sonarr

At the moment I decided not to add `Audio Advanced` Custom Formats to the WEB profile. You will hardly find HD audio with WEB-DL (Most newer WEBDL will have Atmos). If you also want HD audio formats, I would suggest going for Remuxes.

## Link to tested Media Player Devices

[Tested Media Players](https://docs.google.com/spreadsheets/d/15Wf_jy5WqOPShczFKQB28cCetBgAGcnA0mNOG-ePwDc/edit#gid=0){:target="_blank" rel="noopener noreferrer"}
