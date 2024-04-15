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

    !!! tip "MULTi definition per indexers"
        Certains indexers dans **Radarr** vous permettront de choisir l'audio qui est normalement inclus dans une version `MULTi` en tant qu'option. Vous devriez choisir seulement `Original` et `French` si vous décidez de l'utiliser.
        Cette option ne devrait être utilisée que pour les indexers français où vous êtes sûr du fait que `MULTi` inclut à la fois l'audio `Original` et l'audio `Français`. L'utiliser avec des indexers plus "internationaux" peut créer un faux positif avec la recognaissance des CFs des versions françaises.

??? abstract "Versions françaises - [Cliquer pour afficher/masquer]"
    | Formats Personnalisés                                                                              | Trash ID                                        |
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
