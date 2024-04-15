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

    !!! tip "MULTi definition per indexers"
        Some Indexers in **Radarr** will let you choose which audio is normally included inside a `MULTi` release as an option. You should choose only `Original` and `French` if you decide to use it.
        This option should only be used for French indexers where you are sure that `MULTi` does include both `Original` and `French` audio. Doing so in more "international" indexers can create to false positive with the French Audio CFs.

??? abstract "French Audio Versions - [Click to show/hide]"
    | Custom Format                                                                                      | Trash ID                                        |
    | -------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
    | [{{ radarr['cf']['french-vff']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vff)       | {{ radarr['cf']['french-vff']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vof']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vof)       | {{ radarr['cf']['french-vof']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vfi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vfi)       | {{ radarr['cf']['french-vfi']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vf2']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vf2)       | {{ radarr['cf']['french-vf2']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vfq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vfq)       | {{ radarr['cf']['french-vfq']['trash_id'] }}    |
    | [{{ radarr['cf']['french-voq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#voq)       | {{ radarr['cf']['french-voq']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vq)         | {{ radarr['cf']['french-vq']['trash_id'] }}     |
    | [{{ radarr['cf']['french-vfb']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vfb)       | {{ radarr['cf']['french-vfb']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) | {{ radarr['cf']['french-vostfr']['trash_id'] }} |
