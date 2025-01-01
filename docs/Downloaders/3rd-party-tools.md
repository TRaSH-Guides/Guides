# 3rd Party tools

Here you will find a collection of 3rd party tools for several downloaders we cover.

## qBit Manage

This is a program used to manage your qBittorrent instance such as:

- Tag torrents based on tracker URL and set seed goals/limit upload speed by tag (only tag torrents that have no tags)
- Update categories based on the save directory
- Remove unregistered torrents (delete data & torrent if it is not being cross-seeded, otherwise it will just remove the torrent)
- Automatically add cross-seed torrents in a paused state. _Note: cross-seed now allows for torrent injections directly to qBit, making this feature obsolete._
- Recheck paused torrents sorted by lowest size and resume if completed
- Remove orphaned files from your root directory that are not referenced by qBittorrent
- Tag any torrents that have no hardlinks and allow the option to cleanup to delete these torrents and contents based on maximum ratio and/or time-seeded
- RecycleBin function to move files into a RecycleBin folder instead of deleting the data directly when deleting a torrent
- Built-in scheduler to run the script every x minutes. (Can use --run command to run without the scheduler)
- Webhook notifications with Notifiarr and Apprise API integration.

[qBit Manage](https://github.com/StuffAnThings/qbit_manage){:target="\_blank" rel="noopener noreferrer"}

---

## qBitrr

This is a program used to manage your qBittorrent instance and Arr instances

Features

- Monitor qBit for Stalled/bad entries and delete them then blacklist them on Arrs (Option to also trigger a re-search action).
- Monitor qBit for completed entries and tell the appropriate Arr instance to import it:
    - `qbitrr DownloadedMoviesScan` for Radarr
    - `qbitrr DownloadedEpisodesScan` for Sonarr
- Skip files in qBit entries by extension, folder or regex.
- Monitor the completed folder and clean it up.
- Usage of [ffprobe](https://github.com/FFmpeg/FFmpeg){:target="\_blank" rel="noopener noreferrer"} to ensure downloaded entries are valid media.
- Trigger periodic RSS Syncs on the appropriate Arr instances.
- Trigger Queue update on appropriate Arr instances.
- Search requests from [Overseerr](https://github.com/sct/overseerr){:target="\_blank" rel="noopener noreferrer"} or [Ombi](https://github.com/Ombi-app/Ombi){:target="\_blank" rel="noopener noreferrer"}.
- Automatically add/remove trackers
- Set per tracker values
- **Sonarr v4 support**
- **Radarr v4 and v5 support**
- Monitor Arr's databases to trigger missing episode searches.
- Searches Radarr missing movies based on Minimum Availability
- Customizable searching by series or singular episodes
- Optionally searches year by year in ascending or descending order (config option available)
- Search for CF Score unmet and cancel torrents based on CF Score or Quality unmet search

[qBitrr](https://github.com/Feramance/qBitrr){:target="\_blank" rel="noopener noreferrer"}

---

## qbittorrent-cli

A cli to manage qBittorrent. Add torrents, reannounce and import from other clients.

- Add torrents to qBittorrent from a file or magnet link. Useful in combination with autodl-irssi
- Reannounce torrents for troublesome trackers
- Set limits on how many simultaneously active downloads are allowed
- Import torrents with state from Deluge and rTorrent

[qbittorrent-cli](https://github.com/ludviglundgren/qbittorrent-cli){:target="\_blank" rel="noopener noreferrer"}

---

## qbittools

qbittools is a feature-rich CLI for the management of torrents in qBittorrent.

[qbittools](https://gitlab.com/AlexKM/qbittools){:target="\_blank" rel="noopener noreferrer"}

---

## cross-seed

Fully-automatic cross-seeding

Run cross-seed 24/7 to:

- Search for cross-seeds as soon as new torrents are finished downloading
- Race torrents starting at 100% - before the uploader even joins.

[![Discord Support](https://img.shields.io/discord/880949701845872672?style=flat-square&color=4051B5&logo=discord)](https://discord.gg/jpbUFzS5Wb){:target="\_blank" rel="noopener noreferrer"}
[![Github](https://img.shields.io/github/v/release/mmgoodnow/cross-seed?color=4051B5&display_name=tag&label=Version&logo=github)](https://github.com/mmgoodnow/cross-seed){:target="\_blank" rel="noopener noreferrer"}
[![Website](https://img.shields.io/website?label=Website&url=https%3A%2F%2Fwww.cross-seed.org%2F)](https://www.cross-seed.org/){:target="\_blank" rel="noopener noreferrer"}

---

--8<-- "includes/support.md"
