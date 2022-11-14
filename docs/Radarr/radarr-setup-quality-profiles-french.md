# How to setup Quality Profiles

*aka How to setup Custom Formats (French)*<br><br>

!!! note
    This guide is created and maintained by [Someone said "Nice"?](https://github.com/NiceTSY)

!!! tip
    Cette page est aussi disponible en Français: [Guide en Français](/Radarr/radarr-setup-custom-formats-french-fr/){:target="_blank" rel="noopener noreferrer"}.

So what is the best way to set up the Custom Profiles and which one to use with which scores to get French and English Audio?

Keep in mind that most releases are MULTi (understand DUAL audio, original and French audio) and it will be difficult to only have French audio, unless you are willing to get 720p, or you are only looking for French movies.

Therefore, you will need a slightly modified MULTi Custom Format than the one find in the original guide. This one also recognize VO and VFF in the name and rename the import. This is important for the score to match before and after the import and to avoid download loop.

--8<-- "includes/cf/score-attention.md"

------

## Basics

It is quite important that you follow and understand what is envisioned by Trash's guide:

- Adding Custom Formats, as explained in [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
- Setting up a quality Profile to make use of the Custom Formats, as explained in [How to setup Quality Profiles | Basics section](/Radarr/radarr-setup-quality-profiles/#basics){:target="_blank" rel="noopener noreferrer"}.

------

!!! warning "Mandatory"

    The only change that is needed and **mandatory** for French Custom Formats to work is to set the preferred language profile for your releases to `Any`.

    ??? check "Screenshot example - [CLICK TO EXPAND]"
        ![!cf-quality-profile-cf](images/cf-french-profile-language.png)

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

## Examples

--8<-- "includes/cf/score-attention.md"

------

### French Audio Versions

Those are all optional and only there to rename your release or to avoid a certain type of French Audio. Examples:

- You do not want VFQ or VQ audio, in this case you will put them at `-10000` instead of `0`.
- You only want VOSTFR, in this case you will ignore any mention of **MULTi Custom Formats** and give the [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) Custom Format a score of `1000`.

{! include-markdown "../../includes/french-guide/radarr-french-audio-version.md" !}

------

### Releases you should avoid

In my opinion, this is a must-have for every Quality Profile you use. All these Custom Formats make sure you don't get Low Quality Releases.

{! include-markdown "../../includes/french-guide/radarr-french-unwanted.md" !}

------

#### Prefer HQ Encodes-1080p

{! include-markdown "../../includes/french-guide/radarr-french-example-hd-encodes.md" !}

------

#### Remux-1080p

{! include-markdown "../../includes/french-guide/radarr-french-example-1080p-remuxes.md" !}

------

#### Prefer HQ Encodes-2160p

{! include-markdown "../../includes/french-guide/radarr-french-example-uhd-encodes.md" !}

------

#### Remux-2160p

{! include-markdown "../../includes/french-guide/radarr-french-example-2160p-remuxes.md" !}

------

## Acknowledgements

- A big thanks to all the people that helped me to test those profiles and formats (and continue to do so).
- A special one to MySuperChef and PrL for their time and explanations.
- A special one to Piou and Wikoul who are potentially both now in asylums due to the amount of testing.
- [TRaSH](https://trash-guides.info/), for granting me a small space on his guide for this, his knowledge, and his friendliness.

--8<-- "includes/support.md"
