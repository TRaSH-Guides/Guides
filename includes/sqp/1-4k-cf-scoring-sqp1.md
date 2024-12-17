#### Custom Formats and scores

**The following Custom Formats are required:**

??? abstract "Audio - [Click to show/hide]"

    | Custom Format                                                                                                 |                                          Score                                           | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['truehd-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd-atmos)       |  :warning: {{ radarr['cf']['truehd-atmos']['trash_scores']['sqp-1-2160p'] }} :warning:   | {{ radarr['cf']['truehd-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['dts-x']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-x)                     |      :warning: {{ radarr['cf']['dts-x']['trash_scores']['sqp-1-2160p'] }} :warning:      | {{ radarr['cf']['dts-x']['trash_id'] }}           |
    | [{{ radarr['cf']['atmos-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#atmos-undefined) | :warning: {{ radarr['cf']['atmos-undefined']['trash_scores']['sqp-1-2160p'] }} :warning: | {{ radarr['cf']['atmos-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['ddplus-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus-atmos)       |  :warning: {{ radarr['cf']['ddplus-atmos']['trash_scores']['sqp-1-2160p'] }} :warning:   | {{ radarr['cf']['ddplus-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['truehd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd)                   |     :warning: {{ radarr['cf']['truehd']['trash_scores']['sqp-1-2160p'] }} :warning:      | {{ radarr['cf']['truehd']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-hd-ma']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-ma)             |    :warning: {{ radarr['cf']['dts-hd-ma']['trash_scores']['sqp-1-2160p'] }} :warning:    | {{ radarr['cf']['dts-hd-ma']['trash_id'] }}       |
    | [{{ radarr['cf']['flac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#flac)                       |      :warning: {{ radarr['cf']['flac']['trash_scores']['sqp-1-2160p'] }} :warning:       | {{ radarr['cf']['flac']['trash_id'] }}            |
    | [{{ radarr['cf']['pcm']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pcm)                         |       :warning: {{ radarr['cf']['pcm']['trash_scores']['sqp-1-2160p'] }} :warning:       | {{ radarr['cf']['pcm']['trash_id'] }}             |
    | [{{ radarr['cf']['dts-hd-hra']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-hra)           |   :warning: {{ radarr['cf']['dts-hd-hra']['trash_scores']['sqp-1-2160p'] }} :warning:    | {{ radarr['cf']['dts-hd-hra']['trash_id'] }}      |
    | [{{ radarr['cf']['ddplus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus)                   |     :warning: {{ radarr['cf']['ddplus']['trash_scores']['sqp-1-2160p'] }} :warning:      | {{ radarr['cf']['ddplus']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-es']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-es)                   |     :warning: {{ radarr['cf']['dts-es']['trash_scores']['sqp-1-2160p'] }} :warning:      | {{ radarr['cf']['dts-es']['trash_id'] }}          |
    | [{{ radarr['cf']['dts']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts)                         |       :warning: {{ radarr['cf']['dts']['trash_scores']['sqp-1-2160p'] }} :warning:       | {{ radarr['cf']['dts']['trash_id'] }}             |
    | [{{ radarr['cf']['aac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#aac)                         |       :warning: {{ radarr['cf']['aac']['trash_scores']['sqp-1-2160p'] }} :warning:       | {{ radarr['cf']['aac']['trash_id'] }}             |
    | [{{ radarr['cf']['dd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dd)                           |       :warning: {{ radarr['cf']['dd']['trash_scores']['sqp-1-2160p'] }} :warning:        | {{ radarr['cf']['dd']['trash_id'] }}              |

    !!! warning "Scores marked with a :warning: warning :warning: are different to those used in the main public guide"

    !!! danger "The CF with `0` you can choose to add with a score of `0` or just don't add them.<br>The reason why we score them this low is to prevent transcoding as much as possible.<br>The reason why `DTS` and `DTS-ES` have a score of `0` is to make sure that you don't limit yourself too much."

??? abstract "All HDR Formats + DV (WEBDL) - [Click to show/hide]"

    **Why would I choose All HDR formats + add `DV (WEBDL)` with a score of `-10000`?**

    - Because you want maximum compatibility across all devices.
    - You must add **ALL** the HDR formats - don't leave any of them out!
    - You must add DV-WEBDL with a score if `-10000`!

    {! include-markdown "../../includes/cf/dv-limitations-atv.md" !}

    {! include-markdown "../../includes/cf/dv-info-green-purple.md" !}

    {! include-markdown "../../includes/cf/dv-info-profiles.md" !}

    | Custom Format                                                                                             |                             Score                              | Trash ID                                        |
    | --------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------: | ----------------------------------------------- |
    | [{{ radarr['cf']['dv-hdr10plus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10plus)   | {{ radarr['cf']['dv-hdr10plus']['trash_scores']['default'] }}  | {{ radarr['cf']['dv-hdr10plus']['trash_id'] }}  |
    | [{{ radarr['cf']['dv-hdr10']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10)           |   {{ radarr['cf']['dv-hdr10']['trash_scores']['default'] }}    | {{ radarr['cf']['dv-hdr10']['trash_id'] }}      |
    | [{{ radarr['cf']['dv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv)                       |      {{ radarr['cf']['dv']['trash_scores']['default'] }}       | {{ radarr['cf']['dv']['trash_id'] }}            |
    | [{{ radarr['cf']['dv-hlg']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hlg)               |    {{ radarr['cf']['dv-hlg']['trash_scores']['default'] }}     | {{ radarr['cf']['dv-hlg']['trash_id'] }}        |
    | [{{ radarr['cf']['dv-sdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-sdr)               |    {{ radarr['cf']['dv-sdr']['trash_scores']['default'] }}     | {{ radarr['cf']['dv-sdr']['trash_id'] }}        |
    | [{{ radarr['cf']['hdr10plus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus)         |   {{ radarr['cf']['hdr10plus']['trash_scores']['default'] }}   | {{ radarr['cf']['hdr10plus']['trash_id'] }}     |
    | [{{ radarr['cf']['hdr10']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10)                 |     {{ radarr['cf']['hdr10']['trash_scores']['default'] }}     | {{ radarr['cf']['hdr10']['trash_id'] }}         |
    | [{{ radarr['cf']['hdr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr)                     |      {{ radarr['cf']['hdr']['trash_scores']['default'] }}      | {{ radarr['cf']['hdr']['trash_id'] }}           |
    | [{{ radarr['cf']['hdr-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr-undefined) | {{ radarr['cf']['hdr-undefined']['trash_scores']['default'] }} | {{ radarr['cf']['hdr-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['pq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pq)                       |      {{ radarr['cf']['pq']['trash_scores']['default'] }}       | {{ radarr['cf']['pq']['trash_id'] }}            |
    | [{{ radarr['cf']['hlg']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hlg)                     |      {{ radarr['cf']['hlg']['trash_scores']['default'] }}      | {{ radarr['cf']['hlg']['trash_id'] }}           |
    | [{{ radarr['cf']['dv-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-webdl)           |   {{ radarr['cf']['dv-webdl']['trash_scores']['default'] }}    | {{ radarr['cf']['dv-webdl']['trash_id'] }}      |

    !!! danger "The reason why we add `DV (WEBDL)` is because you want maximum compatibility across all devices :warning:"

??? abstract "HQ Release Groups - [Click to show/hide]"

    | Custom Format                                                                                                                        |                                            Score                                            | Trash ID                                             |
    | ------------------------------------------------------------------------------------------------------------------------------------ | :-----------------------------------------------------------------------------------------: | ---------------------------------------------------- |
    | [{{ radarr['cf']['bhdstudio']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/bhdstudio.json) |                 {{ radarr['cf']['bhdstudio']['trash_scores']['default'] }}                  | {{ radarr['cf']['bhdstudio']['trash_id'] }}          |
    | [{{ radarr['cf']['hallowed']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/hallowed.json)   |                  {{ radarr['cf']['hallowed']['trash_scores']['default'] }}                  | {{ radarr['cf']['hallowed']['trash_id'] }}           |
    | [{{ radarr['cf']['web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-01)                                |                {{ radarr['cf']['web-tier-01']['trash_scores']['default'] }}                 | {{ radarr['cf']['web-tier-01']['trash_id'] }}        |
    | [{{ radarr['cf']['web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-02)                                |                {{ radarr['cf']['web-tier-02']['trash_scores']['default'] }}                 | {{ radarr['cf']['web-tier-02']['trash_id'] }}        |
    | [{{ radarr['cf']['web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-03)                                |                {{ radarr['cf']['web-tier-03']['trash_scores']['default'] }}                 | {{ radarr['cf']['web-tier-03']['trash_id'] }}        |
    | [{{ radarr['cf']['hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-01)                    | :warning: {{ radarr['cf']['hd-bluray-tier-01']['trash_scores']['sqp-1-2160p'] }} :warning:  | {{ radarr['cf']['hd-bluray-tier-01']['trash_id'] }}  |
    | [{{ radarr['cf']['hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-02)                    | :warning: {{ radarr['cf']['hd-bluray-tier-02']['trash_scores']['sqp-1-2160p'] }} :warning:  | {{ radarr['cf']['hd-bluray-tier-02']['trash_id'] }}  |
    | [{{ radarr['cf']['hd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-03)                    | :warning: {{ radarr['cf']['hd-bluray-tier-03']['trash_scores']['sqp-1-2160p'] }} :warning:  | {{ radarr['cf']['hd-bluray-tier-03']['trash_id'] }}  |
    | [{{ radarr['cf']['uhd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-01)                  | :warning: {{ radarr['cf']['uhd-bluray-tier-01']['trash_scores']['sqp-1-2160p'] }} :warning: | {{ radarr['cf']['uhd-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['uhd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-02)                  | :warning: {{ radarr['cf']['uhd-bluray-tier-02']['trash_scores']['sqp-1-2160p'] }} :warning: | {{ radarr['cf']['uhd-bluray-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['uhd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#uhd-bluray-tier-03)                  | :warning: {{ radarr['cf']['uhd-bluray-tier-03']['trash_scores']['sqp-1-2160p'] }} :warning: | {{ radarr['cf']['uhd-bluray-tier-03']['trash_id'] }} |

    !!! warning "Scores marked with a :warning: warning :warning: are different to those used in the main public guide"

    !!! tip

        If you use SQP-1 (1080p) as your main/second Radarr you want to remove the following HQ Release Groups

        - [{{ radarr['cf']['hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-01)
        - [{{ radarr['cf']['hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-02)
        - [{{ radarr['cf']['hd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-03)

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/sqp/radarr-unwanted-uhd-sqp1.md" !}

{! include-markdown "../../includes/sqp/hd-radarr-resolution.md" !}

{! include-markdown "../../includes/sqp/1-4k-streaming-services.md" !}

**The following Custom Formats are optional:**

??? abstract "Miscellaneous (Optional) - [Click to show/hide]"

    !!! danger "Adding any of the `HDR10+ Boosts` could result in less streaming optimized releases :warning:"

    | Custom Format                                                                                                       |                                Score                                | Trash ID                                             |
    | ------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------: | ---------------------------------------------------- |
    | [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups)       |  {{ radarr['cf']['bad-dual-groups']['trash_scores']['default'] }}   | {{ radarr['cf']['bad-dual-groups']['trash_id'] }}    |
    | [{{ radarr['cf']['evo-no-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl)             |    {{ radarr['cf']['evo-no-webdl']['trash_scores']['default'] }}    | {{ radarr['cf']['evo-no-webdl']['trash_id'] }}       |
    | [{{ radarr['cf']['no-rlsgroup']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup)               |    {{ radarr['cf']['no-rlsgroup']['trash_scores']['default'] }}     | {{ radarr['cf']['no-rlsgroup']['trash_id'] }}        |
    | [{{ radarr['cf']['obfuscated']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#obfuscated)                 |     {{ radarr['cf']['obfuscated']['trash_scores']['default'] }}     | {{ radarr['cf']['obfuscated']['trash_id'] }}         |
    | [{{ radarr['cf']['retags']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#retags)                         |       {{ radarr['cf']['retags']['trash_scores']['default'] }}       | {{ radarr['cf']['retags']['trash_id'] }}             |
    | [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene)                           |       {{ radarr['cf']['scene']['trash_scores']['default'] }}        | {{ radarr['cf']['scene']['trash_id'] }}              |
    | [{{ radarr['cf']['hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hdr10plus-boost)       |  {{ radarr['cf']['hdr10plus-boost']['trash_scores']['default'] }}   | {{ radarr['cf']['hdr10plus-boost']['trash_id'] }}    |
    | [{{ radarr['cf']['dv-hdr10plus-boost']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dv-hdr10plus-boost) | {{ radarr['cf']['dv-hdr10plus-boost']['trash_scores']['default'] }} | {{ radarr['cf']['dv-hdr10plus-boost']['trash_id'] }} |

    ---

    Breakdown and Why

    - **{{ radarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release and add their own language track (e.g. AAC 2.0 Portuguese) as the first track. Afterward, FFprobe would determine that the media file is Portuguese. It's a common rule that you only add the best audio as the main track.
    Also they often even rename the release name into Portuguese.
    - **{{ radarr['cf']['evo-no-webdl']['name'] }}:** This group is often banned for low-quality Blu-ray releases, but their WEB-DLs are okay.
    - **{{ radarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group which could result in LQ groups being scored incorrectly. For example, a lot of EVO releases end up with a stripped group name. These releases would appear as "upgrades" and could end up getting a decent score after other CFs are scored.
    - **{{ radarr['cf']['obfuscated']['name'] }}:** [*Optional*] Use these only if you wish to avoid renamed releases.
    - **{{ radarr['cf']['retags']['name'] }}:** [*Optional*] Use this if you want to avoid retagged releases. Retagged releases often are not consistent with the quality of the original group's release.
    - **{{ radarr['cf']['scene']['name'] }}:** [*Optional*] Use this only if you want to avoid SCENE releases.
    - **{{ radarr['cf']['hdr10plus-boost']['name'] }}:** [*Optional*] (use this one only if you have a (Samsung) TV that supports HDR10+ and don't mind the chance to get less streaming optimized releases)
    - **{{ radarr['cf']['dv-hdr10plus-boost']['name'] }}:** [*Optional*] (use this one only if you don't mind the chance to get less streaming optimized releases)

{! include-markdown "../../includes/cf/radarr-misc-uhd-optional.md" !}

??? abstract "Movie Versions - [Click to show/hide]"

    | Custom Format                                                                                                           |                                 Score                                 | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------: | ------------------------------------------------------ |
    | [{{ radarr['cf']['remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remaster)                         |       {{ radarr['cf']['remaster']['trash_scores']['default'] }}       | {{ radarr['cf']['remaster']['trash_id'] }}             |
    | [{{ radarr['cf']['4k-remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#4k-remaster)                   |     {{ radarr['cf']['4k-remaster']['trash_scores']['default'] }}      | {{ radarr['cf']['4k-remaster']['trash_id'] }}          |
    | [{{ radarr['cf']['criterion-collection']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#criterion-collection) | {{ radarr['cf']['criterion-collection']['trash_scores']['default'] }} | {{ radarr['cf']['criterion-collection']['trash_id'] }} |
    | [{{ radarr['cf']['masters-of-cinema']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#masters-of-cinema)       |  {{ radarr['cf']['masters-of-cinema']['trash_scores']['default'] }}   | {{ radarr['cf']['masters-of-cinema']['trash_id'] }}    |
    | [{{ radarr['cf']['vinegar-syndrome']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vinegar-syndrome)         |   {{ radarr['cf']['vinegar-syndrome']['trash_scores']['default'] }}   | {{ radarr['cf']['vinegar-syndrome']['trash_id'] }}     |
    | [{{ radarr['cf']['special-edition']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#special-edition)           |   {{ radarr['cf']['special-edition']['trash_scores']['default'] }}    | {{ radarr['cf']['special-edition']['trash_id'] }}      |

    !!! info

        - If you prefer 1080p/2160p WEBDL with IMAX-E then add [{{ radarr['cf']['imax-enhanced']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax-enhanced) with the default scores.
        - The reason why we don't add [{{ radarr['cf']['imax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax) is because BHDStudio didn't add IMAX to their filename before 2023-07-27.

        !!! danger "Adding `IMAX`/`IMAX Enhanced` will replace the BHDStudio release in most cases :warning:"
