# How to setup Custom Formats (French)

So what's the best way to setup the Custom Profiles and which one to use with which scores to get French and English Audio?

Keep in mind that most releases are MULTi (understand DUAL audio, original and French audio) and it will be difficult to only have French audio, unless you are willing to get 720p or you are only looking for French movies.

Therefore you will need a slightly modified MULTi Custom Format than the one find in the original guide. This one also recognise VO and VFF in the name and rename the import. This is important for the score to match before and after the import and to avoid download loop.

--8<-- "includes/cf/score-attention.md"

------

## Basics

------

!!! attention

    This section seems quite similar to the original guide but few information change and are needed for profiles to work. Please be sure you read it thoughtfully.

------

After you've added the Custom Formats, as explained in [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
You will need to set it up in the quality Profile you want to use/prefer to make use of the Custom Formats.

`Settings` => `Profiles`

![!cf-settings-profiles](images/cf-settings-profiles.png)

!!! info "Radarr Custom Formats can be set per profile and isn't global"
Select the profile that you want to use/prefer.

![!cf-quality-profiles](images/cf-quality-profiles.png)

![!cf-profile-selected](images/cf-profile-selected.png)

1. Profile name.
1. Allow upgrades. Radarr will stop upgrading quality once (3) is met.
1. Upgrade until the selected quality.
1. The `Minimum Custom Format Score` allowed to download. [More Info](#minimum-custom-format-score)
1. Keep upgrading Custom Format until this score is reached. (setting this to `0` means no upgrades will happen based on Custom Formats)
1. Your preferred language profile for your releases, choose `Any`

!!! info "We do choose `Any` for the language profile as otherwise an English movies recognised with French audio in Radarr will not be grabbed and vice-versa."

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

{! include-markdown "../../includes/merge-quality/radarr-current-logic.md" !}

------

## MULTi Custom Format

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

------

## I am only interested in VOSTFR!

My strongest suggestion will be for you to look at Bazarr. It will do an amazing job for getting your subtitle on every movies. An other option is to disregard the MULTi part and just add the [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) with a strong score.

------

## Examples

Here I will explain how to make the most use of the French Custom Formats and show you some personal examples that I'm using. You can use these to get an idea on how to setup your own.

All these examples make use of the [Collection of Custom Formats](/Radarr/Radarr-collection-of-custom-formats/){:target="_blank" rel="noopener noreferrer"} from the original guide and mix them with the French Custom Formats.

!!! attention "Attention"
    Those examples use the original guide Custom Formats too for fallback. Meaning that if you do not find a MULTi you will still have a good scoring for single audio.

    This is the first intent of those Custom Formats. However, they can work alone and you can safely not add the original Custom Formats.

--8<-- "includes/cf/score-attention.md"

------

### French Audio Versions

Those are all optional and only there to rename your release or to avoid a certain type of French Audio (e.g. you do not want VFQ or VQ audio, in this case you will put them at `-10000` instead of `0`).

{! include-markdown "../../includes/french-guide/radarr-french-audio-version.md" !}

------

### Releases you should avoid

This is a must have for every Quality Profile you use in my opinion. All these Custom Formats make sure you don't get Low Quality Releases.

{! include-markdown "../../includes/french-guide/radarr-french-unwanted.md" !}

------

#### Prefer HQ Encodes

If you prefer HQ Encodes (Bluray-720/1080/2160p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}. If you think the sizes are too big to your preference then stop reading and see if the other tutorials are helpful for you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                                                                        | Score                                                                          | Trash ID                                                                    |
    | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
    | [{{ radarr['cf']['french-hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq-webdl)  | {{ radarr['cf']['french-hq-webdl']['trash_score'] }} | {{ radarr['cf']['french-hq-webdl']['trash_id'] }} |
    | [{{ radarr['cf']['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl)                                      | {{ radarr['cf']['hq-webdl']['trash_score'] }}                                  | {{ radarr['cf']['hq-webdl']['trash_id'] }}                                  |
    | [{{ radarr['cf']['french-hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq-remux)  | 0                                                                              | {{ radarr['cf']['french-hq-remux']['trash_id'] }} |
    | [{{ radarr['cf']['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux)                                      | 0                                                                              | {{ radarr['cf']['hq-remux']['trash_id'] }}                                  |
    | [{{ radarr['cf']['french-hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq)              | {{ radarr['cf']['french-hq']['trash_score'] }}       | {{ radarr['cf']['french-hq']['trash_id'] }}       |
    | [{{ radarr['cf']['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)                                                  | {{ radarr['cf']['hq']['trash_score'] }}                                        | {{ radarr['cf']['hq']['trash_id'] }}                                        |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups) | ??????                                                                         | {{ radarr['cf']['french-scene']['trash_id'] }}    |

    !!! info "French Scene groups are included as a fallback if you really want MULTi release despite quality. Either score the CF to `{{ radarr['cf']['french-scene']['trash_score'] }}` or `0` depending on what you want to achieve."

I decided not to add `Audio Advanced` Custom Formats to the encodes profile, being with encodes I prefer higher video quality. If you also want HD audio formats I would suggest to go for the Remuxes.

Use the following main settings in your profile.

![!cf-profile-encodes](images/cf-profile-encodes.png)

!!! attention "Make sure you don't check the BR-DISK."

The reason why I didn't select the WEB-DL 720p is because you will hardly find any releases that aren't done as 1080p WEB-DL.

??? example "The following workflow will be applied:"

    - It will try to download MULTi release first, and fallback to best quality single audio after.
    - It will download WEB-DL 1080p for the streaming movies you see more often lately.
    - It will upgrade till Bluray-1080p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 9999.

    So why such a ridiculously high `Upgrade Until Custom` and not a score of `100`?

    Because I'm too lazy to calculate the maximum for every Quality Profile I use, and I want it to upgrade to the highest possible score anyway.

!!! tip

    If you prefer 2160/4K encodes you might consider to change `Upgrade Until Quality` to Bluray-2160p and enable:

    {! include-markdown "../../includes/cf/radarr-hdr-formats.md" !}

------

#### Remux-1080p

If you prefer 1080p Remuxes (Remux-1080p)

I suggest to first follow the [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="_blank" rel="noopener noreferrer"}
If you think the sizes are too big to your preference then stop reading and see if the other tutorials are helpful to you. :bangbang:

For this Quality Profile we're going to make use of the following Custom Formats

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                                                                        | Score                                                                          | Trash ID                                                                    |
    | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
    | [{{ radarr['cf']['french-hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq-webdl)  | {{ radarr['cf']['french-hq-webdl']['trash_score'] }} | {{ radarr['cf']['french-hq-webdl']['trash_id'] }} |
    | [{{ radarr['cf']['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl)                                      | {{ radarr['cf']['hq-webdl']['trash_score'] }}                                  | {{ radarr['cf']['hq-webdl']['trash_id'] }}                                  |
    | [{{ radarr['cf']['french-hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq-remux)  | {{ radarr['cf']['french-hq-remux']['trash_score'] }} | {{ radarr['cf']['french-hq-remux']['trash_id'] }} |
    | [{{ radarr['cf']['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux)                                      | {{ radarr['cf']['hq-remux']['trash_score'] }}                                  | {{ radarr['cf']['hq-remux']['trash_id'] }}                                  |
    | [{{ radarr['cf']['french-hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq)              | 0                                                                              | {{ radarr['cf']['french-hq']['trash_id'] }}       |
    | [{{ radarr['cf']['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)                                                  | 0                                                                              | {{ radarr['cf']['hq']['trash_id'] }}                                        |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups) | ??????                                                                         | {{ radarr['cf']['french-scene']['trash_id'] }}    |

    !!! info "French Scene groups are included as a fallback if you really want MULTi release despite quality. Either score the CF to `{{ radarr['cf']['french-scene']['trash_score'] }}` or `0` depending on what you want to achieve."

Use the following main settings in your profile.

![!cf-profile-remux1080](images/cf-profile-remux1080.png)

!!! attention "Make sure you don't check the BR-DISK."

The reason why I didn't select the WEB-DL 720p is because you will hardly find any releases that aren't done as 1080p WEB-DL.

??? example "The following workflow will be applied:"

    - It will try to download MULTi release first, and fallback to best quality single audio after.
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

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-hdr-formats.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                                                                        | Score                                                                          | Trash ID                                                                    |
    | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
    | [{{ radarr['cf']['french-hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq-webdl)  | {{ radarr['cf']['french-hq-webdl']['trash_score'] }} | {{ radarr['cf']['french-hq-webdl']['trash_id'] }} |
    | [{{ radarr['cf']['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl)                                      | {{ radarr['cf']['hq-webdl']['trash_score'] }}                                  | {{ radarr['cf']['hq-webdl']['trash_id'] }}                                  |
    | [{{ radarr['cf']['french-hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq-remux)  | {{ radarr['cf']['french-hq-remux']['trash_score'] }} | {{ radarr['cf']['french-hq-remux']['trash_id'] }} |
    | [{{ radarr['cf']['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux)                                      | {{ radarr['cf']['hq-remux']['trash_score'] }}                                  | {{ radarr['cf']['hq-remux']['trash_id'] }}                                  |
    | [{{ radarr['cf']['french-hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-hq)              | 0                                                                              | {{ radarr['cf']['french-hq']['trash_id'] }}       |
    | [{{ radarr['cf']['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)                                                  | 0                                                                              | {{ radarr['cf']['hq']['trash_id'] }}                                        |
    | [{{ radarr['cf']['french-scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-scene-groups) | ??????                                                                         | {{ radarr['cf']['french-scene']['trash_id'] }}    |

    !!! info "French Scene groups are included as a fallback if you really want MULTi release despite quality. Either score the CF to `{{ radarr['cf']['french-scene']['trash_score'] }}` or `0` depending on what you want to achieve."

Use the following main settings in your profile.

![!cf-profile-remux2160](images/cf-profile-remux2160.png)

!!! attention "Make sure you don't check the BR-DISK."

??? example "The following workflow will be applied:"

    - It will try to download MULTi release first, and fallback to best quality single audio after.
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

    Avoid using the x264/x265 Custom Format with a score if possible, it's smarter to use the [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} Custom Format.

    Something like 95% of video files are x264 and have much better direct play support. If you have more than a of couple users, you will notice much more transcoding.

    Use x265 only for 4k releases and the [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} makes sure you still get the x265 releases.

## Thanks

A big Thanks to [rg9400](https://github.com/rg9400) for providing me with info needed to create the Tips section.

--8<-- "includes/support.md"
