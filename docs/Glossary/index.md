# Glossary

A list of commonly used words and terms, grouped by application or function.

---

## Radarr, Sonarr and Lidarr

These applications manage your media libraries, for movies, TV and music respectively.

### Custom Format

An object in Radarr, Sonarr and Lidarr that will match aspects of any given release based on data captured from its name. Matching criteria are set by the user. Custom formats can be assigned scores on a per-[Quality Profile](#quality-profile) basis.

### Quality

A specific release quality describing the source and optionally resolution, for example Bluray-2160p or Remux-1080p.

### Quality Definitions

Minimum, Preferred and Maximum file sizes for any given [Quality](#quality). Measured in megabytes per minute.

### Quality Profile

A named grouping of qualities, [Custom Format](#custom-format) scores, and other settings that movies, TV shows and collections can be assigned to.

---

## Torrents

### Cross-Seed

The act of [seeding](#seeder) the same torrent to multiple [trackers](#tracker). Also refers to the application of the same name that automates this process.

### Deluge

A lightweight, Free Software, cross-platform BitTorrent client.

### qBit Manage

A program used to manage your [qBittorrent](#qbittorrent) instance, and automate actions against torrents based on their time, tracker, and other attributes.

### qBittorrent

A free, cross-platform and open-source BitTorrent client.

### Leecher

A BitTorrent user who is actively downloading a torrent. This is known as 'leeching' Also a term used to refer to users who download torrents but do not seed them afterwards.

### Peer

A general name for both [Seeders](#seeder) and [Leechers](#leecher).

### Seeder

BitTorrent users who have a complete copy of all the files in a single torrent, and are sharing them. This is known as 'seeding'.

### Swarm

All BitTorrent users for any given torrent that are connected and sharing any part of the file. Made up of 'seeders' and 'leechers'.

### Torrent File

A file that contains metadata about files and folders to be distributed, and usually also a list of the network locations of [trackers](#tracker). Torrent files have the extension .torrent.

### Tracker

Computers that help participants in the system find each other and form efficient distribution groups called [swarms](#swarm). 'Tracker' is also an informal name given to sites that host [.torrent files](#torrent-file) and run their own tracker.

---

## Shorthand

Many words and terms also have equivalent acronyms, initialisms or shorthand versions.

### CF

CloudFlare, [Custom Formats](#custom-format).

### qBit

[qBittorrent](#qbittorrent).

### QP

[Quality Profile](#quality-profile).
