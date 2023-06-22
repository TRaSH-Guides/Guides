# How to setup Quality Profiles Anime

*aka How to setup Custom Formats (Anime)*<br><br>

!!! note
    This guide is created and maintained by [FonduemangVI](https://github.com/FonduemangVI) and [rg9400](https://github.com/rg9400)

It's recommended to run two Radarr instances. One for Anime Movies and one for Normal Movies, or you can make use of Quality Profiles and score different Custom Formats (CFs) as required.

The aim of this guide is to grab the best release overall (as per [SeaDex](https://releases.moe/){:target="_blank" rel="noopener noreferrer"}) and not necessarily just dual audio.
The vast majority of releases can be found on [Nyaa](https://nyaa.si/){:target="_blank" rel="noopener noreferrer"} or [AB](https://animebytes.tv/){:target="_blank" rel="noopener noreferrer"}

!!! info ""
    Nyaa is a public tracker while AB is an invite only tracker.

---

## Media Management

### Recommended naming scheme

For naming please refer to [Recommended naming scheme](/Radarr/Radarr-recommended-naming-scheme/){:target="_blank" rel="noopener noreferrer"}

---

## Quality Settings

For quality settings please refer to [Radarr Quality Definitions](/Radarr/Radarr-Quality-Settings-File-Size/#radarr-quality-definitions){:target="_blank" rel="noopener noreferrer"}

---

## Quality Profile

We need to create a new profile called `Remux-1080p - Anime` due to the way anime can be named we will need to merge a few qualities together see [here](/Radarr/Tips/Merge-quality/){:target="_blank" rel="noopener noreferrer"} for an example.

We need to add `Bluray-1080p Remux` and `Bluray-1080p` into a group together, `HDTV-1080p` into the same group as `WEBDL-1080p` and `WEBRip-1080p`, and lastly `HDTV-720p` into the same group as `WEBDL-720p` and `WEBRip-720p` so that the scoring will work correctly.

Go to `Settings` => `Profiles`

![!cf-settings-profiles](images/cfa-settings-profiles.png)

![!cfa-mergedqualities](images/cfa-mergedqualities.png)

We then need to select and organise the qualities like below.

![!cfa-qualityorder](images/cfa-qualityorder.png)

---

## Anime CF/Scoring

!!! note
    We're going to make use of the below custom formats. See [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"} for how to import them.

{! include-markdown "../../includes/cf/radarr-anime.md" !}
<!-- --8<-- "includes/cf/radarr-anime.md" -->

### Default Scoring

The scoring that has been set is the recommended scoring, however some of the CFs are optional depending on what you prefer.
`Anime Dual Audio`, `Uncensored` and `10bit` can be given positive scores if you want to prefer content with these attributes.

`Anime Raws` and `Dubs Only` are negatively scored, however if you prefer these attributes you can give them a positive score.

Once the custom formats have been imported you can set the scores as above. To do this go to `Settings` => `Profiles` and select the `Remux-1080p - Anime` profile that was setup before.

![!cf-settings-profiles](images/cfa-settings-profiles.png)

In the profile enter the scores as per the above table in this section.

![!cfa-default-scoring](images/cfa-default-scoring.png)

After you are done it should look like the image above.

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

After this has been done your profile should look like below. This is an example of the Default Scoring setup.

![!cfa-complete](images/cfa-complete.png)

### Acknowledgements

Most of my information and knowledge came from:

- rg9400 (Building the Custom Formats, Guidance on anime groups and general knowledge share.)

- V01 from SeaDex (Guidance on anime groups and general knowledge share.)

- Drazzilb (Guidance on anime groups, testing and general knowledge share.)

- [TRaSH](https://trash-guides.info/) (For allowing me to utilize his website for our guide and general knowledge share.)

{! include-markdown "../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
