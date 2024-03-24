??? abstract "Optional - [Click to show/hide]"

    !!! tip "**I recommend to use the `x265 (no HDR/DV)` over the `x265 (HD)`, Read the Why below and don't forget to read the warning, :warning: Only ever include one of them :warning:**"
    !!! tip "**I recommend to use the `SDR`,<br> This will help to prevent to grab UHD/4k releases without HDR Formats**"

    | Custom Format                                                                                                       | Score                                                            | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------- |
    | [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups)       | {{ radarr['cf']['bad-dual-groups']['trash_scores']['default'] }} | {{ radarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ radarr['cf']['dv-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl)                     | :interrobang:                                                    | {{ radarr['cf']['dv-webdl']['trash_id'] }}        |
    | [{{ radarr['cf']['hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus-boost)       | {{ radarr['cf']['hdr10plus-boost']['trash_scores']['default'] }} | {{ radarr['cf']['hdr10plus-boost']['trash_id'] }} |
    | [{{ radarr['cf']['evo-no-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl)             | {{ radarr['cf']['evo-no-webdl']['trash_scores']['default'] }}    | {{ radarr['cf']['evo-no-webdl']['trash_id'] }}    |
    | [{{ radarr['cf']['no-rlsgroup']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup)               | {{ radarr['cf']['no-rlsgroup']['trash_scores']['default'] }}     | {{ radarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ radarr['cf']['obfuscated']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#obfuscated)                 | {{ radarr['cf']['obfuscated']['trash_scores']['default'] }}      | {{ radarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ radarr['cf']['retags']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#retags)                         | {{ radarr['cf']['retags']['trash_scores']['default'] }}          | {{ radarr['cf']['retags']['trash_id'] }}          |
    | [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene)                           | {{ radarr['cf']['scene']['trash_scores']['default'] }}           | {{ radarr['cf']['scene']['trash_id'] }}           |
    | [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning: | {{ radarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}   | {{ radarr['cf']['x265-no-hdrdv']['trash_id'] }}   |
    | [{{ radarr['cf']['sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#sdr)                               | {{ radarr['cf']['sdr']['trash_scores']['default'] }}             | {{ radarr['cf']['sdr']['trash_id'] }}             |
    | [{{ radarr['cf']['dv-disk']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-disk)                       | {{ radarr['cf']['dv-disk']['trash_scores']['default'] }}         | {{ radarr['cf']['dv-disk']['trash_id'] }}         |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.
    - **{{ radarr['cf']['dv-webdl']['name'] }}:** This is a special Custom Format that Block WEBDL with Dolby Vision but without HDR10 fallback.

        This Custom Format works together with the normal DV Custom Format that you can use to prefer Dolby Vision.

        Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

        Remuxes and Bluray have a fallback to HDR10.

        !!! tip
            `[DV WEBDL]` = This custom format you need to score depending of your personal use and setup.

            - If you only watch your movies on a setup that completely supports Dolby Vision from start to end then give it a score of `0` or just don't add it.
            - If you (or family members you share your collection with) have a setup that doesn't support Dolby Vision then you should add this with a score of `{{ radarr['cf']['dv-webdl']['trash_scores']['default'] }}`.

    - **{{ radarr['cf']['hdr10plus-boost']['name'] }}:** [*Optional*] (use this one only if you have a (Samsung) TV that supports HDR10+ and you don't have a Setup that supports DV or you prefer HDR10+)
    - **{{ radarr['cf']['evo-no-webdl']['name'] }}:** This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
    - **{{ radarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
    - **{{ radarr['cf']['obfuscated']['name'] }}:** [*Optional*] (use these only if you dislike renamed releases)
    - **{{ radarr['cf']['retags']['name'] }}:** [*Optional*] (use these only if you dislike retagged releases)
    - **{{ radarr['cf']['scene']['name'] }}:** [*Optional*] (use these only if you dislike scene releases)
    - **{{ radarr['cf']['x265-no-hdrdv']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        **But it will allow x265 releases if they have HDR and/or DV**

        *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

        In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}`

        !!! Danger "Don't use this together with [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"

    - **{{ radarr['cf']['sdr']['name'] }}:** This will help to prevent to grab UHD/4k releases without HDR Formats.
    - **{{ radarr['cf']['dv-disk']['name'] }}:** This will boost the score for Dolby Vision Releases using the original full quality Dolby Vision layer from the disc release to replace the old WEBDL HYBRID release.
