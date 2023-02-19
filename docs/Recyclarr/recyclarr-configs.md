# Collection of Recyclarr configs

Here you will find a collection of Recyclarr configs based on the following guides:

- [Radarr - How to setup Quality Profiles](/Radarr/radarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"}
- [Radarr - How to setup Quality Profiles Anime](/Radarr/radarr-setup-quality-profiles-anime){:target="_blank" rel="noopener noreferrer"}
- [Sonarr - How to setup Quality Profiles](/Sonarr/sonarr-setup-quality-profiles){:target="_blank" rel="noopener noreferrer"}
- [Sonarr - How to setup Quality Profiles Anime](/Sonarr/sonarr-setup-quality-profiles-anime){:target="_blank" rel="noopener noreferrer"}
- [Sonarr - How to setup Quality Profiles French](/Sonarr/sonarr-setup-quality-profiles-french){:target="_blank" rel="noopener noreferrer"}

<!--- [Radarr - How to setup Quality Profiles French](/Radarr/radarr-setup-quality-profiles-french){:target="_blank" rel="noopener noreferrer"}-->

--8<-- "includes/support.md"

---

## INDEX

---

| Radarr                                | Sonarr                                              |
| ------------------------------------- | --------------------------------------------------- |
| [HD Bluray + WEB](#hd-bluray-web)     | [WEB-1080p](#web-1080p)                             |
| [UHD Bluray + WEB](#uhd-bluray-web)   | [WEB-2160p](#web-2160p)                             |
| [Remux + WEB 1080p](#remux-web-1080p) | [Anime (Sonarr)](#anime-sonarr)                     |
| [Remux + WEB 2160p](#remux-web-2160p) | [French WEB-1080p MULTi](#french-web-1080p-multi)   |
| [Anime (Radarr)](#anime-radarr)       | [French WEB-1080p VOSTFR](#french-web-1080p-vostfr) |
|                                       | [French Anime MULTi](#french-anime-multi)           |
|                                       | [French Anime VOSTFR](#french-anime-vostfr)         |

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

### UHD Bluray + WEB

??? question "UHD Bluray + WEB - [CLICK TO EXPAND]"

    If you prefer High Quality UHD Encodes (Bluray-2160p)

    Size: 20-60 GB for a Bluray-2160p depending on the running time.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/uhd-bluray-web.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### Remux + WEB 1080p

??? question "Remux + WEB 1080p - [CLICK TO EXPAND]"

    If you prefer 1080p Remuxes (Remux-1080p)

    Size: 20-40 GB for a Remux-1080p depending on the running time.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/remux-web-1080p.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### Remux + WEB 2160p

??? question "Remux + WEB 2160p - [CLICK TO EXPAND]"

    If you prefer 2160p Remuxes (Remux-2160p)

    Size: 40-100 GB for a Remux-2160p depending on the running time.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/remux-web-2160p.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### Anime (Radarr)

??? question "Anime (Radarr) - [CLICK TO EXPAND]"

    It's recommended to run two Radarr instances. One for Anime Movies and one for Normal Movies, or you can make use of Quality Profiles and score different Custom Formats (CFs) as required.

    The aim of this guide is to grab the best release overall (as per [SeaDex](https://sneedex.moe/){:target="_blank" rel="noopener noreferrer"}) and not necessarily just dual audio.
    The vast majority of releases can be found on [Nyaa](https://nyaa.si/){:target="_blank" rel="noopener noreferrer"} or [AB](https://animebytes.tv/){:target="_blank" rel="noopener noreferrer"}

    !!! info ""
        Nyaa is a public tracker while AB is an invite only tracker.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/anime.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

## Sonarr

---

### WEB-1080p

??? question "WEB-1080p - [CLICK TO EXPAND]"

    If you prefer 720p/1080p WEBDL (WEB-1080p)

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/web-1080p-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### WEB-2160p

??? question "WEB-2160p - [CLICK TO EXPAND]"

    If you prefer 2160p WEBDL (WEB-2160p)

    The only deal breaker with 2160p is when you get them with DV/HDR, 2160p without DV/HDR is a minimal profit.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/web-2160p-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### Anime (Sonarr)

??? question "Anime (Sonarr) - [CLICK TO EXPAND]"

    It's recommended to run two Sonarr instances. One for Anime and one for normal TV shows, or you can make use of Quality Profiles and score different Custom Formats (CFs) as required.

    The aim of this guide is to grab the best release overall (as per [SeaDex](https://sneedex.moe/){:target="_blank" rel="noopener noreferrer"}) and not necessarily just dual audio.
    The vast majority of releases can be found on [Nyaa](https://nyaa.si/){:target="_blank" rel="noopener noreferrer"} or [AB](https://animebytes.tv/){:target="_blank" rel="noopener noreferrer"}

    !!! info ""
        Nyaa is a public tracker while AB is an invite only tracker.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/anime-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### French WEB-1080p MULTi

??? question "French WEB-1080p MULTi - [CLICK TO EXPAND]"

    If you prefer 720p/1080p WEBDL (WEB-1080p) - French MULTi

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/french-web-1080p-multi-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### French WEB-1080p VOSTFR

??? question "French WEB-1080p VOSTFR - [CLICK TO EXPAND]"

    If you prefer 720p/1080p WEBDL (WEB-1080p) - French VOSTFR

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/french-web-1080p-vostfr-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### French Anime MULTi

??? question "French Anime MULTi - [CLICK TO EXPAND]"

    If you are looking to grab Anime with MULTi audio (original + French).

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/french-anime-multi-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### French Anime VOSTFR

??? question "French Anime VOSTFR - [CLICK TO EXPAND]"

    If you are looking to grab Anime with French sub (VOSTFR)

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/sonarr/french-anime-vostfr-v4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---
