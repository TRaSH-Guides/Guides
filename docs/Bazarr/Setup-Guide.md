# Setup Guide

!!! note

    In this guide we will try to explain the basic setup you need to do to get started with Bazarr.
    For a more detailed few of all the setting check the following [LINK](https://wiki.bazarr.media/Additional-Configuration/Settings/){:target="_blank" rel="noopener noreferrer"}.

Before Bazarr works we need to setup and configure a few settings.

After installation and starting up, you open a browser and go to <http://ip_where_installed:6767>.

---

## Sonarr

First we're going to setup Sonarr.

`Settings` => `Sonarr`

![!Settings => Sonarr](images/qs-settings-sonarr.png)

### Use Sonarr

Click on `Enabled`

![!Sonarr](images/qs-sonarr.png)

1. Enable Sonarr.
1. Enter the hostname or the IP address of the computer running your Sonarr instance.

    !!! info

        **Be aware that when using Bazarr in docker, you cannot reach another container on the same Docker host using the loopback address (ex.: 127.0.0.1 or localhost). Loopback address refer to the Bazarr Docker container, not the Docker host.**

1. Enter the TCP port of your Sonarr instance. Default is 8989.
1. Mainly used by those who expose Sonarr behind a reverse proxy (ex.: /sonarr). Don't forget the leading slash. In fact, it should look exactly the same as in Sonarr settings. Meanly used when you use a reverse proxy.

    !!! info

        **If you don't use a reverse proxy or don't know what it is leave this empty !!!**

1. Enter your Sonarr API key here.
1. Enable this if your Sonarr instance is exposed trough SSL.

    !!! info

        **Not needed if you reach it with a local IP address.**

1. Click the `Test` button after filling in all the fields. Make sure the test is successful before you proceed.

### Options

![!Sonarr - Options](images/qs-sonarr-options.png)

1. Select the minimum score (in percentage) required for a subtitles file to be downloaded.

    !!! info

        **Are your subs often out of sync or just bad? Raise the score!**

1. Episodes from series with those tags (case sensitive) in Sonarr will be excluded from automatic download of Subtitles. In Sonarr you add a custom tag to a show, in this case the shows with these tags will be ignored by Bazarr.

1. Episodes from series with these types in Sonarr will be excluded from automatic download of Subtitles.

    Options: `Standard`, `Anime`, `Daily`

1. Automatic download of Subtitles will only happen for monitored shows/episodes in Sonarr.

### Path Mappings

!!! note

    You should only use this section if Sonarr and Bazarr use a different path to access the same files.

    (for example if you run Sonarr on a different device then Bazarr or have a Synology and mix packages with Docker.)

![!Sonarr Path Mappings](images/qs-sonarr-path-mappings-add.png)

Click on `Add` and you will get a extra option

![!Sonarr Path Mappings](images/qs-sonarr-path-mappings.png)

1. Here you enter the path that Sonarr uses to access your shows.
1. Here you enter the path that Bazarr uses to access your shows.

!!! attention

    **IF YOU GOT THE SAME VALUES ON BOTH SIDES THEN YOU DON'T NEED IT !!!**

    **IT SHOULD ALSO BE REMOVED OR ELSE YOU WILL GET A ERROR.**

![!Sonarr Path Mappings Mapped](images/qs-sonarr-path-mappings-mapped.png)

!!! info

    *If everything runs on Docker you normally don't need to use this except if you got messed up paths and then it would be smarter to fix those first to have consistent and well planned paths.*

    Please take a look at TRaSH's Hardlink Tutorial <https://trash-guides.info/hardlinks>

!!! danger "Don't forget to Save your settings !!!"

    ![Save](images/qs-save.png)

---

## Radarr

Next we're going to setup Radarr.

`Settings` => `Radarr`

![!Settings => Radarr](images/qs-settings-radarr.png)

### Use Radarr

Click on `Enabled`

![!Radarr](images/qs-radarr.png)

1. Enable Radarr.
1. Enter the hostname or the IP address of the computer running your Sonarr instance.

    !!! info

        **Be aware that when using Bazarr in docker, you cannot reach another container on the same Docker host using the loopback address (ex.: 127.0.0.1 or localhost). Loopback address refer to the Bazarr Docker container, not the Docker host.**

1. Enter the TCP port of your Radarr instance. Default is 7878.
1. Mainly used by those who expose Radarr behind a reverse proxy (ex.: /radarr). Don't forget the leading slash. In fact, it should look exactly the same as in Radarr settings. Meanly used when you use a reverse proxy.

    !!! info

        **If you don't use a reverse proxy or don't know what it is leave this empty !!!**

1. Enter your Radarr API key here.
1. Enable this if your Radarr instance is exposed trough SSL.

    !!! info

        **Not needed if you reach it with a local IP address.**

1. Click the `Test` button after filling in all the fields. Make sure the test is successful before you proceed.

### Options (Radarr)

![!Radarr - Options](images/qs-radarr-options.png)

1. Select the minimum score (in percentage) required for a subtitles file to be downloaded.

    !!! info

        **Are your subs often out of sync or just bad? Raise the score!**

1. Movies with those tags (case sensitive) in Radarr will be excluded from automatic download of Subtitles, In Radarr you add a custom tag to a movie.

1. Automatic download of Subtitles will only happen for monitored movies in Radarr.

### Path Mappings (Radarr)

!!! note

    You should only use this section if Radarr and Bazarr use a different path to access the same files.

    (for example if you run Radarr on a different device then Bazarr or have a Synology and mix packages with Docker.)

![!Radarr Path Mappings](images/qs-radarr-path-mappings-add.png)

Click on `Add` and you will get a extra option

![!Radarr Path Mappings](images/qs-radarr-path-mappings.png)

1. Here you enter the path that Radarr uses to access your movies.
1. Here you enter the path that Bazarr uses to access your movies.

!!! attention

    **IF YOU GOT THE SAME VALUES ON BOTH SIDES THEN YOU DON'T NEED IT !!!**

    **IT SHOULD ALSO BE REMOVED OR ELSE YOU WILL GET A ERROR.**

![!Path Mappings Radarr Mapped](images/qs-radarr-path-mappings-mapped.png)

!!! info

    *If everything runs on Docker you normally don't need to use this except if you got messed up paths and then it would be smarter to fix those first to have consistent and well planned paths.*

    Please take a look at TRaSH's Hardlink Tutorial <https://trash-guides.info/hardlinks>

!!! danger "Don't forget to Save your settings !!!"

    ![Save](images/qs-save.png)

---

## Languages

Here we're going to configure which subtitle languages you prefer/want.

`Settings` => `Languages`

![!Settings => Languages](images/qs-settings-languages.png)

### Subtitles Language

!!! warning

    **We don't recommend enabling `Single Language` option unless absolutely required (ie: media player not supporting language code in subtitles filename). Results may vary.

    Be aware the language code (ex.: en) is not going to be included in the subtitles file name when enabling this.**

![!Subtitles Language](images/qs-subtitles-language.png)

Here you select which languages you want for your subtitles, you can just start typing your language name and it will show you what's available.

These languages are the subtitle languages you later use for the `Languages Profiles`

In this example I selected `Dutch` and `English`.

### Languages Profiles

Select `Add New Profile`

![!Languages Profiles](images/qs-languages-profiles.png)

1. How you want to name your language profile.
1. Click on `Add` to add the languages you enabled earlier in [Subtitle Language](#subtitles-language).
1. Select the languages you want to enable for your profile (Including the optional settings).
    - Forced => [FAQ - What are Forced Subtitles](https://wiki.bazarr.media/Troubleshooting/FAQ/#what-are-forced-subtitles){:target="_blank" rel="noopener noreferrer"}
    - HI => Hearing Impaired
    - Exclude Audio => Exclude if matching audio
1. Optional select the cutoff where you want that Bazarr stops downloading other languages.
1. Save your settings.

??? info "Cutoff"

    ![!Cutoff](images/qs-cutoff.png)

    So you can have a profile that states: English, Dutch, German, French
    With cutoff Dutch, if it finds Dutch, it will download it and call it a day.
    If no Dutch is found it will continue searching the other languages till Dutch is found.

### Default Settings

![!Default Settings](images/qs-default-settings.png)

Automatic applied `Languages Profiles` to Series and Movies added to Bazarr **after** enabling this option.

!!! danger "Don't forget to Save your settings !!!"

    ![Save](images/qs-save.png)

---

## Providers

Here we're going to select which Subtitle Providers you want to use.

`Settings` => `Providers`

![!Settings => Providers](images/qs-settings-providers.png)

![!Providers](images/qs-providers.png)

1. Click on the Plus sign box.
1. Select the subtitles providers you would like to enable. it is best to select multiple providers and create/use a account with them especially when you got allot of wanted subtitles. Some subtitle providers requires a extra paid Anti-Captcha Service.
1. Your enabled providers.

!!! tip

    If possible don't forget to support them for their free service

!!! danger "Don't forget to Save your settings !!!"

    ![Save](images/qs-save.png)

---

## Subtitles

Here we will configure some extra settings for your subtitles

`Settings` => `Subtitles`

![!Settings => Subtitles](images/qs-settings-subtitles.png)

### Subtitle Options

![!Subtitle Options](images/qs-subtitles-options.png)

1. Where you want your subtitles it's recommended to put them `AlongSide Media File`.
1. If you want to upgrade preciously downloaded subtitles.
1. How many days to go back in history to upgrade them.
1. If you want to upgrade manually downloaded subtitles.

### Anti-Captcha Options

![!Anti-Captcha Options](images/qs-anti-captcha.png)

Here you can select which Anti-Captcha provider you want to use.

[Why (or) do I need the Anti-Captcha ?](https://wiki.bazarr.media/Troubleshooting/FAQ/#why-or-do-i-need-the-anti-captcha){:target="_blank" rel="noopener noreferrer"}

!!! tip

    We Recommend the following provider => <https://anti-captcha.com/>

### Performance / Optimization

![!Performance / Optimization](images/qs-performance-optimization.png)

1. When searching for subtitles, Bazarr will search less frequently to limit call to providers.
1. Search multiple providers at once (Don't choose this on low powered devices).
1. If you want to use the embedded subtitles in the media files [More Info](https://wiki.bazarr.media/Additional-Configuration/Settings/#use-embedded-subtitles){:target="_blank" rel="noopener noreferrer"}

### Automatic Subtitles Synchronization

Enable this option for automatic subtitles synchronization.

![!Automatic Subtitles Synchronization](images/qs-automatic-subtitles-sync.png)

!!! danger "Don't forget to Save your settings !!!"

    ![Save](images/qs-save.png)
---

Now wait till Bazarr gets all the info needed from Sonarr/Radarr.

## IMPORTANT

!!! important

    **Don't forget [After Install Configuration](/Bazarr/After-install-configuration/) !!!**

---

If you still have questions please check the [Troubleshooting](https://wiki.bazarr.media/Troubleshooting/Asking-for-help-or-report-a-problem/){:target="_blank" rel="noopener noreferrer"} section in the wiki.
For more info about the other settings check the [Settings](https://wiki.bazarr.media/Additional-Configuration/Settings/){:target="_blank" rel="noopener noreferrer"} wiki.
