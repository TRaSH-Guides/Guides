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

{! include-markdown "../../includes/third-party-apps/qui.md" !}

{! include-markdown "../../includes/third-party-apps/cross-seed.md" !}

{! include-markdown "../../includes/third-party-apps/autobrr.md" !}

## Management and Notifications

Third-party tools that handle post-download cleanup, extraction, transcoding, and notifications.

{! include-markdown "../../includes/third-party-apps/qbit-manage.md" !}

{! include-markdown "../../includes/third-party-apps/notifiarr.md" !}

{! include-markdown "../../includes/third-party-apps/unpackerr.md" !}

{! include-markdown "../../includes/third-party-apps/tdarr.md" !}

## Scripts and Resources

Community-maintained scripts and reference tooling that complement an arr-stack setup but aren't standalone applications.

{! include-markdown "../../includes/third-party-apps/daps.md" !}

{! include-markdown "../../includes/third-party-apps/bz-scripts.md" !}

{! include-markdown "../../includes/third-party-apps/baker-scripts.md" !}

## Approved Guides

Guides outside this repo that we point people to for topics TRaSH Guides doesn't cover directly.

### Servarr Wiki

The [Servarr Wiki](https://wiki.servarr.com/){:target="\_blank" rel="noopener noreferrer"} is the official wiki for Sonarr, Radarr, Lidarr, Readarr, Prowlarr, and Whisparr. It covers installation, application setup, and troubleshooting that sits outside the scope of a quality/naming guide — start there for anything app-configuration related that isn't a Custom Format or naming question.

### Davo's Community Lidarr Guide

TRaSH Guides does not maintain a Lidarr-specific guide. For Lidarr setup, we point to [Davo's Community Lidarr Guide](https://wiki.servarr.com/lidarr/community-guide){:target="\_blank" rel="noopener noreferrer"} instead.
