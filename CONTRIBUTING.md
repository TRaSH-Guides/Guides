# Contributing Guidelines

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

Here you will find a set of guidelines for contributing to [TRaSH Guides](https://trash-guides.info/),
These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Guidelines

- Make sure you're editing the latest version.
- If you propose changes make sure it doesn't break anything else in the Guides.
- Make sure that after the changes you don't get any [markdownlint](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md) errors
- If the `metadata.json` and `metadata.schema.json` needs changes, announce it first in the Discord `#development` channel and ping `voidpointer` and `nitsua` so the 3rd party apps don't break :bangbang:

## Branch naming

We're trying to be as consistent as possible for automation of the changelog.

- **feat/xxx** Commits, that adds a new feature
- **fix/xxx**  Commits, that fixes a bug/issue
- **style/xxx** Commits, that do not affect the meaning (white-space, formatting, missing semi-colons, etc)
- **chore/xxx** Miscellaneous commits (administrative / cleanup / backend)

Where 'xxx' can stand for Starr/Sonarr/Radarr/Guide etc

*Examples:*

- `feat/Starr-ELEANOR-to-Scene-CF`
- `feat/Radarr-CiNEPHiLES-to-Remux-Tier-02`
- `feat/maintenance`
- `fix/dv-hdr10-cf-should-match-dv-hdr10+`

[Source](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#types)

## Pull Request naming

We're trying to be as consistent as possible for automation of the changelog.

- **feat(xxx):** Commits, that adds a new feature
- **fix(xxx):**  Commits, that fixes a bug/issue
- **style(xxx):** Commits, that do not affect the meaning (white-space, formatting, missing semi-colons, etc)
- **chore(xxx):** Miscellaneous commits (administrative / cleanup / backend)

Where 'xxx' can stand for Starr/Sonarr/Radarr/Guide etc

*Examples:*

- `feat(starr): add ELEANOR to Scene CF`
- `feat(radarr): add CiNEPHiLES to Remux Tier 02`
- `feat(maintenance): various changes to the Starr CFs`
- `fix(starr): DV HDR10 CF should match DV HDR10+`

[Source](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#types)

## When doing a PR that is WIP

When doing a PR that is in-progress and not yet complete / ready for review or not yet done fully, please ensure it is a **DRAFT Pull Request**

## Radarr/Sonarr Custom Format (JSON)

### Release Group Reclassifications, Removals, or Additions

- When adding a RlsGrp to a Custom Format for whatever reason, please add in the PR why it's added/removed/moved.

### General Guidelines

- Custom Format name needs to match json name :bangbang:
- No hashcode can exists multiple times :bangbang:
- JSON file format shall consist of the following TRaSH specific data appended to the json exported from Starr

```json
{
  "trash_id": "HASHCODE",
  "trash_score": 50,
  "trash_scores": {
    "default": 50,
    "some_other_profile": 100
  },
  "trash_regex": "https://regex101.com/r/pADWJD/5",
STARRJSONEXPORT
}
```

General Structure

- json file name - name of the [json file](#file-naming)
- `trash_id` - Generated [HashCode](#hashcode) for the Custom Format
- `trash_score` - (Legacy) [Default Score for the Custom Format](#scoring). Note that Custom Formats with Default Scores of 0 should NOT have a `trash_score`
- `trash_scores` - (New) Json object of [score(s) for the Custom Format](#scoring). Note that Custom Formats with Default Scores of 0 should NOT have a `trash_scores.default`
- `trash_regex` - Link to [regex test cases](#regex-test-cases) for regex
- STARRJSONEXPORT - The exported custom format created within Starr. Note that this will have a leading `{` that will need to have the `trash` specific regex added after

### File Naming

- JSON file names are always written in small letters, spaces are replaced by a dash, no spaces or special characters except a dash :bangbang:

### Hashcode

- When adding the hashcode for **Radarr** use the following naming `CF_name`  e.g. the Custom Format `BR-DISK` would be the hash of [`BR-DISK`](https://md5.gromweb.com/?string=BR-DISK)
- When adding the hashcode for **Radarr Anime** use the following naming `Radarr Anime CF_name`  e.g. the Custom Format `BR-DISK` would be the hash of [`Radarr Anime BR-DISK`](https://md5.gromweb.com/?string=Radarr+Anime+BR-DISK).
- When adding the hashcode for **Sonarr** use the following naming `Sonarr CF_name` e.g. the Custom Format `BR-DISK` would be the hash of [`Sonarr BR-DISK`](https://md5.gromweb.com/?string=Sonarr+BR-DISK).
- When adding the hashcode for **Sonarr Anime** use the following naming `Sonarr Anime CF_name`  e.g. the Custom Format `BR-DISK` would be the hash of [`Sonarr Anime BR-DISK`](https://md5.gromweb.com/?string=Sonarr+Anime+BR-DISK).

### Regex Test Cases

- Provide a link to your regex example of your Custom Format using the following [Template](https://regex101.com/r/4DypIW/1).

When adding a regex test case:

- Replace the actual movie name with `Movie`.
- Replace the actual Series name with `Series`.
  - Remove the actual Series title.
- Replace the actual group name with `RlsGrp`

When updating or adding a new CF the test case url (`trash_regex`) needs to be prepended to the exported from Starr json

```json
{
  "trash_regex": "https://regex101.com/r/pADWJD/5",
}
```

### Scoring

- Scores must be added both as a single value under (legacy) `trash_score` and as JSON objects under `trash_scores`, for example:

```json
{
  "trash_score": 50,
  "trash_scores": {
    "default": 50,
    "some_other_profile": 100
  },
}
```

- This allows for Custom Formats to be assigned different scores for different profiles
- The `trash_score` value MUST be the same as the `trash_scores.default` value
- The legacy `trash_score` value is currently retained for compatibility reasons, but will eventually be removed
- Default Scores of 0 (`trash_score` or `trash_scores.default` are FORBIDDEN

## YAML file naming

- If a hashcode is needed **No** hashcode can exist multiple times :bangbang:
- Use [this website](https://md5.gromweb.com) to generate an md5 hash
- YAML file names are always written in small letters, spaces are replaced by a dash, no spaces or special characters except a dash :bangbang:

## Recommendations

Use [VSCode](https://code.visualstudio.com/) for editing. VS Code should recommend extensions to you
based on the `.vscode/extensions.json` file; you should install all of them.

## Preview Docs Locally

### Prerequisites

These prerequisites are taken from the [mkdocs installation instructions][mkdocinstall].

- Install a recent version of [Python 3](https://www.python.org/).
- `pip` is also required, but should come with Python. Run `pip --version` to check if its available
  and working. See the [installation instructions](https://pip.pypa.io/en/stable/installation/).

[mkdocinstall]: https://www.mkdocs.org/user-guide/installation/

### Mkdocs Installation

First, install mkdocs:

```bash
pip install mkdocs
```

Then, install dependent modules using the command below. This command should be run in the root
directory of the repository (i.e. where the `requirements.txt` file is). If the `pip` command does
not work, refer to the mkdocs installation page linked in the Prerequisite section above.

```bash
pip install -r docs/requirements.txt
```

Once everything is installed, run the command below to start a local dev server to preview your
changes to mkdocs:

```bash
mkdocs serve
```
