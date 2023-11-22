# How to set up Quality Profiles

*aka How to set up Custom Formats*<br><br>
So what's the best way to set up the Custom Formats and which ones to use with which scores to set up your quality profiles?

There isn't a "best" setup, it depends on your media setup (hardware devices) and your personal preferences.

Some prefer high-quality audio (HD Audio), others high-quality video. Many prefer both.

Here I will try to explain how to make the most use of Custom Formats to help you to set up your quality profiles for your personal needs.

I created a [flowchart](#which-quality-profile-should-you-choose) to make your decision/choices easier.

------

## Basics

After you've added the Custom Formats, as explained in [How to import Custom Formats](/Sonarr/sonarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
You will need to set it up in the quality Profile you want to use/prefer to make use of the Custom Formats.

`Settings` => `Profiles`

![!cf-settings-profiles](images/cf-settings-profiles.png)

!!! info "Sonarr Custom Formats can be set per profile and isn't global"
Select the profile that you want to use/prefer.

![!cf-quality-profiles](images/cf-quality-profiles.png)

![!cf-profile-selected](images/cf-profile-selected.png)

1. Profile name.
1. Allow upgrades. Sonarr will stop upgrading quality once (3) is met.
1. Upgrade until the selected quality.
1. The `Minimum Custom Format Score` that is allowed to download. [More Info](#minimum-custom-format-score)
1. Keep upgrading Custom Format until this score is reached. (setting this to `0` means no upgrades will happen based on Custom Formats)

At the bottom, in your chosen profile, you will see the added Custom Formats where you can start setting up the scores.

??? success "Screenshot example - [Click to show/hide]"
    ![!cf-quality-profile-cf](images/cf-quality-profile-cf.png)

    !!! warning
        These screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

        - Always follow the data described in the guide.
        - If you have any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.

!!! info "Keep in mind Custom Formats are made to fine-tune your Quality Profile.<br>Generally, quality trumps all"

    Custom formats are controlled by Quality Profiles.

    - The Upgrade Until score prevents upgrading once a release with this desired score has been downloaded.
    - A score of 0 results in the custom format being informational only.
    - The Minimum score requires releases to reach this threshold otherwise they will be rejected.
    - Custom formats that match with undesirable attributes should be given a negative score to lower their appeal.
    - Outright rejections should be given a negative score low enough that even if all of the other formats with positive scores were added, the score would still fall below the minimum.

------

{! include-markdown "../../includes/merge-quality/sonarrv4-current-logic.md" !}

------

## Which Quality Profile should you choose

??? abstract "Which Quality Profile should you choose - [Click to show/hide]"

    ![Flowchart](/Sonarr/images/flowchart-quality-profiles-sonarr.png)

    If you're unsure or have questions do not hesitate to ask for help on Discord

    [![Discord chat](https://img.shields.io/discord/492590071455940612?style=for-the-badge&color=4051B5&logo=discord){ .off-glb }](https://trash-guides.info/discord){:target="_blank" rel="noopener noreferrer"}

------

## TRaSH Quality Profiles

The following Quality Profiles can be combined into a single Quality Profile if you, for example, want to be able to upgrade from 1080p to 4K/2160p.

### WEB-1080p

If you prefer 720p/1080p WEBDL (WEB-1080p)

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

{! include-markdown "../../includes/cf/sonarr-optional.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-streaming-services.md" !}

{! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}

I decided not to add `Audio Advanced` Custom Formats to the WEB profile, You will hardly find HD audio with WEB-DL (most newer WEBDL will have Atmos). If you want HD audio formats, I would suggest going with Remuxes.

Use the following main settings in your profile.

![!cf-profile-web1080](images/cf-profile-web1080.png)

!!! info ""

    For some older shows, you might want to enable the `WEB 720p`, or even the `HDTV 1080p`.

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? abstract "Workflow Logic - [Click to show/hide]"

    - It will download WEB-DL 1080p. (If you also enabled `WEB 720p` and/or `HDTV 1080p` it will upgrade until `Upgrade Until`)
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

------

### WEB-2160p

If you prefer 2160p WEBDL (WEB-2160p)

The only deal breaker with 2160p is when the release includes DV/HDR. 2160p without DV/HDR is of minimal benefit.

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

{! include-markdown "../../includes/cf/sonarr-optional.md" !}

{! include-markdown "../../includes/cf/sonarr-optional-uhd.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-uhd-streaming-services.md" !}

{! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}

I decided not to add `Audio Advanced` Custom Formats to the WEB profile. You will hardly find HD audio with WEB-DL (Most newer WEBDL will have Atmos). If you also want HD audio formats, I would suggest going for Remuxes.

Use the following main settings in your profile.

![!cf-profile-web2160](images/cf-profile-web2160.png)

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? abstract "Workflow Logic - [Click to show/hide]"

    - This will download WEB-2160p with HDR/DV.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

------

## Custom Format Groups

The following custom format groups should be combined with the Quality Profiles above. Users will need to choose which options and custom formats they prefer.

### HDR Formats

- You have a 4K TV and a hardware media player device (such as Roku, AppleTV, Shield, SmartTV App, etc.) that supports several HDR formats (such as Dolby Vision, HDR10, HDR10+, etc.).

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

------

## FAQ & INFO

### Why only WEB-DL

??? question "Why do you only have a release profile for WEB-DL - [Click to show/hide]"

    I only do WEB-DL, myself, for TV shows. In my opinion, WEB-DL is the sweet spot between quality and size (you often don't see big differences anyway for TV shows) except for shows like GOT, Vikings, etc.

### Why prefer P2P groups

??? question "Why do you prefer P2P groups over scene groups - [Click to show/hide]"

    Scene groups are always in a rush to bring releases out as fast as possible.

    I noticed, often, that I got Repacks/Propers from them, or of different groups and quality. P2P release groups are a bit smarter, and sort of work together, by not doing the same releases. Also, I noticed that with some scene releases the 5.1 audio was stripped out or converted to AAC audio.

    In my opinion, the P2P releases are better quality. However, there is one scene group that does bring out quality releases `-deflate`/`-inflate`.

### Why so many repacks/propers

??? question "Why do I see so many repacks/propers of Amazon WEB-DLs lately - [Click to show/hide]"

    A large portion of Amazon WEB-DLs in the last weeks have only had 192Kbps DD+5.1 (because that's all Amazon made available initially). The proper 640Kbps DD+5.1 audio might appear a few hours, or a few months, later. The lower quality release will be REPACKED when the higher quality audio is available.

### Proper and Repacks

??? tip "Proper and Repacks - [Click to show/hide]"

    I also suggest that you change the Propers and Repacks settings in Radarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Sonarr/sonarr-collection-of-custom-formats/#repackproper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Format preferences will be used instead.

### Custom Formats to avoid certain releases

??? question "How to use a Custom Format to avoid certain releases? - [Click to show/hide]"

    For Custom Formats you really want to avoid, set it to something really low like `-10000` and not something like `-10`.
    When you add your preferred Custom Format and set it to something like `+10`, it's possible that, for example, the `BR-DISK` will be downloaded - (-10)+(+10)=0 - if your `Minimum Custom Format Score` is set at `0`.

### Releases you should avoid

This is a must-have for every Quality Profile you use in my opinion. All these Custom Formats make sure you don't get Low Quality Releases.

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

### Custom Formats with a score of 0

??? question "What do Custom Formats with a score of 0 do? - [Click to show/hide]"

    All Custom Formats with a score of 0 are purely informational and don't do anything.

### Minimum Custom Format Score

??? info "Minimum Custom Format Score - [Click to show/hide]"

    Some people suggest not to use negative scores for your Custom Formats and set this option to a higher score than 0.

    The reason why I don't prefer/use this is because you could limit yourself when some new groups or whatever will be released.

    Also, it makes it much more clear what you prefer and what you want to avoid.

### Audio Channels

??? info "Audio Channels - [Click to show/hide]"

    Elsewhere in the guide, you will find a separate group of custom formats called `Audio Channels`. These will match the number of audio channels in a release, for example, 2.0 (stereo) or 5.1/7.1 (surround sound). Personally, I wouldn't add the audio channels Custom Formats as you could limit yourself in the amount of releases you're able to get. Only use them if you have a specific need for them.

    Using this with any kind of Remux Quality Profile is useless, in my opinion, being that 99% of all Remuxes are multi-audio anyway. You can get better scores just by using the `Audio Advanced` Custom Formats.

### Avoid using the x264/x265 Custom Format

??? tip "Avoid using the x264/x265 Custom Format - [Click to show/hide]"

    Avoid using the x264/x265 Custom Format with a score if possible, it's smarter to use the [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} Custom Format.

    Something like 95% of video files are x264 and have much better direct play support. If you have more than a of couple users, you will notice much more transcoding.

    Use x265 only for 4k releases and the [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} makes sure you still get the x265 releases.

### Why am I getting purple or green colors

{! include-markdown "../../includes/cf/dv-info-green-purple.md" !}

### Dolby Vision Profiles

{! include-markdown "../../includes/cf/dv-info-profiles.md" !}

## Thanks

Special thanks to everyone who helped with the testing and creation of these Custom Formats.

--8<-- "includes/support.md"
