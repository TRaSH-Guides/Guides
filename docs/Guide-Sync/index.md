# Guide Sync

Here you will find officially supported third-party Guide Sync Tools. These tools follow the Guide guidelines.

!!! Info
    If you are the author of another TRaSH Guides sync tool and would like to be added to this list, you must also be active in our Guide Discord server for support questions. This means we can work with you if we need to make Guide changes that affect third-party sync tools.<br>If you want to be added here, please open a new post in our [#suggestions](https://discord.com/channels/492590071455940612/1021029470389403818){:target="\_blank" rel="noopener noreferrer"} section of our Discord to make a request.

These are third-party applications that sync several sections of the guide with your Sonarr/Radarr (or multiple).

## Features

Both Radarr and Sonarr share the same feature set across all the officially supported third-party Guide Sync Tools.

### Definitions

- **Custom Formats**: Sync individual custom format definitions from the TRaSH Guides.
- **Custom Format Groups**: Sync a curated bundle of related custom formats together.
- **Quality Profiles**: Sync guide-provided quality profile configurations, including qualities, groups, upgrade settings, and associated custom format scores.
- **Quality Definitions (file sizes)**: Sync recommended min/max file size limits per quality level.
- **Naming Scheme**: Sync file and folder naming patterns from the guides.
- **User-defined Custom Formats**: Author your own custom format specifications that don't exist in the TRaSH Guides. You can also add TRaSH custom formats that aren't part of a synced profile.
- **User-defined Quality Profiles**: Build a quality profile from scratch rather than starting from a guide template.
- **Score multiplier**: Apply a multiplier to all TRaSH scores in a profile (e.g., 0.5x to halve them) rather than overriding each one individually.
- **Profile cloning**: Copy an existing profile to a new name or another instance.
- **Profile renaming**: Change the display name of a synced profile.

### TRaSH-Guide sync

Syncing content from the TRaSH Guides to your Sonarr/Radarr instances.

| Feature                          |     Notifiarr      |     Recyclarr      |     Configarr      |      Clonarr       |
|----------------------------------|:------------------:|:------------------:|:------------------:|:------------------:|
| Custom Formats                   | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Custom Format Groups             | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Quality Profiles                 | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Quality Definitions (file sizes) | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Naming Scheme                    | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |

### Customization

Going beyond the guides with your own settings.

| Feature                       |     Notifiarr      |     Recyclarr      |     Configarr      |      Clonarr       |
|-------------------------------|:------------------:|:------------------:|:------------------:|:------------------:|
| User-defined Custom Formats   | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| User-defined Quality Profiles |        (1)         | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Override/modify scores        | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Score multiplier              | :white_check_mark: |  :material-minus:  |  :material-minus:  |  :material-minus:  |
| Profile cloning               | :white_check_mark: |  :material-minus:  | :white_check_mark: | :white_check_mark: |
| Profile renaming              | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Clear all Custom Formats      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |

1. Profiles are based on guide templates with customizable settings; cannot create a profile from scratch.

### Setup and operation

| Feature                           |     Notifiarr      |     Recyclarr      |     Configarr      |      Clonarr       |
|-----------------------------------|:------------------:|:------------------:|:------------------:|:------------------:|
| GUI (graphical user interface)    | :white_check_mark: |  :material-minus:  |  :material-minus:  | :white_check_mark: |
| Predefined config files/templates |  :material-minus:  | :white_check_mark: | :white_check_mark: |  :material-minus:  |
| Multi-instance support            | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Notifications                     | :white_check_mark: | :white_check_mark: |  :material-minus:  | :white_check_mark: |
| Whisparr/Readarr/Lidarr support   |  :material-minus:  |  :material-minus:  | :white_check_mark: |  :material-minus:  |

---

## Notifiarr

[Notifiarr](https://notifiarr.com){:target="\_blank" rel="noopener noreferrer"} ([Patron feature](https://notifiarr.wiki/pages/faq/faq/#q-what-are-the-user-level-differences){:target="\_blank" rel="noopener noreferrer"})

Notifiarr provides notification aggregation, system monitoring, and TRaSH Guides Sync as part of its one-time Patron paid features.

Once set up, it is fully automated and checks for updates to custom formats and guide profiles every X minutes. It then sends these updates to your Radarr and Sonarr clients.

[Instructions](https://notifiarr.wiki/pages/integrations/trash/){:target="\_blank" rel="noopener noreferrer"}

### Video Tutorial

!!! tip ""

    Big thanks to IBRACORP for creating a great video that covers the basics.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/YTpaw_qGG5E?start=270" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    Also check out other videos on the [IBRACORP YouTube channel](https://www.youtube.com/c/IBRACORP/videos){:target="_blank" rel="noopener noreferrer"}.

---

## Recyclarr

[Info](/Recyclarr/){:target="\_blank" rel="noopener noreferrer"} // [Documentation](https://recyclarr.dev/guide/){:target="\_blank" rel="noopener noreferrer"}

Recyclarr is a command-line application utilizing configuration files to sync the guides to Radarr &
Sonarr.

---

## Configarr

[GitHub](https://github.com/raydak-labs/configarr){:target="\_blank" rel="noopener noreferrer"} // [Documentation](https://configarr.raydak.de){:target="\_blank" rel="noopener noreferrer"}

Configarr is a synchronization tool primarily designed to run as a scheduled job (e.g., Cron) in containerized environments such as Docker or Kubernetes.
Configarr is compatible with the Recyclarr templates until v7.4.0.
It enables the use of all Custom Formats and Quality Profiles defined in TRaSH-Guides while also allowing users to create new Custom Formats tailored to their specific setup.

Main features are:

- Supports all TRaSH Guide–provided JSON structures (Custom Formats, Quality Profiles, Naming).
- Customizability: Create and adjust everything as you need for your setup, like your own CustomFormats, different QualityProfiles, ...
- Container focus for best support in Docker and Kubernetes environments
- more in the Configarr docs

---

## Clonarr

![GitHub Release](https://img.shields.io/github/v/release/ProphetSe7en/clonarr?label=latest) ![GitHub last commit](https://img.shields.io/github/last-commit/ProphetSe7en/clonarr/main?label=last%20commit)

[GitHub](https://github.com/ProphetSe7en/clonarr){:target="\_blank" rel="noopener noreferrer"} // [Documentation](https://github.com/ProphetSe7en/clonarr/blob/main/docs/GETTING-STARTED.md){:target="\_blank" rel="noopener noreferrer"}

TRaSH Guides sync tool for Radarr and Sonarr featuring a built-in web UI. Easily browse, customize, and sync Custom Formats, Quality Profiles, Scores, and Quality Sizes — no YAML configs, no CLI, just a browser.

Designed as an alternative to config-driven tools like Recyclarr, with a visual interface for creating, testing, and deploying TRaSH profiles.

![Clonarr Preview](https://raw.githubusercontent.com/ProphetSe7en/clonarr/refs/heads/main/docs/images/clonarr-preview.gif)

For questions, help, or bug reports:

- **Discord:** [`#clonarr`](https://discord.com/channels/492590071455940612/1495685561552207913) on the [TRaSH Guides Discord](https://trash-guides.info/discord) (under Community Apps)
- **GitHub:** [prophetse7en/clonarr/issues](https://github.com/prophetse7en/clonarr/issues)

---

--8<-- "includes/support.md"
