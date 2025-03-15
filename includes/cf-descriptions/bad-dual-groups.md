<!-- markdownlint-disable MD041-->
**Bad dual/Multi groups**<br>

These release groups do not use the original language as the first audio track, the first audio language track is used to determine which language the original media file uses. Therefore, the first audio language track should always be the original language audio track, not a random one. If the first audio language track is not the original, they may fail to import the file, or it could result in download loops.

Examples:

- These groups take the original release and add their language (e.g., Portuguese) as the main audio track (AAC 2.0). After renaming and FFprobe, the media file will be recognized as Portuguese AAC audio. Adding the best audio as the first track is a common rule. They also often translate or rename the release name to Portuguese.
- These groups do not use the original language as the first audio track.
<!-- markdownlint-enable MD041-->
