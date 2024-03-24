# How to setup Quality Profiles French

!!! note "This guide is created and maintained by [Someone said "Nice"?](https://github.com/NiceTSY)"

!!! tip "Cette page est aussi disponible en Français: [Guide en Français](/Sonarr/sonarr-setup-quality-profiles-french-fr/){:target="_blank" rel="noopener noreferrer"}."

So what is the best way to set up the Custom Formats and which one to use with which scores to get French and English Audio?

Keep in mind that most releases are MULTi (understand DUAL audio, original and French audio) and it can be difficult to only have French audio, unless you are willing to get 720p, or you are only looking for French TVShows.

Regarding quality there isn't a best setup, it depends on your setup (hardware devices) and your own personal preferences.

Some prefer high quality audio (HD Audio), others high quality video. Many prefer both.

TRaSH created a [flowchart](/Sonarr/sonarr-setup-quality-profiles/#which-quality-profile-should-you-choose){:target="_blank" rel="noopener noreferrer"} to make your decision/choices easier. Remember that this chart does not include any of the following Custom Formats and you will still need to read this guide to get MULTi releases.

------

## Basics

It is quite important that you follow and understand what is envisioned by Trash's guide:

- Adding Custom Formats, as explained in [How to import Custom Formats](/Sonarr/sonarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
- Setting up a quality Profile to make use of the Custom Formats, as explained in [How to setup Quality Profiles | Basics section](/Sonarr/sonarr-setup-quality-profiles/#basics){:target="_blank" rel="noopener noreferrer"}.

------

## I am only interested in French subs (VOSTFR)

There is two options:

### Using TRaSH's guide and Bazarr

!!! tip "This is the preferred method."

- Set up Sonarr using [How to setup Quality Profiles | Which Quality Profile should you choose](/Sonarr/sonarr-setup-quality-profiles/#which-quality-profile-should-you-choose){:target="_blank" rel="noopener noreferrer"}.
- Set up [Bazarr](/Bazarr/Setup-Guide){:target="_blank" rel="noopener noreferrer"}. It will do an amazing job for getting your subtitle on every shows.
- Enjoy your shows with subs.
- (Optional) Add the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr){:target="_blank" rel="noopener noreferrer"} Custom Format with a score of `{{ sonarr['cf']['french-vostfr']['trash_scores']['french-vostfr'] }}`.

### Using the following examples and the VOSTFR Custom Format

- Continue to read this page.
- Ignore any mention of **MULTi Custom Formats**.
- Add the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr){:target="_blank" rel="noopener noreferrer"} Custom Format with a score of `{{ sonarr['cf']['french-vostfr']['trash_scores']['french-vostfr'] }}`.

------

## Usages

There is two ways of using those French Custom Formats, with and without the Guide's original Group tiers (which can be found there: [Collection of Custom Formats](/Sonarr/sonarr-collection-of-custom-formats/){:target="_blank" rel="noopener noreferrer"}).
To illustrate this, you will see an **"Original mix (optional)"** section in each of the examples below. You need to understand that if you add the Custom Formats from this optional section if Sonarr do not find a MULTi you will still have a good scoring for single audio.

!!! warning "Attention"
    If you use the **"Original mix (optional)"**. You need to understand that even if in the beginning the main focus of those French Custom Formats is to work alongside the original ones.
    You could end up with a single audio release when a MULTi release exists. This is because it was not scored high enough to trump the other scoring.

An example for Anime in MULTi/VOSTFR is also provided at the end: [Anime Example](#anime-example)

------

## Examples of Quality Profile

--8<-- "includes/cf/score-attention.md"

------

### French Audio Versions

Those are all optional and only there to rename your release or to prefer a certain type of French Audio. Examples:

- You prefer VFF (including VFI and VF2) audio, in this case you will put them at `101` instead of `0`.
- You only want VOSTFR, in this case you will ignore any mention of **MULTi Custom Formats** and give the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr) Custom Format a score of `{{ sonarr['cf']['french-vostfr']['trash_scores']['french-vostfr'] }}`.

!!! warning "Attention"
    It is not really recommended to put any of the VF Custom Formats (VFF, VFQ, VQ, VFB, VFI, VF2) to a negative score. Instead increase the score of your preferred audio.

{! include-markdown "../../includes/french-guide/sonarr-french-audio-version-en.md" !}

------

### French Speaking Streaming Services

Those are all optional and only there for information and does not have a score attached. This is due to the fact that few releases are tagged with them, so scoring them is difficult. Moreover, streaming services covered by TRaSH's guide are often of better quality than the following.

{! include-markdown "../../includes/french-guide/sonarr-french-streaming-services-en.md" !}

------

### TRaSH recommendations

{! include-markdown "../../includes/cf/sonarr-suggest-attention.md" !}

------

#### WEBDL-1080p

If you prefer 720p/1080p WEBDL (WEB-1080p)

{! include-markdown "../../includes/french-guide/sonarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/french-guide/sonarr-french-unwanted-en.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-streaming-services.md" !}

{! include-markdown "../../includes/french-guide/sonarr-cf-french-web-scoring-en.md" !}

`Audio Advanced` Custom Formats are not included to the WEB profile, as you will hardly find HD audio with WEB-DL (only newer WEBDL will have Atmos). If you also want HD audio formats it is suggested to go for the Remuxes.

Use the following main settings in your profile.

![!cf-profile-web1080](images/cf-profile-web1080.png)

!!! info ""

    For some older shows you might want to enable the `WEB 720p` or even the `HDTV 1080p`.

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

!!! example "The following workflow will be applied:"

    - It will download WEB-DL 1080p. (If you also enabled `WEB 720p` and/or `HDTV 1080p` it will upgrade till `Upgrade Until`)
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

------

#### WEBDL-2160p

If you prefer 2160p WEBDL (WEB-2160p)

The only deal breaker with 2160p is when you get them with DV/HDR, 2160p without DV/HDR is a minimal profit.

{! include-markdown "../../includes/cf/sonarr-all-hdr-formats.md" !}

{! include-markdown "../../includes/french-guide/sonarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/french-guide/sonarr-french-unwanted-uhd-en.md" !}

{! include-markdown "../../includes/cf/sonarr-optional-uhd.md" !}

{! include-markdown "../../includes/cf/sonarr-misc.md" !}

{! include-markdown "../../includes/cf/sonarr-uhd-streaming-services.md" !}

{! include-markdown "../../includes/french-guide/sonarr-cf-french-web-scoring-en.md" !}

Use the following main settings in your profile.

![!cf-profile-web2160](images/cf-profile-web2160.png)

!!! info ""

    The reason why WEB 1080p is merged with the 2160p is because some NF releases won't be released as 4k, but DV/HDR releases are still wanted.
    If you want to do the same make sure you replace [x265 (HD)](/Sonarr/sonarr-collection-of-custom-formats/#x265-hd){:target="_blank" rel="noopener noreferrer"} with [x265 (no HDR/DV)](/Sonarr/sonarr-collection-of-custom-formats/#x265-no-hdrdv){:target="_blank" rel="noopener noreferrer"}.

!!! example "The following workflow will be applied:"

    - It will download WEB-1080p with HDR/DV.
    - It will upgrade to WEB-2160p when available.
    - The downloaded media will be upgraded to any of the added Custom Formats until a score of 10000.

------

#### Anime Example

If you are looking to grab Anime with either French sub or MULTi audio (original + French).

{! include-markdown "../../includes/french-guide/sonarr-french-anime-info-en.md" !}

{! include-markdown "../../includes/french-guide/sonarr-french-multi-audio-en.md" !}

{! include-markdown "../../includes/french-guide/sonarr-french-unwanted-uhd-en.md" !}

{! include-markdown "../../includes/french-guide/sonarr-french-streaming-services-anime-en.md" !}

{! include-markdown "../../includes/french-guide/sonarr-cf-french-anime-scoring-en.md" !}

------

### HDR Formats

TRaSH provides great guides and explanations about them at the following links:

- [HDR Formats](/Sonarr/sonarr-setup-quality-profiles/#hdr-formats){:target="_blank" rel="noopener noreferrer"}

------

## FAQ & INFO

A FAQ regarding most of the questions you could have is provided by TRaSH: [FAQ & Info](/Sonarr/sonarr-setup-quality-profiles/#faq-info){:target="_blank" rel="noopener noreferrer"}

------

## Acknowledgements

- A big thanks to all the people that helped me to test those profiles and formats (and continue to do so).
- A special one to MySuperChef, PrL and KoUiGnAmAnN for their time and explanations.
- A special one to SeiyaGame, TheFrenchNaruto and Maxence which provided all of the Anime information.
- A special one to Piou and Wikoul who are potentially both now in asylums due to the amount of testing.
- [TRaSH](https://trash-guides.info/), for granting me a small space on his guide for this, his knowledge, and his friendliness.

--8<-- "includes/support.md"
