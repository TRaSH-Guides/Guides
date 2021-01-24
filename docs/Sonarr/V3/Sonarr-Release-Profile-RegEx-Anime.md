# Release Profile RegEx (Anime)

!!! note
    This Guide is Created and Maintained by [Visorask](https://github.com/Visorask)

    It's recommended to run 2 Sonarr's 1 for Anime and 1 for normal tv shows, or you can make use of tags.

    Being that release profiles are global without the use of a tag.

## Dual-Audio Regex

Having tested most of these settings, they work pretty well but Anime is a fickle beast to toy with so be warned.

---

## Anime Delete

??? tip "If you have issues with extra files being download like NCED or NCOP"

    If you have issues with sonarr picking up a bunch of:

    - NCED
    - NCOP
    - Music Videos
    - OP's

    Then this script (linux based only) will delete these files and get rid of them and you don't have to worry about them cluttering up your Auto or Manual import process.

    ```bash
    #!/usr/bin/env bash

    # Set the following location to your completed download location for Anime.
    # Usually one of the following paths:
    # Dockers => /data/{usenet|torrents}/anime
    # Cloudbox => /mnt/local/downloads/nzbs/nzbget/completed/sonarranime
    location="/your/download/path/here"

    find $location -type f \( -iname "*op[0-9]*" -o -iname "*nced*" -o -iname "*ncop*" -o -iname "*music video*" \) -exec rm -rf {} \;
    ```

    This script will be called through a custom connection in sonarr.

    1. Copy the contents of the script into whatever filepath sonarr has access to (`/config/app/` or `/appdata/sonarr/scripts`)
    1. Edit the `location="/your/download/path/here"` and make sure it's in quotes.
    1. Then save it and chmod +x the script.
    1. In Sonarr go to `Settings` => `Connect` => Click on the `+` Symbol => and select `Custom Script`
    1. Change Name to whatever you like.
    1. Select `On Grab` and `On Import`.
    1. Click the Folder icon or type in the path to the script you chose earlier.

    ![!rpa-customscript](images/rpa-customscript.png)

    Now when you download or import any files the script will run and clear out those files that you most likely won't use and if you want them well this script isn't for you.

## Media Management

!!! note

    There a few settings which make life a lot easier when tracking down and keeping certain information for your Anime and with tweaks to make it work better with [HamaAgent](https://github.com/ZeroQI/Hama.bundle){:target="_blank" rel="noopener noreferrer"} for plex.

### Suggested naming scheme

For this I used the [Sonarr Recommended naming scheme](/Sonarr/V3/Sonarr-recommended-naming-scheme/#anime-episode-format){:target="_blank" rel="noopener noreferrer"} for Sonarr with only a small change for the `Series Folder Format` for easier matching.

#### Anime Episode Format

Has all necessary information and a little extra if you needed to rebuild.

```bash
{Series TitleYear} - S{season:00}E{episode:00} - {absolute:000} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRange]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{-Release Group}
```

??? summary "RESULTS:"

    Single Episode:

    `The Series Title! (2010) - S01E01 - 001 - Episode Title 1 [AMZN WEBDL-1080p v2][HDR][10bit][x264][DTS 5.1][JA]-RlsGrp`

    Multi Episode:

    `The Series Title! (2010) - S01E01-E02-E03 - 001-002-003 - Episode Title [AMZN WEBDL-1080p v2][HDR][10bit][x264][DTS 5.1][JA]-RlsGrp`

#### Series Folder Format

Adding year back in with tvdb id allows matching to be correct. Thanks salty.

```bash
{Series TitleTheYear} [tvdb-{TvdbId}]
```

RESULT:

`The Series Title! (2010) [tvdb-12345]`

#### Season Folder Format

The only one real option to use in my opinion.

```bash
Season {season:00}
```

RESULT:

`Season 01`

#### Multi-Episode Style

```bash
Scene
```

RESULTS:

![results](images/results.png)

??? success "example"

    ![!Example image of above](images/rpa-mediamanage.png)

---

## Quality Profile

We need to add HDTV-1080p into the same group as WEB-DL and WEBRip 1080p so that it will download correctly and not upgrade past HDTV-1080P if Preferred Words does not allow it.

![!rpa-quality-profile-group](images/rpa-quality-profile-group.png)

---

## Release Profiles

!!! important
    We're going to make use of 2 separate release profiles.

### First Release Profile

!!! note

    Check mark `Include Preferred when Renaming` and add `{Preferred Words}` to your renaming scheme else you could get a download loop issues!!!

#### Dual Audio

Add this to your Preferred with a score of [500]

```bash
/(dual[ ._-]?audio)/i
```

---

#### Multi-Audio

Add this to your Preferred with a score of [400]

```bash
/(multi[ ._-]?audio)/i
```

---

#### Optional (uncensored)

Add this to your Preferred with a score of [1000]/[-1000] if you want the uncensored version of anime. If you would like it to be priority then set to 1000. If you do not want uncensored set it to -1000.

```bash
/\b(uncensored)\b/i
```

---

??? success "example"
    ![!rpa-release-profile-1](images/rpa-release-profile-1.png)

---

### Second Release Profile

!!! warning
    DO NOT Check mark `Include Preferred when Renaming`

#### Must Not Contain

The reason most of these are added is due to their shitty quality or just in general are not as good as other stuff that is out there. This can be tweaked as needed. Let me know if you run into any issues here. You should be able to just copy paste these in one go.

```bash
/(CuaP|EMBER|PnPSubs|ICEBLUE|URANiME|SLAX|Golumpa|KaiDubs|PuyaSubs|Raws-Maji)/i,
/\b(Beatrice|ohys|Kawaiika|neko|LowPower)\b(?=[ ._-]?(raws)\b)/i,
/(?=(english|funi)).*(dub|dubbed)|\b(dub|dubbed)\b/i
```

??? success "example"
    ![!rpa-must-not-contain.png](/images/rpa-must-not-contain.png)

#### Preferred

Add this to your Preferred with a score of [460]

Dual-Audio

```bash
/(ANThELIa|\bZR\b|kametsu|\bctr\b|\bscy\b|deanzel|\bshir\b)/i
```

```bash
/(\bMK\b|lostyears|exiled-destiny|E-D|BluDragon|Kawairemux)/i
```

---

Add this to your Preferred with a score of [440]

Generic Dual-Audio

```bash
/(iahd|anihls|mkvultra|\bdhd\b|teneighty|redblade|haiku|\bdhd\b)/i
```

---

Add this to your Preferred with a score of [420]

Multi-Audio - Multi-Subs (Usually from Netflix or similar)

```bash
/(\[DragsterPS\])/i
```

---

Add this to your Preferred with a score of [400]

Dual-Audio - Mostly older content but has some newer stuff. Really good quality and searches different sources.

```bash
/(\[Koten_Gars\])/i
```

---

Add this to your Preferred with a score of [380]

Dual-Audio - Mostly older and limited, but what he does have is amazing quality.

```bash
/\b(Hark0n)\b/i
```

---

Add this to your Preferred with a score of [360]

Dual-Audio - xPearse has some raws.

```bash
/(\[GHOST\]|\[xPearse\]|\[Moodkiller\])/i
```

---

Add this to your Preferred with a score of [340]

Dual-Audio - NPC is mostly older.

```bash
/(\[NPC\]|\[A-L\])/i
```

---

Add this to your Preferred with a score of [320]

Dual-Audio

```bash
/(\[Cleo\])/i
```

---

Add this to your Preferred with a score of [300]

Subs with multi such as German, French , Spanish, Italian, Russian, Arabic, Portuguese and English

```bash
/\b(Erai-raws)\b/i
```

---

Add this to your Preferred with a score of [280]

Subs mainly but has Dual-Audio

```bash
/(\[Anime Time\]|\[Mysteria\])/i
```

---

Add this to your Preferred with a score of [260]

FanSubs, occasional dual audio for ASW/Akihito

```bash
/(\[Asenshi\]|\[AkihitoSubs\]|\[ASW\])/i
```

---

Add this to your Preferred with a score of [240]

Subs, Replaces HorribleSubs below for newer content

```bash
/(\[SubsPlease\]|\[Hi10\])/i
```

---

Add this to your Preferred with a score of [220]

Subs (Now defunct but stil good SubsPlease has taken the mantle.)

```bash
/\b(horriblesubs|sallysubs)\b/i
```

---

Add this to your Preferred with a score of [200]

Anime RG has Dual Audio and multiple audio such as German, French, Italian, Spanish, Arabic, Portuguese. | Judas: Similar to Erai-raws with multi subs. | Subs

```bash
/(\[AnimeRG\]|\[Judas\]|Commie|GJM)/i
```

---

Add this to your Preferred with a score of [180]

Subs, FanSubs

```bash
/(\[SNSbu\]|\[DB\]|\[Coalgirls\]|FFF|FFFansubs|BluRayDesuYo)/i
```

---

Add this to your Preferred with a score of [160]

Little bit of Dual-Audio | Mainly Fansub

```bash
/(\[CH\])/i
```

---

Add this to your Preferred with a score of [140]

FanSubs

```bash
/(\[Licca\]|\[Soldado\])/i
```

---

Add this to your Preferred with a score of [120]

Subs

```bash
/(\[SakuraCircle\])/i
```

---

Add this to your Preferred with a score of [100]

FanSubs

```bash
/(\[Orphan\]|\[Yabai\])/i
```

---

Add this to your Preferred with a score of [80]

Subs

```bash
/(\[kBaraka\])/i
```

---

Add this to your Preferred with a score of [60]

Take 10bit fan-subbed videos from other groups and release an 8bit hardsubbed version of it. We do this because while 10bit offers quite a few advantages, not everyone's PS3, 360, hardware player, toaster etc can play it.

```bash
/(\[DeadFish\])/i
```

---

Add this to your Preferred with a score of [40]

FanSubs

```bash
/(\[NewbSubs\]|\[Nii-sama\]|\[Nii-sama\])/i
```

---

??? success "example"
    ![!rpa-release-profile-2.png](images/rpa-release-profile-2.png)

---

### Acknowledgements

Most of my information and knowledge came from Kaiser and rg9400 for the anime releases and best groups on discord and [TRaSH](https://trash-guides.info/) for his amazing regex.
