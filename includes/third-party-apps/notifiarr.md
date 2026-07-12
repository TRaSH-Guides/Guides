### Notifiarr

[Notifiarr](https://notifiarr.com/){:target="\_blank" rel="noopener noreferrer"} is a hosted Discord bot paired with an optional self-hosted client that aggregates events from your media stack into unified, richly-formatted Discord notifications.

- Two-part architecture: the Discord bot itself is Notifiarr-managed (no bot-hosting required); a separate open-source client daemon runs on your own host to read local app data and push it up.
- Broad integration roster: Starr apps, Plex/Emby/Jellyfin, Overseerr/Jellyseerr, Unpackerr, autobrr, cross-seed, qbit-manage, and infra tools like Watchtower and Uptime Kuma, plus generic Apprise passthrough for anything not natively supported.
- Rich embeds (poster art, queue/episode detail) and scheduled dashboard/health snapshots, not just event-driven pings — distinct from wiring a raw per-app Discord webhook yourself.
- TRaSH Guides Sync is also available, gated behind a one-time [Patron donation](https://notifiarr.wiki/pages/faq/faq/#q-what-are-the-user-level-differences){:target="\_blank" rel="noopener noreferrer"} and run through the self-hosted client — full details on the [Guide Sync](../../docs/Guide-Sync/index.md) page. This entry is about the free notification/monitoring platform.
