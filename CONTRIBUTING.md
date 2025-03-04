# Contributing Guidelines

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

Here you will find a set of guidelines for contributing to [TRaSH Guides](https://trash-guides.info/),
These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Guidelines

- Make sure you're editing the latest version.
- If you propose changes, ensure they don't break anything else in the guides.
- Make sure that after the changes, you don't get any [markdownlint](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md) errors
- If the `metadata.json` and `metadata.schema.json` needs changes, announce it first in the Discord `#development` channel and ping `voidpointer` and `nitsua` so the 3rd party apps don't break :bangbang:

## Branch naming

> [!IMPORTANT]
> We're trying to be as consistent as possible because of the automation of the changelog.

- **feat/xxx** Commits that adds a new feature
- **fix/xxx** Commits that fixes a bug/issue
- **style/xxx** Commits that do not affect the meaning (white-space, formatting, missing semi-colons, grammar, etc.)
- **chore/xxx** Miscellaneous commits (administrative, cleanup, backend, etc.)

> [!note]
> Where `xxx` can stand for the main [Guide Categories](#guide-categories) in the guide.

_Examples:_

- `feat/Starr-ELEANOR-to-Scene-CF`
- `feat/radarr-CiNEPHiLES-to-Remux-Tier-02`
- `style/radarr minor-grammar corrections`
- `fix/starr-dv-hdr10-cf-should-match-dv-hdr10+`

## Pull Request naming

> [!IMPORTANT]
> Because the changelog is created automatically, we want to make the PR name as clear and consistent as possible.

The PR naming consists of 3 parts.

part1(part2): part3 => type(guide category): short detailed descriptions

### Types

[Source](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#types)

- **feat(xxx):** Commits that adds a new feature
- **fix(xxx):** Commits that fixes a bug/issue
- **style(xxx):** Commits that do not affect the meaning (white-space, formatting, missing semi-colons, grammar, etc)
- **chore(xxx):** Miscellaneous commits (administrative, cleanup, backend, etc)

> [!note]
> Where `xxx` can stand for the main [Guide Categories](#guide-categories) in the guide.

### Guide categories

The following Guide categories can be used for the PR name.

```yml
- type(radarr): #Radarr related
- type(radarr-german): #Radarr related but for the German guides
- type(radarr-french): #Radarr related but for the French guides
- type(radarr-anime): #Radarr related but for the Anime guides
- type(sonarr): #Sonarr related
- type(sonarr-german): #Sonarr related but for the German guides
- type(sonarr-french): #Sonarr related but for the French guides
- type(sonarr-anime): #Sonarr related but for the Anime guides
- type(starr): #Sonarr and Radarr related
- type(starr-german): #Sonarr and Radarr related but for the German guides
- type(starr-french): #Sonarr and Radarr related but for the French guides
- type(starr-anime): #Sonarr and Radarr related but for the Anime guides
- type(prowlarr): #Prowlarr related
- type(lidarr): #Lidarr related
- type(bazarr): #Bazarr related
- type(hardlinks): #Hardlinks/File and Folder Structure related
- type(downloaders): #Downloaders related
- type(plex): #Plex related
- type(guide-sync): # Officially supported third-party party Guide Sync Tools related
- type(misc): #Miscellaneous guides that do not fit in any other categories but are still related to Radarr/Sonarr, etc
- type(glossary): #Any additions/changes to the glossary page
```

_Examples:_

- feat(guide-sync): Add more groups to give the user more personal options
- feat(guide-sync): Add new Quality Profiles for Radarr/Sonarr
- feat(starr): [NEW Guide] How does the current rank logic work
- feat(downloaders): [NZBGet] Updated the guide to reflect the recent changes with v24.5

## When doing a PR that is WIP

> [!TIP]
> When doing a PR that is in progress and not yet complete/ready for review or not yet done fully, please ensure it is a **DRAFT Pull Request**

## Radarr/Sonarr Custom Format (JSON)

### Release Group Reclassifications, Removals, or Additions

> [!WARNING]
> **When adding a release group to a Custom Format, please explain why it's added/removed/moved in the PR.**

### General Guidelines

> [!CAUTION]
>
> - Custom Format name needs to match JSON name :bangbang:
> - No hashcode can exist multiple times :bangbang:
>
- Tiers only hold release groups that have at least done several dozen objectively high-quality releases or are added for a specific reason. (If they do mainly niche stuff and/or foreign stuff, they won't be added)
- All Tier Groups must use retail sources. Fanres and upscaled groups are forbidden. This is due to the high effort required and the near impossibility of systematically guaranteeing quality without manually checking every single movie.
- JSON file format shall consist of the following TRaSH-specific data appended to the JSON exported from Starr

```json
{
    "trash_id": "HASHCODE",
    "trash_scores": {
        "default": 50,
        "some_other_profile": 100
    },
    "trash_regex": "https://regex101.com/r/pADWJD/5",
STARRJSONEXPORT
}
```

General Structure

- JSON file name - the name of the [json file](#file-naming)
- `trash_id` - Generated [HashCode](#hashcode) for the Custom Format
- `trash_scores` - JSON object of [score(s) for the Custom Format](#scoring). Note that Custom Formats with Default Scores of 0 should NOT have a `trash_scores.default`
- `trash_regex` - Link to [regex test cases](#regex-test-cases) for regex
- STARRJSONEXPORT - The exported custom format created within Starr. Note that this will have a leading `{` that will need to have the trash-specific regex added after it.

### File Naming

> [!CAUTION]
> JSON file names are always written in lowercase, spaces are replaced by a dash, and no spaces or special characters except a dash :bangbang:

### Hashcode

- When adding the hashcode for **Radarr**, use the following naming convention: `CF_name` e.g., the Custom Format `BR-DISK` would be the hash of [`BR-DISK`](https://md5.gromweb.com/?string=BR-DISK)
When adding the hashcode for **Radarr Anime**, use the following naming convention: `Radarr Anime CF_name`. For example, the Custom Format `BR-DISK` would be the hash of [`Radarr Anime BR-DISK`](https://md5.gromweb.com/?string=Radarr+Anime+BR-DISK).
- When adding the hashcode for **Sonarr**, use the following naming convention: `Sonarr CF_name` e.g. the Custom Format `BR-DISK` would be the hash of [`Sonarr BR-DISK`](https://md5.gromweb.com/?string=Sonarr+BR-DISK).
- When adding the hashcode for **Sonarr Anime**, use the following naming convention: `Sonarr Anime CF_name` e.g. the Custom Format `BR-DISK` would be the hash of [`Sonarr Anime BR-DISK`](https://md5.gromweb.com/?string=Sonarr+Anime+BR-DISK).

### Regex Test Cases

- Provide a link to your regex example of your Custom Format using the following [Template](https://regex101.com/r/4DypIW/1).

When adding a regex test case:

- Replace the actual movie name with `Movie`.
- Replace the actual Series name/title with `Series`.
- Replace the actual group name with `RlsGrp`

When updating or adding a new CF, the test case URL (`trash_regex`) needs to be prepended to the exported from Starr JSON.

```json
{
    "trash_regex": "https://regex101.com/r/pADWJD/5"
}
```

### Scoring

- Scores must be added as JSON objects under `trash_scores`, for example:

```json
{
    "trash_scores": {
        "default": 50,
        "some_other_profile": 100
    }
}
```

- This allows for Custom Formats to be assigned different scores for different profiles
- Default Scores of 0 (e.g., as in `trash_scores.default`) are FORBIDDEN

## YAML file naming

> [!CAUTION]
>
> - If a hashcode is needed **No** hashcode can exist multiple times :bangbang:
>
- Use [this website](https://md5.gromweb.com) to generate an md5 hash
- YAML file names are always written in small letters, spaces are replaced by a dash, and no spaces or special characters except a dash :bangbang:

## Quality Profiles and 3rd party sync apps

> [!IMPORTANT]
> When creating a new quality profile or editing an existing one, it's mandatory to ensure that these settings are updated/added to the following locations for the third-party sync apps.

- Radarr: `docs/json/radarr/quality-profiles`
    - `docs/json/radarr/cf-groups`
- Sonarr: `docs/json/sonarr/quality-profiles`
    - `docs/json/Sonarr/cf-groups`

- `docs/json/xxxarr/quality-profiles` = The base quality profile with all the mandatory Custom Formats.
- `docs/json/xxxarr/cf-groups` = The optional/User choices that wouldn't break the Quality Profile.

### quality-profiles

The quality-profiles hold the basic quality profile settings that you also see in the Radarr/Sonarr GUI.

![image](https://github.com/user-attachments/assets/b2d743d8-0f1e-41bd-baa1-7ceaf52c43cc)

> [!TIP]
> Use one of the existing quality-profiles.json files as your base.

- JSON file name - use the name of the quality profile that you used in the `"name":' in the JSON

> [!CAUTION]
> JSON file names are always written in lowercase, spaces are replaced by a dash, and no spaces or special characters except a dash :bangbang:

- `trash_id` - Generated [HashCode](#hashcode) for the profile name you used for the `"name":' in the JSON
- `name` - Quality Profile name.
    - If the profile is for a foreign language, start with `[Language]` => example: `[German] HD Bluray + WEB`.
    - If the profile is for anime, start with `[Anime]` => example: `[Anime] Something`.
- `trash_description` - Description of what the quality profile covers => example: `Quality Profile that covers:<br>- WEBDL: 1080p<br>- Bluray: 720p, 1080p`
    - The following HTML code is allowed in the description: `<b>`, `</b>`, `<br>` and `<a href="link-here" target="_blank">text-here</a>`.
- `group` — Sort order to ensure the quality profiles stay together. The default public guide will always be the first.
    - [1-9] English/International Public Guides (None Anime).
    - [11-19] German Guides (Incl. Anime).
    - [21-29] French Guides (Incl. Anime).
    - [81-89] English/International Public Guides (Anime).
    - [91-99] Restricted Use.
- `upgradeAllowed` - Upgrades Allowed.
- `cutoff` - Upgrade Until.
- `minFormatScore` - Minimum Custom Format Score.
- `cutoffFormatScore` - Upgrade Until Custom Format Score.
- `minUpgradeFormatScore` - Minimum Custom Format Score Increment.
- `language` - Language. **(This is only for Radarr)**
- `items` - Qualities. => The allowed quality sources are in reverse order, meaning that the highest quality allowed in your profile is at the bottom of the list.
- `formatItems` - Custom Formats. => The mandatory Custom Formats that are needed for this quality profiles, excluding the ones that are added with the [cf-groups](cf-groups)

### cf-groups

The cf-groups can hold several Custom Formats.
Depending on the chosen profile, the end user gets a selection of groups where certain groups are enabled by default with certain Custom Formats or some groups holding Custom Formats that the end user can choose if they want to have it enabled or disabled.

The cf-group.json exists of two properties.

- Green is the group properties.
- Blue is the Custom Format properties.

![image](https://github.com/user-attachments/assets/0776b71e-ff55-4d36-aea2-fb7034e64477)

> [!TIP]
> Use one of the existing cf-groups.json files as an example.

#### Group Specific settings

> [!note]
>
> - All Groups are optional and by default disabled. The user can enable or disable the group (If the CF should always be enabled, put it in the [quality profile](#quality-profiles-explanation))
> - If you want the group to be enabled by default, add `"default": "true",` above `"custom_formats": [`. (If the group does not have to be enabled by default, there is no need to add `"default": "false",`)

- JSON file name - use the name of the quality profile that you used in the `"name":' in the JSON

> [!CAUTION]
> JSON file names are always written in lowercase, spaces are replaced by a dash, and no spaces or special characters except a dash :bangbang:

- `trash_id` - Generated [HashCode](#hashcode) for the group name you used for the `"name":' in the JSON
- `name` - Group name.
    - If the group is for a foreign language, start with `[Language]` => example: `[German] HD Bluray + WEB`.
    - If the group is for anime, start with `[Anime]` => example: `[Anime] Something`.
- `trash_description` - Description of what the group covers => example: `Collection of UK Streaming Services for Radarr`
    - The following HTML code is allowed in the description: `<b>`, `</b>`, `<br>` and `<a href="link-here" target="_blank">text-here</a>`.
- `default": "true"` - [**OPTIONAL**] If you want the group to be enabled by default.

#### Group Custom Format specific settings

> [!note]
>
> - `required: true` => If the group is enabled, all the CF in that group are enabled, but the end user can still disable the full group (no individual choosing possible).
> - `required: false` => If the group is enabled, the end user can choose which CF he wants to be added individually, and they are not checked by default.
> - `default: true`/`required: false` => If the group is enabled, the end user can choose which CF he wants to be added individually, and they are checked by default.

- `custom_formats` -
    - `name` - CF name found in the JSON.
    - `trash_id` - CF trash_id found in the JSON.
    - `required` - [true|false] See the above note for a description
    - `default": "true"` - [**OPTIONAL**] If you want the CF to be enabled by default.
- `quality_profiles`
    - `exclude` - Add the Quality Profiles you want to exclude from this group, using the quality-profiles `name` and `trash_id`.

---

## Recommendations

Use [VSCode](https://code.visualstudio.com/) for editing. VS Code should recommend extensions to you
based on the `.vscode/extensions.json` file, you should install all of them.

## Preview Docs Locally

### Prerequisites

These prerequisites are taken from the [mkdocs installation instructions][mkdocinstall].

- Install a recent version of [Python 3](https://www.python.org/).
- `pip` is also required, but it should come with Python. Run `pip --version` to check if it's available and working. See the [installation instructions](https://pip.pypa.io/en/stable/installation/).

[mkdocinstall]: https://www.mkdocs.org/user-guide/installation/

Alternatively, you can check out the docker container and instructions maintained by [zakkarry](https://github.com/zakkarry) specifically for developing the guides [here](https://gist.github.com/zakkarry/1305f713539c9fee22bdeeddcff3a263). The documentation in the README explains the installation process.

### Mkdocs Installation

First, install mkdocs:

```bash
pip install mkdocs
```

Then, you can install dependent modules using the command below. This command should be run in the repository's root directory (i.e., where the `requirements.txt` file is). If the `pip` command does
If it doesn't work, please check the mkdocs installation page linked in the Prerequisite section above.

```bash
pip install -r docs/requirements.txt
```

Once everything is installed, run the command below to start a local dev server to preview your
changes to mkdocs:

```bash
mkdocs serve
```
