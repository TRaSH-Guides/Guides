# Getting Started

New to TRaSH-Guides? This page walks you through the recommended order for setting up your media server, from the ground up. Follow the steps in order.

## 1. Set Up Shares and Folder Structure

Before installing any applications, set up a proper share and folder structure. This is the foundation on which everything else depends. It enables [hardlinks](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#what-are-hardlinks){:target="\_blank" rel="noopener noreferrer"} and [instant moves](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#what-are-instant-moves-atomic-moves){:target="\_blank" rel="noopener noreferrer"}, so your files can be hardlinked and/or moved between folders without duplicating data or waiting for long imports.

[Optimal Shares and Folders](/File-and-Folder-Structure/){ .md-button target="\_blank" rel="noopener noreferrer" }

---

## 2. Set Up Your Download Client

Next, install and configure your preferred download client. This is what Radarr and Sonarr will use to import your wanted releases. Configure your download client with the correct categories and paths, so [hardlinks](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#what-are-hardlinks){:target="\_blank" rel="noopener noreferrer"} and [instant moves](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/#what-are-instant-moves-atomic-moves){:target="\_blank" rel="noopener noreferrer"} work.

[Set Up Your Download Client](/Downloaders/){ .md-button target="\_blank" rel="noopener noreferrer" }

---

## 3. Set Up Your Official *Arr Apps

With your folders and download client ready, set up your *Arr apps.

### Radarr

<sub><sup>For Installation, Quick Start Guide, and the basics of Radarr, please check the official [WikiArr](https://wiki.servarr.com/en/radarr){:target="\_blank" rel="noopener noreferrer"}.</sup></sub>

Follow these guides on the Radarr page, in order:

1. [Quality Settings (File Size)](/Radarr/Radarr-Quality-Settings-File-Size/){:target="\_blank" rel="noopener noreferrer"} - Some recommendations to prevent low-quality or fake releases. These quality file size settings have been created and tested using information gathered from release comparisons across various sources and from the community.
1. [Recommended naming scheme](/Radarr/Radarr-recommended-naming-scheme/){:target="\_blank" rel="noopener noreferrer"} - Recommended naming scheme provided with the help of the Sonarr/Radarr (Support) Team and information provided by the community to prevent download loops.
1. [How to set up Quality Profiles](/Radarr/radarr-setup-quality-profiles/){:target="\_blank" rel="noopener noreferrer"} - How to make the most of the Custom Formats, including specifics of our recommended configuration. You can use these examples to understand how to set up your preferences.
    - [How to set up Quality Profiles Anime](/Radarr/radarr-setup-quality-profiles-anime/){:target="\_blank" rel="noopener noreferrer"} - Same as above but specific for anime.
    - [How to set up Quality Profiles (French)](/Radarr/radarr-setup-quality-profiles-french-en/){:target="\_blank" rel="noopener noreferrer"} - Same as above but specific for French and English Audio.
    - [How to set up Quality Profiles (German)](/Radarr/radarr-setup-quality-profiles-german-en/){:target="\_blank" rel="noopener noreferrer"} - Same as above but specific for German and English Audio.

More tips for Radarr are available on the [Radarr guides page](/Radarr/#available-guides){:target="\_blank" rel="noopener noreferrer"}.

### Sonarr

<sub><sup>For Installation, Quick Start Guide, and the basics of Sonarr, please check the official [WikiArr](https://wiki.servarr.com/en/sonarr){:target="\_blank" rel="noopener noreferrer"}.</sup></sub>

Once Radarr is configured, do the same for Sonarr and your TV library.

Follow these guides on the Sonarr page, in order:

1. [Quality Settings (File Size)](/Sonarr/Sonarr-Quality-Settings-File-Size/){:target="\_blank" rel="noopener noreferrer"} - Some recommendations to prevent low-quality or fake releases. These quality file size settings have been created and tested using information gathered from release comparisons across various sources and from the community.
1. [Recommended naming scheme](/Sonarr/Sonarr-recommended-naming-scheme/){:target="\_blank" rel="noopener noreferrer"} - Recommended naming scheme provided with the help of the Sonarr/Radarr (Support) Team and information provided by the community to prevent download loops.
1. [How to set up Quality Profiles](/Sonarr/sonarr-setup-quality-profiles/){:target="\_blank" rel="noopener noreferrer"} - How to make the most of Custom Formats, including specifics of our recommended configuration. You can use these examples to understand how to set up your preferences.
    - [How to set up Quality Profiles Anime](/Sonarr/sonarr-setup-quality-profiles-anime/){:target="\_blank" rel="noopener noreferrer"} - Same as above but specific for anime.
    - [How to set up Quality Profiles (French)](/Sonarr/sonarr-setup-quality-profiles-french-en/){:target="\_blank" rel="noopener noreferrer"} - Same as above but specific for French and English Audio.
    - [How to set up Quality Profiles (German)](/Sonarr/sonarr-setup-quality-profiles-german-en/){:target="\_blank" rel="noopener noreferrer"} - Same as above but specific for German and English Audio.

More tips for Sonarr are available on the [Sonarr guides page](/Sonarr/#available-guides){:target="\_blank" rel="noopener noreferrer"}.

!!! tip "Automate these steps"
    The quality settings, naming scheme, and quality profile steps above, including the other profiles with custom formats and our suggested, tested scoring, can be automated with one of the officially supported third-party [Guide Sync Tools](/Guide-Sync/){:target="\_blank" rel="noopener noreferrer"}. These tools follow the guidelines described on that page.

    We still recommend reading through the written guides above first, so you understand what each option covers.

    If you need help choosing which quality profile fits your needs, ask in [#support](https://trash-guides.info/discord){:target="\_blank" rel="noopener noreferrer"} on Discord.

### Prowlarr

Prowlarr manages your indexers and syncs them to your other *Arr apps, so you don't have to set up indexers in Radarr and Sonarr individually.

For Installation and the basics of Prowlarr, please check the official [Prowlarr Quick Start Guide](https://wiki.servarr.com/prowlarr){:target="\_blank" rel="noopener noreferrer"}.

---

## 4. Set up Media Server

Finally, set up the media server that will actually play your library back.

### Plex

[Suggested Plex Media Server Settings](/Plex/Tips/Plex-media-server/){ .md-button target="\_blank" rel="noopener noreferrer" }

### Jellyfin

Not available yet. Once someone is willing to write and support a Jellyfin guide, it will be linked here.

### Emby

Not available yet. Once someone is willing to write and support an Emby guide, it will be linked here.

--8<-- "includes/support.md"
