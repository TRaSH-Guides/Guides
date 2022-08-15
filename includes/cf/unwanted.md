??? summary "Unwanted - [CLICK TO EXPAND]"
    | Custom Format                           | Score                                          | LINK                                                                                                                                                  |
    | --------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
    | {{ radarr['br-disk']['name'] }}         | {{ radarr['br-disk']['trash_score'] }}         | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#br-disk){: .header-icons target=_blank rel="noopener noreferrer" }         |
    | {{ radarr['evo-no-webdl']['name'] }}    | {{ radarr['evo-no-webdl']['trash_score'] }}    | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl){: .header-icons target=_blank rel="noopener noreferrer" }    |
    | {{ radarr['lq']['name'] }}              | {{ radarr['lq']['trash_score'] }}              | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#lq){: .header-icons target=_blank rel="noopener noreferrer" }              |
    | {{ radarr['x265-7201080p']['name'] }}   | {{ radarr['x265-7201080p']['trash_score'] }}   | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#x265-7201080p){: .header-icons target=_blank rel="noopener noreferrer" }   |
    | {{ radarr['3d']['name'] }}              | {{ radarr['3d']['trash_score'] }}              | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#3d){: .header-icons target=_blank rel="noopener noreferrer" }              |
    | {{ radarr['no-rlsgroup']['name'] }}     | {{ radarr['no-rlsgroup']['trash_score'] }}     | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup){: .header-icons target=_blank rel="noopener noreferrer" }     |
    | {{ radarr['obfuscated']['name'] }}      | {{ radarr['obfuscated']['trash_score'] }}      | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#obfuscated){: .header-icons target=_blank rel="noopener noreferrer" }      |
    | {{ radarr['retags']['name'] }}          | {{ radarr['retags']['trash_score'] }}          | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#retags){: .header-icons target=_blank rel="noopener noreferrer" }          |
    | {{ radarr['bad-dual-groups']['name'] }} | {{ radarr['bad-dual-groups']['trash_score'] }} | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups){: .header-icons target=_blank rel="noopener noreferrer" } |
    | {{ radarr['dv-webdl']['name'] }}        | ??????                                         | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl){: .header-icons target=_blank rel="noopener noreferrer" }        |

    ??? example "Breakdown and Why - [CLICK TO EXPAND]"

        - **{{ radarr['br-disk']['name'] }} :** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
        - **{{ radarr['evo-no-webdl']['name'] }}:** This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
        - **{{ radarr['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
        - **{{ radarr['x265-7201080p']['name'] }}:** This blocks/ignores 720/1080p releases that are encoded in x265 - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.
        - **{{ radarr['3d']['name'] }}:** Is 3D still a thing for home use ?
        - **{{ radarr['no-rlsgroup']['name'] }}:** [Optional] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
        - **{{ radarr['obfuscated']['name'] }}:** [Optional] (use these only if you dislike renamed releases)
        - **{{ radarr['retags']['name'] }}:** [Optional] (use these only if you dislike retagged releases)
        - **{{ radarr['bad-dual-groups']['name'] }}:** These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
        Also they often even rename the release name in to Portuguese.
        - **{{ radarr['dv-webdl']['name'] }}:** This is a special Custom Format that Block WEBDL with Dolby Vision but without HDR10 fallback.

            This Custom Format works together with the normal DV Custom Format that you can use to prefer Dolby Vision.

            Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

            Remuxes and Bluray have a fallback to HDR10.

            !!! hint
                `[DV WEBDL]` = This custom format you need to score depending of your personal use and setup.

                - If you only watch your movies on a setup that completely supports Dolby Vision from start to end then give it a score of `0` or just don't add it.
                - If you (or family members you share your collection with) have a setup that doesn't support Dolby Vision then you should add this with a score of `-10000`.