??? summary "Explanation - [CLICK TO EXPAND]"
    | Acronyms                         | French Explanation                                                                  | English Explanation                                                   |
    | -------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
    | TRUEFRENCH or VFF                | Version Francophone Française (doublage réalisé en France)                          | Full French version (dubbing done in France)                          |
    | FRENCH or VF<sup>[1]</sup>       | Version Francophone (normalement equivalent à la VFQ)                               | French version (normally equivalent to VFQ)                           |
    | VOF                              | Version Originale Française                                                         | Original French Version                                               |
    | VFI                              | Version Francophone Internationale                                                  | International French Version                                          |
    | VFQ                              | Version Francophone Québécoise                                                      | Canadian French Version                                               |
    | VQ                               | Version Québécoise (accent Québécois important, ex: Les Simpsons le film)           | Quebec Version (strong Quebec accent, ex: The Simpsons movie)         |
    | VFB                              | Version Francophone Belge                                                           | Belgian French Version                                                |
    | VF[1-9] or FR[1-9]<sup>[2]</sup> | Indique le nombre de doublage présent (normalement VF2 soit VFF et VFQ)             | Indicates the number of dubs present (normally VF2 being VFF and VFQ) |
    | VOSTFR<sup>[3]</sup>             | Indique que l'audio est dans la langue originale, avec des sous-titres en français. | Indicates soundtrack in the original language, with French subtitles  |

    - *[1] VF is included under the VFQ Custom Format, but it should be noted that it was often mismatched with VFF instead of VFQ pre-2022.*
    - *[2] VF[1-9] is included under the VFI Custom Format.*
    - *[3] It should be noted that SUBFRENCH is included in this Custom Format. However, SUB often means that the subtitle was embedded inside the picture (hardcoded). French releases tend to mix the two, leading to some VOSTFR being labelled as SUBFRENCH and SUBFRENCH as VOSTFR.*

    - *[1] VF est inclus dans le Format Personnalisé VFQ, mais il convient de noter qu'il était souvent associé à VFF au lieu de VFQ avant 2022.*
    - *[2] VF [1-9] est inclus dans le Format Personnalisé VFI.*
    - *[3] Il est à noter que le SUBFRENCH est inclus dans ce Format Personnalisé. Néanmoins, SUB signifie souvent que le sous-titre a été intégré à l'image (hardcoded). Les sorties françaises ont tendance à mélanger les deux, ce qui fait que certains VOSTFR sont étiquetés comme SUBFRENCH et SUBFRENCH comme VOSTFR.*

    !!! tip "Indexers renaming in Prowlarr"
        Some Indexers in Prowlarr can rename `MULTi` releases to `MULTi.TRUEFRENCH` or `MULTi.FRENCH`. I do not recommend using such a feature along with those Custom Formats as it can lead to false positives from the VFF or VFQ Custom Formats.

        Certains indexeurs dans Prowlarr peuvent renommer les versions `MULTi` en `MULTi.TRUEFRENCH` ou `MULTi.FRENCH`. Je ne recommande pas l'utilisation d'une telle fonction car elle peut entraîner des faux positifs avec les formats personnalisés VFF ou VFQ.

??? summary "French Audio Versions - [CLICK TO EXPAND]"
    | Custom Format                                                                                      | Score | Trash ID                                        |
    | -------------------------------------------------------------------------------------------------- | ----- | ----------------------------------------------- |
    | [{{ radarr['cf']['french-vff']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vff)       | 0     | {{ radarr['cf']['french-vff']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vof']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vof)       | 0     | {{ radarr['cf']['french-vof']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vfi']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vfi)       | 0     | {{ radarr['cf']['french-vfi']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vfq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vfq)       | 0     | {{ radarr['cf']['french-vfq']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vq)         | 0     | {{ radarr['cf']['french-vq']['trash_id'] }}     |
    | [{{ radarr['cf']['french-vfb']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vfb)       | 0     | {{ radarr['cf']['french-vfb']['trash_id'] }}    |
    | [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) | 0     | {{ radarr['cf']['french-vostfr']['trash_id'] }} |
