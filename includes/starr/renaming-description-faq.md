<!-- markdownlint-disable MD041-->
On the Radarr/Sonarr Discord, people often ask:

- "What's the best way to name my files and folders?"
- "Why doesn't my naming scheme work well?"

While naming is a personal choice, adding non-recoverable information to your filenames is strongly recommended for several good reasons.

## FAQ

??? question "Why should I include extra information in filenames?"

    - **Easy re-imports**: If you ever need to reinstall or re-import your media in Radarr/Sonarr or media servers like Plex/Emby/Jellyfin, having all the details in the filename helps everything get imported correctly. Without this info, files might get wrongly identified as HDTV or WEB-DL quality.
    - **Prevents duplicate downloads**: Radarr/Sonarr won't accidentally download the same file again.

??? question "What's non-recoverable information and can't be recovered later?"

    - **Quality source** (HDTV, WEB-DL, Blu-ray, Remux, etc.)
    - **Release group** (the team that created the release)
    - **Edition type** (Director's Cut, Theatrical, Unrated, etc.)
    - **Repack/Proper status** (whether it's a fixed version)

??? question "Why is the non-recoverable information important/needed?"

    - **Stops download loops**: With a proper naming Radarr/Sonarr knows what you already have.
    - **Quality source**: Can you tell what quality `Movie (2023).mkv` is just by looking at it? Probably not. Without this info, you can't easily upgrade or downgrade your files, and you might download the same movie or TV show again.
    - **Release group**: Knowing the release group helps you identify if there are known issues with that specific release. It also helps you find extra information about hybrid releases or source materials.
    - **Edition type**: Tells you if you have the Director's Cut, Theatrical version, Unrated version, etc.
    - **Repack/Proper**: Shows whether you have the fixed version or the original (possibly broken) release.

??? question "Don't Plex, Emby, and Jellyfin work fine with simple names like `movie (year).ext`/`tv showname SxxExx.ext`?"

    - Yes, they do work with simple names. However, these media servers only care about organizing and playing your files—they don't track quality or help prevent duplicate downloads. That's what Radarr/Sonarr handles.

??? question "Why are the recommended filenames so long?"

    - **Complete information**: To ensure your files have all the details needed to prevent download loops after import.
    - **Only used parts show up**: If your file doesn't have certain attributes (like being a repack), those parts won't appear in the filename.
    - **Media servers hide filenames anyway**: Plex, Emby, and Jellyfin display movie titles and show information, not the actual filename, so the length doesn't matter for viewing.

---

*This naming guide was created with help from the Sonarr/Radarr support team and community feedback.*
<!-- markdownlint-enable MD041-->
