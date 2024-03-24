??? abstract "Explanation - [Click to show/hide]"
    | Acronyms                   | French Explanation                                                                  | English Explanation                                                   |
    | -------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
    | TRUEFRENCH or VFF          | Version Francophone Française (doublage réalisé en France)                          | Full French version (dubbing done in France)                          |
    | FRENCH or VF<sup>[1]</sup> | Version Francophone (normalement equivalent à la VFQ)                               | French version (normally equivalent to VFQ)                           |
    | VOF                        | Version Originale Française                                                         | Original French Version                                               |
    | VFI                        | Version Francophone Internationale                                                  | International French Version                                          |
    | VFQ                        | Version Francophone Québécoise                                                      | Canadian French Version                                               |
    | VOQ                        | Version Original Québécoise (ex: Bon Cop, Bad Cop)                                  | Quebec Original Version (ex: Bon Cop, Bad Cop)                        |
    | VQ                         | Version Québécoise (accent Québécois important, ex: Les Simpsons le film)           | Quebec Version (strong Quebec accent, ex: The Simpsons movie)         |
    | VFB                        | Version Francophone Belge                                                           | Belgian French Version                                                |
    | VF[1-9] or FR[1-9]         | Indique le nombre de doublage présent (normalement VF2 soit VFF et VFQ)             | Indicates the number of dubs present (normally VF2 being VFF and VFQ) |
    | VOSTFR<sup>[2]</sup>       | Indique que l'audio est dans la langue originale, avec des sous-titres en français. | Indicates soundtrack in the original language, with French subtitles  |

    - *[1] VF is included under the VFQ Custom Format, but it should be noted that it was often mismatched with VFF instead of VFQ pre-2022.*
    - *[2] It should be noted that SUBFRENCH is included in this Custom Format. However, SUB often means that the subtitle was embedded inside the picture (hardcoded). French releases tend to mix the two, leading to some VOSTFR being labelled as SUBFRENCH and SUBFRENCH as VOSTFR.*

    !!! tip "Indexers renaming in Prowlarr"
        Some Indexers in **Prowlarr** can rename `MULTi` releases to `MULTi.TRUEFRENCH` or `MULTi.FRENCH`. It is not recommend to use such a feature along with those Custom Formats as it can lead to false positives from the VFF, VFQ and VQ Custom Formats.

??? abstract "French Audio Versions - [Click to show/hide]"
    | Custom Format                                                                                      | Trash ID                                        |
    | -------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
    | [{{ sonarr['cf']['french-vff']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vff)       | {{ sonarr['cf']['french-vff']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-vof']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vof)       | {{ sonarr['cf']['french-vof']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-vfi']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vfi)       | {{ sonarr['cf']['french-vfi']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-vf2']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vf2)       | {{ sonarr['cf']['french-vf2']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-vfq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vfq)       | {{ sonarr['cf']['french-vfq']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-voq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#voq)       | {{ sonarr['cf']['french-voq']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-vq']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vq)         | {{ sonarr['cf']['french-vq']['trash_id'] }}     |
    | [{{ sonarr['cf']['french-vfb']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vfb)       | {{ sonarr['cf']['french-vfb']['trash_id'] }}    |
    | [{{ sonarr['cf']['french-vostfr']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#vostfr) | {{ sonarr['cf']['french-vostfr']['trash_id'] }} |
