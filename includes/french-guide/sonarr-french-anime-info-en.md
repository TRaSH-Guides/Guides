!!! info "Important"
    In a first time you should follow the original Anime Guide following sections:

    - [How to setup Quality Profiles Anime | Media Management](/Sonarr/sonarr-setup-quality-profiles-anime/#media-management){:target="_blank" rel="noopener noreferrer"}.
    - [How to setup Quality Profiles Anime | Quality Settings](/Sonarr/sonarr-setup-quality-profiles-anime/#quality-settings){:target="_blank" rel="noopener noreferrer"}.
    - [How to setup Quality Profiles Anime | Quality Profile](/Sonarr/sonarr-setup-quality-profiles-anime/#quality-profile){:target="_blank" rel="noopener noreferrer"}.

    Do not continue before you read those three sections and you followed their instructions.

    !!! info "Original Scoring"
        Those are the original scoring from the Anime Guide and need to be followed depending what you want to achieve. It will unsure that if a VOSTFR or MULTi releases is not found you will still have a good quality releases:

        - [Default Scoring](/Sonarr/sonarr-setup-quality-profiles-anime/#default-scoring){:target="_blank" rel="noopener noreferrer"}: Default scoring that will insure that you have good English subbed releases at least. *Remember that if you only want subbed releases, this should be your preferred and you should try to set up [Bazarr](/Bazarr/Setup-Guide){:target="_blank" rel="noopener noreferrer"} to get VOSTFR.*
        - [Dual Audio](/Sonarr/sonarr-setup-quality-profiles-anime/#dual-audio-scoring){:target="_blank" rel="noopener noreferrer"}: If you want to have Dual Audio releases (original and English audio) in case Sonarr does not find a VOSTFR or MULTi release.
        - [Uncensored Scoring](/Sonarr/sonarr-setup-quality-profiles-anime/#uncensored-scoring){:target="_blank" rel="noopener noreferrer"}: If you prefer uncensored releases.

    ??? warning "Type of FanSubs - [CLICK TO EXPAND]"
        Those Custom Formats are optionals and allow to know which type of FanSubs your releases have. Only the FastSub is not wanted as it is often done too quickly and are often not well done.

        | Custom Format                                                                                 | Score                                        | Trash ID                                  |
        | --------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- |
        | [{{ sonarr['cf']['fansub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fansub)   | 0                                            | {{ sonarr['cf']['fansub']['trash_id'] }}  |
        | [{{ sonarr['cf']['fastsub']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#fastsub) | {{ sonarr['cf']['fastsub']['trash_score'] }} | {{ sonarr['cf']['fastsub']['trash_id'] }} |
