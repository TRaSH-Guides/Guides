!!! info "Important"

    In a first time you should follow the original Anime Guide following sections:

    - [How to set up Quality Profiles Anime | Media Management](/Sonarr/sonarr-setup-quality-profiles-anime/#media-management){:target="_blank" rel="noopener noreferrer"}.
    - [How to set up Quality Profiles Anime | Quality Settings](/Sonarr/sonarr-setup-quality-profiles-anime/#quality-settings){:target="_blank" rel="noopener noreferrer"}.
    - [How to set up Quality Profiles Anime | Quality Profile](/Sonarr/sonarr-setup-quality-profiles-anime/#quality-profile){:target="_blank" rel="noopener noreferrer"}.

    Do not continue before you read those three sections and you followed their instructions.

    !!! info "Original Scoring"

        Those are the original scoring from the Anime Guide and need to be followed depending what you want to achieve. It will unsure that if a VOSTFR or MULTi releases is not found you will still have a good quality releases:

        - [Default Scoring](/Sonarr/sonarr-setup-quality-profiles-anime/#default-scoring){:target="_blank" rel="noopener noreferrer"}: Default scoring that will insure that you have good English subbed releases at least.
        - [Dual Audio](/Sonarr/sonarr-setup-quality-profiles-anime/#dual-audio-scoring){:target="_blank" rel="noopener noreferrer"}: If you want to have Dual Audio releases (original and English audio) in case Sonarr does not find a VOSTFR or MULTi release.
        - [Uncensored Scoring](/Sonarr/sonarr-setup-quality-profiles-anime/#uncensored-scoring){:target="_blank" rel="noopener noreferrer"}: If you prefer uncensored releases.

        :warning: Careful to not add the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr) Custom Format with a score of `{{ sonarr['cf']['french-vostfr']['trash_scores']['anime-sonarr'] }}` as stated in the original guide. Otherwise, you will hinder your chance to get "French" releases.

    !!! info "Only want VOSTFR anime"

        For this example if you prefer VOSTFR over potential MULTi/DUAL (original and French) audio releases, you should score the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr) to `{{ sonarr['cf']['french-vostfr']['trash_scores']['french-anime-vostfr'] }}`.

         *(Optional) You can also try to set up [Bazarr](/Bazarr/Setup-Guide){:target="_blank" rel="noopener noreferrer"} to get French Sub. This is less preferred as fewer anime subs can be found online than from normal TV shows. However, it can be still a great backup.*
