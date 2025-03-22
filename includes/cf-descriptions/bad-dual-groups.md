<!-- markdownlint-disable MD041-->
**Bad dual/Multi groups**<br>

These release groups do not use the original language of the media as the first audio track. Since ffprobe relies on the first audio track to determine the primary language of the release, incorrect ordering can lead to parsing issues. This may result in failed imports, misidentified files, or even download loops. To ensure proper handling, the original language should always be the first audio track in the release.

Examples:

- These groups take the original release and add their language (e.g., Portuguese) as the main audio track (AAC 2.0). After renaming and FFprobe, the media file will be recognized as Portuguese AAC audio. Adding the best audio as the first track is a common rule. They also often translate or rename the release name to Portuguese.
- These groups do not use the original language as the first audio track.
<!-- markdownlint-enable MD041-->
