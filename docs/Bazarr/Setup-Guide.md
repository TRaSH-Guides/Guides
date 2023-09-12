# Setup Guide

!!! note

  In this guide, we will try to explain the basic setup you need to get started with Bazarr.
  For a more detailed view of all the settings, check the following [LINK](https://wiki.bazarr.media/Additional-Configuration/Settings/){:target="_blank" rel="noopener noreferrer"}.

Before Bazarr works, we need to setup and configure a few settings.

After installation and starting up Bazarr, open a browser and go to <http://ip_where_installed:6767>.

----

## Sonarr

First we're going to setup Sonarr.

`Settings` => `Sonarr`

![!Settings => Sonarr](images/qs-settings-sonarr.png)

### Use Sonarr

Click `Enabled`.

![!Sonarr](images/qs-sonarr.png)

1. Enable Sonarr.
1. Enter the hostname or the IP address of the computer running your Sonarr instance.

  !!! info

    **When using Bazarr in Docker, you *cannot* reach another container on the same Docker host using the loopback address (ex.: 127.0.0.1 or localhost). Loopback address refers to the Bazarr Docker container, not the Docker host.**

1. Enter the TCP port of your Sonarr instance (default is 8989).
1. Sonarr uses the Base URL *only* if used with a "Reverse Proxy" (ex: Nginx Proxy Manager or SWAG) and *must* have a leading slash if it is needed (ex: /sonarr).

  !!! info

    **If you don't use a reverse proxy, or don't know what that is, leave this empty!**

1. Enter your Sonarr API key here.
1. Enable this if your Sonarr instance is exposed through SSL.

  !!! info

    **This is not needed if you reach Sonarr with a local IP address (192.168.1.150, 10.10.26.75, etc.).**

1. Click `Test` after filling in all the fields. Make sure the test is successful before you proceed.

### Options

![!Sonarr - Options](images/qs-sonarr-options.png)

1. Select the minimum score (in percentage) required for a subtitle file to be downloaded.

  !!! info

    **Are your subs often out of sync or just bad? Raise the score!**

1. Episodes from series with those tags (case-sensitive) in Sonarr will be excluded from automatic downloading of subtitles. In Sonarr, you add a custom tag to a show. In this case the shows with these tags will be ignored by Bazarr.

1. Episodes from series with these types in Sonarr will be excluded from automatic downloading of subtitles.

  Options: `Standard`, `Anime`, `Daily`

1. Automatic downloading of subtitles will only happen for monitored shows/episodes in Sonarr.

### Path Mappings

!!! note

  You should only use this section if Sonarr and Bazarr use a different path to access the same files.

  (For example: if you run Sonarr on a different device than Bazarr or have a Synology and mix packages with Docker.)

![!Sonarr Path Mappings](images/qs-sonarr-path-mappings-add.png)

Click `Add` to get an extra option:

![!Sonarr Path Mappings](images/qs-sonarr-path-mappings.png)

1. Enter the path that Sonarr uses to access your shows.
1. Enter the path that Bazarr uses to access your shows.

!!! warning

  **IF YOU HAVE THE SAME VALUES ON BOTH SIDES, YOU DON'T NEED PATH MAPPING!**

  **USING PATH MAPPING IF THIS IS THE CASE CAN CAUSE ERRORS.**

![!Sonarr Path Mappings Mapped](images/qs-sonarr-path-mappings-mapped.png)

!!! info

  *If everything runs on Docker, you normally don't need to use this. However, if you have messed up paths, then it would be smarter to fix those first.*

  Please review the hardlink tutorial [HERE](https://trash-guides.info/hardlinks){:target="_blank" rel="noopener noreferrer"}.

!!! danger "Don't forget to save your settings!!!"

  ![Save](images/qs-save.png)

----

## Radarr

Next, we're going to setup Radarr.

`Settings` => `Radarr`

![!Settings => Radarr](images/qs-settings-radarr.png)

### Use Radarr

Click `Enabled`.

![!Radarr](images/qs-radarr.png)

1. Enable Radarr.
1. Enter the hostname or the IP address of the computer running your Radarr instance.

  !!! info

    **When using Bazarr in Docker, you *cannot* reach another container on the same Docker host using the loopback address (ex.: 127.0.0.1 or localhost). Loopback address refers to the Bazarr Docker container, not the Docker host.**

1. Enter the TCP port of your Radarr instance (default is 7878).
1. Radarr uses the Base URL *only* if used with a "Reverse Proxy" (ex: Nginx Proxy Manager or SWAG) and *must* have a leading slash if it is needed (ex: /radarr).

  !!! info

    **If you don't use a reverse proxy, or don't know what that is, leave this empty!**

1. Enter your Radarr API key here.
1. Enable this if your Radarr instance is exposed through SSL.

  !!! info

    **This is not needed if you reach it with a local IP address (192.168.1.150, 10.10.26.75, etc.).**

1. Click `Test` after filling in all fields. Make sure the test is successful before you proceed.

### Options (Radarr)

![!Radarr - Options](images/qs-radarr-options.png)

1. Select the minimum score (in percentage) required for a subtitle file to be downloaded.

  !!! info

    **Are your subs often out of sync or just bad? Raise the score!**

1. Movies with those tags (case sensitive) in Radarr will be excluded from automatic downloading of subtitles. In Radarr you add a custom tag to a movie.

1. Automatic downloading of subtitles will only happen for monitored movies in Radarr.

### Path Mappings (Radarr)

!!! note

  You should only use this section if Radarr and Bazarr use a different path to access the same files.

  (For example: if you run Radarr on a different device than Bazarr or have a Synology and mix packages with Docker.)

![!Radarr Path Mappings](images/qs-radarr-path-mappings-add.png)

Click `Add` to get an extra option

![!Radarr Path Mappings](images/qs-radarr-path-mappings.png)

1. Here you enter the path that Radarr uses to access your movies.
1. Here you enter the path that Bazarr uses to access your movies.

!!! warning

  **IF YOU HAVE THE SAME VALUES ON BOTH SIDES, YOU DON'T NEED PATH MAPPING!**

  **USING PATH MAPPING IF THIS IS THE CASE CAN CAUSE ERRORS.**

![!Path Mappings Radarr Mapped](images/qs-radarr-path-mappings-mapped.png)

!!! info

  *If everything runs on Docker, you normally don't need to use this. However, if you have messed up paths, then it would be smarter to fix those first.*

  Please review the hardlink tutorial [HERE](https://trash-guides.info/hardlinks){:target="_blank" rel="noopener noreferrer"}.

!!! danger "Don't forget to save your settings!!!"

  ![Save](images/qs-save.png)

----

## Languages

Here we're going to configure which subtitle languages you prefer/want.

`Settings` => `Languages`

![!Settings => Languages](images/qs-settings-languages.png)

### Subtitles Language

!!! warning

  **Don't enable the `Single Language` option unless absolutely required (ie: if your media player doesn't support a language code in the subtitles filename). Results may vary.**

  Be aware the language code (ex.: en) is not going to be included in the subtitles file name when enabling this.**

![!Subtitles Language](images/qs-subtitles-language.png)

Here you select which languages you want for your subtitles. (You can start typing your language name, and it will show you what's available.)

These languages are the subtitle languages you later use for the `Languages Profiles`

In this example, I selected `Dutch` and `English`.

### Languages Profiles

Select `Add New Profile`

![!Languages Profiles](images/qs-languages-profiles.png)

1. How you want to name your language profile.
1. Click `Add` to add the languages you enabled earlier in [Subtitle Language](#subtitles-language).
1. Select the languages you want to enable for your profile (including the optional settings).
  - Forced => [FAQ - What are Forced Subtitles](https://wiki.bazarr.media/Troubleshooting/FAQ/#what-are-forced-subtitles){:target="_blank" rel="noopener noreferrer"}
  - HI => Hearing Impaired
  - Exclude Audio => Exclude if matching audio
1. Select the cutoff where you want Bazarr to stop downloading other languages (optional).
1. Save your settings.

??? info "Cutoff"

  ![!Cutoff](images/qs-cutoff.png)

  You can have a profile that states: English, Dutch, German, French
  With the cutoff set to `Dutch`, if Bazarr finds Dutch subtitles, it will download only the Dutch subtitles.
  If no Dutch is found, it will continue searching the other languages till Dutch is found.

### Default Settings

![!Default Settings](images/qs-default-settings.png)

Automatically applied `Languages Profiles` to Series and Movies added to Bazarr **after** enabling this option.

!!! danger "Don't forget to save your settings !!!"

  ![Save](images/qs-save.png)

----

## Providers

Here we're going to select which subtitle providers you want to use.

`Settings` => `Providers`

![!Settings => Providers](images/qs-settings-providers.png)

![!Providers](images/qs-providers.png)

1. Click the Plus sign box.
1. Select the subtitle providers you would like to enable. It is best to select multiple providers and create/use an account with them, especially if you have a lot of wanted subtitles. Some subtitle providers require an extra paid Anti-Captcha Service.
1. Your enabled providers.

!!! tip

  If possible, support the subtitle providers for their free services.

!!! danger "Don't forget to save your settings!!!"

  ![Save](images/qs-save.png)

----

## Subtitles

Here we will configure some extra settings for your subtitles

`Settings` => `Subtitles`

![!Settings => Subtitles](images/qs-settings-subtitles.png)

### Subtitle Options

![!Subtitle Options](images/qs-subtitles-options.png)

1. Where you want your subtitles (it's recommended to put them `AlongSide Media File`).
1. If you want to upgrade previously downloaded subtitles.
1. How many days to go back in history to upgrade them.
1. If you want to upgrade manually downloaded subtitles.

### Anti-Captcha Options

![!Anti-Captcha Options](images/qs-anti-captcha.png)

Here you can select which Anti-Captcha provider you want to use.

[(Why) do I need the Anti-Captcha ?](https://wiki.bazarr.media/Troubleshooting/FAQ/#why-or-do-i-need-the-anti-captcha){:target="_blank" rel="noopener noreferrer"}

!!! tip

  We recommend <https://anti-captcha.com/>.

### Performance / Optimization

![!Performance / Optimization](images/qs-performance-optimization.png)

1. When searching for subtitles, Bazarr will search less frequently to limit calls to providers.
1. Search multiple providers at once. (Don't choose this on low-powered devices.)
1. If you want to use the embedded subtitles in the media files [More Info](https://wiki.bazarr.media/Additional-Configuration/Settings/#use-embedded-subtitles){:target="_blank" rel="noopener noreferrer"}

### Automatic Subtitles Synchronization

Enable this option for automatic subtitles synchronization.

![!Automatic Subtitles Synchronization](images/qs-automatic-subtitles-sync.png)

!!! danger "Don't forget to save your settings!!!"

  ![Save](images/qs-save.png)

----

Now wait until Bazarr gets all the info needed from Sonarr/Radarr.

## IMPORTANT

!!! tip

  **Don't forget [After Install Configuration](/Bazarr/After-install-configuration/)!!!**

----

If you still have questions, please check the [Troubleshooting](https://wiki.bazarr.media/Troubleshooting/Asking-for-help-or-report-a-problem/){:target="_blank" rel="noopener noreferrer"} section in the Bazarr wiki.
For more info about the other settings, check the [Settings](https://wiki.bazarr.media/Additional-Configuration/Settings/){:target="_blank" rel="noopener noreferrer"} section in the Bazarr wiki.
