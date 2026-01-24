# How to setup Quality Profiles Anime

_aka How to set up Custom Formats (Anime)_<br><br>

!!! note

    This guide is created and maintained by [FonduemangVI](https://github.com/FonduemangVI) and [rg9400](https://github.com/rg9400)

The aim of this guide is to grab the best release overall (as per [SeaDex](https://releases.moe/){:target="\_blank" rel="noopener noreferrer"}) and not necessarily just dual audio.
The vast majority of releases can be found on [Nyaa](https://nyaa.si/){:target="\_blank" rel="noopener noreferrer"}

---

## Media Management

### Recommended naming scheme

For naming please refer to [Recommended naming scheme](/Radarr/Radarr-recommended-naming-scheme/){:target="\_blank" rel="noopener noreferrer"}

---

## Quality Settings

For quality settings please refer to [Radarr Quality Definitions](/Radarr/Radarr-Quality-Settings-File-Size/#animeanimatedcartoons){:target="\_blank" rel="noopener noreferrer"}

---

## Quality Profile

We need to create a new profile called `Remux-1080p - Anime` due to the way anime can be named we will need to merge a few qualities together see [here](/Radarr/Tips/Merge-quality/){:target="\_blank" rel="noopener noreferrer"} for an example.

We need to add `Bluray-1080p Remux` and `Bluray-1080p` into a group together, `HDTV-1080p` into the same group as `WEBDL-1080p` and `WEBRip-1080p`, and lastly `HDTV-720p` into the same group as `WEBDL-720p` and `WEBRip-720p` so that the scoring will work correctly.

Go to `Settings` => `Profiles`

![!cf-settings-profiles](images/cfa-settings-profiles.png)

![!cfa-mergedqualities](images/cfa-mergedqualities.png)

We then need to select and organise the qualities as seen below.

![!cfa-qualityorder](images/cfa-qualityorder.png)

---

## Anime CF/Scoring

!!! note

    We're going to make use of the below custom formats. See [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="\_blank" rel="noopener noreferrer"} for how to import them.

{! include-markdown "../../includes/cf/radarr-anime.md" !}

### Default Scoring

The scoring that has been set is the recommended scoring, however some of the CFs are optional depending on what you prefer.
`Anime Dual Audio`, `Uncensored` and `10bit` can be given positive scores if you want to prefer content with these attributes.

`Anime Raws` and `Dubs Only` are negatively scored, however if you prefer these attributes you can give them a positive score.

Once the custom formats have been imported you can set the scores as above. To do this go to `Settings` => `Profiles` and select the `Remux-1080p - Anime` profile that was setup before.

![!cf-settings-profiles](images/cfa-settings-profiles.png)

In the profile enter the scores as per the above table in this section.

![!cfa-default-scoring](images/cfa-default-scoring.png)

After you are done it should look similar to the image above, but using the current Guide Scores from the above tables.

### Dual Audio Scoring

If you prefer `Dual Audio` releases you have a few options depending on your preference.

If you want to prefer `Dual Audio` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of `101`, and if you want to prefer it over any tiers give the `CF` a score of `2000`.

If you must have `Dual Audio` releases set the `Minimum Custom Format Score` to 2000 in the `Remux-1080p - Anime` profile that you setup earlier.

Using this scoring you will still benefit from the tiers if a better release group does a `Dual Audio` release.

Below is an example of the scoring set to prefer `Dual Audio` over any tier.

![!cfa-da-scoring](images/cfa-da-scoring.png)

### Uncensored Scoring

!!! note

    Most BDs are uncensored by default, so most groups do not include that in the name.

If you prefer `Uncensored` releases you have a few options depending on your preference.

If you want to prefer `Uncensored` within the same tier give the `CF` a score of `10`, if you want it to be preferred a tier above give the `CF` a score of `101`.

Using this scoring you will still benefit from the tiers if a better release group does an `Uncensored` release.

Below is an example of the scoring set to prefer `Uncensored` a tier above.

![!cfa-uncensored-scoring](images/cfa-uncensored-scoring.png)

### Finishing up

Once you have set your preferred scoring you will need to make two more changes to your `Remux-1080p - Anime` profile.

Make sure `Upgrades Allowed` is ticked then set the `Upgrade Until` section to `Remux-1080p` and the `Upgrade Until Custom Format Score` to `10000` and set `Language` to `Original`

After this has been done your profile should look as seen below. This is an example of the Default Scoring setup.

![!cfa-complete](images/cfa-complete.png)

---

## FAQ

??? question "Is this guide meant for backfilling my library?"

    No. This guide is designed to grab the best available releases going forward, not for backfilling an existing library. Backfilling would require manual intervention and searching to find older releases.

??? question "Why are there no English subtitles available for some anime?"

    Not all anime releases include English subtitles. If you want to filter for only releases with English subtitles, or if you prefer raw (no subs) releases, you can configure this in Prowlarr.

    Go to `Indexers` => Select your anime indexer => and look for the `Anime English-Translated` category option.

    ![!indexer-anime-english-translated](/Prowlarr/images/indexer-anime-english-translated.png)

??? question "How do I configure this for no Remuxes?"

    If you don't want Remuxes, you can simply remove `Bluray-1080p Remux` from your quality profile or uncheck it in the qualities list. The guide will then prefer the highest-scoring encodes instead.

??? question "How do I set up a WEB-only profile?"

    If you only want WEB releases (no Bluray encodes or Remuxes), create a quality profile that only includes `WEBDL-1080p`, `WEBRip-1080p`, `WEBDL-720p`, and `WEBRip-720p`. The Anime Web Tier custom formats will still score these releases appropriately.

??? question "Should I run a single instance or dual instances?"

    It's recommended to run two Radarr instances (one for Anime and one for regular movies). This allows you to have completely separate quality profiles, custom formats, and settings optimised for each type of content without conflicts. However, if you prefer a single instance, you can create separate quality profiles and assign movies accordingly.

---

### Acknowledgements

Most of my information and knowledge came from:

- rg9400 (Building the Custom Formats, Guidance on anime groups and sharing general knowledge.)

- V01 from SeaDex (Guidance on anime groups and sharing general knowledge.)

- Drazzilb (Guidance on anime groups, testing and sharing general knowledge.)

- [TRaSH](https://trash-guides.info/) (For allowing me to utilize his website for our guide and sharing general knowledge.)

--8<-- "includes/support.md"
