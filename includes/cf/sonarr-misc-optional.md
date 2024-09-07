??? abstract "Miscellaneous (Optional) - [Click to show/hide]"

    | Custom Format                                                                                                 |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ sonarr['cf']['bad-dual-groups']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#bad-dual-groups) | {{ sonarr['cf']['bad-dual-groups']['trash_scores']['default'] }} | {{ sonarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ sonarr['cf']['no-rlsgroup']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#no-rlsgroup)         |   {{ sonarr['cf']['no-rlsgroup']['trash_scores']['default'] }}   | {{ sonarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ sonarr['cf']['obfuscated']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#obfuscated)           |   {{ sonarr['cf']['obfuscated']['trash_scores']['default'] }}    | {{ sonarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ sonarr['cf']['retags']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#retags)                   |     {{ sonarr['cf']['retags']['trash_scores']['default'] }}      | {{ sonarr['cf']['retags']['trash_id'] }}          |
    | [{{ sonarr['cf']['scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#scene)                     |      {{ sonarr['cf']['scene']['trash_scores']['default'] }}      | {{ sonarr['cf']['scene']['trash_id'] }}           |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release and add their own language track (e.g. AAC 2.0 Portuguese) as the first track. Afterward, FFprobe would determine that the media file is Portuguese. It's a common rule that you only add the best audio as the main track.
    Also they often even rename the release name into Portuguese.
    - **{{ sonarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group which could result in LQ groups being scored incorrectly. For example, a lot of EVO releases end up with a stripped group name. These releases would appear as "upgrades" and could end up getting a decent score after other CFs are scored.
    - **{{ sonarr['cf']['obfuscated']['name'] }}:** [*Optional*] Use these only if you wish to avoid renamed releases.
    - **{{ sonarr['cf']['retags']['name'] }}:** [*Optional*] Use this if you wish to avoid retagged releases. Retagged releases often are not consistent with the quality of the original group's release (e.g. TGx downsampling an NTb release from 5.1 audio to 2.0 audio, yet maintaining the NTb naming).
    - **{{ sonarr['cf']['scene']['name'] }}:** [*Optional*] Use this only if you want to avoid SCENE releases.
