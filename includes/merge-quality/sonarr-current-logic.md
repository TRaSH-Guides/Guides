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

        \* Use Custom Formats and TRaSH Guide's [season pack custom format](https://trash-guides.info/Sonarr/sonarr-collection-of-custom-formats/#season-pack) with a score greater than zero to prefer season packs.

    !!! warning ""

        REPACKS and PROPERs are v2 of Qualities and thus rank above a non-repack of the same quality. [Set Media Management => File Management `Download Proper & Repacks` to "Do Not Prefer"](/sonarr/settings#file-management) and use [TRaSH's Repack/Proper Custom Format](https://trash-guides.info/Sonarr/sonarr-collection-of-custom-formats/#repackproper) with a positive score as suggested by [TRaSH's Guides](https://trash-guides.info/Sonarr/sonarr-setup-quality-profiles/)
