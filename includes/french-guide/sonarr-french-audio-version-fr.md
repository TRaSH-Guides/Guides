??? abstract "Explications - [Cliquer pour afficher/masquer]"
    | Acronymes                  | Définition française                                                                | Définition anglaise                                                   |
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

    - *[1] VF est inclus dans le Format Personnalisé VFQ, mais il convient de noter qu'il était souvent associé à VFF au lieu de VFQ avant 2022.*
    - *[2] Il est à noter que le SUBFRENCH est inclus dans ce Format Personnalisé. Néanmoins, SUB signifie souvent que le sous-titre a été intégré à l'image (hardcoded). Les sorties françaises ont tendance à mélanger les deux, ce qui fait que certains VOSTFR sont étiquetés comme SUBFRENCH et SUBFRENCH comme VOSTFR.*

    !!! tip "Indexers renaming in Prowlarr"
        Certains indexeurs dans **Prowlarr** peuvent renommer les versions `MULTi` en `MULTi.TRUEFRENCH` ou `MULTi.FRENCH`. L'utilisation de cette fonction n'est pas recommandé, car elle peut entraîner des faux positifs avec les formats personnalisés VFF, VFQ et VQ.

??? abstract "Versions françaises - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                              | Trash ID                                        |
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
