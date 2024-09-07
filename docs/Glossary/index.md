# Glossary

This glossary provides definitions of commonly used terms and phrases, organized by application or function.

---

## Media Management Applications

**Radarr**, **Sonarr**, and **Lidarr** are applications designed to manage your media libraries:

- **Radarr**: For movies
- **Sonarr**: For TV shows
- **Lidarr**: For music

### Custom Format

A feature that matches specific aspects of a release based on information extracted from its name. Users choose the matching criteria, and Custom Formats can be assigned scores on a per-[Quality Profile](#quality-profile) basis.

### Quality

Refers to the specific release quality that describes both the source and, optionally, the resolution. Examples of qualities include **Bluray-2160p** and **Remux-1080p**, though many others exist.

### Quality Definitions

Defines the Minimum, Preferred, and Maximum file sizes for any given [Quality](#quality). Sizes are measured in megabytes per minute.

### Quality Profile

A defined group of qualities, [Custom Format](#custom-format) scores, and additional settings that can be assigned to movies, TV shows, and collections.

---

## Torrents

### Cross-Seed

The act of [seeding](#seeder) the same torrent across multiple [trackers](#tracker). It also refers to a software application of the same name that automates this process.

### Deluge

A lightweight, free, cross-platform BitTorrent client.

### qBit Manage

A program that helps manage your [qBittorrent](#qbittorrent) instance, allowing for the automation of actions on torrents based on various attributes, such as time and tracker.

### qBittorrent

A free, open-source, cross-platform BitTorrent client.

### Leecher

A BitTorrent user who is actively downloading a torrent (referred to as 'leeching'). This term can also describe users who download torrents without sharing them afterward.

### Peer

A general term that encompasses both [Seeders](#seeder) and [Leechers](#leecher).

### Seeder

BitTorrent users who possess the complete set of files in a specific torrent and are sharing them, a process known as 'seeding'.

### Swarm

The collective group of all BitTorrent users connected to a given torrent, sharing parts of the file. This group includes both [Seeders](#seeder) and [Leechers](#leecher).

### Torrent File

A file containing metadata about the files and folders to be distributed, along with a list of network locations of [trackers](#tracker). Torrent files typically bear the extension `.torrent`.

### Tracker

Servers that assist participants in locating each other and forming efficient distribution groups known as [swarms](#swarm). The term 'tracker' is also informally used for sites that host [.torrent files](#torrent-file) and operate their own tracker servers.

---

## Shorthand

This section lists equivalent acronyms, initialisms, or shorthand versions for various terms.

### CF

**CloudFlare**, [Custom Formats](#custom-format).

### qBit

[qBittorrent](#qbittorrent).

### QP

[Quality Profile](#quality-profile).
