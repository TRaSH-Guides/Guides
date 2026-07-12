### natorr scripts

[natorr scripts](https://github.com/BZ00001/scripts){:target="\_blank" rel="noopener noreferrer"} is a set of four standalone Python scripts for Radarr/Sonarr/Plex/Kometa maintenance, by TRaSH Guides contributor BZ00001, originally derived from DAPS modules but rewritten with no framework dependency.

- `upgradinatorr.py` — tag-based cycling search for quality upgrades across Radarr/Sonarr.
- `renameinatorr.py` — batches file/folder renames to match your naming format, using the same tag-cycle approach.
- `asset_cleanup.py` and `blocklist_cleaner.py` — prune orphaned Kometa poster assets and stale Sonarr/Radarr blocklist entries, respectively.
- Each script is self-contained (single Python file + YAML config), dry-run by default, with Discord webhook notifications — a lighter-weight alternative to DAPS for anyone who doesn't want the Docker/web-UI framework.