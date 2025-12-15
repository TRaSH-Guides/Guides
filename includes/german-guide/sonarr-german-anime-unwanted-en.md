<!-- markdownlint-disable MD041-->
??? abstract "German Anime Unwanted - [Click to show/hide]"

    | Custom Format                                                                                                                       |                                      Score                                      | Trash ID                                                  |
    | ----------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------: | --------------------------------------------------------- |
    | [{{ sonarr['cf']['br-disk']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#br-disk)                                       |             {{ sonarr['cf']['br-disk']['trash_scores']['german-anime'] }}             | {{ sonarr['cf']['br-disk']['trash_id'] }}                 |
    | [{{ sonarr['cf']['lq']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#lq)                                                 |               {{ sonarr['cf']['lq']['trash_scores']['german-anime'] }}                | {{ sonarr['cf']['lq']['trash_id'] }}                      |
    | [{{ sonarr['cf']['lq-release-title']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#lq-release-title)                     |        {{ sonarr['cf']['lq-release-title']['trash_scores']['german-anime'] }}         | {{ sonarr['cf']['lq-release-title']['trash_id'] }}        |
    | [{{ sonarr['cf']['german-lq']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#german-lq)                                   |           {{ sonarr['cf']['german-lq']['trash_scores']['default'] }}            | {{ sonarr['cf']['german-lq']['trash_id'] }}               |
    | [{{ sonarr['cf']['german-lq-release-title']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#german-lq-release-title)       |    {{ sonarr['cf']['german-lq-release-title']['trash_scores']['default'] }}     | {{ sonarr['cf']['german-lq-release-title']['trash_id'] }} |
    | [{{ sonarr['cf']['german-microsized']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#german-microsized)                   |       {{ sonarr['cf']['german-microsized']['trash_scores']['default'] }}        | {{ sonarr['cf']['german-microsized']['trash_id'] }}       |
    | [{{ sonarr['cf']['x265-hd']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#x265-hd) :warning:                             |        :warning: {{ sonarr['cf']['x265-hd']['trash_scores']['german-anime'] }}        | {{ sonarr['cf']['x265-hd']['trash_id'] }}                 |
    | [{{ sonarr['cf']['extras']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#extras)                                         |             {{ sonarr['cf']['extras']['trash_scores']['german-anime'] }}              | {{ sonarr['cf']['extras']['trash_id'] }}                  |
    | [{{ sonarr['cf']['av1']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#av1)                                               |               {{ sonarr['cf']['av1']['trash_scores']['german-anime'] }}               | {{ sonarr['cf']['av1']['trash_id'] }}                     |
    | [{{ sonarr['cf']['upscaled']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#upscaled)                                     |            {{ sonarr['cf']['upscaled']['trash_scores']['german-anime'] }}             | {{ sonarr['cf']['upscaled']['trash_id'] }}                |
    | [{{ sonarr['cf']['anime-raws']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#anime-raws)                                                 |               {{ sonarr['cf']['anime-raws']['trash_scores']['german-anime'] }}               | {{ sonarr['cf']['anime-raws']['trash_id'] }}                         |
    | [{{ sonarr['cf']['anime-lq-groups']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#anime-lq-groups)                                       |            {{ sonarr['cf']['anime-lq-groups']['trash_scores']['german-anime'] }}             | {{ sonarr['cf']['anime-lq-groups']['trash_id'] }}                    |
    | [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/Sonarr-collection-of-custom-formats/#vostfr)                                                  |           {{ sonarr['cf']['french-vostfr']['trash_scores']['german-anime'] }}           | {{ sonarr['cf']['french-vostfr']['trash_id'] }}                      |

    ---

    Breakdown and Why

    - **{{ sonarr['cf']['br-disk']['name'] }}:** This is a custom format to help Sonarr recognize & ignore BR-DISK (ISO's and Blu-ray folder structure) in addition to the standard BR-DISK quality.
    - **{{ sonarr['cf']['lq']['name'] }}:** A collection of known Low Quality groups that are often banned from the top trackers because of the lack of quality or other reasons.
    - **{{ sonarr['cf']['lq-release-title']['name'] }}:** A collection of terms seen in the titles of low-quality releases that are not captured by using a release group name.
    - **{{ sonarr['cf']['german-lq']['name'] }}:** A collection of known Low Quality German groups that are often banned from the top trackers because of the lack of quality or other reasons.
    - **{{ sonarr['cf']['german-lq-release-title']['name'] }}:** A collection of terms seen in the titles of low-quality releases that are not captured by using a release group name.
    - **{{ sonarr['cf']['german-microsized']['name'] }}:** A collection of German groups producing low quality micro-sized releases. However, if lower quality for Anime in favor of storage space is acceptable to you, you can also set this to 0.
    - :warning: **{{ sonarr['cf']['x265-hd']['name'] }}:** This blocks/ignores 720/1080p (HD) releases that are encoded in x265. However, as there are certain German groups (ZeroTwo, VECTOR, ...) which produce high bitrate 1080p x265 encodes we recommend setting the score of this custom format to 0.
    - **{{ sonarr['cf']['extras']['name'] }}:** Blocks releases that only contain extras
    - **{{ sonarr['cf']['av1']['name'] }}:** This blocks all releases encoded in AV1.
    - **{{ sonarr['cf']['upscaled']['name'] }}:** A custom format to prevent Sonarr from grabbing upscaled releases.
    - **{{ sonarr['cf']['anime-raws']['name'] }}:** A collection of known groups that release raws.
    - **{{ sonarr['cf']['anime-lq-groups']['name'] }}:** A collection of known low-quality groups.
    - **{{ sonarr['cf']['french-vostfr']['name'] }}:** Indicates soundtrack in the original language, with French subtitles. It should be noted that SUBFRENCH is included inside this Custom Format. However, SUB often means that the subtitle was embedded inside the picture (hardcoded). French releases tend to mix both, leading to some VOSTFR being labeled as SUBFRENCH and SUBFRENCH as VOSTFR.
<!-- markdownlint-enable MD041-->
