<!-- markdownlint-disable MD041-->
### Sonarr current logic

??? abstract "Sonarr current logic - [Click to show/hide]"

    As of 2024-01-16 the logic is as follows:

    The Current logic on how downloads are compared is **Quality Trumps All** :bangbang:

    1. Quality
    1. Custom Format Score
    1. Protocol
    1. Episode Count
    1. Episode Number
    1. Indexer Priority
    1. Seeds/Peers (If Torrent)
    1. Age (If Usenet)
    1. Size

    [Source: Wiki Servarr](https://wiki.servarr.com/sonarr/faq#how-are-possible-downloads-compared){:target="_blank" rel="noopener noreferrer"}

    !!! warning ""

        \* Use the [Season Pack Custom Format](/Sonarr/sonarr-collection-of-custom-formats/#season-pack) with a score greater than zero to prefer season packs.

    !!! warning ""

        REPACKS and PROPERs are v2 of Qualities and thus rank above a non-repack of the same quality.

        `Settings` => `Media Management` => `File Management` => `Proper & Repacks` Change to `Do Not Prefer` and use the [Repack/Proper Custom Format](/Sonarr/sonarr-collection-of-custom-formats/#repackproper){:target="_blank" rel="noopener noreferrer"}
<!-- markdownlint-enable MD041-->
