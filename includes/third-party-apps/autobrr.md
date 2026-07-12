### autobrr

[autobrr](https://autobrr.com/){:target="\_blank" rel="noopener noreferrer"} watches IRC announce channels and RSS/torznab feeds and pushes matching releases straight to your download client the moment they're announced — the closest thing to instant grabs without hammering indexers with polling.

- Filters can match on release name, category, resolution, source, and more before ever touching Sonarr/Radarr.
- Pushes directly to qBittorrent (or other supported clients) — no separate `*arr` search cycle needed for the releases it catches.
- The auto-generated-filter functionality that used to live in the separate `omegabrr` project (keeping filters in sync with what's monitored in Sonarr/Radarr/Lidarr/Readarr/Whisparr) has since been folded directly into autobrr itself — `omegabrr` is now archived and deprecated, so use autobrr's own built-in equivalent instead of looking for the old standalone tool.
- Related tool: [qui](#qui) — same project, covered above, for qBittorrent management.
