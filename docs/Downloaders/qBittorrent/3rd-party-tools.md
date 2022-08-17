# 3rd Party tools

Here you will find a collection of 3rd party tools and other related links for qBittorrent.

## qBit Manage

This is a program used to manage your qBittorrent instance such as:

- Tag torrents based on tracker URL and set seed goals/limit upload speed by tag (only tag torrents that have no tags)
- Update categories based on save directory
- Remove unregistered torrents (delete data & torrent if it is not being cross-seeded, otherwise it will just remove the torrent)
- Automatically add cross-seed torrents in paused state. *Note: cross-seed now allows for torrent injections directly to qBit, making this feature obsolete.*
- Recheck paused torrents sorted by lowest size and resume if completed
- Remove orphaned files from your root directory that are not referenced by qBittorrent
- Tag any torrents that have no hard links and allows optional cleanup to delete these torrents and contents based on maximum ratio and/or time seeded
- RecycleBin function to move files into a RecycleBin folder instead of deleting the data directly when deleting a torrent
- Built-in scheduler to run the script every x minutes. (Can use --run command to run without the scheduler)
- Webhook notifications with Notifiarr and Apprise API integration.

[qBit Manage](https://github.com/StuffAnThings/qbit_manage){:target="_blank" rel="noopener noreferrer"}

------

## qbittorrent-cli

A cli to manage qBittorrent. Add torrents, reannounce and import from other clients.

- Add torrents to qBittorrent from file or magnet link. Useful in combination with autodl-irssi
- Reannounce torrents for troublesome trackers
- Set limits on how many simultaneously active downloads are allowed
- Import torrents with state from Deluge and rTorrent

[qbittorrent-cli](https://github.com/ludviglundgren/qbittorrent-cli){:target="_blank" rel="noopener noreferrer"}

------

## qbittools

qbittools is a feature rich CLI for the management of torrents in qBittorrent.

[qbittools](https://gitlab.com/AlexKM/qbittools){:target="_blank" rel="noopener noreferrer"}

------

## A Dark but not black qBittorrent WebUI

A darker theme for qBittorrent WebUI (made with the help of the Walkerservers community)

- It's dark, but not black
- It has different colors for ratio-values (see screenshot)
- It has a mix of Fontawesome and custom icons

![!Example](https://raw.githubusercontent.com/brettpetch/nightwalker/main/preview.png)

[Nightwalker](https://github.com/brettpetch/nightwalker){:target="_blank" rel="noopener noreferrer"}

------

## cross-seed

Fully-automatic cross-seeding

Run cross-seed 24/7 to:

- Search for cross-seeds as soon as new torrents are finished downloading
- Race starting at 100% before the uploader even joins.

[![Discord Support](https://img.shields.io/discord/880949701845872672?style=flat-square&color=4051B5&logo=discord)](https://discord.gg/jpbUFzS5Wb){:target="_blank" rel="noopener noreferrer"}
[![Github](https://img.shields.io/github/v/release/mmgoodnow/cross-seed?color=4051B5&display_name=tag&label=Version&logo=github)](https://github.com/mmgoodnow/cross-seed){:target="_blank" rel="noopener noreferrer"}
[![Website](https://img.shields.io/website?label=Website&url=https%3A%2F%2Fwww.cross-seed.org%2F)](https://www.cross-seed.org/){:target="_blank" rel="noopener noreferrer"}

------

{! include-markdown "../../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
