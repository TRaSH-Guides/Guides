# How to Sync 2 Radarr or Sonarr with each other

<div class="annotate" markdown>
In this guide, we will try to explain how you can sync two (or more) Radarr/Sonarr instances with each other.

I'm going to show two different options on how you can set up your sync with two Radarr/Sonarr instances.

- Option 1: This option is best used if you want a 1:1 copy of your Radarr/Sonarr instances as it'll sync everything.
- Option 2: This option is best used if you only want to cherry-pick which Movies/TV Shows you want as 4K/2160p (UHD).

!!! bug ""

    We're not going to explain how to set up two Radarr/Sonarr instances for your system, being it depends on how you have it installed/running. [Radarr Multiple Instance Information](https://wiki.servarr.com/radarr/installation#multiple-instances) and [Sonarr Multiple Instance Information](https://wiki.servarr.com/sonarr/installation#multiple-instances)

## Preparation

For this, you need to have prepared the following:

- Two Radarr/Sonarr instances are fully set up (Indexers, Custom Formats, Downloaders, etc).
- One download client (_Two if you prefer Usenet and Torrents_).
- Your download client has two separate categories (movies-hd, movies-uhd, tv-hd, tv-uhd, etc)

!!! warning

    :bangbang:You can't use the same root (media library) folder for both Radarr/Sonarr instances.:bangbang:

    Make sure you use two separate root folders in Radarr/Sonarr (movies-hd, movies-uhd, tv-hd, tv-uhd, etc)

---

### Option 1

!!! info ""

    In this example, I'm going to use two Radarr instances (The basics are the same for Sonarr).

    - ^^==Radarr 1==^^ = My main 4K/2160p (UHD) Radarr.
    - {++Radarr 2++} = My 1080p Radarr that I've set up for a streaming-optimized quality profile. [^1]

    This option is best used if you want a 1:1 copy of your Radarr/Sonarr instances

#### Adding the Radarr Sync list

In {++Radarr 2++} go to `Settings` => `Lists`

![Radarr Settings Lists](images/radarr-settings-lists.png)

Click on the + to add a list and select `Radarr`

![Radarr add List](images/radarr-add-list.png)

Then you get a screen with the following options:

![Radarr Add Lists Options](images/radarr-add-lists-options.png)

1. The name you want to call your Sync list.
1. Enable to Enable the list.
1. Enable so the movies will be automatically added.
1. Enable so the movies will be added and monitored (if disabled then there will be no search done for the movies).
1. Enable so Radarr will perform a search when a movie is added.
1. When Radarr shall consider a movie as available. (1)
1. The Quality Profile you want to use for {++Radarr 2++}.
1. Your {++Radarr 2++} root location for your media library.
1. Tags that will be added on import from this list (if you use multiple lists it makes it easier to determine from which list the movie was added)
1. The Full URL to ^^==Radarr 1==^^ (Use container name or local URL if they run on the same system).
1. Your API Key of ^^==Radarr 1==^^. :circle-question:{ title="After adding your API key, click on the test button at the bottom to see if you have a successful connection." }
1. Which Profile of ^^==Radarr 1==^^ you want to Sync with {++Radarr 2++}. :circle-question:{ title="The dropdown box is filled after you made a successful connection with Radarr 1" }
1. [_Optional_] Use tags from ^^==Radarr 1==^^ to add Movies to {++Radarr 2++}. :circle-question:{ title="The dropdown box is filled after you made a successful connection with Radarr 1" }
1. [_Optional_] Add all movies from the chosen root folder from ^^==Radarr 1==^^. :circle-question:{ title="The dropdown box is filled after you made a successful connection with Radarr 1" }

#### Radarr Download client setup

You don't need a separate download client for your two Radarr instances, this all can be done with one download client (_Two if you prefer Usenet and Torrents_).

`Settings` => `Download Clients`

![!Radarr - Settings Download Clients](images/radarr-settings-download-clients.png)

Select your preferred download client.

![!Radarr - Settings Download Clients Categories](images/radarr-settings-download-clients-categories.png)

The only thing you need to change/create is a separate `Category` that you're going to use for {++Radarr 2++}

!!! warning

    This can't and shouldn't be the same category you use for ^^==Radarr 1==^^ but a separate `Category`.

### How does this Radarr Sync work

You now only need to make use of ^^==Radarr 1==^^. All movies you add to ^^==Radarr 1==^^ will be synced to {++Radarr 2++} at a scheduled time.

---

### Option 2

!!! info ""

    In this example, I'm going to use two Sonarr instances (The basics are the same for Radarr).

    - ^^==Sonarr 1==^^ = My main 1080p WEB-DL Sonarr.
    - {++Sonarr 2++} = 4K/2160p (UHD) WEB-DL Sonarr.

    This option is best used if you only want to have a few TV shows (or movies if you use this option with Radarr) as 4K/2160p (UHD)

#### Extra preparation

In ^^==Sonarr 1==^^ go to `Settings` => `Profiles`

![!Sonarr - Settings - Profiles](images/sonarr-settings-profiles.png)

Clone your used profile and rename your profile from `Profilename - Copy` to `Profilename!`

![!Sonarr - Clone Profile](images/sonarr-clone-profile.png)

#### Adding the Sonarr Sync list

In {++Sonarr 2++} go to `Settings` => `Import Lists`

![!Sonarr Settings Import Lists](images/sonarr-settings-import-lists.png)

Click on the + to add a list and select `Sonarr`

![!Sonarr add List](images/sonarr-add-list.png)

Then you get a screen with the following options:

![!Sonarr Add Lists Options](images/sonarr-add-lists-options.png)

1. The name you want to call your Sync list.
1. Enable so the TV Shows will be automatically added.
1. Enable so Sonarr will perform a search when a TV Show is added.
1. Choose how you want the series monitored initially. (2)
1. Which new seasons should be monitored automatically? (3)
1. Your {++Sonarr 2++} root location for your media library.
1. The Quality Profile you want to use for {++Sonarr 2++}.
1. Series Type. (4)
1. If you want to use Season Folders (**RECOMMENDED**).
1. Tags that will be added on import from this list (if you use multiple lists it makes it easier to determine from which list the TV Shows was added)
1. The Full URL to ^^==Sonarr 1==^^ (Use container name or local URL if they run on the same system).
1. Your API Key of ^^==Sonarr 1==^^. :circle-question:{ title="After adding your API key, click on the test button at the bottom to see if you have a successful connection." }
1. Sync season monitoring (**SUGGESTION: DISABLED**)
1. The Cloned Profile of ^^==Sonarr 1==^^ that we're going to use to sync with {++Sonarr 2++}.
1. [_Optional_] Use tags from ^^==Sonarr 1==^^ to add TV Shows to {++Sonarr 2++}. :circle-question:{ title="The dropdown box is filled after you made a successful connection with Sonarr 1" }
1. [_Optional_] Add all TV Shows from the chosen root folder from ^^==Sonarr 1==^^. :circle-question:{ title="The dropdown box is filled after you made a successful connection with Sonarr 1" }
1. This is a Deprecated option.

#### Sonarr Download client setup

You don't need a separate download client for your two Sonarr/Radarr instances, this can all be done with one download client (_Two if you prefer Usenet and Torrents_).

`Settings` => `Download Clients`

![!Sonarr - Settings Download Clients](images/sonarr-settings-download-clients.png)

Select your preferred download client.

![!Sonarr Categories](images/sonarr-categories.png)

Only thing you need to change/create is a separate `Category` that you're going to use for {++Sonarr 2++}

!!! tip

    This can't and shouldn't be the same category you use for ^^==Sonarr 1==^^ but a separate `Category`.

### How does this Sonarr Sync work

You now only need to make use of ^^==Sonarr 1==^^. When you have a TV show (or a movie if you use this option with Radarr) that you also want as 4K/2160p (UHD) then you make sure you make use of the Cloned Quality Profile. And it will sync at a scheduled time.

---
</div>

--8<-- "includes/annotations/sync-2-radarr-sonar.md"

[^1]:

    If you're interested in the 1080p streaming optimized quality profile you can join our [discord](https://trash-guides.info/discord) and get access to the Special Quality Profiles channel (access-to-sqp) by accepting the rules.

    This is a special quality profile we created for people who are interested in it.

    This release profile is fine-tuned for when you want to run a 2nd Radarr for 1080p and want minimum to no transcoding and smaller sizes for the second copies.

    Why choose this quality profile?

    - Streaming optimized (optimized for PLEX, Emby, Jellyfin, and other streaming platforms)
    - Small sizes
    - Good quality
    - Only AC3 Audio (downmixed lossless audio track to Dolby Digital 5.1 for optimal compatibility)
    - You want maximum compatibility between all devices and still have an HQ release.
    - You run two instances of Radarr and want both versions or just the 1080p ones.
    - You want to have minimum to no transcoding for low-powered devices or remote streaming.

--8<-- "includes/support.md"
