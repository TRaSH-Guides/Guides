??? abstract "HQ Source Groups - [Click to show/hide]"
    | Custom Format                                                                                                   |                            Score                             | Trash ID                                      |
    | --------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------: | --------------------------------------------- |
    | [{{ sonarr['cf']['web-tier-01']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-01)           | {{ sonarr['cf']['web-tier-01']['trash_scores']['default'] }} | {{ sonarr['cf']['web-tier-01']['trash_id'] }} |
    | [{{ sonarr['cf']['web-tier-02']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-02)           | {{ sonarr['cf']['web-tier-02']['trash_scores']['default'] }} | {{ sonarr['cf']['web-tier-02']['trash_id'] }} |
    | [{{ sonarr['cf']['web-tier-03']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-tier-03)           | {{ sonarr['cf']['web-tier-03']['trash_scores']['default'] }} | {{ sonarr['cf']['web-tier-03']['trash_id'] }} |
    | [{{ sonarr['cf']['web-scene']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#web-scene) :exclamation: |  {{ sonarr['cf']['web-scene']['trash_scores']['default'] }}  | {{ sonarr['cf']['web-scene']['trash_id'] }}   |

    !!! info
        :exclamation: = The reason why this Custom Format gets positively scored is because it's the only quality scene group that exists (up until now). Scene groups don't add a streaming service to their release names, so the score is adjusted to take this into account.
