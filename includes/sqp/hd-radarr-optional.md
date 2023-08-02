??? abstract "Optional - [Click to show/hide]"
    | Custom Format                                                                                                 |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups) | {{ radarr['cf']['bad-dual-groups']['trash_scores']['default'] }} | {{ radarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ radarr['cf']['evo-no-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl)       |  {{ radarr['cf']['evo-no-webdl']['trash_scores']['default'] }}   | {{ radarr['cf']['evo-no-webdl']['trash_id'] }}    |
    | [{{ radarr['cf']['no-rlsgroup']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup)         |   {{ radarr['cf']['no-rlsgroup']['trash_scores']['default'] }}   | {{ radarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ radarr['cf']['obfuscated']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#obfuscated)           |   {{ radarr['cf']['obfuscated']['trash_scores']['default'] }}    | {{ radarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ radarr['cf']['retags']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#retags)                   |     {{ radarr['cf']['retags']['trash_scores']['default'] }}      | {{ radarr['cf']['retags']['trash_id'] }}          |
    | [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene)                     |      {{ radarr['cf']['scene']['trash_scores']['default'] }}      | {{ radarr['cf']['scene']['trash_id'] }}           |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.
    - **{{ radarr['cf']['evo-no-webdl']['name'] }}:** This group is often banned for the low quality Blu-ray releases, but their WEB-DL are okay.
    - **{{ radarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
    - **{{ radarr['cf']['obfuscated']['name'] }}:** [*Optional*] (use these only if you dislike renamed releases)
    - **{{ radarr['cf']['retags']['name'] }}:** [*Optional*] (use these only if you dislike retagged releases)
    - **{{ radarr['cf']['scene']['name'] }}:** [*Optional*] (use these only if you dislike scene releases)
