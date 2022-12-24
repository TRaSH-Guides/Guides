# How to setup Quality Profiles French

*aka How to setup Custom Formats (French)*<br><br>

!!! note "This guide is created and maintained by [Someone said "Nice"?](https://github.com/NiceTSY)"

!!! tip "Cette page est aussi disponible en Français: [Guide en Français](/Radarr/radarr-setup-quality-profiles-french-fr/){:target="_blank" rel="noopener noreferrer"}."

So what is the best way to set up the Custom Formats and which one to use with which scores to get French and English Audio?

Keep in mind that most releases are MULTi (understand DUAL audio, original and French audio) and it will be difficult to only have French audio, unless you are willing to get 720p, or you are only looking for French movies.

Regarding quality there isn't a best setup, it depends on your setup (hardware devices) and your own personal preferences.

Some prefer high quality audio (HD Audio), others high quality video. Many prefer both.

TRaSH created a [flowchart](/Radarr/Radarr-setup-custom-formats/#which-quality-profile-should-you-choose){:target="_blank" rel="noopener noreferrer"} to make your decision/choices easier. Remember that this chart does not include any of the following Custom Formats and you will still need to read this guide to get MULTi releases.

------

## Basics

It is quite important that you follow and understand what is envisioned by Trash's guide:

- Adding Custom Formats, as explained in [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
- Setting up a quality Profile to make use of the Custom Formats, as explained in [How to setup Quality Profiles | Basics section](/Radarr/radarr-setup-quality-profiles/#basics){:target="_blank" rel="noopener noreferrer"}.

------

!!! warning "Mandatory"

    The only change that is needed and **mandatory** for French Custom Formats to work is to set the preferred language profile for your releases to `Any`.

    ??? check "Screenshot example - [CLICK TO EXPAND]"
        ![!cf-quality-profile-cf](images/french-cf-profile-language.png)

    !!! info
        We do choose `Any` for the language profile, as otherwise an English movie identified with French audio in Radarr will not be grabbed and vice-versa.

------

## I am only interested in French subs (VOSTFR)

There is two options:

### Using TRaSH's guide and Bazarr

!!! tip "This is the preferred method."

- Set up Radarr using [How to setup Quality Profiles | Which Quality Profile should you choose](/Radarr/radarr-setup-quality-profiles/#which-quality-profile-should-you-choose).
- Set up [Bazarr](/Bazarr/Setup-Guide). It will do an amazing job for getting your subtitle on every movies.
- Enjoy your movies with subs.
- (Optional) Add the [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) Custom Format with a score of `1000`.

### Using the following examples and the VOSTFR Custom Format

- Continue to read this page.
- Ignore any mention of **MULTi Custom Formats**.
- Add the [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) Custom Format with a score of `1000`.

------

## Usages

There is two ways of using those French Custom Formats, with and without the Guide's original Group tiers (which can be found there: [Collection of Custom Formats](/Radarr/Radarr-collection-of-custom-formats/){:target="_blank" rel="noopener noreferrer"}).
To illustrate this, you will see an **"Original mix (optional)"** section in each of the examples below. You need to understand that if you add the Custom Formats from this optional section if Radarr do not find a MULTi you will still have a good scoring for single audio.

!!! warning "Attention"
    If you use the **"Original mix (optional)"**. You need to understand that even if in the beginning the main focus of those French Custom Formats is to work alongside the original ones.
    You could end up with a single audio release when a MULTi release exists. This is because it was not scored high enough to trump the other scoring.

------

## Examples of Quality Profile

--8<-- "includes/cf/score-attention.md"

------

### French Audio Versions

Those are all optional and only there to rename your release or to avoid a certain type of French Audio. Examples:

- You do not want VFQ or VQ audio, in this case you will put them at `-10000` instead of `0`.
- You only want VOSTFR, in this case you will ignore any mention of **MULTi Custom Formats** and give the [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) Custom Format a score of `1000`.

{! include-markdown "../../includes/french-guide/radarr-french-audio-version-en.md" !}

------

### Releases you should avoid

This is a must-have for every Quality Profile you use. All these Custom Formats make sure you don't get Low Quality Releases.

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-en.md" !}

------

### TRaSH recommendations

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

------

#### HD Bluray + WEB

If you prefer High Quality HD Encodes (Bluray-720/1080p)

- *Size: 6-15 GB for a Bluray-1080p depending on the running time.*

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-cf-french-hd-bluray-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

`Audio Advanced` Custom Formats are not included to the encodes profile, as you will hardly find HD audio with HD Bluray Encodes. With HD Bluray Encodes it is suggested to go for quality. If you also want HD audio formats you should go for the Remuxes or UHD Encodes.

Use the following main settings in your profile.

![HD Bluray + WEB](images/french-qp-bluray-webdl.png)

!!! attention "Make sure you don't check the BR-DISK."

The reason why WEB-DL 720p is not selected is because you will hardly find any releases that aren't done as 1080p WEB-DL.

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? summary "Workflow Logic - [CLICK TO EXPAND]"

    - When the WEB-1080p is released it will download the WEB-1080p. (streaming services)
    - When the Bluray-1080p is released it will upgrade to the Bluray-1080p.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of `10000`.

------

#### UHD Bluray + WEB

If you prefer High Quality UHD Encodes (Bluray-2160p)

- *Size: 20-60 GB for a Bluray-2160p depending on the running time.*

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-en.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-hdr-formats.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-cf-french-uhd-bluray-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

Use the following main settings in your profile.

![UHD Bluray + WEB](images/french-qp-uhd-bluray-webdl.png)

!!! attention "Make sure you don't check the BR-DISK."

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? summary "Workflow Logic - [CLICK TO EXPAND]"

    **Depending what's released first and available the following Workflow Logic will be used:**

    - When the WEB-2160p is released it will download the WEB-2160p. (streaming services)
    - When the Bluray-2160p is released it will upgrade to the Bluray-2160p.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of `10000`.

------

#### Remux + WEB 1080p

If you prefer 1080p Remuxes (Remux-1080p)

- *Size: 20-40 GB for a Remux-1080p depending on the running time.*

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-en.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-cf-french-remux-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

Use the following main settings in your profile.

![Remux + WEB 1080p](images/french-qp-remux-webdl-1080p.png)

!!! attention "Make sure you don't check the BR-DISK."

The reason why I didn't select the WEB-DL 720p is because you will hardly find any releases that aren't done as 1080p WEB-DL.

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? summary "Workflow Logic - [CLICK TO EXPAND]"

    - When the WEB-1080p is released it will download the WEB-1080p. (streaming services)
    - When the REMUX-1080p is released it will upgrade to the REMUX-1080p.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of `10000`.

------

#### Remux + WEB 2160p

If you prefer 2160p Remuxes (Remux-2160p)

- *Size: 40-100 GB for a Remux-2160p depending on the running time.*

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-en.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-hdr-formats.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions.md" !}

{! include-markdown "../../includes/french-guide/radarr-cf-french-remux-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-misc.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

Use the following main settings in your profile.

![Remux + WEB 2160p](images/french-qp-remux-webdl-2160p.png)

!!! attention "Make sure you don't check the BR-DISK."

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

??? summary "Workflow Logic - [CLICK TO EXPAND]"

    - When the WEB-2160p is released it will download the WEB-2160p. (streaming services)
    - When the REMUX-2160p is released it will upgrade to the REMUX-2160p.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of `10000`.

------

### Advanced Audio and HDR Formats

TRaSH provides great guides and explanations about them at the following links:

- [Advanced Audio](/Radarr/radarr-setup-quality-profiles/#advanced-audio){:target="_blank" rel="noopener noreferrer"}
- [HDR Formats](/Radarr/radarr-setup-quality-profiles/#hdr-formats){:target="_blank" rel="noopener noreferrer"}
- [HDR Formats + DV (WEBDL)](/Radarr/radarr-setup-quality-profiles/#hdr-formats-dv-webdl){:target="_blank" rel="noopener noreferrer"}
- [HDR Formats + DV (WEBDL) + HDR10+ Boost](/Radarr/radarr-setup-quality-profiles/#hdr-formats-dv-webdl-hdr10-boost){:target="_blank" rel="noopener noreferrer"}

------

## Acknowledgements

- A big thanks to all the people that helped me to test those profiles and formats (and continue to do so).
- A special one to MySuperChef and PrL for their time and explanations.
- A special one to Piou and Wikoul who are potentially both now in asylums due to the amount of testing.
- [TRaSH](https://trash-guides.info/), for granting me a small space on his guide for this, his knowledge, and his friendliness.

--8<-- "includes/support.md"
