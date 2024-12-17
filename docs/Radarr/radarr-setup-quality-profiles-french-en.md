# How to set up Quality Profiles (French)

*aka How to Set Up Custom Formats to Get French Audio and/or Subs*<br><br>

!!! note "This guide is created and maintained by [Someone Said "Nice"?](https://github.com/NiceTSY)"

!!! tip "Cette page est aussi disponible en Français : [Guide en Français](/Radarr/radarr-setup-quality-profiles-french-fr/){:target="\_blank" rel="noopener noreferrer"}."

---

## Basics

It is quite important that you follow and understand what is envisioned by TRaSH's guide:

- Adding Custom Formats, as explained in [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
- Setting up a quality Profile to make use of the Custom Formats, as explained in [How to setup Quality Profiles | Basics section](/Radarr/radarr-setup-quality-profiles/#basics){:target="_blank" rel="noopener noreferrer"}.

!!! warning "Please read those two sections before continuing the guide as they hold important information. The rest of this guide will assume you did."

!!! tip
    TRaSH created a [flowchart](/Radarr/Radarr-setup-custom-formats/#which-quality-profile-should-you-choose){:target="\_blank" rel="noopener noreferrer"} to make your decision easier. Remember that this chart does not include any of the following Custom Formats, and you will still need to read this guide to get MULTi releases.

---

## FAQ

!!! info "I am not French from France but from Canada, does the guide still work?"
    Yes, the guide does accommodate for all types of French: VFF, VFQ, and VFB (even though this one is quite rare). Just make sure you check the scoring of the [French Audio Versions](#french-audio-versions) section.

!!! info "I am only interested in getting French subs (VOSTFR)"
    Please follow the **Want Original with subs** (**VOSTFR**) profile.

!!! info "Can I get HDLight or 4KLight?"
    Probably not, this guide is not geared toward these specific types. If space is an issue for you, prefer Web-DL or 720p Blu-ray releases.

!!! info "FlareSolverr?"
    Please refer to the [How to set up FlareSolverr](/Prowlarr/prowlarr-setup-flaresolverr/){:target="\_blank" rel="noopener noreferrer"} section.

---

## Prowlarr specific settings

!!! abstract "Indexers - Replace MULTi by another language in release name option"
    Prowlarr allows MULTi to be replaced by another language. This option is great in theory but will lead to false positives regarding the French audio CFs.
    Please prefer using the Radarr-specific settings "Indexers - Multi Languages option" below.

!!! abstract "Indexers - Replace VOSTFR and SUBFRENCH with ENGLISH option"
    This option should not be used, mostly because you lose some information regarding the release.
    Moreover, `VOSTFR` does not mean that the audio is in `English` but rather it is the `Original` audio, meaning it could be `Spanish`, `Korean`, etc.

!!! abstract "Indexers - Replace VFQ with FRENCH"
    Same as for the MULTi option, this will lead to false positives regarding the French audio CFs. Keep it disabled.

??? success "Screenshot example - [Click to show/hide]"
    ![French Prowlarr specific settings](images/french-prowlarr-settings.png)

---

## Radarr specific settings

!!! abstract "Media Management - Standard Movie Format and Movie Folder Format"
    Please have a look there: [Recommended naming scheme](/Radarr/Radarr-recommended-naming-scheme/){:target="_blank" rel="noopener noreferrer"}.

    !!! tip "Movie format/folder with French movie name"
        Radarr supports the ISO-2 naming convention for naming a movie, so replacing `{Movie CleanTitle}` with `{Movie CleanTitle:fr}` will change the name to its French version.

!!! abstract "Indexers - Multi Languages option"
    In Radarr, you can tell that MULTi in an indexer means that a release possesses at least certain audio. For the purpose of this guide, you will select `Original` and `French`.
    This option should only be used for French indexers. Doing so in more "international" indexers can create false positives with the French Audio CFs.

    If you do not see the option, it is because you need to activate the "Advanced Options" of Radarr.

    ??? success "Screenshot example - [Click to show/hide]"
        ![French Radarr MULTi settings](images/french-starr-multi-settings.png)

---

## Score logic

--8<-- "includes/cf/score-attention.md"

---

## Quality Profiles

{! include-markdown "../../includes/french-guide/french-guide-language-profiles-en.md" !}

---

### French Audio Versions

{! include-markdown "../../includes/french-guide/french-guide-french-audio-information-en.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-audio-version-en.md" !}

---

### HD Bluray + WEB (1080p)

!!! tip "Basic Settings"
    Make sure you merge the Blu-ray and WEB qualities into one group under your Quality Profile's qualities. This is due to the fact that potential releases with `French` audio may not exist in WEB.
    The reason why we didn't select the WEB-DL 720p is that you will hardly find any releases that aren't done as 1080p WEB-DL.

    ??? success "VOSTFR + MULTi.VO Profile Screenshot - [Click to show/hide]"
        ![UHD Bluray + WEB for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-bluray-webdl-hd-vo.png)

    ??? success "MULTi.VF Profile Screenshot - [Click to show/hide]"
        ![UHD Bluray + WEB for MULTi.VF Profile](images/french-radarr-qp-bluray-webdl-hd-vf.png)

!!! warning "Make sure you don't check the BR-DISK."

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**The following Custom Formats are required:**

{! include-markdown "../../includes/french-guide/radarr-cf-french-hd-bluray-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-en.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**The following Custom Formats are optional:**

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe-noremux.md" !}

Note: The `Advanced Audio` Custom Formats aren't used in the HD Bluray + WEB profile, as HD Bluray Encodes do not often come with HD audio. If you want HD audio, we would suggest going with a Remux or UHD Encode.

---

### HD Remux (1080p)

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-en.md" !}

!!! tip "Basic Settings"
    Make sure you merge the Blu-ray and WEB qualities into one group under your Quality Profile's qualities. This is due to the fact that potential releases with `French` audio may not exist in WEB.
    The reason why we didn't select the WEB-DL 720p is that you will hardly find any releases that aren't done as 1080p WEB-DL.

    ??? success "VOSTFR + MULTi.VO Profile Screenshot - [Click to show/hide]"
        ![HD Remux for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-remux-hd-vo.png)

    ??? success "MULTi.VF Profile Screenshot - [Click to show/hide]"
        ![HD Remux for MULTi.VF Profile](images/french-radarr-qp-remux-hd-vf.png)

!!! warning "Make sure you don't check the BR-DISK."

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**The following Custom Formats are required:**

{! include-markdown "../../includes/french-guide/radarr-cf-french-remux-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-en.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**The following Custom Formats are optional:**

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe.md" !}

---

### UHD Bluray + WEB (2160p)

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-en.md" !}

!!! tip "Basic Settings"
    Make sure you merge the Blu-ray and WEB qualities into one group under your Quality Profile's qualities. This is due to the fact that potential releases with `French` audio may not exist in WEB.

    ??? success "VOSTFR + MULTi.VO Profile Screenshot - [Click to show/hide]"
        ![HD Bluray + WEB for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-bluray-webdl-uhd-vo.png)

    ??? success "MULTi.VF Profile Screenshot - [Click to show/hide]"
        ![HD Bluray + WEB for MULTi.VF Profile](images/french-radarr-qp-bluray-webdl-uhd-vf.png)

!!! warning "Make sure you don't check the BR-DISK."

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**The following Custom Formats are required:**

{! include-markdown "../../includes/french-guide/radarr-cf-french-uhd-bluray-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-all-hdr-formats.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-en.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**The following Custom Formats are optional:**

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-misc-uhd-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe-noremux.md" !}

---

### UHD Remux (2160p)

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-en.md" !}

!!! tip "Basic Settings"
    Make sure you merge the Blu-ray and WEB qualities into one group under your Quality Profile's qualities. This is due to the fact that potential releases with `French` audio may not exist in WEB.

    ??? success "VOSTFR + MULTi.VO Profile Screenshot - [Click to show/hide]"
        ![UHD Remux for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-remux-uhd-vo.png)

    ??? success "MULTi.VF Profile Screenshot - [Click to show/hide]"
        ![UHD Remux for MULTi.VF Profile](images/french-radarr-qp-remux-uhd-vf.png)

!!! warning "Make sure you don't check the BR-DISK."

{! include-markdown "../../includes/starr/move-quality-to-top.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**The following Custom Formats are required:**

{! include-markdown "../../includes/french-guide/radarr-cf-french-remux-web-scoring-en.md" !}

{! include-markdown "../../includes/cf/radarr-all-hdr-formats.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-en.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**The following Custom Formats are optional:**

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-misc-uhd-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe.md" !}

---

### Advanced Audio and HDR Formats

TRaSH provides great guides and explanations about them at the following links:

- [Advanced Audio](/Radarr/radarr-setup-quality-profiles/#advanced-audio){:target="\_blank" rel="noopener noreferrer"}
- [HDR Formats](/Radarr/radarr-setup-quality-profiles/#hdr-formats){:target="\_blank" rel="noopener noreferrer"}

---

## Other Infos

A FAQ regarding most of the questions you could have is provided by TRaSH: [FAQ & Info](/Radarr/radarr-setup-quality-profiles/#faq-info){:target="\_blank" rel="noopener noreferrer"}

---

## Acknowledgements

- A big thanks to all the people who helped me make and test those profiles and formats (and continue to do so).
- A special thanks to MySuperChef and PrL for their time and explanations.
- A special thanks to Piou and Wikoul who are potentially both now in asylums due to the amount of testing.
- [TRaSH](https://trash-guides.info/), for granting me a small space on his guide for this, his knowledge, and his friendliness.

--8<-- "includes/support.md"
