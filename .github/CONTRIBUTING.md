# Contributing Guidelines

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

Here you will find a set of guidelines for contributing to TRaSH Guides, Which you can find [HERE](https://trash-guides.info/),
These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Guidelines

- Make sure you're editing the latest version.
- If you propose changes make sure it doesn't break anything else in the Guides.
- Make sure that after the changes you don't get any [markdownlint](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md) errors
- If the `metadata.json` and `metadata.schema.json` needs changes, announce it first in the Discord `#development` channel and ping`voidpointer` and `nitsua` so the 3rd party apps don't break :bangbang:

## Radarr/Sonarr Custom Format (JSON)

- Custom Format name needs to match json name :bangbang:
- No hashcode can exists multiple times :bangbang:
- JSON file names are always written in small letters, spaces are replaced by a dash, no spaces or special characters except a dash :bangbang:
- When adding the hashcode for Radarr use the following naming `CF_name` on the following [link+example](https://md5.gromweb.com/?string=BR-DISK).
- When adding the hashcode for Radarr Anime use the following naming `Radarr Anime CF_name` on the following [link+example](https://md5.gromweb.com/?string=Radarr+Anime+BR-DISK).
- When adding the hashcode for Sonarr use the following naming `Sonarr CF_name` on the following [link+example](https://md5.gromweb.com/?string=Sonarr+BR-DISK).
- When adding the hashcode for Sonarr Anime use the following naming `Sonarr Anime CF_name` on the following [link+example](https://md5.gromweb.com/?string=Sonarr+Anime+BR-DISK).
- Provide a link to your regex example of your Custom Format using the following [Template](https://regex101.com/r/fXmQQm/1).
- When adding a RlsGRp to a Custom Format for what ever reason, please add in the PR why it's added/removed/moved.

When adding a regex test case

- Replace the actual movie name with `Movie`.
- Replace the actual series name with `Series`.
- Remove the actual Series title.
- Replace the actual group name with `RlsGrp`

When updating or adding a new CF the test case url needs to be added to the json.

```json
{
  "trash_id": "hashcode",
  "trash_score": "score",
  "trash_regex": "https://regex101.com/r/pADWJD/5",
  "name": "CF_name",
```

## YAML file naming

- If a hashcode is needed **No** hashcode can exist multiple times :bangbang:
- YAML file names are always written in small letters, spaces are replaced by a dash, no spaces or special characters except a dash :bangbang:

## Recommendations

- use [VSCode](https://code.visualstudio.com/) for editing with the following extension  [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
