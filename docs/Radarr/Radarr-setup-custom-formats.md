# How to setup Custom Formats

So what's the best way to setup the Custom Profiles and which one to use with which scores?

There isn't a best scores setup, being that everyone has its own personal preference what they prefer Audio or Video or perhaps both.

But being I still get a lot of questions about it I decided to create a Guide for it.

Here I will try to explain with some personal used examples how to make the most use of Custom Formats. That you can use to get a idea how to setup yours.

------

## Basics

First the basics where we going to explain where to setup the Custom Formats after you've added them, what we've explained in [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
And a short description what the settings means.

`Settings` => `Profiles`

??? check "example - [CLICK TO EXPAND]"
    ![!cf-settings-profiles](images/cf-settings-profiles.png)

Then select the profile that you use/prefer.

![!cf-quality-profiles](images/cf-quality-profiles.png)

!!! info "Radarr Custom Format can be set per profile and isn't global"

![!cf-profile-selected](images/cf-profile-selected.png)

1. Profile name.
1. If you want that Radarr will upgrade till the quality set in (3.).
1. Upgrade till the selected Quality.
1. The `Minimum Custom Format Score` allowed to download. [More Info](#minimum-custom-format-score)
1. Keep upgrading Custom Format till this score is reached. (setting this to `0` means no upgrades will happen based on Custom Formats)
1. Your preferred language profile for your Releases.

In your chosen profile at the bottom you will see the added Custom Profiles where you can start setting up the scores.

??? check "example - [CLICK TO EXPAND]"
    ![!cf-quality-profile-cf](images/cf-quality-profile-cf.png)

    !!! attention
        These screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

        - Always follow the data described in the guide.
        - If you got any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.

------

!!! attention
    Keep in mind Custom Formats are made to fine tune your Quality Profile

    Generally Quality Trumps All

--8<-- "includes/merge-quality/radarr-current-logic.md"

My suggestion is to create tiers of scores based on what things matter to you.

Personally I would only add the Custom Formats that do what you actually prefer especially in the beginning, including the [Releases you should avoid](#releases-you-should-avoid)

!!! info

    Custom formats are implemented within and have their impact controlled by Quality Profiles.

    - The Upgrade Until score prevents upgrading once a release with this desired score has been downloaded.
    - A score of 0 results in the custom format being informational only.
    - The Minimum score requires releases to reach this threshold otherwise they will be rejected.
    - Custom formats that match with undesirable attributes should be given a negative score to lower their appeal.
    - Outright rejections should be given a negative score low enough that even if all of the other formats with positive scores were added, the score would still fall below the minimum.

------

## Examples

Here I will show how to make the most use of Custom Formats and show some personal examples that I'm using. That you can use to get a idea how to setup yours.

All these examples make use of the [Collection of Custom Formats](/Radarr/Radarr-collection-of-custom-formats/){:target="_blank" rel="noopener noreferrer"}

------

### Releases you should avoid

In my opinion this is a must for every Quality Profile you use, all these Custom Formats make sure you don't get Low Quality Releases.

--8<-- "includes/cf/unwanted.md"

------

#### Prefer Advanced Audio

Lets say you prefer HD audio (with object metadata)

In this example I have lossy Atmos over lossless DTS because the object metadata matters more to me over lossy vs lossless

--8<-- "includes/cf/audio.md"

------

#### Prefer HDR Metadata

Lets say you prefer HDR metadata

Then we would use the following order.

--8<-- "includes/cf/hdr-metadata.md"

------

!!! important

    I also suggest to change the Propers and Repacks settings in Radarr !!!

    Instructions can be found [HERE](#proper-and-repacks)

------

#### Prefer HQ Encodes

If you prefer HQ Encodes (Bluray-720/1080/2160p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}
If you think the sizes are to big to your preference then stop reading and see if the other tutorials are helpful for you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

--8<-- "includes/cf/movie-versions.md"

--8<-- "includes/cf/unwanted.md"

--8<-- "includes/cf/misc.md"

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format        | Score | LINK |
    | -------------------- | ----- | ---- |
    | HQ-WEBDL             | 1750  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ-Remux             |    0  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-remux){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ                   | 1800  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq){: .header-icons target=_blank rel="noopener noreferrer" } |

I decided not to add `Audio Advanced` Custom Formats to the encodes profile being with encodes I prefer higher video quality, If you also want HD audio formats I would suggest to go for the Remuxes.

Use the following main settings in your profile.

![!cf-profile-encodes](images/cf-profile-encodes.png)

!!! fail ""

    Make sure you don't check the BR-DISK, The reason why I didn't select the WEB-DL 720p is because you will find hardly any releases that aren't done as 1080p WEB-DL

??? example "The following workflow will be applied:"

    - It will download WEB-DL 1080p for the streaming movies you see more often lately.
    - It will upgrade till Bluray-1080p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats till a score of 9999.

    So why such a ridiculous high `Upgrade Until Custom` and not a score of `100` ?

    Because I'm to lazy to calculate the maximum for every of my used Quality Profile and I want it to upgrade to the highest as possible anyway.

!!! tip

    If you prefer 2160/4K encodes you might consider to change `Upgrade Until Quality` to Bluray-2160p and enable:

    --8<-- "includes/cf/hdr-metadata.md"

------

#### Remux-1080p

If you prefer 1080p Remuxes (Remux-1080p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}
If you think the sizes are to big to your preference then stop reading and see if the other tutorials are helpful for you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

--8<-- "includes/cf/audio.md"

--8<-- "includes/cf/movie-versions.md"

--8<-- "includes/cf/unwanted.md"

--8<-- "includes/cf/misc.md"

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format        | Score | LINK |
    | -------------------- | ----- | ---- |
    | HQ-WEBDL             | 1750  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ-Remux             | 1900  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-remux){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ                   |    0  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq){: .header-icons target=_blank rel="noopener noreferrer" } |

Use the following main settings in your profile.

![!cf-profile-remux1080](images/cf-profile-remux1080.png)

!!! fail ""

    Make sure you don't check the BR-DISK, The reason why I didn't select the WEB-DL 720p is because you will find hardly any releases that aren't done as 1080p WEB-DL

??? example "The following workflow will be applied:"

    - It will download WEB-DL 1080p for the streaming movies you see more often lately.
    - It will upgrade till Remux-1080p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats till a score of 9999.

    So why such a ridiculous high `Upgrade Until Custom` and not a score of `500` ?

    Because I'm to lazy to calculate the maximum for every of my used Quality Profile and I want it to upgrade to the highest as possible anyway.

------

#### Remux-2160p

If you prefer 2160p Remuxes (Remux-2160p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}
If you think the sizes are to big to your preference then stop reading and see if the other tutorials are helpful for you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

--8<-- "includes/cf/audio.md"

--8<-- "includes/cf/hdr-metadata.md"

--8<-- "includes/cf/movie-versions.md"

--8<-- "includes/cf/unwanted.md"

--8<-- "includes/cf/misc.md"

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format        | Score | LINK |
    | -------------------- | ----- | ---- |
    | HQ-WEBDL             | 1750  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ-Remux             | 1900  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-remux){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ                   |    0  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq){: .header-icons target=_blank rel="noopener noreferrer" } |

Use the following main settings in your profile.

![!cf-profile-remux2160](images/cf-profile-remux2160.png)

!!! fail ""

    Make sure you don't check the BR-DISK.

??? example "The following workflow will be applied:"

    - It will download WEB-DL 2160p for the streaming movies you see more often lately.
    - It will upgrade till Remux-2160p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats till a score of 9999.

    So why such a ridiculous high `Upgrade Until Custom` and not a score of `500` ?

    Because I'm to lazy to calculate the maximum for every of my used Quality Profile and I want it to upgrade to the highest as possible anyway.

------

## FAQ & INFO

### Proper and Repacks

??? tip "Proper and Repacks - [CLICK TO EXPAND]"

    I also suggest to change the Propers and Repacks settings in Radarr

    `Media Management` => `File Management` to `Do Not Prefer` and use the [Repack/Proper](/Radarr/Radarr-collection-of-custom-formats/#repack-proper) Custom Format.

    ![!cf-mm-propers-repacks-disable](images/cf-mm-propers-repacks-disable.png)

    This way you make sure the Custom Formats preferences will be used and not ignored.

### Custom Formats to avoid certain releases

??? FAQ "How to use a Custom Formats to avoid certain releases? - [CLICK TO EXPAND]"

    For Custom Formats you really want to avoid, set it to something really low like `-10000` and not something like `-10`.
    Being when you add a Custom Format what you prefer and you set it to something like `+10` it could happen that for example the `BR-DISK` will be downloaded (-10)+(+10)=0 and if your `Minimum Custom Format Score` is set at `0`.

### Custom Formats with a score of 0

??? FAQ "What do Custom Formats with a score of 0 do? - [CLICK TO EXPAND]"

    All Custom Formats with a score of 0 are pure informational and don't do anything.

### Minimum Custom Format Score

??? info "Minimum Custom Format Score - [CLICK TO EXPAND]"

    Some people suggest not to use minus score for your Custom Formats and set this option to a higher score then 0.

    The reason why I don't prefer/use this is because you could limit your self when some new groups or what ever will be released.

    Also it makes it much more clear what you prefer and what you want to avoid.

### Audio Channels

??? info "Audio Channels - [CLICK TO EXPAND]"

    Personally I wouldn't add the audio channels Custom Formats being you could limit your self in the amount of releases you're able to get. Only use this if you got specific reasons that you need them.

    Using it with any kind of Remuxes Quality Profile is useless in my opinion being that 99% of all remuxes are multi audio anyway. and you can better score using the `Audio Advanced` Custom Formats

### Avoid using the x264/x265 Custom Format

??? tip "Avoid using the x264/x265 Custom Format - [CLICK TO EXPAND]"

    If possible avoid using the x264/x265 Custom Format with a score, it's smarter to use the [720/1080p no x265](/Radarr/Radarr-collection-of-custom-formats/#x265-7201080p){:target="_blank" rel="noopener noreferrer"} Custom Format.

    Something like 95% of video files are x264 and have much better direct play support. If you have more than a couple users, you will notice much more transcoding.

    Use x265 only for 4k releases and the [720/1080p no x265](/Radarr/Radarr-collection-of-custom-formats/#x265-7201080p){:target="_blank" rel="noopener noreferrer"} makes sure you still can get the x265 releases.

## Thanks

A big Thanks to [rg9400](https://github.com/rg9400) for providing me with info needed to create the Tips section.

--8<-- "includes/support.md"
