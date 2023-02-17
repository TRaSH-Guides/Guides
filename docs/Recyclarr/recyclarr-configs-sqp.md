# Collection of Recyclarr SQP configs

Here you will find a collection of Recyclarr configs based on the SQPs.

!!! warning

    - Anything here is for private use only and not for public use. :bangbang:
    - I expect from the users that got the link to this page to honour it. :bangbang:
    - Yes, you can talk in the public channels that you use a specific SQP.
    - If others are interested they can join.

--8<-- "includes/support.md"

---

## INDEX

---

| Radarr                                                          |
| --------------------------------------------------------------- |
| [Streaming Optimized (SQP-1)](#streaming-optimized-sqp-1)       |
| [UHD Remux\|Bluray\|IMAX-E (SQP-2)](#uhd-remuxblurayimax-e-sqp-2) |
| [UHD Remux\|IMAX-E (SQP-3)](#uhd-remuximax-e-sqp-3)              |
| [UHD WEBDL\|IMAX-E (SQP-4)](#uhd-webdlimax-e-sqp-4)              |
| [UHD Bluray\|IMAX-E (SQP-5)](#uhd-blurayimax-e-sqp-5)            |

---

## Radarr

---

### Streaming Optimized (SQP-1)

??? question "Streaming Optimized (SQP-1) - [CLICK TO EXPAND]"

    - You want maximum compatibility between all devices and still a HQ releases.
    - You run 2 instances of Radarr and want both version or just for the 1080p ones.
    - You want to have minimum till none transcoding for low powered devices or remote streaming.
    - If available for you Streaming optimized. (Optimized for PLEX, emby, Jellyfin, and other streaming platforms)
    - Small sizes.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/sqp-1.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### UHD Remux|Bluray|IMAX-E (SQP-2)

??? question "UHD Remux|Bluray|IMAX-E (SQP-2) - [CLICK TO EXPAND]"

    - You got a decent audio setup. (that supports all HD audio formats)
    - You got a setup that completely supports DoVi from start to end.
    - You do want the highest quality as possible to watch but want to save space for archiving without losing video and audio quality.
    - HDR/DoVi (Depending what's offered and often both)
    - HD Audio (Atmos, TrueHD etc...)
    - You don't want to wait for the HQ Encodes to be released, to watch it.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/sqp-2.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### UHD Remux|IMAX-E (SQP-3)

??? question "UHD Remux|IMAX-E (SQP-3) - [CLICK TO EXPAND]"

    - You got a decent audio setup. (that supports all HD audio formats)
    - You got a setup that completely supports DoVi from start to end.
    - HDR/DoVi (Depending what's offered and often both)
    - HD Audio (Atmos, TrueHD etc...)
    - You want the highest quality possible, with the option to upgrade to IMAX Enhanced.

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/sqp-3.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### UHD WEBDL|IMAX-E (SQP-4)

??? question "UHD WEBDL|IMAX-E (SQP-4) - [CLICK TO EXPAND]"

    - You got a setup that completely supports DoVi from start to end.
    - HDR/DoVi (Depending what's offered and often both)
    - If available HD Audio (Atmos, TrueHD etc...)
    - You're okay with WEBDL, with the option to upgrade to IMAX Enhanced.
    - You don't need the huge Remuxes or UHD Bluray Encodes but still want HDR Formats.
    - You want a smaller files for your kids movies (Disney/Pixar etc)

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/sqp-4.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---

### UHD Bluray|IMAX-E (SQP-5)

??? question "UHD Bluray|IMAX-E (SQP-5) - [CLICK TO EXPAND]"

    - You got a decent audio setup. (that supports all HD audio formats)
    - You got a setup that completely supports DoVi from start to end.
    - You do want the highest quality as possible to watch but want to save space for archiving without losing video and audio quality.
    - HDR/DoVi (Depending what's offered and often both)
    - HD Audio (Atmos, TrueHD etc...)

??? example "YAML - [CLICK TO EXPAND]"

    ```yaml
    [[% filter indent(width=4) %]][[% include 'recyclarr-configs/radarr/sqp-5.yml' %]][[% endfilter %]]
    ```

<sub><sup>[TOP](#index)</sup>

---