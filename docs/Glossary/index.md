# Glossary

This glossary provides definitions and explanations of commonly used terms, abbreviations, and phrases.

---

## A

### Atomic Move

!!! info

    Also known as: [Instant Move](#instant-move)

This action moves the file instantly, rather than copying it to a new location and deleting it from the original.

---

## B

---

## C

### CF

Depending on its context, whether discussing hosting or media management applications, this can refer to **CloudFlare** or [Custom Formats](#custom-format).

### Cross-Seed

The act of [seeding](#seeder) the same torrent files or data across multiple [trackers](#tracker) without re-downloading. It also refers to a [software application of the same name](https://www.cross-seed.org){:target="\_blank" rel="noopener noreferrer"} that automates this process.

`Cross-Seed` and `crossseed` or `xseed` often refer to the application, while `cross seed` or `xseed` can refer to the action.

### Custom Format

!!! info

    Also known as: [CF](#cf)

A feature that applies pattern matching to a release based on information inferred from the release name on the corresponding indexer during a search. Users can customize patterns in a Custom Format, which can then be assigned individual scores within each [Quality Profile](#quality-profile).

After the release has been imported, when using the TRaSH recommended naming scheme, the Custom Format score will automatically be updated to match the properties of the _actual_ media file, rather than strictly by its original naming alone.

---

## D

### Deluge

[Deluge](https://deluge-torrent.org/){:target="\_blank" rel="noopener noreferrer"} is a lightweight, free, open-source, cross-platform BitTorrent client.

### DMCA Takedown

!!! info

    Also known as: DMCA

DMCA is an abbreviation for [`Digital Millennium Copyright Act`](https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act){:target="\_blank" rel="noopener noreferrer"}.

The DMCA Takedown process allows creators to send notices to hosting/service providers that have material that infringes on their copyright.

When a DMCA takedown request is issued to a [Usenet Service Provider (USP)](#usenet-service-provider), parts of the release may end up missing or incomplete, leaving you unable to complete the extraction.

[More info from Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act){:target="\_blank" rel="noopener noreferrer"}

---

## E

---

## F

---

## G

---

## H

---

## I

### Indexer

An indexer is a search engine from which you can download NZB files. NZB files point to the locations of all the different parts that make up an entire file or release on Usenet. Most indexers require registration and some are invite-only.

When used in the context of Radarr/Sonarr/Prowlarr (or other media management software), "indexers" can refer to both Usenet indexers and [torrent trackers](#tracker).

### Instant Move

See [Atomic Move](#atomic-move).

---

## J

---

## K

---

## L

### Leecher

A BitTorrent user who is actively downloading a torrent (referred to as 'leeching'). This term can also describe those who download torrents without sharing them afterward.

### [Lidarr](../Lidarr/index.md)

An application designed to help with the automation and management of your music library. One of a group of applications, including Prowlarr, Radarr, and Sonarr, collectively known as the "arrs".

---

## M

---

## N

### Notice & Takedown

!!! info

    Also known as: N&T

The European equivalent of [DMCA](#dmca-takedown).

[More info from Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Notice_and_take_down){:target="\_blank" rel="noopener noreferrer"}

---

## O

---

## P

### PAR (PAR2) Files

PAR and PAR2 files, or 'Parity Archive Volume' files, are primarily used in Usenet to help repair incomplete or corrupted files. However, their presence does not always guarantee successful reconstruction of the original data.

### Peer

A general term that collectively refers to both [Seeders](#seeder) and [Leechers](#leecher).

### Perma-Seed

Seeding your torrents permanently ("forever"). Most often this is done in conjunction with [hard linked](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/) files, which allows files to 'exist' in two places without taking up any additional hard disk space.

### [Prowlarr](../Prowlarr/index.md)

An application designed to help with the automation and management of your [trackers](#tracker) and [indexers](#indexer). One of a group of applications, including Lidarr, Prowlarr, and Sonarr, collectively known as the "arrs".

---

## Q

### qBit Manage

!!! info

    Also known as: qbm, qbitmanage, qb_manage

[qBit Manage](https://github.com/StuffAnThings/qbit_manage){:target="\_blank" rel="noopener noreferrer"} is a tool for managing your [qBittorrent](#qbittorrent) instance. It automates actions on torrents meeting specified criteria, such as time seeded and tracker.

### qBittorrent

!!! info

    Also known as: qb, qbit, qbittorrent

[qBittorrent](https://www.qbittorrent.org/){:target="\_blank" rel="noopener noreferrer"} is a free, open-source, cross-platform BitTorrent client. Please note that it is highly recommended to avoid new major and minor (X and X.X) versions until properly validated by the community, as these often contain significant changes and/or bugs.

### Quality

Refers to the specific quality of a release, describing both the source and, optionally, the resolution. Examples of qualities include **Bluray-2160p** and **Remux-1080p**, though many others exist.

### Quality Definitions

Defines the minimum, preferred, and maximum file sizes for any given [Quality](#quality). Sizes are measured in megabytes per minute.

### Quality Profile

!!! info

    Also known as: QP

A defined group, and preferential ordering, of qualities, [Custom Format](#custom-format) scores, and additional settings that can be assigned to movies, TV shows, and collections.

---

## R

### [Radarr](../Radarr/index.md)

An application designed to help with the automation and management of your movie library. One of a group of applications, including Lidarr, Prowlarr, and Sonarr, collectively known as the "arrs".

---

## S

### Seeder

BitTorrent users who possess the complete set of files in a specific torrent and are sharing them, a process known as 'seeding'.

### [Sonarr](../Sonarr/index.md)

An application designed to help with the automation and management of your TV show/series library. One of a group of applications, including Lidarr, Prowlarr, and Radarr, collectively known as the "arrs".

### Swarm

The group of [Peers](#peer), collectively, on a specific torrent (this includes both [Seeders](#seeder) and [Leechers](#leecher)) who are actively sharing any portion of the torrent.

This can also refer to the surge of users downloading a torrent shortly after its release.

---

## T

### Torrent File

A file that contains metadata and integrity information about the files and folders associated with a torrent, as well as a list of network locations for its [trackers](#tracker). Torrent files usually have the extension `.torrent`.

### Tracker

Servers that help [Peers](#peer) locate each other and form an efficient distribution group for a torrent, known as its [swarm](#swarm). The term 'tracker' is also used commonly as a reference to sites that host [.torrent files](#torrent-file) and operate their own tracker servers.

---

## U

### Usenet Service Provider

!!! info

    Also known as: USP

Usenet providers manage the servers that store content and offer subscription-based access for downloading files. [Indexers](#indexer) are required to search for and locate releases on Usenet.

---

## V

---

## W

---

## X

---

## Y

---

## Z
