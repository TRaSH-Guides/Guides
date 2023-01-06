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

        :warning: If you add the [{{ sonarr['cf']['anime-lq-groups']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#anime-lq-groups) Custom Format, do not forget to add the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr) one with a score of `1000` to counter-balance (do not forget to addition the `101` if only want VOSTFR anime). Keep in mind that this will probably be not necessary in the future if the VOSTFR condition disappear from the [{{ sonarr['cf']['anime-lq-groups']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#anime-lq-groups).

    !!! info "Only want VOSTFR anime"
        For this example if you prefer VOSTFR over potential MULTi/DUAL (original and French) audio releases, you should score the [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr) to `101`, and disregard all the `Multi` and French version Custom Formats.
