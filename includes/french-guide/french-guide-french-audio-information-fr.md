Cette section est optionnelle et est uniquement là pour renommer votre release ou pour éviter d'obtenir un certain type d'audio français. Exemples :

- Vous préférez avoir à la fois la VFF et la VFQ, connues sous le nom de VF2 ; dans ce cas, vous attribuerez un score de `101` à VF2 et laisserez les autres à `0` (par défaut).
- Vous préférez la VFF à la VFQ ; dans ce cas, vous attribuerez un score de `101` pour la VFF et la VF2, laisserez VFI à `0` (par défaut), et mettrez VFQ à `-101`.
- Vous préférez la VFQ à la VFF ; dans ce cas, vous attribuerez un score de `101` pour la VFQ et la VF2, laisserez VFI à `0` (par défaut), et mettrez VFF à `-101`.
- Vous ne voulez absolument pas d'audio VQ ; dans ce cas, vous le mettrez à `-10000`.

!!! tip "Indexeurs"
    Tous les indexeurs ne signalent pas le type de version française qu'une release possède. Par conséquent, vous pouvez toujours obtenir un audio français non désiré.
    Attribuer un score à ces Formats Personnalisés peut également créer une boucle ; veuillez lire l'avertissement ci-dessous.

!!! warning "Attention"
    Il a été prouvé qu'augmenter le score d'un audio à plus de `101` (sauf pour `VOSTFR`) peut entraîner une boucle de téléchargement, où une release est téléchargée à plusieurs reprises.
    Il a aussi été prouvé que diminuer le score d'un audio à moins de `-101` (sauf si absolument non désiré comme dans l'exemple) peut également entraîner une boucle de téléchargement.

??? abstract "Explications - [Cliquer pour afficher/masquer]"

    | Acronymes                  | Définition française                                                               | Définition anglaise                                                   |
    |----------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
    | TRUEFRENCH or VFF          | Version francophone française (doublage réalisé en France)                         | Full French version (dubbing done in France)                          |
    | FRENCH or VF<sup>[1]</sup> | Version francophone (normalement équivalente à la VFQ)                             | French version (normally equivalent to VFQ)                           |
    | VOF                        | Version originale française                                                        | Original French Version                                               |
    | VFI                        | Version francophone internationale                                                 | International French Version                                          |
    | VFQ                        | Version francophone québécoise (doublage réalisé au Québec)                        | Canadian French Version (dubbing done in Quebec)                      |
    | VOQ                        | Version originale québécoise (ex. : Bon Cop, Bad Cop)                              | Quebec Original Version (e.g., Bon Cop, Bad Cop)                      |
    | VQ                         | Version québécoise (accent québécois important, ex. : Les Simpson, le film)        | Quebec Version (strong Quebec accent, e.g., The Simpsons movie)       |
    | VFB                        | Version francophone belge                                                          | Belgian French Version                                                |
    | VF[1-9] or FR[1-9]         | Indique le nombre de doublages présents (normalement VF2, soit VFF et VFQ)         | Indicates the number of dubs present (normally VF2 being VFF and VFQ) |
    | VOSTFR<sup>[2]</sup>       | Indique que l'audio est dans la langue originale, avec des sous-titres en français | Indicates soundtrack in the original language, with French subtitles  |

    - *[1] VF est inclus dans le Format Personnalisé VFQ, mais il convient de noter qu'il était souvent associé à VFF au lieu de VFQ avant 2022.*
    - *[2] Il est à noter que SUBFRENCH est inclus dans ce Format Personnalisé.*
