# What does my Media Player Support

We've created an Excel sheet with several tested Media Player devices with info that our community has provided.

We hope this Excel sheet will be helpful for everyone looking for a reliable Media Player device.

Do you see a missing Player/Product? Are you able to provide the needed info? Please join [TRaSH Guides Discord](https://trash-guides.info/discord){:target="_blank" rel="noopener noreferrer"}

??? question "How can I provide info on a missing player? What do I need to provide? - [Click to show/hide]"

    - Currently, it's only possible to provide info if the playback is seen in Tautulli.
    - Player or Product that can run the Plex client directly or indirectly (Infuse, Plex Kodi Connect, Plex2Zidoo, etc)
    - Preferably a TV that can do Dolby Vision, but we also need HDR10+ results.
    - Player and Product info can be seen in Tautulli.
    - When doing a playback test for HDR formats provide screenshots of what Tautulli and your TV show, along with whatever other devices you have that show what formats are being used.
    - When doing an audio format test provide screenshots from Tautulli and your AVR.
    - Provide this info in [TRaSH Guides Discord](https://trash-guides.info/discord){:target="_blank" rel="noopener noreferrer"} in #request-suggestions with a title starting with: `Test Media Player <your tested device>`

## What does the spreadsheet cover

This sheet will only cover Players/Products that can run the Plex client directly or indirectly (*Jellyfin/Emby isn't covered **yet** due to the lack of a proper Tautulli app and feedback/info from users*).

!!! info "Jellyfin/Emby"

    While these principles are based on Plex and the capabilities of certain devices, the capabilities of these devices also apply to JellyFin and Emby. Assuming that it's possible to do the equivalent streaming method (direct or indirect play) with your media server, the hardware should act the same as if Plex was used.

The following aspects are covered

### Does it support the most common HDR formats

The sheet also has notes added for extra info

- Dolby Vision Profile 5 (*does not have an HDR10 baselayer, so it cannot fallback to HDR10*)
- Dolby Vision Profile 7 (*DV + HDR10 baselayer, so it can fallback to HDR10*)
- Dolby Vision Profile 8 (*DV + HDR10 baselayer, so it can fallback to HDR10*)
- HDR10
- HDR10+ (*HDR10+ has also a HDR10 baselayer, so it can fallback to HDR10*)

#### Which Profile is used by what

- Profile 5 => WEBDL (Streaming Services)
- Profile 7 => Untouched Remuxes and BR-DISK
- Profile 8 => Encodes, Hybrid Remuxes, Hybrid WEBDL, and in some cases standard WEBDL like from Hulu

### Does it support audio passthrough in the most common formats

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

## Link to tested Media Player Devices

[Tested Media Players](https://docs.google.com/spreadsheets/d/15Wf_jy5WqOPShczFKQB28cCetBgAGcnA0mNOG-ePwDc/edit?usp=sharing){:target="_blank" rel="noopener noreferrer"}

!!! info "A lot of results have a note added that provides extra information, such as fallback HDR or audio formats, as well as other information that we've gathered from several sources."

---

## What should I do next with this info

The next thing to do is set up a proper quality profile with the info you gathered from this sheet.
To make this easier, we've made a section labeled "How to set up a quality profile for Radarr/Sonarr" that has a flowchart to help you even more to decide what to choose.

### Radarr

[How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most of Custom Formats and shows some specifics of my configuration. You can use these examples to get an idea of how to set up your preferences.

#### How to make use of HDR Formats for Radarr

- [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most of Custom Formats and shows some specifics of my configuration. You can use

{! include-markdown "../../includes/cf/radarr-all-hdr-formats.md" !}

#### How to make use of Audio Formats for Radarr

- [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most use of Custom Formats and shows some specifics of my configuration. You can use

{! include-markdown "../../includes/cf/radarr-audio.md" !}

---

### Sonarr

[How to set up Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most of Custom Formats and shows some specifics of my configuration. You can use these examples to get an idea of how to set up your preferences.

#### How to make use of HDR Formats for Sonarr

- [How to set up Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"} - Explains how to make the most of Custom Formats and shows some specifics of my configuration. You can use these examples to get an idea of how to set up your preferences.

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

#### How to make use of Audio Formats for Sonarr

At the moment, we've decided not to add `Audio Advanced` Custom Formats to the WEB profile. You will hardly find HD audio with WEB-DL (Most newer WEBDL will have Atmos). If you also want HD audio formats, we would suggest going for Remuxes.

--8<-- "includes/support.md"
