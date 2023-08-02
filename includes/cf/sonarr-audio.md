??? abstract "Audio - [Click to show/hide]"

    {! include-markdown "../../includes/cf/audio-info.md" !}

    ![!Audio Flowchart](/Radarr/images/flowchart-audio.png)

    | Custom Format                                                                                                 |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ sonarr['cf']['truehd-atmos']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#truehd-atmos)       |  {{ sonarr['cf']['truehd-atmos']['trash_scores']['default'] }}   | {{ sonarr['cf']['truehd-atmos']['trash_id'] }}    |
    | [{{ sonarr['cf']['dts-x']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dts-x)                     |      {{ sonarr['cf']['dts-x']['trash_scores']['default'] }}      | {{ sonarr['cf']['dts-x']['trash_id'] }}           |
    | [{{ sonarr['cf']['atmos-undefined']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#atmos-undefined) | {{ sonarr['cf']['atmos-undefined']['trash_scores']['default'] }} | {{ sonarr['cf']['atmos-undefined']['trash_id'] }} |
    | [{{ sonarr['cf']['ddplus-atmos']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#ddplus-atmos)       |  {{ sonarr['cf']['ddplus-atmos']['trash_scores']['default'] }}   | {{ sonarr['cf']['ddplus-atmos']['trash_id'] }}    |
    | [{{ sonarr['cf']['truehd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#truehd)                   |     {{ sonarr['cf']['truehd']['trash_scores']['default'] }}      | {{ sonarr['cf']['truehd']['trash_id'] }}          |
    | [{{ sonarr['cf']['dts-hd-ma']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dts-hd-ma)             |    {{ sonarr['cf']['dts-hd-ma']['trash_scores']['default'] }}    | {{ sonarr['cf']['dts-hd-ma']['trash_id'] }}       |
    | [{{ sonarr['cf']['flac']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#flac)                       |      {{ sonarr['cf']['flac']['trash_scores']['default'] }}       | {{ sonarr['cf']['flac']['trash_id'] }}            |
    | [{{ sonarr['cf']['pcm']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#pcm)                         |       {{ sonarr['cf']['pcm']['trash_scores']['default'] }}       | {{ sonarr['cf']['pcm']['trash_id'] }}             |
    | [{{ sonarr['cf']['dts-hd-hra']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dts-hd-hra)           |   {{ sonarr['cf']['dts-hd-hra']['trash_scores']['default'] }}    | {{ sonarr['cf']['dts-hd-hra']['trash_id'] }}      |
    | [{{ sonarr['cf']['ddplus']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#ddplus)                   |     {{ sonarr['cf']['ddplus']['trash_scores']['default'] }}      | {{ sonarr['cf']['ddplus']['trash_id'] }}          |
    | [{{ sonarr['cf']['dts-es']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dts-es)                   |     {{ sonarr['cf']['dts-es']['trash_scores']['default'] }}      | {{ sonarr['cf']['dts-es']['trash_id'] }}          |
    | [{{ sonarr['cf']['dts']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dts)                         |       {{ sonarr['cf']['dts']['trash_scores']['default'] }}       | {{ sonarr['cf']['dts']['trash_id'] }}             |
    | [{{ sonarr['cf']['aac']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#aac)                         |       {{ sonarr['cf']['aac']['trash_scores']['default'] }}       | {{ sonarr['cf']['aac']['trash_id'] }}             |
    | [{{ sonarr['cf']['dd']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dd)                           |       {{ sonarr['cf']['dd']['trash_scores']['default'] }}        | {{ sonarr['cf']['dd']['trash_id'] }}              |
