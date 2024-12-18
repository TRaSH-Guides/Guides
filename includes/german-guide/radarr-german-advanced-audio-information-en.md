!!! warning "Information regarding audio quality"

    It should be noted that there can be problems if you use the HD audio Custom Formats, as:

    - There is a best practice in the German scene which assert that the German audio should be the first (default) audio in DL/ML releases.
    - It may or may not be the case that the quality of the German audio track is mentioned in the title.
    - Some movies (and TV shows, mostly from the pre-streaming era) lack an equivalent German audio track to the original audio's highest quality one.

    Resulting in the following:

    - The quality of the audio indicated in the release's title might not refer to the German audio.
    - The German audio could be of lesser quality than the one mentioned in the title.
    - Radarr will only score pre-import audio based on the release title, and post-import based on the release's first (default) audio (after ffprobe).
    - The final score for the release can be lower than the pre-import.

    !!! tip

        This is why the Group tiers exist; they try to get hold of the groups that tend to provide the best original and German audio for a release. However, it is not infallible, and, once again, a movie may not have an equivalent German audio track to the original audio's highest quality one.
