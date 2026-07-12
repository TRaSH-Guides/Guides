# Third-Party Apps and Approved Guides

This page lists community tools and guides that complement the TRaSH Guides ecosystem. These are not TRaSH Guides projects — they are built and maintained by third parties, listed here because they are widely used alongside the guide and worth knowing about.

!!! info "Guide Sync Tools live elsewhere"
    Looking for a tool that syncs Custom Formats, Quality Profiles, or Naming Schemes from the guide into Sonarr/Radarr (Recyclarr, Notifiarr, Configarr, Clonarr)? Those are covered in detail, with a full feature comparison, on the [Guide Sync](../Guide-Sync/index.md) page — including the requirements to get a new sync tool added there.

## Minimum requirements to be listed

We keep this list intentionally small. An app is only added here if it:

- Follows the guide — its defaults and recommended setup don't fight the folder structure, naming scheme, or Custom Format conventions described elsewhere in these docs.
- Shares the same [folder structure](../File-and-Folder-Structure/index.md) rather than inventing its own.
- Makes direct use of the guide's Custom Formats/data (via [Guide-Sync](../Guide-Sync/index.md) JSON, or by reading TRaSH-published data directly) rather than reimplementing scoring from scratch.

If you maintain a tool you think belongs here, open a request in [#suggestions](https://discord.com/channels/492590071455940612/1021029470389403818){:target="\_blank" rel="noopener noreferrer"} on the TRaSH Discord.

## Download Automation

Third-party tools that automate cross-seeding and searching on top of your existing Sonarr/Radarr/Prowlarr setup.

| App | Description |
| --- | --- |
| [qui](https://github.com/autobrr/qui){:target="\_blank" rel="noopener noreferrer"} | Multi-instance qBittorrent web UI from the autobrr project. A background automation engine scans on a roughly 20-second interval and can act on torrents by tag, category, speed/share limits, or force recheck/reannounce. |
| [cross-seed](https://www.cross-seed.org/){:target="\_blank" rel="noopener noreferrer"} | Finds and injects cross-seedable torrents across your indexers, matched against your existing library, so a single piece of media can seed to multiple trackers without duplicating files on disk. Supports both on-demand and continuous RSS/announce-driven matching. |
| [autobrr](https://autobrr.com/){:target="\_blank" rel="noopener noreferrer"} | Watches IRC announce channels and RSS/torznab feeds and pushes matching releases straight to your download client the moment they're announced. Filters match on release name, category, resolution, and source before ever touching Sonarr/Radarr. |

## Management and Notifications

Third-party tools that handle post-download cleanup, extraction, subtitles, and notifications.

| App | Description |
| --- | --- |
| [qbit-manage](https://github.com/StuffAnThings/qbit_manage){:target="\_blank" rel="noopener noreferrer"} | Tags, categorizes, and enforces share limits on qBittorrent torrents by tracker, category, and hardlink status. Hardlink-aware cleanup plus removal of unregistered/orphaned torrents, with cross-seed-aware guards so shared data isn't deleted out from under an active sibling. |
| [Notifiarr](https://notifiarr.com/){:target="\_blank" rel="noopener noreferrer"} | Hosted Discord bot paired with an optional self-hosted client that aggregates events from Starr apps, Plex/Emby/Jellyfin, Overseerr/Jellyseerr, and infra tools into unified Discord notifications — no bot-hosting required. |
| [Unpackerr](https://github.com/Unpackerr/unpackerr){:target="\_blank" rel="noopener noreferrer"} | Extracts compressed downloads (Rar/Zip/7-Zip/Gzip/ISO, including nested archives) so Sonarr/Radarr/Lidarr/Readarr can import them, polling each app's own API for queued imports, then deletes the extracted copies once import succeeds. |
| [Bazarr](https://www.bazarr.media/){:target="\_blank" rel="noopener noreferrer"} | Searches, downloads, and syncs subtitles for your Sonarr/Radarr library from multiple providers, with sync-score based automatic subtitle-sync tuning. |

## Scripts and Resources

Community-maintained scripts and reference tooling that complement an arr-stack setup but aren't standalone applications.

### DAPS (Drazzilb's Arr PMM Scripts)

[DAPS](https://github.com/Drazzilb08/daps){:target="\_blank" rel="noopener noreferrer"} is a collection of media-library automation modules run via Docker with a built-in web UI (port 8000) rather than flat YAML-only config. 11 modules including:

- `poster_renamerr`, `border_replacerr`, `poster_cleanarr` — Kometa/Plex poster asset management
- `upgradinatorr` — tag-based quality-upgrade search cycling
- `nohl` — no-hardlink detection
- `unmatched_assets`, `health_checkarr`, `jduparr`, `labelarr`, `sync_gdrive`

### natorr scripts

[natorr scripts](https://github.com/BZ00001/scripts){:target="\_blank" rel="noopener noreferrer"} is a set of four standalone Python scripts for Radarr/Sonarr/Plex/Kometa maintenance by TRaSH Guides contributor BZ00001, originally derived from DAPS modules but rewritten with no framework dependency. Each is a self-contained Python file + YAML config, dry-run by default, with Discord webhook notifications:

- [`upgradinatorr.py`](https://github.com/BZ00001/scripts/blob/main/upgradinatorr/upgradinatorr.py){:target="\_blank" rel="noopener noreferrer"} — tag-based cycling search for quality upgrades across Radarr/Sonarr
- [`renameinatorr.py`](https://github.com/BZ00001/scripts/blob/main/renameinatorr/renameinatorr.py){:target="\_blank" rel="noopener noreferrer"} — batches file/folder renames to match your naming format, using the same tag-cycle approach
- [`asset_cleanup.py`](https://github.com/BZ00001/scripts/blob/main/asset_cleanup/asset_cleanup.py){:target="\_blank" rel="noopener noreferrer"} — prunes orphaned Kometa poster assets
- [`blocklist_cleaner.py`](https://github.com/BZ00001/scripts/blob/main/blocklist_cleaner/blocklist_cleaner.py){:target="\_blank" rel="noopener noreferrer"} — prunes stale Sonarr/Radarr blocklist entries

### baker-scripts

The [baker-scripts](https://github.com/baker-scripts){:target="\_blank" rel="noopener noreferrer"} org hosts several smaller, focused utilities for Starr-app and homelab workflows:

- [StarrScripts](https://github.com/baker-scripts/StarrScripts){:target="\_blank" rel="noopener noreferrer"} — shell scripts covering \*arr update/trigger automation, including cross-seed/qui triggers on import and duplicate-file detection
- [docs-templates](https://github.com/baker-scripts/docs-templates){:target="\_blank" rel="noopener noreferrer"} — MkDocs documentation templates, including a templatized Plex setup guide for standing up your own user-facing Plex documentation with variable substitution
- [docker-compose-debugger](https://github.com/baker-scripts/docker-compose-debugger){:target="\_blank" rel="noopener noreferrer"} — browser-based, client-side-only tool that parses and sanitizes `docker compose config` output, redacting secrets before you share a compose file in a support channel

## Approved Guides

Guides outside this repo that we point people to for topics TRaSH Guides doesn't cover directly.

### Servarr Wiki

The [Servarr Wiki](https://wiki.servarr.com/){:target="\_blank" rel="noopener noreferrer"} is the official wiki for Sonarr, Radarr, Lidarr, Readarr, Prowlarr, and Whisparr. It covers installation, application setup, and troubleshooting that sits outside the scope of a quality/naming guide — start there for anything app-configuration related that isn't a Custom Format or naming question.

### Davo's Community Lidarr Guide

TRaSH Guides does not maintain a Lidarr-specific guide. For Lidarr setup, we point to [Davo's Community Lidarr Guide](https://wiki.servarr.com/lidarr/community-guide){:target="\_blank" rel="noopener noreferrer"} instead.
