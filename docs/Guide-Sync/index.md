# Guide Sync

These are 3rd party applications to sync several sections of the guide with your Sonarr/Radarr (or multiple).

| Feature                                                                            |     Notifiarr      |     Recyclarr      |
|------------------------------------------------------------------------------------|:------------------:|:------------------:|
| GUI (graphical user interface)                                                     | :white_check_mark: |                    |
| Radarr Custom Formats                                                              | :white_check_mark: | :white_check_mark: |
| Radarr Use Flowchart to choose the correct Custom Formats for your Quality Profile | :white_check_mark: |                    |
| Radarr predefined config files available                                           |                    | :white_check_mark: |
| Radarr Clear all Custom Formats                                                    | :white_check_mark: | :white_check_mark: |
| Radarr Scores                                                                      | :white_check_mark: | :white_check_mark: |
| Radarr Quality Settings (File Size)                                                | :white_check_mark: | :white_check_mark: |
| Radarr Naming Scheme                                                               | :white_check_mark: | :white_check_mark: |
| Radarr Quality Profiles                                                            |    :white_check_mark:                | :white_check_mark: |
| Sonarr Custom Formats                                                              | :white_check_mark: | :white_check_mark: |
| Sonarr predefined config files available                                           |                    | :white_check_mark: |
| Sonarr Clear all Release Profiles                                                  | :white_check_mark: |                    |
| Sonarr Clear all Custom Formats                                                    | :white_check_mark: | :white_check_mark: |
| Sonarr Scores                                                                      | :white_check_mark: | :white_check_mark: |
| Sonarr Quality Settings (File Size)                                                | :white_check_mark: | :white_check_mark: |
| Sonarr Naming Scheme                                                               | :white_check_mark: | :white_check_mark: |
| Sonarr Quality Profiles                                                            | :white_check_mark:                   | :white_check_mark: |

---

## Notifiarr

It's possible with [Notifiarr](https://notifiarr.com){:target="\_blank" rel="noopener noreferrer"} ([Patron feature](https://notifiarr.wiki/FAQ#patron){:target="\_blank" rel="noopener noreferrer"})

Notifiarr is a service much bigger in scope than just custom format syncing.

After setup, it's fully automated and will check every X minutes for updates to the Custom Formats or Sonarr Release Profile and will update it to your Radarr or Sonarr (Multiple Client Support).

Just enable the Custom Formats/Release Profiles you want.

??? success "Examples - [Click to show/hide]"

    Radarr Custom Formats Table
    ![!Notifiarr Custom Format Table](images/sync/notifiarr-cf-table.png)

    Radarr Custom Formats (Multiple Instances possible)
    ![!Notifiarr Custom Formats Audio](images/sync/notifiarr-cf-audio.png)

    Radarr Custom Formats (Multiple Instances possible)
    ![!Notifiarr Custom Formats HDR Formats](images/sync/notifiarr-cf-hdr.png)

    Radarr scoring (Multiple profiles possible)
    ![!Notifiarr Scores](images/sync/notifiarr-scores.png)

    Sonarr Release Profile (Multiple Instances possible)
    ![!Notifiarr Sonarr](images/sync/notifiarr-sonarr.png)

[Instructions](https://notifiarr.wiki/en/Website/Integrations/Trash){:target="\_blank" rel="noopener noreferrer"}

### Video Tutorial

!!! tip ""

    Big Thanks to IBRACORP who created a great video that covers the basics.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/DCxU3Vzaz6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    Also check out other videos from IBRACORP  [HERE](https://www.youtube.com/c/IBRACORP/videos){:target="_blank" rel="noopener noreferrer"}

---

## Recyclarr

[Info](/Recyclarr/){:target="\_blank" rel="noopener noreferrer"} // [Documentation](https://recyclarr.dev/wiki/){:target="\_blank" rel="noopener noreferrer"}

Recyclarr is a command line application utilizing configuration files to sync the guides to Radarr &
Sonarr.

--8<-- "includes/support.md"
