### Radarr current logic

??? abstract "Radarr current logic - [Click to show/hide]"

    As of 2021-11-06 the logic is as follows:

    The Current logic on how downloads are compared is **Quality Trumps All** :bangbang:

    1. Quality
    1. Custom Format Score
    1. Protocol
    1. Indexer Priority
    1. Indexer Flags
    1. Seeds/Peers (If Torrent)
    1. Age (If Usenet)
    1. Size

    [Source: Wiki Servarr](https://wiki.servarr.com/radarr/faq#how-are-possible-downloads-compared){:target="_blank" rel="noopener noreferrer"}

    !!! warning ""
        REPACKS and PROPERs are v2 of Qualities and thus rank above a non-repack of the same quality.

         `Settings` => `Media Management` => `File Management` => `Proper & Repacks` Change to `Do Not Prefer` and use the [Repack/Proper Custom Format](/Radarr/Radarr-collection-of-custom-formats/#repackproper){:target="_blank" rel="noopener noreferrer"}
