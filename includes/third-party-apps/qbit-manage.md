### qbit-manage

[qbit-manage](https://github.com/StuffAnThings/qbit_manage){:target="\_blank" rel="noopener noreferrer"} tags, categorizes, and enforces share limits on qBittorrent torrents based on tracker, category, and hardlink status — the cleanup layer that sits on top of your download client rather than your \*arr apps.

- Tag-based share-limit groups (ratio, seeding time, inactivity) with a recycle bin safety net before anything is actually deleted.
- Hardlink-aware cleanup: tags (and can remove) torrents whose data is no longer hardlinked into your media library, so upgraded/replaced files don't sit seeding forever for no reason.
- Removes unregistered and orphaned torrents/files, with cross-seed-aware guards so a torrent sharing data with an active sibling is never deleted out from under it.
- Ships a Web UI and REST API in addition to the CLI/scheduler, so it doesn't require shell access to configure or trigger.
