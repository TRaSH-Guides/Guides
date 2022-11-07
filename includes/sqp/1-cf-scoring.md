#### Custom Formats and scores

??? summary "Audio - [CLICK TO EXPAND]"
    !!! danger "The CF with `0` you can choose to add with a score of `0` or just don't add them.<br>The reason why we score them this low is to prevent transcoding as much as possible<br>The reason why `DTS` has a score of `0` is to make sure you don't limit your self to much."

    | Custom Format                                                                                                 |            Score | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | ---------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['truehd-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd-atmos)       | :warning: -10000 | {{ radarr['cf']['truehd-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['dts-x']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-x)                     | :warning: -10000 | {{ radarr['cf']['dts-x']['trash_id'] }}           |
    | [{{ radarr['cf']['atmos-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#atmos-undefined) |      :warning: 0 | {{ radarr['cf']['atmos-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['ddplus-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus-atmos)       |      :warning: 0 | {{ radarr['cf']['ddplus-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['truehd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd)                   | :warning: -10000 | {{ radarr['cf']['truehd']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-hd-ma']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-ma)             | :warning: -10000 | {{ radarr['cf']['dts-hd-ma']['trash_id'] }}       |
    | [{{ radarr['cf']['flac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#flac)                       |      :warning: 0 | {{ radarr['cf']['flac']['trash_id'] }}            |
    | [{{ radarr['cf']['pcm']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pcm)                         |      :warning: 0 | {{ radarr['cf']['pcm']['trash_id'] }}             |
    | [{{ radarr['cf']['dts-hd-hra']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-hra)           | :warning: -10000 | {{ radarr['cf']['dts-hd-hra']['trash_id'] }}      |
    | [{{ radarr['cf']['ddplus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus)                   |      :warning: 0 | {{ radarr['cf']['ddplus']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-es']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-es)                   | :warning: -10000 | {{ radarr['cf']['dts-es']['trash_id'] }}          |
    | [{{ radarr['cf']['dts']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts)                         |      :warning: 0 | {{ radarr['cf']['dts']['trash_id'] }}             |
    | [{{ radarr['cf']['aac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#aac)                         |      :warning: 0 | {{ radarr['cf']['aac']['trash_id'] }}             |
    | [{{ radarr['cf']['dd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dd)                           |      :warning: 0 | {{ radarr['cf']['dd']['trash_id'] }}              |

??? summary "Movie Versions - [CLICK TO EXPAND]"

    !!! danger "Adding `IMAX`/`IMAX Enhanced` will replace the BHDStudio release :warning:"

    | Custom Format                                                                                                           | Score                                                     | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
    | [{{ radarr['cf']['hybrid']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hybrid)                             | {{ radarr['cf']['hybrid']['trash_score'] }}               | {{ radarr['cf']['hybrid']['trash_id'] }}               |
    | [{{ radarr['cf']['remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remaster)                         | {{ radarr['cf']['remaster']['trash_score'] }}             | {{ radarr['cf']['remaster']['trash_id'] }}             |
    | [{{ radarr['cf']['4k-remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#4k-remaster)                   | {{ radarr['cf']['4k-remaster']['trash_score'] }}          | {{ radarr['cf']['4k-remaster']['trash_id'] }}          |
    | [{{ radarr['cf']['criterion-collection']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#criterion-collection) | {{ radarr['cf']['criterion-collection']['trash_score'] }} | {{ radarr['cf']['criterion-collection']['trash_id'] }} |
    | [{{ radarr['cf']['special-edition']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#special-edition)           | {{ radarr['cf']['special-edition']['trash_score'] }}      | {{ radarr['cf']['special-edition']['trash_id'] }}      |
    | [{{ radarr['cf']['imax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax)                                 | {{ radarr['cf']['imax']['trash_score'] }}                 | {{ radarr['cf']['imax']['trash_id'] }}                 |
    | [{{ radarr['cf']['imax-enhanced']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax-enhanced)               | {{ radarr['cf']['imax-enhanced']['trash_score'] }}        | {{ radarr['cf']['imax-enhanced']['trash_id'] }}        |

    !!! tip "{{ radarr['cf']['imax-enhanced']['name'] }}"
        {{ radarr['cf']['imax-enhanced']['name'] }}: Get More Picture Instead of Black Bars.

        {{ radarr['cf']['imax-enhanced']['name'] }} exclusive expanded aspect ratio is 1:90:1, which offers up to 26% more picture for select sequences, meaning more of the action is visible on screen.

        If you don't prefer `{{ radarr['cf']['imax-enhanced']['name'] }}` then don't add it or use a score of `0`

??? summary "HQ Release Groups - [CLICK TO EXPAND]"

    !!! danger "Adding `HD Bluray Tier xx` means you get less or not streaming optimized :warning:"
    | Custom Format                                                                                                                        |                                            Score | Trash ID                                            |
    | ------------------------------------------------------------------------------------------------------------------------------------ | -----------------------------------------------: | --------------------------------------------------- |
    | [{{ radarr['cf']['bhdstudio']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/bhdstudio.json) |   {{ radarr['cf']['bhdstudio']['trash_score'] }} | {{ radarr['cf']['bhdstudio']['trash_id'] }}         |
    | [{{ radarr['cf']['web-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-01)                                | {{ radarr['cf']['web-tier-01']['trash_score'] }} | {{ radarr['cf']['web-tier-01']['trash_id'] }}       |
    | [{{ radarr['cf']['web-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-02)                                | {{ radarr['cf']['web-tier-02']['trash_score'] }} | {{ radarr['cf']['web-tier-02']['trash_id'] }}       |
    | [{{ radarr['cf']['web-tier-03']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#web-tier-03)                                | {{ radarr['cf']['web-tier-03']['trash_score'] }} | {{ radarr['cf']['web-tier-03']['trash_id'] }}       |
    | [{{ radarr['cf']['hd-bluray-tier-01']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-01)                    |                                   :warning: 1100 | {{ radarr['cf']['hd-bluray-tier-01']['trash_id'] }} |
    | [{{ radarr['cf']['hd-bluray-tier-02']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hd-bluray-tier-02)                    |                                   :warning: 1050 | {{ radarr['cf']['hd-bluray-tier-02']['trash_id'] }} |

    !!! Danger "- Don’t use HQ-xxx or UHD (xxx) and Tiers together<br>- Remux Tier 01-02 replaces HQ-Remux<br>- UHD Bluray Tier 01-03 replaces UHD (xxx)<br>- Web Tier 01-03 replaces HQ-WEBDL"

{! include-markdown "../../includes/cf/radarr-misc.md" !}

{! include-markdown "../../includes/cf/radarr-unwanted.md" !}

{! include-markdown "../../includes/sqp/hd-radarr-optional.md" !}

{! include-markdown "../../includes/sqp/hd-radarr-resolution.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}
