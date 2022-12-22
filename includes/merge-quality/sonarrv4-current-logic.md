### Sonarr v4 current logic

??? summary "Sonarr v4 current logic - [CLICK TO EXPAND]"

    As of v4 release the logic is as follows:

    The Current logic on how downloads are compared is **Quality Trumps All** :bangbang:

    1. Quality
    1. Custom Formats
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
