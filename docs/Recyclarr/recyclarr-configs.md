# Collection of Recyclarr configs

Here you will find a collection of Recyclarr configs based on the following guides.

- [Radarr - How to setup Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"}
- [Radarr - How to setup Quality Profiles Anime](/Radarr/radarr-setup-quality-profiles-anime){:target="_blank" rel="noopener noreferrer"}
- [Radarr - How to setup Quality Profiles French](/Radarr/radarr-setup-quality-profiles-french){:target="_blank" rel="noopener noreferrer"}
- [Sonarr - How to setup Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"}
- [Sonarr - How to setup Quality Profiles Anime](/Sonarr/sonarr-setup-quality-profiles-anime){:target="_blank" rel="noopener noreferrer"}
- [Sonarr - How to setup Quality Profiles French](/Sonarr/sonarr-setup-quality-profiles-french){:target="_blank" rel="noopener noreferrer"}

!!! danger "For the Radarr SQP you should join the discord channel `#access-to-sqp`."

--8<-- "includes/support.md"

---

## INDEX

---

| Radarr                                | Sonarr                        |
| ------------------------------------- | ----------------------------- |
| [HD Bluray + WEB](#hd-bluray-web)     | [WEB-1080p](#web-1080p)       |
| [UHD Bluray + WEB](#uhd-bluray-web)   | [WEB-2160p](#web-2160p)       |
| [Remux + WEB 1080p](#remux-web-1080p) | [Sonarr Anime](#sonarr-anime) |
| [Remux + WEB 2160p](#remux-web-2160p) |                               |
| [SQP-1](#sqp-1)                       |                               |
| [SQP-2](#sqp-2)                       |                               |
| [SQP-3](#sqp-3)                       |                               |
| [SQP-4](#sqp-4)                       |                               |
| [SQP-5](#sqp-5)                       |                               |

---

## Radarr

---

### HD Bluray + WEB

??? question "HD Bluray + WEB - [CLICK TO EXPAND]"

    If you prefer High Quality HD Encodes (Bluray-720p/1080p)

    Size: 6-15 GB for a Bluray-1080p depending on the running time.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/hd-bluray-web.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

## Sonarr

---

### WEB-1080p

??? question "WEB-1080p - [CLICK TO EXPAND]"

    If you prefer High Quality HD Encodes (Bluray-720p/1080p)

    Size: 6-15 GB for a Bluray-1080p depending on the running time.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/web-1080p-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### WEB-2160p

??? question "WEB-2160p - [CLICK TO EXPAND]"

    If you prefer High Quality HD Encodes (Bluray-720p/1080p)

    Size: 6-15 GB for a Bluray-1080p depending on the running time.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/web-2160p-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---
