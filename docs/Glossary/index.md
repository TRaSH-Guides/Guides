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

Defines the minimum, preferred, and maximum file sizes for any given [Quality](#quality). Sizes are measured in megabytes per minute.

### Quality Profile

A defined group of qualities, [Custom Format](#custom-format) scores, and additional settings that can be assigned to movies, TV shows, and collections.

---

## Torrents

### Cross-Seed

The act of [seeding](#seeder) the same torrent files or data across multiple [trackers](#tracker) without re-downloading. It also refers to a [software application of the same name](https://www.cross-seed.org) that automates this process.

### Deluge

A lightweight, free, open-source, cross-platform BitTorrent client.

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

The collective group of all [Peers](#peer) of a given torrent, sharing parts of the file. This group includes both [Seeders](#seeder) and [Leechers](#leecher).

### Torrent File

A file containing metadata about the files and folders to be distributed, along with a list of network locations of [trackers](#tracker). Torrent files typically bear the extension `.torrent`.

### Tracker

Servers that assist [Peers](#peer) in locating each other and forming efficient distribution groups known as [swarms](#swarm). The term 'tracker' is also informally used for sites that host [.torrent files](#torrent-file) and operate their own tracker servers.

### Perma-Seed

Seed (some of) your torrents permanently. Most often, this is done in conjunction with [hard linked](/Hardlinks/Hardlinks-and-Instant-Moves/) files, which allows files to 'exist' in two places whilst not taking up extra hard disk space.

---

## Usenet

### Atomic Moves

This is a real file move, carried out instantaneously, not the copying of a file from the download folder to the media folder and then deleting the file from the download folder.

### Instant Moves

Same as [Atomic Moves](#atomic-moves).

### DMCA

Also known as: "DMCA takedown". The DMCA Takedown process allows creators to send notices to service providers that have material that infringes their copyright.
When this happens, you often end up with missing/incomplete parts and can't complete the download or repair it with PAR2.

[More info from the Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act){:target="\_blank" rel="noopener noreferrer"}

### N&T

Also known as "Notice&Takedown". The European equivalent of [DMCA](#dmca).

[More info from the Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Notice_and_take_down){:target="\_blank" rel="noopener noreferrer"}

### USP

Short for **U**senet **S**ervice **P**rovider

Usenet providers maintain the servers that store Usenet's content and offer you access to download files. [Indexers](#indexers) are required to search for files on Usenet to help you locate specific files within the network.

### Indexers

An indexer is essentially a search engine from which you can download NZB files. These NZB files point to the locations of different parts that make up an entire file, such as a video file. Most indexers require registration, some are invite-only.

When used in the context of Radarr/Sonarr, indexers can refer to both Usenet indexers and [torrent trackers](#tracker).

---

## Shorthand

This section lists equivalent acronyms, initialisms, or shorthand versions for various terms.

### CF

**CloudFlare**, [Custom Formats](#custom-format).

### qBit

[qBittorrent](#qbittorrent).

### QBM

[qBit Manage](#qbit-manage).

### QP

[Quality Profile](#quality-profile).
