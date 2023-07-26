### Sonarr current logic

??? abstract "Sonarr current logic - [Click to show/hide]"

    As of 2021-11-06 the logic is as follows:

    The Current logic on how downloads are compared is **Quality Trumps All** :bangbang:

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

    !!! warning ""
        REPACKS and PROPERs are v2 of Qualities and thus rank above a non-repack of the same quality.

         `Settings` => `Media Management` => `File Management` => `Proper & Repacks` Change to `Do Not Prefer` and use a preferred word regex of `/\b(repack|proper)\b/i`
