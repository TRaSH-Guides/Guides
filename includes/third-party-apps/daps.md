### DAPS (Drazzilb's Arr PMM Scripts)

[DAPS](https://github.com/Drazzilb08/daps){:target="\_blank" rel="noopener noreferrer"} is a collection of media-library automation modules covering poster/asset management for Kometa (Plex Meta Manager), upgrade-search cycling, and library hygiene, run via a Docker container with a built-in web UI.

- 11 modules including `poster_renamerr`, `border_replacerr`, and `poster_cleanarr` (Kometa/Plex poster asset management), `upgradinatorr` (tag-based quality-upgrade search cycling), `nohl` (no-hardlink detection), `unmatched_assets`, `health_checkarr`, `jduparr`, `labelarr`, and `sync_gdrive`.
- Ships as a Docker image with a web UI (port 8000) for configuration, rather than flat YAML-only config.
