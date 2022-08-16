# How to setup Custom Formats

So what's the best way to setup the Custom Profiles and which one to use with which scores?

There isn't a best score setup, being that everyone has their own personal preferences. Some prefer high quality audio, others high quality video. Many prefer both.

Here I will try to explain with some personal used examples how to make the most use of Custom Formats that you can use to get an idea how to setup yours.

------

## Basics

Here we're going to explain where to setup the Custom Formats after you've added them, as explained in [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
You will also see a short description of what each setting means.

`Settings` => `Profiles`

??? check "example - [CLICK TO EXPAND]"
    ![!cf-settings-profiles](images/cf-settings-profiles.png)

Select the profile that you use/prefer.

![!cf-quality-profiles](images/cf-quality-profiles.png)

!!! info "Radarr Custom Formats can be set per profile and isn't global"

![!cf-profile-selected](images/cf-profile-selected.png)

1. Profile name.
1. Allow upgrades. Radarr will stop upgrading quality once (3) is met.
1. Upgrade until the selected quality.
1. The `Minimum Custom Format Score` allowed to download. [More Info](#minimum-custom-format-score)
1. Keep upgrading Custom Format until this score is reached. (setting this to `0` means no upgrades will happen based on Custom Formats)
1. Your preferred language profile for your releases. (Original is recommended)

At the bottom in your chosen profile you will see the added Custom Formats where you can start setting up the scores.

??? check "example - [CLICK TO EXPAND]"
    ![!cf-quality-profile-cf](images/cf-quality-profile-cf.png)

    !!! attention
        These screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

        - Always follow the data described in the guide.
        - If you got any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.

------

!!! attention
    Keep in mind Custom Formats are made to fine tune your Quality Profile

    Generally, quality trumps all

{! include-markdown "../../includes/merge-quality/radarr-current-logic.md" !}
<!-- --8<-- "includes/merge-quality/radarr-current-logic.md" -->

My suggestion is to create tiers of scores based on what things matter to you.

Personally, I would only add the Custom Formats that do what you actually prefer. Especially in the beginning, including the [Releases you should avoid](#releases-you-should-avoid)

!!! info

    Custom formats are controlled by Quality Profiles.

    - The Upgrade Until score prevents upgrading once a release with this desired score has been downloaded.
    - A score of 0 results in the custom format being informational only.
    - The Minimum score requires releases to reach this threshold otherwise they will be rejected.
    - Custom formats that match with undesirable attributes should be given a negative score to lower their appeal.
    - Outright rejections should be given a negative score low enough that even if all of the other formats with positive scores were added, the score would still fall below the minimum.

------

## Examples

Here I will explain how to make the most use of Custom Formats and show you some personal examples that I'm using. You can use these to get an idea on how to setup your own.

All these examples make use of the [Collection of Custom Formats](/Radarr/Radarr-collection-of-custom-formats/){:target="_blank" rel="noopener noreferrer"}

------

### Releases you should avoid

This is a must have for every Quality Profile you use in my opinion. All these Custom Formats make sure you don't get Low Quality Releases.

{! include-markdown "../../includes/cf/unwanted.md" !}
<!-- --8<-- "includes/cf/unwanted.md" -->

------

#### Prefer Advanced Audio

Lets say you prefer HD audio (with object metadata)

In this example I have lossy Atmos over lossless DTS because the object metadata matters more to me over lossy vs lossless.

{! include-markdown "../../includes/cf/audio.md" !}
<!-- --8<-- "includes/cf/audio.md" -->

------

#### Prefer HDR Metadata

Lets say you prefer HDR metadata

Then we would use the following order:

{! include-markdown "../../includes/cf/hdr-metadata.md" !}
<!-- --8<-- "includes/cf/hdr-metadata.md" -->

------

!!! important

    I also suggest to change the Propers and Repacks settings in Radarr!!!

    Instructions can be found [HERE](#proper-and-repacks)

------

#### Prefer HQ Encodes

If you prefer HQ Encodes (Bluray-720/1080/2160p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}. If you think the sizes are too big to your preference then stop reading and see if the other tutorials are helpful for you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

{! include-markdown "../../includes/cf/movie-versions.md" !}
<!-- --8<-- "includes/cf/movie-versions.md" -->

{! include-markdown "../../includes/cf/unwanted.md" !}
<!-- --8<-- "includes/cf/unwanted.md" -->

{! include-markdown "../../includes/cf/misc.md" !}
<!-- --8<-- "includes/cf/misc.md" -->

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                             | Score                                   | Trash ID                             |
    | ----------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------ |
    | [{{ radarr['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl) | {{ radarr['hq-webdl']['trash_score'] }} | {{ radarr['hq-webdl']['trash_id'] }} |
    | [{{ radarr['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux) | 0                                       | {{ radarr['hq-remux']['trash_id'] }} |
    | [{{ radarr['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)             | {{ radarr['hq']['trash_score'] }}       | {{ radarr['hq']['trash_id'] }}       |

I decided not to add `Audio Advanced` Custom Formats to the encodes profile, being with encodes I prefer higher video quality. If you also want HD audio formats I would suggest to go for the Remuxes.

Use the following main settings in your profile.

![!cf-profile-encodes](images/cf-profile-encodes.png)

!!! fail ""

    Make sure you don't check the BR-DISK. The reason why I didn't select the WEB-DL 720p is because you will hardly find any releases that aren't done as 1080p WEB-DL

??? example "The following workflow will be applied:"

    - It will download WEB-DL 1080p for the streaming movies you see more often lately.
    - It will upgrade till Bluray-1080p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

!!! tip

    If you prefer 2160/4K encodes you might consider to change `Upgrade Until Quality` to Bluray-2160p and enable:

    {! include-markdown "../../includes/cf/hdr-metadata.md" !}
    <!-- --8<-- "includes/cf/hdr-metadata.md" -->

------

#### Remux-1080p

If you prefer 1080p Remuxes (Remux-1080p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}
If you think the sizes are too big to your preference then stop reading and see if the other tutorials are helpful to you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

{! include-markdown "../../includes/cf/audio.md" !}
<!-- --8<-- "includes/cf/audio.md" -->

{! include-markdown "../../includes/cf/movie-versions.md" !}
<!-- --8<-- "includes/cf/movie-versions.md" -->

{! include-markdown "../../includes/cf/unwanted.md" !}
<!-- --8<-- "includes/cf/unwanted.md" -->

{! include-markdown "../../includes/cf/misc.md" !}
<!-- --8<-- "includes/cf/misc.md" -->

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                             | Score                                   | Trash ID                             |
    | ----------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------ |
    | [{{ radarr['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl) | {{ radarr['hq-webdl']['trash_score'] }} | {{ radarr['hq-webdl']['trash_id'] }} |
    | [{{ radarr['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux) | {{ radarr['hq-remux']['trash_score'] }} | {{ radarr['hq-remux']['trash_id'] }} |
    | [{{ radarr['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)             | 0                                       | {{ radarr['hq']['trash_id'] }}       |

Use the following main settings in your profile.

![!cf-profile-remux1080](images/cf-profile-remux1080.png)

!!! fail ""

    Make sure you don't check the BR-DISK. The reason why I didn't select the WEB-DL 720p is because you will hardly find any releases that aren't done as 1080p WEB-DL

??? example "The following workflow will be applied:"

    - It will download WEB-DL 1080p for the streaming movies you see more often lately.
    - It will upgrade till Remux-1080p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `500`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

------

#### Remux-2160p

If you prefer 2160p Remuxes (Remux-2160p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}
If you think the sizes are too big to your preference then stop reading and see if the other tutorials are helpful to you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

{! include-markdown "../../includes/cf/audio.md" !}
<!-- --8<-- "includes/cf/audio.md" -->

{! include-markdown "../../includes/cf/hdr-metadata.md" !}
<!-- --8<-- "includes/cf/hdr-metadata.md" -->

{! include-markdown "../../includes/cf/movie-versions.md" !}
<!-- --8<-- "includes/cf/movie-versions.md" -->

{! include-markdown "../../includes/cf/unwanted.md" !}
<!-- --8<-- "includes/cf/unwanted.md" -->

{! include-markdown "../../includes/cf/misc.md" !}
<!-- --8<-- "includes/cf/misc.md" -->

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                             | Score                                   | Trash ID                             |
    | ----------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------ |
    | [{{ radarr['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl) | {{ radarr['hq-webdl']['trash_score'] }} | {{ radarr['hq-webdl']['trash_id'] }} |
    | [{{ radarr['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux) | {{ radarr['hq-remux']['trash_score'] }} | {{ radarr['hq-remux']['trash_id'] }} |
    | [{{ radarr['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)             | 0                                       | {{ radarr['hq']['trash_id'] }}       |

Use the following main settings in your profile.

![!cf-profile-remux2160](images/cf-profile-remux2160.png)

!!! fail ""

    Make sure you don't check the BR-DISK.

??? example "The following workflow will be applied:"

    - It will download WEB-DL 2160p for the streaming movies you see more often lately.
    - It will upgrade to Remux-2160p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `500`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

------

## FAQ & INFO

### Proper and Repacks

??? tip "Proper and Repacks - [CLICK TO EXPAND]"

    I also suggest to change the Propers and Repacks settings in Radarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Radarr/Radarr-collection-of-custom-formats/#repack-proper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Format preferences will be used instead.

### Custom Formats to avoid certain releases

??? FAQ "How to use a Custom Format to avoid certain releases? - [CLICK TO EXPAND]"

    For Custom Formats you really want to avoid, set it to something really low like `-10000` and not something like `-10`.
    Being when you add a Custom Format what you prefer and you set it to something like `+10` it could happen that for example the `BR-DISK` will be downloaded (-10)+(+10)=0 and if your `Minimum Custom Format Score` is set at `0`.

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

    Personally I wouldn't add the audio channels Custom Formats being you could limit yourself in the amount of releases you're able to get. Only use this if you got specific reasons that you need them.

    Using it with any kind of Remuxes Quality Profile is useless in my opinion being that 99% of all remuxes are multi audio anyway. You can get better scores using the `Audio Advanced` Custom Formats.

### Avoid using the x264/x265 Custom Format

??? tip "Avoid using the x264/x265 Custom Format - [CLICK TO EXPAND]"

    Avoid using the x264/x265 Custom Format with a score if possible, it's smarter to use the [720/1080p no x265](/Radarr/Radarr-collection-of-custom-formats/#x265-7201080p){:target="_blank" rel="noopener noreferrer"} Custom Format.

    Something like 95% of video files are x264 and have much better direct play support. If you have more than a of couple users, you will notice much more transcoding.

    Use x265 only for 4k releases and the [720/1080p no x265](/Radarr/Radarr-collection-of-custom-formats/#x265-7201080p){:target="_blank" rel="noopener noreferrer"} makes sure you still get the x265 releases.

## Thanks

A big Thanks to [rg9400](https://github.com/rg9400) for providing me with info needed to create the Tips section.

{! include-markdown "../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
