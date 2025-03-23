<!-- markdownlint-disable MD041-->
**Bad Dual/Multi groups**<br>

These release groups do not use the original language of the media as the first audio track. Since ffprobe relies on the first audio track to determine the primary language of the release, incorrect ordering can lead to parsing issues. This may result in failed imports, misidentified files, or even download loops. To ensure proper handling, the original language should always be the first audio track in the release.
<!-- markdownlint-enable MD041-->
