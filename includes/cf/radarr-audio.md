??? abstract "Audio - [Click to show/hide]"

    **Why should I choose All Audio formats?**

    - You have a hardware media player device and an audio setup that supports **ALL** HD Audio (TrueHD, DTS-X, DTS-HD, etc).

        {! include-markdown "../../includes/cf/audio-limitations-atv.md" !}

    - You've chosen a profile that includes Audio Formats. You should use all the Audio formats with Remuxes/UHD Encodes.
    - You should add **ALL** the Audio formats - don't leave any of them out!
    - Audio transcoding has a low impact on your server. If your server can't handle audio transcoding, consider choosing another quality profile.

    {! include-markdown "../../includes/cf/audio-info.md" !}

    {! include-markdown "../../includes/cf/which-audio-formats-should-i-choose.md" !}

    | Custom Format                                                                                                 |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['truehd-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd-atmos)       |  {{ radarr['cf']['truehd-atmos']['trash_scores']['default'] }}   | {{ radarr['cf']['truehd-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['dts-x']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-x)                     |      {{ radarr['cf']['dts-x']['trash_scores']['default'] }}      | {{ radarr['cf']['dts-x']['trash_id'] }}           |
    | [{{ radarr['cf']['atmos-undefined']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#atmos-undefined) | {{ radarr['cf']['atmos-undefined']['trash_scores']['default'] }} | {{ radarr['cf']['atmos-undefined']['trash_id'] }} |
    | [{{ radarr['cf']['ddplus-atmos']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus-atmos)       |  {{ radarr['cf']['ddplus-atmos']['trash_scores']['default'] }}   | {{ radarr['cf']['ddplus-atmos']['trash_id'] }}    |
    | [{{ radarr['cf']['truehd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#truehd)                   |     {{ radarr['cf']['truehd']['trash_scores']['default'] }}      | {{ radarr['cf']['truehd']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-hd-ma']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-ma)             |    {{ radarr['cf']['dts-hd-ma']['trash_scores']['default'] }}    | {{ radarr['cf']['dts-hd-ma']['trash_id'] }}       |
    | [{{ radarr['cf']['flac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#flac)                       |      {{ radarr['cf']['flac']['trash_scores']['default'] }}       | {{ radarr['cf']['flac']['trash_id'] }}            |
    | [{{ radarr['cf']['pcm']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pcm)                         |       {{ radarr['cf']['pcm']['trash_scores']['default'] }}       | {{ radarr['cf']['pcm']['trash_id'] }}             |
    | [{{ radarr['cf']['dts-hd-hra']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-hd-hra)           |   {{ radarr['cf']['dts-hd-hra']['trash_scores']['default'] }}    | {{ radarr['cf']['dts-hd-hra']['trash_id'] }}      |
    | [{{ radarr['cf']['ddplus']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ddplus)                   |     {{ radarr['cf']['ddplus']['trash_scores']['default'] }}      | {{ radarr['cf']['ddplus']['trash_id'] }}          |
    | [{{ radarr['cf']['dts-es']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts-es)                   |     {{ radarr['cf']['dts-es']['trash_scores']['default'] }}      | {{ radarr['cf']['dts-es']['trash_id'] }}          |
    | [{{ radarr['cf']['dts']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dts)                         |       {{ radarr['cf']['dts']['trash_scores']['default'] }}       | {{ radarr['cf']['dts']['trash_id'] }}             |
    | [{{ radarr['cf']['aac']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#aac)                         |       {{ radarr['cf']['aac']['trash_scores']['default'] }}       | {{ radarr['cf']['aac']['trash_id'] }}             |
    | [{{ radarr['cf']['dd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dd)                           |       {{ radarr['cf']['dd']['trash_scores']['default'] }}        | {{ radarr['cf']['dd']['trash_id'] }}              |
