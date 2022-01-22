# How to Merge Quality

The Current logic on how downloads are compared is **Quality Trumps All** :bangbang:

In some cases it might be preferred to not have Quality Trump All, and let it be Handled via Preferred Words / Custom Formats.

To accomplish this you will need to merge the Quality's with each other.

## Current Logic

Here you will see the current logic so you understand How the possible downloads are compared.

As of 2021-11-06 the logic is as follows:

### Radarr current logic

??? summary "Radarr current logic- [CLICK TO EXPAND]"

    1. Quality
    1. Custom Format Score
    1. Protocol
    1. Indexer Priority
    1. Indexer Flags
    1. Seeds/Peers (If Torrent)
    1. Age (If Usenet)
    1. Size

    [Source: Wiki Servarr](https://wiki.servarr.com/radarr/faq#how-are-possible-downloads-compared){:target="_blank" rel="noopener noreferrer"}

    !!! attention ""
        REPACKS and PROPERs are v2 of Qualities and thus rank above a non-repack of the same quality.

         `Settings` => `Media Management` => `File Management` => `Proper & Repacks` Change to `Do Not Prefer` and use the [Repack/Proper Custom Format](/Radarr/Radarr-collection-of-custom-formats/#repack-proper){:target="_blank" rel="noopener noreferrer"}

### Sonarr current logic

??? summary "Sonarr current logic- [CLICK TO EXPAND]"

    1. Quality
    1. Language
    1. Preferred Word Score
    1. Protocol
    1. Episode Count
    1. Episode Number
    1. Indexer Priority
    1. Seeds/Peers (If Torrent)
    1. Age (If Usenet)
    1. Size

    [Source: Wiki Servarr](https://wiki.servarr.com/sonarr/faq#how-are-possible-downloads-compared){:target="_blank" rel="noopener noreferrer"}

    !!! attention ""
        REPACKS and PROPERs are v2 of Qualities and thus rank above a non-repack of the same quality.

         `Settings` => `Media Management` => `File Management` => `Proper & Repacks` Change to `Do Not Prefer` and use a preferred word regex of `/\b(repack|proper)\b/i`

## Merge the Qualities

Go to your preferred Quality Profile or Create a new one.

`Settings` => `Profiles`

In this example we will merge the following qualities together:

- Bluray-720p
- Bluray-1080p
- WEBDL/WEBRIP-1080p

To merge them you need to click on the edit groups.

![!Merge Qualities](images/merge.gif)

When done Sonarr/Radarr upgrades will be handled via Preferred Words / Custom Formats.

--8<-- "includes/support.md"
