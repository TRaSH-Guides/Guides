<!-- markdownlint-disable MD041-->
**BR-DISK**<br>

This is a custom format to help Radarr/Sonarr recognize and ignore BR-DISK (ISOs and Blu-ray folder structure) in addition to the standard BR-DISK quality.

!!! note

    Depending on your renaming scheme, it could happen that Radarr will match renamed files after they are downloaded and imported as `BR-DISK`,
    This is a cosmetic annoyance until we come up with another way to solve this,
    Since this Custom Format is used not to download BR-DISK, it fulfills its purpose as intended.
    There are several reasons why this is happening:

    - Blame the often incorrectly used naming of x265 encodes.
    - Radarr/Sonarr uses dynamic custom formats.

--8<-- "includes/cf-descriptions/apply-10000.md"
<!-- markdownlint-enable MD041-->
