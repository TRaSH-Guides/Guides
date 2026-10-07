<!-- markdownlint-disable MD036 MD041-->
**Bad Dual/Multi groups**

These release groups often do not set the original language of the media as the first audio track. Since ffprobe relies on the first audio track to determine the release's primary language, incorrect ordering can cause parsing errors. This may lead to failed imports, misidentified files, or download loops. To ensure proper processing, the original language should always be the first audio track in the release.
<!-- markdownlint-enable MD036 MD041-->
