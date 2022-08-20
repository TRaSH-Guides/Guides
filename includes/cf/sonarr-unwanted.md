??? summary "Unwanted - [CLICK TO EXPAND]"
    | Custom Format                                                                                                 | Score                                                | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#br-disk)                 | {{ sonarr['cf']['br-disk']['trash_score'] }}         | {{ sonarr['cf']['br-disk']['trash_id'] }}         |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#lq)                           | {{ sonarr['cf']['lq']['trash_score'] }}              | {{ sonarr['cf']['lq']['trash_id'] }}              |
    | [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#x265-hd)                 | {{ sonarr['cf']['x265-hd']['trash_score'] }}         | {{ sonarr['cf']['x265-hd']['trash_id'] }}         |
    | [{{ sonarr['cf']['no-rlsgroup']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#no-rlsgroup)         | {{ sonarr['cf']['no-rlsgroup']['trash_score'] }}     | {{ sonarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ sonarr['cf']['obfuscated']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#obfuscated)           | {{ sonarr['cf']['obfuscated']['trash_score'] }}      | {{ sonarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ sonarr['cf']['retags']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#retags)                   | {{ sonarr['cf']['retags']['trash_score'] }}          | {{ sonarr['cf']['retags']['trash_id'] }}          |
    | [{{ sonarr['cf']['bad-dual-groups']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#bad-dual-groups) | {{ sonarr['cf']['bad-dual-groups']['trash_score'] }} | {{ sonarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ sonarr['cf']['dv-webdl']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#dv-webdl)               | ??????                                               | {{ sonarr['cf']['dv-webdl']['trash_id'] }}        |

    ??? example "Breakdown and Why - [CLICK TO EXPAND]"

        - **{{ sonarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
        - **{{ sonarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
        - **{{ sonarr['cf']['xhd']['name'] }}:** This blocks/ignores 720/1080p releases that are encoded in x265 - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.
        - **{{ sonarr['cf']['no-rlsgroup']['name'] }}:** [Optional] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
        - **{{ sonarr['cf']['obfuscated']['name'] }}:** [Optional] (use these only if you dislike renamed releases)
        - **{{ sonarr['cf']['retags']['name'] }}:** [Optional] (use these only if you dislike retagged releases)
        - **{{ sonarr['cf']['bad-dual-groups']['name'] }}:** These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
        Also they often even rename the release name in to Portuguese.
        - **{{ sonarr['cf']['dv-webdl']['name'] }}:** This is a special Custom Format that Block WEBDL with Dolby Vision but without HDR10 fallback.

            This Custom Format works together with the normal DV Custom Format that you can use to prefer Dolby Vision.

            Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

            Remuxes and Bluray have a fallback to HDR10.

            !!! hint
                `[DV WEBDL]` = This custom format you need to score depending of your personal use and setup.

                - If you only watch your movies on a setup that completely supports Dolby Vision from start to end then give it a score of `0` or just don't add it.
                - If you (or family members you share your collection with) have a setup that doesn't support Dolby Vision then you should add this with a score of `-10000`.
