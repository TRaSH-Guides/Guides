!!! warning "Information regarding 2160p releases"
    It should be noted that many problems can arise from this profile if you use the HD audio Custom Formats, as:

    - French Scene rules assert that the French Audio should be the first (default) audio in a MULTi release. 
    - Rules acknowledge that only the best audio should be noted in the title (will it be the original or the FR audio).
    - Some movies (and TV shows, mostly pre-Streaming era) does not always have an equivalent FR audio than the original highest one.

    Resulting on the following:

    - The quality of the audio in the release's title could not be the French one.
    - The French audio could be of a lesser quality than the titled one.
    - Radarr will only score pre-import audio by the release title. Post-import by the release's first (default) audio (after ffprobe).
    - Final score from the release can be lower than pre-import.

    !!! tip "This is why the Group tiers exist, it try to get hold of the groups that tend to get the best original and French audio for a release. However, it is not bullet proof."
