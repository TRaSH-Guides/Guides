<!-- markdownlint-disable MD041-->
On the Radarr/Sonarr Discord people often ask,

- “What's the recommended/best way to name your files or folders?”
- “Why is my naming scheme bad?”

Even though it is a personal preference, it is still recommended to add non-recoverable information for several reasons.

## FAQ

??? question "Why?"

    - If, for whatever reason, you ever need to do a re-install or a full re-import in the Starr Apps or Plex/Emby/Jellyfin, it's nice to have all that info in the filename so it gets imported correctly and isn't incorrectly matched as HDTV or WEB-DL etc.
    - Prevent download loops.

??? question "What's non-recoverable information?"

    - Quality Source (HDTV, WEBDL, Bluray, Remux, etc..)
    - Release group
    - Edition version
    - Repack/Proper

??? question "Why is the non-recoverable information important/needed?"

    - **Prevent download loops**.
    - **Quality Source (HDTV, WEBDL, Bluray, Remux, etc..)**: Can you tell from the following info: `movie (year).ext`, which quality source the file is from? Probably not, and there is no real way to determine it if it's lost after import. Why would you care? Mainly if you ever want to upgrade or downgrade your media file and to prevent re-downloads of the same file.
    - **Release group**: With the knowledge of which release group your release belongs to, you can determine if the file has any issues related to that specific release. It can also help find extra information if it's a hybrid release or which sources are used.
    - **Edition version**: To determine if the release is an directors cut, theatrical, unrated, etc.
    - **Repack/Proper**: To determine if the release was a repack or a proper, so you know if you have the correct version and not the broken one with playback issues or other issues with the media file.

??? question "But Plex, Emby and Jellyfin work fine with just `movie (year).ext`/`tv showname SxxExx.ext`"

    - True, but they don't care about the quality of your media file you're using, their main purpose is just to provide you with your media library and play the media files.

??? question "Why is the file naming so long?"

    - To make sure your filename contains all the info needed to prevent download loops after import.
    - The so-called "naming tokens" not used in your media file won't be used/shown.
    - Any proper media server (Plex, Emby, or Jellyfin) won't display the actual filename outright anyway, so why worry about how the file's naming looks when it has all the needed info included?

The naming scheme provided here is made with the help of the Sonarr/Radarr (Support) Team and information provided by the community.
<!-- markdownlint-enable MD041-->
