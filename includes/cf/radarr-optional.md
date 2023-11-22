??? abstract "Optional - [Click to show/hide]"
    | Custom Format                                                                                                       |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ radarr['cf']['bad-dual-groups']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bad-dual-groups)       | {{ radarr['cf']['bad-dual-groups']['trash_scores']['default'] }} | {{ radarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ radarr['cf']['evo-no-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#evo-no-webdl)             |  {{ radarr['cf']['evo-no-webdl']['trash_scores']['default'] }}   | {{ radarr['cf']['evo-no-webdl']['trash_id'] }}    |
    | [{{ radarr['cf']['no-rlsgroup']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#no-rlsgroup)               |   {{ radarr['cf']['no-rlsgroup']['trash_scores']['default'] }}   | {{ radarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ radarr['cf']['obfuscated']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#obfuscated)                 |   {{ radarr['cf']['obfuscated']['trash_scores']['default'] }}    | {{ radarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ radarr['cf']['retags']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#retags)                         |     {{ radarr['cf']['retags']['trash_scores']['default'] }}      | {{ radarr['cf']['retags']['trash_id'] }}          |
    | [{{ radarr['cf']['scene']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#scene)                           |      {{ radarr['cf']['scene']['trash_scores']['default'] }}      | {{ radarr['cf']['scene']['trash_id'] }}           |
    | [{{ radarr['cf']['x265-no-hdrdv']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-no-hdrdv) :warning: |  {{ radarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}  | {{ radarr['cf']['x265-no-hdrdv']['trash_id'] }}   |

    ------

    Breakdown and Why

    - **{{ radarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release and add their own language track (e.g. AAC 2.0 Portuguese) as the first track. Afterward, FFprobe would determine that the media file is Portuguese. It's a common rule that you only add the best audio as the main track.
    Also they often even rename the release name into Portuguese.
    - **{{ radarr['cf']['evo-no-webdl']['name'] }}:** This group is often banned for low-quality Blu-ray releases, but their WEB-DLs are okay.
    - **{{ radarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group which could result in LQ groups being scored incorrectly. For example, a lot of EVO releases end up with a stripped group name. These releases would appear as "upgrades" and could end up getting a decent score after other CFs are scored.
    - **{{ radarr['cf']['obfuscated']['name'] }}:** [*Optional*] Use these only if you wish to avoid renamed releases.
    - **{{ radarr['cf']['retags']['name'] }}:** [*Optional*] Use this if you want to avoid retagged releases. Retagged releases often are not consistent with the quality of the original group's release.
    - **{{ radarr['cf']['scene']['name'] }}:** [*Optional*] Use this only if you want to avoid SCENE releases.
    - **{{ radarr['cf']['x265-no-hdrdv']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        **But it will allow x265 releases if they have HDR and/or DV**

        *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

        In your quality profile use the following score for this Custom Format: `{{ radarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}`

        !!! Danger "Don't use this together with [{{ radarr['cf']['x265-hd']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"
