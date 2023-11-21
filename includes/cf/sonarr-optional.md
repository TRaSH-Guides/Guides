??? abstract "Optional - [Click to show/hide]"
    | Custom Format                                                                                                       |                              Score                               | Trash ID                                          |
    | ------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------: | ------------------------------------------------- |
    | [{{ sonarr['cf']['bad-dual-groups']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#bad-dual-groups)       | {{ sonarr['cf']['bad-dual-groups']['trash_scores']['default'] }} | {{ sonarr['cf']['bad-dual-groups']['trash_id'] }} |
    | [{{ sonarr['cf']['no-rlsgroup']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#no-rlsgroup)               |   {{ sonarr['cf']['no-rlsgroup']['trash_scores']['default'] }}   | {{ sonarr['cf']['no-rlsgroup']['trash_id'] }}     |
    | [{{ sonarr['cf']['obfuscated']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#obfuscated)                 |   {{ sonarr['cf']['obfuscated']['trash_scores']['default'] }}    | {{ sonarr['cf']['obfuscated']['trash_id'] }}      |
    | [{{ sonarr['cf']['retags']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#retags)                         |     {{ sonarr['cf']['retags']['trash_scores']['default'] }}      | {{ sonarr['cf']['retags']['trash_id'] }}          |
    | [{{ sonarr['cf']['scene']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#scene)                           |      {{ sonarr['cf']['scene']['trash_scores']['default'] }}      | {{ sonarr['cf']['scene']['trash_id'] }}           |
    | [{{ sonarr['cf']['x265-no-hdrdv']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#x265-no-hdrdv) :warning: |  {{ sonarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}  | {{ sonarr['cf']['x265-no-hdrdv']['trash_id'] }}   |

    ------

    Breakdown and Why

    - **{{ sonarr['cf']['bad-dual-groups']['name'] }}:** [*Optional*] These groups take the original release, then they add their own preferred language (ex. Portuguese) as the main audio track (AAC 2.0), What results after renaming and FFprobe that the media file will be recognized as Portuguese AAC audio. It's a common rule that you add the best audio as first.
    Also they often even rename the release name in to Portuguese.
    - **{{ sonarr['cf']['no-rlsgroup']['name'] }}:** [*Optional*] Some indexers strip out the release group what could result in LQ groups getting a higher score. For example a lot of EVO releases end up stripping the group name, so they appear as "upgrades", and they end up getting a decent score if other things match.
    - **{{ sonarr['cf']['obfuscated']['name'] }}:** [*Optional*] (use these only if you dislike renamed releases)
    - **{{ sonarr['cf']['retags']['name'] }}:** [*Optional*] Use this only if you dislike retagged releases. This will help avoid retagged releases that may no longer meet the quality of the original group (e.g. TGx downsampling a NTb release from 5.1 audio to 2.0 audio yet maintain the NTb naming)
    - **{{ sonarr['cf']['scene']['name'] }}:** [*Optional*] (use these only if you dislike scene releases)
    - **{{ sonarr['cf']['x265-no-hdrdv']['name'] }}:** This blocks 720/1080p (HD) releases that are encoded in x265. - More info [HERE](/Misc/x265-4k/){:target="_blank" rel="noopener noreferrer"}.

        **But it will allow x265 releases if they have HDR and/or DV**

        *Being that some NF releases won't be released as 4k, but you want to have DV/HDR releases.*

        In your quality profile use the following score for this Custom Format: `{{ sonarr['cf']['x265-no-hdrdv']['trash_scores']['default'] }}`

        !!! Danger "Don't use this together with [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#x265-hd), Only ever include one of them :warning:"
