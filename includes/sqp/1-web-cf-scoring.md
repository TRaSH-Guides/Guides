<!-- markdownlint-disable MD041-->
#### Custom Formats and scores

**The following Custom Formats are required:**

??? abstract "Audio - [Click to show/hide]"

    | Custom Format                                                                                                 |                                            Score                                             | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['truehd-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd-atmos)       |  :warning: {{ radarr['cf']['truehd-atmos']['trash_scores']['sqp-1-web-1080p'] }} :warning:   | {{ radarr['cf']['truehd-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['dts-x']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-x)                     |      :warning: {{ radarr['cf']['dts-x']['trash_scores']['sqp-1-web-1080p'] }} :warning:      | {{ radarr['cf']['dts-x']['trash_id'] }}           |
    | [{{ radarr['cf']['atmos-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#atmos-undefined) | :warning: {{ radarr['cf']['atmos-undefined']['trash_scores']['sqp-1-web-1080p'] }} :warning: | {{ radarr['cf']['atmos-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['ddplus-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus-atmos)       |  :warning: {{ radarr['cf']['ddplus-atmos']['trash_scores']['sqp-1-web-1080p'] }} :warning:   | {{ radarr['cf']['ddplus-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['truehd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd)                   |     :warning: {{ radarr['cf']['truehd']['trash_scores']['sqp-1-web-1080p'] }} :warning:      | {{ radarr['cf']['truehd']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-hd-ma']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-ma)             |    :warning: {{ radarr['cf']['dts-hd-ma']['trash_scores']['sqp-1-web-1080p'] }} :warning:    | {{ radarr['cf']['dts-hd-ma']['trash_id'] }}       |
    | [{{ radarr['cf']['flac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#flac)                       |      :warning: {{ radarr['cf']['flac']['trash_scores']['sqp-1-web-1080p'] }} :warning:       | {{ radarr['cf']['flac']['trash_id'] }}            |
    | [{{ radarr['cf']['pcm']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pcm)                         |       :warning: {{ radarr['cf']['pcm']['trash_scores']['sqp-1-web-1080p'] }} :warning:       | {{ radarr['cf']['pcm']['trash_id'] }}             |
    | [{{ radarr['cf']['dts-hd-hra']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-hra)           |   :warning: {{ radarr['cf']['dts-hd-hra']['trash_scores']['sqp-1-web-1080p'] }} :warning:    | {{ radarr['cf']['dts-hd-hra']['trash_id'] }}      |
    | [{{ radarr['cf']['ddplus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus)                   |     :warning: {{ radarr['cf']['ddplus']['trash_scores']['sqp-1-web-1080p'] }} :warning:      | {{ radarr['cf']['ddplus']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-es']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-es)                   |     :warning: {{ radarr['cf']['dts-es']['trash_scores']['sqp-1-web-1080p'] }} :warning:      | {{ radarr['cf']['dts-es']['trash_id'] }}          |
    | [{{ radarr['cf']['dts']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts)                         |       :warning: {{ radarr['cf']['dts']['trash_scores']['sqp-1-web-1080p'] }} :warning:       | {{ radarr['cf']['dts']['trash_id'] }}             |
    | [{{ radarr['cf']['aac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#aac)                         |       :warning: {{ radarr['cf']['aac']['trash_scores']['sqp-1-web-1080p'] }} :warning:       | {{ radarr['cf']['aac']['trash_id'] }}             |
    | [{{ radarr['cf']['dd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dd)                           |       :warning: {{ radarr['cf']['dd']['trash_scores']['sqp-1-web-1080p'] }} :warning:        | {{ radarr['cf']['dd']['trash_id'] }}              |
    | [{{ radarr['cf']['20-stereo']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#20-stereo)             |    :warning: {{ radarr['cf']['20-stereo']['trash_scores']['sqp-1-web-1080p'] }} :warning:    | {{ radarr['cf']['20-stereo']['trash_id'] }}       |

    !!! warning "Scores marked with a :warning: warning :warning: are different to those used in the main public guide"

    !!! danger "The CF with `0` you can choose to add with a score of `0` or just don't add them.<br>The reason why we score them this low is to prevent transcoding as much as possible.<br>The reason why `DTS` and `DTS-ES` have a score of `0` is to make sure that you don't limit yourself too much."

??? abstract "HQ Release Groups - [Click to show/hide]"

    | Custom Format                                                                                                                        |                                             Score                                              | Trash ID                                            |
    | ------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------: | --------------------------------------------------- |
    | [{{ radarr['cf']['bhdstudio']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/bhdstudio.json) |               {{ radarr['cf']['bhdstudio']['trash_scores']['sqp-1-web-1080p'] }}               | {{ radarr['cf']['bhdstudio']['trash_id'] }}         |
    | [{{ radarr['cf']['hallowed']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/hallowed.json)   |                   {{ radarr['cf']['hallowed']['trash_scores']['default'] }}                    | {{ radarr['cf']['hallowed']['trash_id'] }}          |
    | [{{ radarr['cf']['web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-01)                                |                  {{ radarr['cf']['web-tier-01']['trash_scores']['default'] }}                  | {{ radarr['cf']['web-tier-01']['trash_id'] }}       |
    | [{{ radarr['cf']['web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-02)                                |                  {{ radarr['cf']['web-tier-02']['trash_scores']['default'] }}                  | {{ radarr['cf']['web-tier-02']['trash_id'] }}       |
    | [{{ radarr['cf']['web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-03)                                |                  {{ radarr['cf']['web-tier-03']['trash_scores']['default'] }}                  | {{ radarr['cf']['web-tier-03']['trash_id'] }}       |
    | [{{ radarr['cf']['hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-01)                    | :warning: {{ radarr['cf']['hd-bluray-tier-01']['trash_scores']['sqp-1-web-1080p'] }} :warning: | {{ radarr['cf']['hd-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-02)                    | :warning: {{ radarr['cf']['hd-bluray-tier-02']['trash_scores']['sqp-1-web-1080p'] }} :warning: | {{ radarr['cf']['hd-bluray-tier-02']['trash_id'] }} |
    | [{{ radarr['cf']['hd-bluray-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-03)                    | :warning: {{ radarr['cf']['hd-bluray-tier-03']['trash_scores']['sqp-1-web-1080p'] }} :warning: | {{ radarr['cf']['hd-bluray-tier-03']['trash_id'] }} |

    !!! warning "Scores marked with a :warning: warning :warning: are different to those used in the main public guide"

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/sqp/radarr-unwanted-sqp1.md" !}

{! include-markdown "../../includes/sqp/hd-radarr-resolution.md" !}

{! include-markdown "../../includes/sqp/1-streaming-services.md" !}

**The following Custom Formats are optional:**

{! include-markdown "../../includes/sqp/hd-radarr-misc-optional.md" !}

??? abstract "Movie Versions (Optional) - [Click to show/hide]"

    | Custom Format                                                                                                           |                                 Score                                 | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------: | ------------------------------------------------------ |
    | [{{ radarr['cf']['remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remaster)                         |       {{ radarr['cf']['remaster']['trash_scores']['default'] }}       | {{ radarr['cf']['remaster']['trash_id'] }}             |
    | [{{ radarr['cf']['4k-remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#4k-remaster)                   |     {{ radarr['cf']['4k-remaster']['trash_scores']['default'] }}      | {{ radarr['cf']['4k-remaster']['trash_id'] }}          |
    | [{{ radarr['cf']['criterion-collection']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#criterion-collection) | {{ radarr['cf']['criterion-collection']['trash_scores']['default'] }} | {{ radarr['cf']['criterion-collection']['trash_id'] }} |
    | [{{ radarr['cf']['masters-of-cinema']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#masters-of-cinema)       |  {{ radarr['cf']['masters-of-cinema']['trash_scores']['default'] }}   | {{ radarr['cf']['masters-of-cinema']['trash_id'] }}    |
    | [{{ radarr['cf']['vinegar-syndrome']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vinegar-syndrome)         |   {{ radarr['cf']['vinegar-syndrome']['trash_scores']['default'] }}   | {{ radarr['cf']['vinegar-syndrome']['trash_id'] }}     |
    | [{{ radarr['cf']['special-edition']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#special-edition)           |   {{ radarr['cf']['special-edition']['trash_scores']['default'] }}    | {{ radarr['cf']['special-edition']['trash_id'] }}      |
    | [{{ radarr['cf']['imax-enhanced']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax-enhanced)               |    {{ radarr['cf']['imax-enhanced']['trash_scores']['default'] }}     | {{ radarr['cf']['imax-enhanced']['trash_id'] }}        |

    !!! info

        - If you prefer 1080p WEBDL with IMAX-E then add [{{ radarr['cf']['imax-enhanced']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax-enhanced) with the default scores.
        - The reason why we don't add [{{ radarr['cf']['imax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax) is because BHDStudio didn't add IMAX to their filename before 2023-07-27, and a WEB-DL generally does not add movie versions.

        !!! danger "- Adding IMAX/IMAX Enhanced will replace the BHDStudio release in most cases<br>- When adding movie versions except for the `Imax-Enhanced`, a random Blu-ray encode might replace a WEB-DL because WEB-DL generally does not add movie versions."
<!-- markdownlint-enable MD041-->
