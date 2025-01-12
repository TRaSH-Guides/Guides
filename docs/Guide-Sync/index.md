# Guide Sync

Here you will find officially supported third-party party Guide Sync Tools. These tools follow the Guide guidelines.

!!! Info
    If you are the author of another TRaSH Guides sync tool and would like to be added to this list, you must also be active in our Guide Discord server for support questions. This means we can work with you if we need to make Guide changes that affect third-party sync tools.<br>If you want to be added here, please open a new post in our [#suggestions](https://discord.com/channels/492590071455940612/1021029470389403818){:target="\_blank" rel="noopener noreferrer"} section of our Discord to make a request.

These are third-party applications that sync several sections of the guide with your Sonarr/Radarr (or multiple).

## Radarr Features

| Radarr Features                                                                    |     Notifiarr      |     Recyclarr      |     Configarr      |
| ---------------------------------------------------------------------------------- | :----------------: | :----------------: | :----------------: |
| GUI (graphical user interface)                                                     | :white_check_mark: |                    |                    |
| Custom Formats                                                                     | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Interactive Flowchart (choose the correct Custom Formats for your Quality Profile) | :white_check_mark: |                    |                    |
| Predefined config files available (editable to personal preferences)               |                    | :white_check_mark: | :white_check_mark: |
| Predefined profiles sync (with several personal selectable options)                | :white_check_mark: |                    |                    |
| Clear all Custom Formats                                                           | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Scores                                                                             | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Quality Settings (File Size)                                                       | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Naming Scheme                                                                      | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Quality Profiles                                                                   | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Sonarr Features

| Sonarr Features                                                      |     Notifiarr      |     Recyclarr      |     Configarr      |
| -------------------------------------------------------------------- | :----------------: | :----------------: | :----------------: |
| GUI (graphical user interface)                                       | :white_check_mark: |                    |                    |
| Custom Formats                                                       | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Predefined config files available (editable to personal preferences) |                    | :white_check_mark: | :white_check_mark: |
| Predefined profiles sync (with several personal selectable options)  | :white_check_mark: |                    |                    |
| Clear all Custom Formats                                             | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Scores                                                               | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Quality Settings (File Size)                                         | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Naming Scheme                                                        | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Quality Profiles                                                     | :white_check_mark: | :white_check_mark: | :white_check_mark: |

---

### Notifiarr

[Notifiarr](https://notifiarr.com){:target="\_blank" rel="noopener noreferrer"} ([Patron feature](https://notifiarr.wiki/FAQ#q-what-are-the-user-level-differences){:target="\_blank" rel="noopener noreferrer"})

Notifiarr provides notification aggregation, system monitoring, and TRaSH Guides Sync as part of its Patron paid features.

Once set up, it is fully automated and checks for updates to custom formats and guide profiles every X minutes. It then sends these updates to your Radarr and Sonarr clients.

[Instructions](https://notifiarr.wiki/en/Website/Integrations/Trash){:target="\_blank" rel="noopener noreferrer"}

#### Video Tutorial

!!! tip ""

    Big thanks to IBRACORP, who created a great video that covers the basics.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/DCxU3Vzaz6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    Also check out other videos from IBRACORP  [HERE](https://www.youtube.com/c/IBRACORP/videos){:target="_blank" rel="noopener noreferrer"}

---

### Recyclarr

[Info](/Recyclarr/){:target="\_blank" rel="noopener noreferrer"} // [Documentation](https://recyclarr.dev/wiki/){:target="\_blank" rel="noopener noreferrer"}

Recyclarr is a command line application utilizing configuration files to sync the guides to Radarr &
Sonarr.

## Configarr

[Github](https://github.com/raydak-labs/configarr){:target="\_blank" rel="noopener noreferrer"} // [Documentation](https://configarr.raydak.de){:target="\_blank" rel="noopener noreferrer"}

Configarr is a synchronization tool primarily designed to run as a scheduled job (e.g., Cron) within containerized environments like Docker or Kubernetes.
Configarr is compatible with the Recyclarr templates until v7.4.0.
It enables the use of all Custom Formats and Quality Profiles defined in TRaSH-Guides while also allowing users to create new Custom Formats tailored to their specific setup.

Main features are:

- Support all of TRaSH-Guide provided JSON structures (CustomFormats, QualityProfiles, Naming)
- Customizability: Create and adjust everything as you need for your setup like own CustomFormats, different QualityProfiles, ...
- Container focus for best support in Docker and Kubernetes environments
- more in the Configarr docs

--8<-- "includes/support.md"
