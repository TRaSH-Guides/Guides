!!! warning "Information Regarding HD audio"

    It should be noted that many problems can arise from this profile if you use the HD audio Custom Formats, as:

    - French Scene rules assert that the French audio should be the first (default) audio in a MULTi release.
    - The rules state that only the best audio (whether original or FR) should be mentioned in the title.
    - Some movies (and TV shows, mostly from the pre-streaming era) lack an equivalent FR audio track to the original audio's highest quality one.

    Resulting in the following:

    - The quality of the audio indicated in the release's title might not refer to the French audio.
    - The French audio could be of lesser quality than the one mentioned in the title.
    - Radarr will only score pre-import audio based on the release title, and post-import based on the release's first (default) audio (after ffprobe).
    - The final score for the release can be lower than the pre-import.

    !!! tip

        This is why the Group tiers exist; they try to get hold of the groups that tend to provide the best original and French audio for a release. However, it is not infallible, and, once again, a movie may not have an equivalent FR audio track to the original audio's highest quality one.
