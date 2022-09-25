??? summary "Unwanted - [CLICK TO EXPAND]"
    | Custom Format                                                                                                           | Score                                                                    | Trash ID                                          |
    | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------- |
    | [{{ radarr['cf']['br-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#br-disk)                           | {{ radarr['cf']['br-disk']['trash_score'] }}                             | {{ radarr['cf']['br-disk']['trash_id'] }}         |
    | [{{ radarr['cf']['evo-no-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl)                 | {{ radarr['cf']['evo-no-webdl']['trash_score'] }}                        | {{ radarr['cf']['evo-no-webdl']['trash_id'] }}    |
    | [{{ radarr['cf']['lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#lq)                                     | {{ radarr['cf']['lq']['trash_score'] }}                                  | {{ radarr['cf']['lq']['trash_id'] }}              |
    | [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning:                 | {{ radarr['cf']['x265-hd']['trash_score'] }}                             | {{ radarr['cf']['x265-hd']['trash_id'] }}         |
    | [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning:     | {{ radarr['cf']['x265-no-hdrdv']['trash_score'] }}                       | {{ radarr['cf']['x265-no-hdrdv']['trash_id'] }}   |
    | [{{ radarr['cf']['3d']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#3d)                                     | {{ radarr['cf']['3d']['trash_score'] }}                                  | {{ radarr['cf']['3d']['trash_id'] }}              |
    | [{{ radarr['cf']['no-rlsgroup']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup)                   | {{ radarr['cf']['no-rlsgroup']['trash_score'] }}                         | {{ radarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ radarr['cf']['obfuscated']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#obfuscated)                     | {{ radarr['cf']['obfuscated']['trash_score'] }}                          | {{ radarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ radarr['cf']['retags']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#retags)                             | {{ radarr['cf']['retags']['trash_score'] }}                              | {{ radarr['cf']['retags']['trash_id'] }}          |
    | [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups)           | {{ radarr['cf']['bad-dual-groups']['trash_score'] }}                     | {{ radarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ radarr['cf']['dv-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl)                         | ??????                                                                   | {{ radarr['cf']['dv-webdl']['trash_id'] }}        |
    | [{{ radarr['cf']['french-lq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#fr-lq) | {{ radarr['cf']['french-lq']['trash_score'] }} | {{ radarr['cf']['french-lq']['trash_id'] }} |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ radarr['cf']['evo-no-webdl']['name'] }}:** This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
    - **{{ radarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
    - **{{ radarr['cf']['x265-hd']['name'] }}:** This blocks/ignores 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        !!! Danger "Don't use this together with the following Custom Format [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning:"

    - **{{ radarr['cf']['x265-no-hdrdv']['name'] }}:** This blocks/ignores 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        **but it will allow to exclude/bypass if it has HDR and/or DV**

        *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

        In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-no-hdrdv']['trash_score'] }}`

        !!! Danger "Don't use this together with the following Custom Format [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd) :warning:"

    - **{{ radarr['cf']['3d']['name'] }}:** Is 3D still a thing for home use ?
    - **{{ radarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
    - **{{ radarr['cf']['obfuscated']['name'] }}:** [*Optional*] (use these only if you dislike renamed releases)
    - **{{ radarr['cf']['retags']['name'] }}:** [*Optional*] (use these only if you dislike retagged releases)
    - **{{ radarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.
    - **{{ radarr['cf']['dv-webdl']['name'] }}:** This is a special Custom Format that Block WEBDL with Dolby Vision but without HDR10 fallback.

        This Custom Format works together with the normal DV Custom Format that you can use to prefer Dolby Vision.

        Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

        Remuxes and Bluray have a fallback to HDR10.

        !!! hint
            `[DV WEBDL]` = This custom format you need to score depending of your personal use and setup.

            - If you only watch your movies on a setup that completely supports Dolby Vision from start to end then give it a score of `0` or just don't add it.
            - If you (or family members you share your collection with) have a setup that doesn't support Dolby Vision then you should add this with a score of `{{ radarr['cf']['dv-webdl']['trash_score'] }}`.
    - **{{ radarr['cf']['french-lq']['name'] }}:** A collection of known Low Quality French groups that are often banned from the the top trackers because the lack of quality or other reasons.
