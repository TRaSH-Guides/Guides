# Setup Guide

## Docker Compose

```yaml
services:
  bindery:
    image: ghcr.io/vavallee/bindery:latest
    container_name: bindery
    restart: unless-stopped
    ports:
      - "8787:8787"
    volumes:
      - /path/to/config:/config
      - /path/to/books:/books
      - /path/to/downloads:/downloads
    user: "1000:1000"
    environment:
      - TZ=America/New_York
```

Set `user` to the UID:GID that owns your library and download directories (`id -u`:`id -g`). Mismatched UID is the most common cause of permission errors on import.

!!! warning "Path consistency"
    The path Bindery sees inside the container must match the path the download client sees. If qBittorrent maps downloads to `/downloads` and Bindery maps them to `/data/downloads`, import will fail. Use the same bind-mount path in both containers, or configure a path remap under **Settings → Download Clients → Remote Path Mappings**.

---

## First run

Navigate to `http://localhost:8787`. The setup wizard creates the first admin account — pick a strong password, there's no second prompt.

API key is under **Settings → General → Security**. You'll need it when adding Bindery as an app in other tools.

---

## Prowlarr

**Settings → Indexers → Add Prowlarr instance.**

| Field | Value |
|---|---|
| Host | Prowlarr hostname or container name (e.g. `prowlarr`) |
| Port | `9696` |
| API Key | Prowlarr API key (**Settings → General**) |
| Sync Categories | `Books/EBook`, `Books/Comics`, `Books/Mags`, `Books/Technical`, `Audio/Audiobook` — uncheck anything you don't want |

Hit **Test**, then **Save**. Bindery pulls the indexer list from Prowlarr automatically; individual indexers don't need to be added manually.

!!! note "Container networking"
    When both containers are on the same Docker network, use the service name as the hostname (`prowlarr`, not `localhost`). Add `networks` to your Compose file if they're not already on a shared network.

---

## Download client

**Settings → Download Clients → Add.**

=== "qBittorrent"

    | Field | Value |
    |---|---|
    | Host | qBittorrent hostname or container name |
    | Port | `8080` (default) |
    | Username / Password | qBittorrent credentials |
    | Category | `books` (optional but recommended — keeps Bindery grabs separate) |

=== "SABnzbd"

    | Field | Value |
    |---|---|
    | Host | SABnzbd hostname or container name |
    | Port | `8080` (default) |
    | API Key | **Config → General → API Key** in SABnzbd |
    | Category | `books` |

=== "NZBGet"

    | Field | Value |
    |---|---|
    | Host | NZBGet hostname or container name |
    | Port | `6789` (default) |
    | Username / Password | NZBGet credentials |
    | Category | `books` |

=== "Transmission"

    | Field | Value |
    |---|---|
    | Host | Transmission hostname or container name |
    | Port | `9091` (default) |
    | Username / Password | Transmission credentials (if RPC auth is enabled) |

Hit **Test** before saving. Bindery fetches torrent/NZB content itself and sends it to the client directly — the download client never needs to reach the indexer URL, so Docker-internal hostnames work without extra configuration.

---

## Library path

**Settings → General → Library Path.** Set this to the bind-mounted path where you want books to live (e.g. `/books`). This is the import destination, not the download directory.

---

## Adding authors

**Authors → Add Author.** Search by name. Bindery pulls metadata from Hardcover (default) or OpenLibrary.

- **Monitor** — which books to watch for: All, Future, Missing, Existing, or None.
- **Quality Profile** — format and size preferences (EPUB, M4B, MP3, etc.).
- **Search on add** — triggers an immediate indexer search for monitored missing books.

Once an author is added, Bindery polls for new releases and grabs them automatically when they appear on your indexers.

---

## Common issues

**Import fails with permission denied**
: UID/GID mismatch. Verify the `user:` directive in your Compose file matches the owner of `/books` and `/downloads` on the host (`id -u`:`id -g`).

**Download client test fails when using container names**
: The containers need to be on the same Docker network. Add a shared `networks` entry to your Compose file.

**Prowlarr indexers not appearing after save**
: Hit **Test** before saving — Bindery won't sync the indexer list without a successful connectivity check.

**Books found but not importing**
: Check the Activity log (**Activity → History**) for the specific failure reason. Common causes: path mismatch (see path consistency warning above), quality below profile minimum, or a duplicate already in the library.
