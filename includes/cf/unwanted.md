??? summary "Unwanted - [CLICK TO EXPAND]"
    | Custom Format    | Score  | LINK |
    | ---------------- | ------ | ---- |
    | BR-DISK          | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#br-disk){: .header-icons target=_blank rel="noopener noreferrer" } |
    | EVO (no WEBDL)   | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |
    | LQ               | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#lq){: .header-icons target=_blank rel="noopener noreferrer" } |
    | x265 (720/1080p) | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#x265-7201080p){: .header-icons target=_blank rel="noopener noreferrer" } |
    | 3D               | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#3d){: .header-icons target=_blank rel="noopener noreferrer" } |
    | No-RlsGroup      | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup){: .header-icons target=_blank rel="noopener noreferrer" } |
    | Obfuscated       | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#obfuscated){: .header-icons target=_blank rel="noopener noreferrer" } |
    | Retags           | -10000 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#retags){: .header-icons target=_blank rel="noopener noreferrer" } |
    | DV (WEBDL)       | ?????? | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |

    ??? example "Breakdown and Why - [CLICK TO EXPAND]"

        - **BR-DISK:** This is a custom format to help Radarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
        - **EVO (no WEBDL):** This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
        - **LQ:** A collection of known Low Quality groups that are often banned from the the top trackers because the lack of quality or other reasons.
        - **x265 (720/1080p):** This blocks/ignores 720/1080p releases that are encoded in x265 - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.
        - **3D:** Is 3D still a thing for home use ?
        - **No-RlsGroup:** [Optional] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
        - **Obfuscated:** [Optional] (use these only if you dislike renamed releases)
        - **Retags:** [Optional] (use these only if you dislike retagged releases)
        - **DV (WEBDL):** This is a special Custom Format that Block WEBDL with Dolby Vision but without HDR10 fallback.

            This Custom Format works together with the normal DV Custom Format that you can use to prefer Dolby Vision.

            Most WEBDL from Streaming Services don't have the fallback to HDR10, What can results in playback issues like weird colors if you want to play it on a not Dolby Vision compatible setup.

            Remuxes and Bluray have a fallback to HDR10.

            !!! hint
                `[DV WEBDL]` = This custom format you need to score depending of your personal use and setup.

                - If you only watch your movies on a setup that completely supports Dolby Vision from start to end then give it a score of `0` or just don't add it.
                - If you (or family members you share your collection with) have a setup that doesn't support Dolby Vision then you should add this with a score of `-10000`.
