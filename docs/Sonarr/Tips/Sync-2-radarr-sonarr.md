<!-- markdownlint-disable MD041-->
# How to Sync 2 Radarr or Sonarr with each other

This guide will explain how to sync two (or more) Radarr/Sonarr instances.

## Why would you want to run two instances of Sonarr or Radarr?

- You want 1080p and 2160p versions of the same movie or episode.
- You want different versions of the same movie (Special Edition, Theatrical Cut, etc.)
- Etc.

## Which options will we cover

- Option 1 (full sync): This option will show you how to create a 1:1 copy of your Radarr/Sonarr instances, as it will synchronize everything.
- Option 2 (profiles): This option will show you how to cherry-pick which movies/TV shows you want in 4K/2160p (UHD).
- Option 3 (tags): This option can be used for a full sync or to cherry-pick.

## Preparation

::: info

We won't explain how to set up two Radarr/Sonarr instances for your system, as it depends on how it is installed and running.

- [Radarr Multiple Instance Information](https://wiki.servarr.com/radarr/installation#multiple-instances).
- [Sonarr Multiple Instance Information](https://wiki.servarr.com/sonarr/installation#multiple-instances).

:::

For this, you need to have prepared the following:

- Two Radarr/Sonarr instances that are fully set up (Indexers, Custom Formats, Downloaders, etc.).
- One download client (_two if you prefer Usenet and Torrents_).
- Your download client must have two separate categories (movies-hd, movies-uhd, tv-hd, tv-uhd, etc.).

::: warning

:bangbang:You can not use the same root (media library) folder for both Radarr/Sonarr instances.:bangbang:

Make sure to use two separate root folders in Radarr and Sonarr (movies-hd, movies-uhd, tv-hd, tv-uhd, etc.).

:::

---

## Option 1 (full sync)

::: info

In this example, we will use two Radarr instances (the basics are the same for Sonarr).

- <mark>Radarr 1</mark> = The main 4K/2160p (UHD) Radarr.
- <ins>Radarr 2</ins> = The 1080p (HD) Radarr that we have set up for a streaming-optimized quality profile.

This option will show you how to create a 1:1 copy of your Radarr/Sonarr instances, as it will synchronize everything.

:::

### Adding the Radarr Sync list (using full sync)

In Radarr 2, go to `Settings` => `Import Lists`.

![Radarr Settings Lists](../../Radarr/Tips/images/radarr-settings-lists.png)

Click on the + to add a list and select `Radarr`

![Radarr add List](../../Radarr/Tips/images/radarr-add-list.png)

You will get a screen with the following options:

![Radarr Add Lists Options](../../Radarr/Tips/images/radarr-add-lists-options.png)

1. The name you want to call your Sync list.
1. Enable the list.
1. Enable so the movies will be automatically added.
1. Enable it so the movies will be added and monitored (if disabled, no search will be done for the movies).
1. Enable so Radarr will perform a search when a movie is added.
1. When Radarr shall consider a movie as available. [^1]
1. The Quality Profile you want to use for <ins>Radarr 2</ins>.
1. Your <ins>Radarr 2</ins> root location for your media library.
1. Tags that will be added on import from this list (if you use multiple lists, it makes it easier to determine from which list the movie was added)
1. The Full URL to <mark>Radarr 1</mark> (Use container name with `.internal` domain like `http://radarr.internal:7878` or local URL if they run on the same system).
1. Your API Key of <mark>Radarr 1</mark>. <abbr title="After adding your API key, click the test button at the bottom to see if you have a successful connection.">❓</abbr>
1. Which Profile of <mark>Radarr 1</mark> you want to Sync with <ins>Radarr 2</ins>. <abbr title="The dropdown box is filled after you made a successful connection with Radarr 1">❓</abbr>
1. [_Optional_] Use tags from <mark>Radarr 1</mark> to add Movies to <ins>Radarr 2</ins>. <abbr title="The dropdown box is filled after you made a successful connection with Radarr 1">❓</abbr>
1. [_Optional_] Add all movies from the chosen root folder from <mark>Radarr 1</mark>. <abbr title="The dropdown box is filled after you made a successful connection with Radarr 1">❓</abbr>

### Radarr Download client setup (using full sync)

You do not need a separate download client for your two Radarr instances, and this can all be done with one download client (_two if you prefer Usenet and Torrents_).

`Settings` => `Download Clients`

![!Radarr - Settings Download Clients](../../Radarr/Tips/images/radarr-settings-download-clients.png)

Select your preferred download client.

![!Radarr - Settings Download Clients Categories](../../Radarr/Tips/images/radarr-settings-download-clients-categories.png)

The only thing you need to change/create is a separate `Category` that you are going to use for <ins>Radarr 2</ins>

::: warning This must not be the same category you use for <mark>Radarr 1</mark> - use a new `Category`.

:::

### How does this Radarr Sync work (using full sync)

You now only need to make use of <mark>Radarr 1</mark>. All movies you add to <mark>Radarr 1</mark> will be synced to <ins>Radarr 2</ins> at a scheduled time.

---

## Option 2 (profiles)

::: info

In this example, we will use two Sonarr instances (The basics are the same for Radarr).

- <mark>Sonarr 1</mark> = The main 1080p WEB-DL Sonarr.
- <ins>Sonarr 2</ins> = 4K/2160p (UHD) WEB-DL Sonarr.

This option will show how to selectively add which movies/TV shows you want as 4K/2160p (UHD).

:::

### Extra preparation (using profiles)

In <mark>Sonarr 1</mark> go to `Settings` => `Profiles`

![!Sonarr - Settings - Profiles](../../Radarr/Tips/images/sonarr-settings-profiles.png)

Clone your used profile and rename your profile from `Profilename - Copy` to `Profilename!`

![!Sonarr - Clone Profile](../../Radarr/Tips/images/sonarr-clone-profile.png)

### Adding the Sonarr Sync list (using profiles)

In <ins>Sonarr 2</ins> go to `Settings` => `Import Lists`

![!Sonarr Settings Import Lists](../../Radarr/Tips/images/sonarr-settings-import-lists.png)

Click on the + to add a list and select `Sonarr`

![!Sonarr add List](../../Radarr/Tips/images/sonarr-add-list.png)

You will get a screen with the following options:

![!Sonarr Add Lists Options](../../Radarr/Tips/images/sonarr-add-lists-options.png)

1. The name you want to call your Sync list.
1. Enable so that the TV Shows will be automatically added.
1. Enable so Sonarr will perform a search when a TV Show is added.
1. Choose how you want the series monitored initially. [^2]
1. Which new seasons should be monitored automatically? [^3]
1. Your <ins>Sonarr 2</ins> root location for your media library.
1. The Quality Profile you want to use for <ins>Sonarr 2</ins>.
1. Series Type. [^4]
1. If you want to use Season Folders (**RECOMMENDED**).
1. Tags that will be added on import from this list (if you use multiple lists, it makes it easier to determine from which list the TV Shows were added)
1. The Full URL to <mark>Sonarr 1</mark> (Use container name with `.internal` domain like `http://sonarr.internal:8989` or local URL if they run on the same system).
1. Your API Key of <mark>Sonarr 1</mark>. <abbr title="After adding your API key, click the test button at the bottom to see if you have a successful connection.">❓</abbr>
1. Sync season monitoring (**SUGGESTION: DISABLED**)
1. The Cloned Profile of <mark>Sonarr 1</mark> that we are going to use to sync with <ins>Sonarr 2</ins>.
1. [_Optional_] Use tags from <mark>Sonarr 1</mark> to add TV Shows to <ins>Sonarr 2</ins>. <abbr title="The dropdown box is filled after you made a successful connection with Sonarr 1">❓</abbr>
1. [_Optional_] Add all TV Shows from the chosen root folder from <mark>Sonarr 1</mark>. <abbr title="The dropdown box is filled after you made a successful connection with Sonarr 1">❓</abbr>
1. This is a Deprecated option.

### Sonarr Download client setup (using profiles)

You do not need a separate download client for your two Sonarr/Radarr instances, and this can all be done with one download client (_two if you prefer Usenet and Torrents_).

`Settings` => `Download Clients`

![!Sonarr - Settings Download Clients](../../Radarr/Tips/images/sonarr-settings-download-clients.png)

Select your preferred download client.

![!Sonarr Categories](../../Radarr/Tips/images/sonarr-categories.png)

The only thing you need to change/create is a separate `Category` that you are going to use for <ins>Sonarr 2</ins>

::: warning This must not be the same category you use for <mark>Sonarr 1</mark>, - use a new `Category`.

:::

### How does this Sonarr Sync work (using profiles)

You now only need to make use of <mark>Sonarr 1</mark>. When you have a TV show (or a movie if you use this option with Radarr) that you also want as 4K/2160p (UHD), you make sure you use the Cloned Quality Profile. And it will sync at a scheduled time.

---

## Option 3 (tags)

::: info

In this example, we will use two Radarr instances (The basics are the same for Sonarr).

- <mark>Radarr 1</mark> = The main 4K/2160p (UHD) Radarr.
- <ins>Radarr 2</ins> = The 1080p (HD) Radarr we've set up for a streaming-optimized quality profile.

This option will show you how to create a 1:1 copy of your Radarr/Sonarr instances, as it will synchronize everything.

:::

### Add tags

There are different ways to add tags to your movies or shows in Radarr/Sonarr

- [Manually](#manually) add tags.
- [Automated way](#automated) in Radarr/Sonarr using `Auto Tagging`.
- [3rd party apps](#3rd-party) like Jellyseerr, Kometa, and others.

::: tabs

== Manually

**Manually add tags**

In <mark>Radarr 1</mark> select a movie you want to sync to <ins>Radarr 2</ins>, and in the tags box type the tag name you wish to use to trigger the sync in <ins>Radarr 2</ins>.

![Radarr Add Tag Manual](../../Radarr/Tips/images/radarr-add-tag-manual.png)

1. In this example, we will use the tag: `radarr-hd-sync`.
1. Click on Save.

== Automated

**Automated way**

There are different ways to use the built-in Automated way, depending on which conditions you want to use. In this example, we are going to use the root folder

In <mark>Radarr 1</mark> goto `Settings` => `Tags` => `Auto Tagging`, Click on the ![cf-plus-add-small](/Radarr/images/cf-plus-add-small.png) sign and in the `Add Auto Tag` window, click again on the ![cf-plus-add-small](/Radarr/images/cf-plus-add-small.png) sign under conditions.

![Auto Tagging - Add Auto Tag](../../Radarr/Tips/images/radarr-auto-tagging-add-auto-tag.png)

You will be presented with a new window to choose several conditions.

![Auto Tagging - Add Condition](../../Radarr/Tips/images/radarr-auto-tagging-add-condition.png)

For this example, we are going to use the condition: `Root Folder`

![Auto Tagging - Add Condition - Root Folder](../../Radarr/Tips/images/radarr-auto-tagging-add-condition-root-folder.png)

1. The name used for the condition, in this example, we used `Movies (UHD)`.
1. The root folder that we want to keep track of, in this example, we used `/data/media/movies-uhd`.
1. If you use multiple conditions, you can choose which condition is required, in this example, we enabled it.

After you add all the needed info and click on save, you will see the new condition you created.

![Auto Tagging - Add Condition - Final Steps](../../Radarr/Tips/images/radarr-auto-tagging-add-condition-final-steps.png)

1. The name used for the `Auto Tagging`, in this example, we used `Radarr-UHD => HD`.
1. If you want to remove the tags automatically if the condition no longer matches.
1. The tags we will use in <ins>Radarr 2</ins>. In this example, we will use the tag: `radarr-hd-sync`.
1. The condition you created before.
1. Do not forget to click on `Save`.

== 3rd party

**3rd party apps**

You can use several third-party apps for this option. In this example, we will use Jellyseerr (_The same concept also works with Overseerr_).

In Jellyseerr, go to `Settings` => `Services`, where you will add Radarr/Sonarr (_If you already added Radarr/Sonarr, click on edit_).

::: info If you have multiple Radarr added, make sure you edit it in <mark>Radarr 1</mark>

:::

![Tags - Using a 3rd party app - Jellyseerr](../../Radarr/Tips/images/radarr-tags-3rd-party-app-jellyseerr.png)

1. The tags we will use in <ins>Radarr 2</ins>. In this example, we will use the tag: `radarr-hd-sync`.
1. This is more of a Jellyseerr setting for your <mark>Radarr 1</mark>. Enable this setting if you would like to scan your Radarr/Sonarr server for existing media/request status. You should enable this setting so that users cannot submit requests for media that have already been requested or are already available.
1. This is more of a Jellyseerr setting for your <mark>Radarr 1</mark>. Enable this setting to have Radarr/Sonarr automatically search for media upon approval of a request.

:::

### Adding the Radarr Sync list (using tags)

In <ins>Radarr 2</ins> go to `Settings` => `Import Lists`

![Radarr Settings Lists](../../Radarr/Tips/images/radarr-settings-lists.png)

Click on the + to add a list and select `Radarr`

![Radarr add List](../../Radarr/Tips/images/radarr-add-list.png)

You will get a screen with the following options:

![Radarr Add Lists Options](../../Radarr/Tips/images/radarr-add-lists-options-tags.png)

1. The name you want to call your Sync list.
1. Enable the list.
1. Enable so the movies will be automatically added.
1. Enable it so the movies will be added and monitored (if disabled, no search will be done for the movies).
1. Enable so Radarr will perform a search when a movie is added.
1. When Radarr shall consider a movie as available. [^5]
1. The Quality Profile you want to use for <ins>Radarr 2</ins>.
1. Your <ins>Radarr 2</ins> root location for your media library.
1. Tags that will be added on import from this list (if you use multiple lists, it makes it easier to determine from which list the movie was added)
1. The Full URL to <mark>Radarr 1</mark> (Use container name with `.internal` domain like `http://radarr.internal:7878` or local URL if they run on the same system).
1. Your API Key of <mark>Radarr 1</mark>. <abbr title="After adding your API key, click the test button at the bottom to see if you have a successful connection.">❓</abbr>
1. The used tags from <mark>Radarr 1</mark> to add Movies to <ins>Radarr 2</ins>. <abbr title="The dropdown box is filled after you made a successful connection with Radarr 1">❓</abbr>

### Radarr Download client setup (using tags)

You do not need a separate download client for your two Radarr instances, and this can all be done with one download client (_two if you prefer Usenet and Torrents_).

`Settings` => `Download Clients`

![!Radarr - Settings Download Clients](../../Radarr/Tips/images/radarr-settings-download-clients.png)

Select your preferred download client.

![!Radarr - Settings Download Clients Categories](../../Radarr/Tips/images/radarr-settings-download-clients-categories.png)

The only thing you need to change/create is a separate `Category` that you are going to use for <ins>Radarr 2</ins>

::: warning This can not and should not be the same category you use for <mark>Radarr 1</mark>, but a separate `Category`.

:::

### How does this Radarr Sync work (using tags)

Depending on your chosen option, it will sync movies from <mark>Radarr 1</mark> to ^^ <ins>Radarr 2</ins> at a scheduled time.

---
<!--@include: ../../../includes/annotations/sync-2-radarr-sonar.md-->

<!--@include: ../../../includes/support.md-->
<!-- markdownlint-enable MD041-->
