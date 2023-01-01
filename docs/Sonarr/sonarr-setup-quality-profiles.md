# How to setup Quality Profiles

*aka How to setup Custom Formats*<br><br>
So what's the best way to setup the Custom Formats and which ones to use with which scores to setup your quality profiles?

There isn't a best setup, it depends on your setup (hardware devices) and your own personal preferences.

Some prefer high quality audio (HD Audio), others high quality video. Many prefer both.

Here I will try to explain how to make the most use of Custom Formats to help you to setup your quality profiles for your personal needs.

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
1. The `Minimum Custom Format Score` allowed to download. [More Info](#minimum-custom-format-score)
1. Keep upgrading Custom Format until this score is reached. (setting this to `0` means no upgrades will happen based on Custom Formats)

At the bottom in your chosen profile you will see the added Custom Formats where you can start setting up the scores.

??? check "Screenshot example - [CLICK TO EXPAND]"
    ![!cf-quality-profile-cf](images/cf-quality-profile-cf.png)

    !!! attention
        These screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

        - Always follow the data described in the guide.
        - If you got any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.

!!! info "Keep in mind Custom Formats are made to fine tune your Quality Profile.<br>Generally, quality trumps all"

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

??? summary "Which Quality Profile should you choose - [CLICK TO EXPAND]"

    ![Flowchart](/Sonarr/images/flowchart-custom-format-sonarr.png)

    If you're unsure or have questions do not hesitate to ask for help on Discord

    [![Discord chat](https://img.shields.io/discord/492590071455940612?style=for-the-badge&color=4051B5&logo=discord){ .off-glb }](https://trash-guides.info/discord){:target="_blank" rel="noopener noreferrer"}

------

## TRaSH Quality Profiles

### WEB-1080p

If you prefer 720p/1080p WEBDL (WEB-1080p)

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-streaming-services.md" !}

{! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}

I decided not to add `Audio Advanced` Custom Formats to the WEB profile, You will hardly find HD audio with WEB-DL (Most newer WEBDL will have Atmos). If you also want HD audio formats I would suggest to go for the Remuxes.

Use the following main settings in your profile.

![!cf-profile-web1080](images/cf-profile-web1080.png)

!!! info ""

    For some older shows you might want to enable the `WEB 720p` or even the `HDTV 1080p`.

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? summary "Workflow Logic - [CLICK TO EXPAND]"

    - It will download WEB-DL 1080p. (If you also enabled `WEB 720p` and/or `HDTV 1080p` it will upgrade till `Upgrade Until`)
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

------

### WEB-2160p

If you prefer 2160p WEBDL (WEB-2160p)

The only deal breaker with 2160p is when you get them with DV/HDR, 2160p without DV/HDR is a minimal profit.

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-hdr-formats.md" !}

{! include-markdown "../../includes/cf/sonarr-unwanted-uhd.md" !}

{! include-markdown "../../includes/cf/sonarr-optional-uhd.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-streaming-services.md" !}

{! include-markdown "../../includes/cf/sonarr-hq-source-group.md" !}

I decided not to add `Audio Advanced` Custom Formats to the WEB profile, You will hardly find HD audio with WEB-DL (Most newer WEBDL will have Atmos). If you also want HD audio formats I would suggest to go for the Remuxes.

Use the following main settings in your profile.

![!cf-profile-web2160](images/cf-profile-web2160.png)

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? summary "Workflow Logic - [CLICK TO EXPAND]"

    - It will download WEB-2160p with HDR/DV.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

------

### HDR Formats

- You have a setup that supports Dolby Vision.
- You share your media library with other family members that also have have Dolby Vision compatible devices.

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

------

### HDR Formats + DV (WEBDL)

- Not all devices in your chain support Dolby Vision.
- You share your media library with other family members that don't have Dolby Vision compatible devices.

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats-dv-web.md" !}

------

### HDR Formats + DV (WEBDL) + HDR10+ Boost

- Not all devices in your chain support Dolby Vision.
- You share your media library with other family members that don't have Dolby Vision compatible devices.
- You have a (Samsung) TV that supports HDR10+.

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats-dv-web-hdr10plus-boost.md" !}

------

## FAQ & INFO

### Why only WEB-DL

??? faq "Why do you only have a release profile for WEB-DL - [CLICK TO EXPAND]"

    I only do WEB-DL my self for TV shows because in my opinion WEB-DL is the sweet spot between quality and size and you often don't see big differences anyway for TV shows. (Except for shows like GOT, Vikings, etc)

### Why prefer P2P groups

??? faq "Why do you prefer P2P groups over scene groups - [CLICK TO EXPAND]"

    Scene groups always release in a rush to bring it out as fast as possible.

    So I noticed often that I got Repacks/Proper releases from them or from different groups and quality. P2P releases are a bit smarter and work sort of together by not doing the same release. Also, I noticed that with some scene releases the 5.1 audio was stripped out or converted to AAC audio.

    In my opinion the P2P releases are of better quality. There's one scene group that does bring out quality releases `-deflate`/`-inflate`.

### Why so many repacks/propers

??? faq "Why do I see so many repacks/propers of Amazon WEB-DLs lately - [CLICK TO EXPAND]"

    A large portion of Amazon WEB-DLs in the last week have only had 192Kbps DD+5.1, because that's all Amazon made available initially. The proper 640Kbps DD+5.1 audio might appear a few hours later or a few months, but when they get updated, the episodes will be REPACKED.

### Proper and Repacks

??? tip "Proper and Repacks - [CLICK TO EXPAND]"

    I also suggest to change the Propers and Repacks settings in Sonarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Sonarr/sonarr-collection-of-custom-formats/#repackproper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Format preferences will be used instead.

### Custom Formats to avoid certain releases

??? FAQ "How to use a Custom Format to avoid certain releases? - [CLICK TO EXPAND]"

    For Custom Formats you really want to avoid, set it to something really low like `-10000` and not something like `-10`.
    Being when you add a Custom Format what you prefer and you set it to something like `+10` it could happen that for example the `BR-DISK` will be downloaded (-10)+(+10)=0 and if your `Minimum Custom Format Score` is set at `0`.

### Releases you should avoid

This is a must have for every Quality Profile you use in my opinion. All these Custom Formats make sure you don't get Low Quality Releases.

{! include-markdown "../../includes/cf/sonarr-unwanted.md" !}

### Custom Formats with a score of 0

??? FAQ "What do Custom Formats with a score of 0 do? - [CLICK TO EXPAND]"

    All Custom Formats with a score of 0 are pure informational and don't do anything.

### Minimum Custom Format Score

??? info "Minimum Custom Format Score - [CLICK TO EXPAND]"

    Some people suggest not to use negative scores for your Custom Formats and set this option to a higher score then 0.

    The reason why I don't prefer/use this is because you could limit yourself when some new groups or whatever will be released.

    Also it makes it much more clear what you prefer and what you want to avoid.

### Audio Channels

??? info "Audio Channels - [CLICK TO EXPAND]"

    Elsewhere in the guide, you will find a separate group of custom formats called `Audio Channels`. These will match the number of audio channels in a release, for example 2.0 (stereo) or 5.1/7.1 (surround sound). Personally I wouldn't add the audio channels Custom Formats as you could limit yourself in the amount of releases you're able to get. Only use them if you have a specific need for them.

    Using it with any kind of Remuxes Quality Profile is useless in my opinion being that 99% of all remuxes are multi audio anyway. You can get better scores just using the `Audio Advanced` Custom Formats.

### Avoid using the x264/x265 Custom Format

??? tip "Avoid using the x264/x265 Custom Format - [CLICK TO EXPAND]"

    Avoid using the x264/x265 Custom Format with a score if possible, it's smarter to use the [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} Custom Format.

    Something like 95% of video files are x264 and have much better direct play support. If you have more than a of couple users, you will notice much more transcoding.

    Use x265 only for 4k releases and the [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} makes sure you still get the x265 releases.

## Thanks

Special thanks to everyone that helped testing and creating these Custom Formats.

--8<-- "includes/support.md"
