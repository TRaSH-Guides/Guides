# Suggested Scoring

Did you just setup Bazarr and are wondering which scoring you should use/setup for your subtitles and sync?

I'll suggest a scoring that would work for most common languages. With this scoring, 99% of your downloaded subs should be the correct ones for your release.

- Setting it too low could result in bad subs or onest that are completely out of sync or un-syncable.
- Setting it too high could result in less subs.

## Sonarr Subtitle Minimum Score

`Settings` => `Sonarr`

![!Sonarr: Minimum Score](images/settings-sonarr-options-minimum-score.png)

Set the Minimum Score to `90`

## Radarr Subtitle Minimum Score

`Settings` => `Radarr`

![!Radarr: Minimum Score](images/settings-radarr-options-minimum-score.png)

Set the Minimum Score to `80`

## Synchronization Score Threshold

`Settings` => `Subtitles`

![!Score Threshold](images/settings-subtitles-sync-score.png)

- Enable `Automatic Subtitles Synchronization` at step 3.
- Enable `Series Score Threshold` at step 4 and set the score to `96`.[^1]
- Enable `Movies Score Threshold` at step 5 and set the score to `86`.[^1]

This will set the Synchronization Score Threshold (at which score bazarr will sync the subtitles).

!!! info
    The synchronization is a best-effort attempt based on the following:

    - it uses the embedded subtitles track as reference, if not present.
    - it needs to extract the audio track and analyze it to define start of sentence markers.

[^1]:
    Why not set the Synchronization Score to max?
    It's kinda useless. To start with, why would you want to try to sync perfectly matching subs in the first place?

    I personally noticed that when setting it too high (98-100), I would get subs that are 1 second too slow/fast.

{! include-markdown "../../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
