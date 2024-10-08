Those are all optional and only there to rename your release or to refrain getting a certain type of French Audio. Examples:

- You prefer to have both VFF and VFQ, known as VF2 audio, in this case you will score VF2 at `101`, and keep the others at `0` (default).
- You prefer VFF over VFQ, in this case you will score VFF and VF2 at `101`, VFI to `0` (default), and VFQ to `-101`.
- You prefer VFQ over VFF, in this case you will score VFQ and VF2 at `101`, VFI to `0` (default), and VFF to `-101`.
- You absolutely do not want VQ audio, in this case you will put it to `-10000`.

!!! tip "Indexers"
    Not all indexers are reporting the type of **French Audio** a release have. Therefore you can still get unwanted French Audio.
    Scoring those CFs can also create download loop, please read the warning below.

!!! warning "Attention"
    It was proven that raising the score of an audio to more than `101` (but for `VOSTFR`) as higher chance to lead to download loop and therefore is not recommended.
    It was proven that downgrading the score of an audio to more than `-101` (unless absolutely not wanted as in the example) as higher chance to lead to download loop and therefore is not recommended.

??? abstract "Explanation - [Click to show/hide]"

    | Acronyms                   | French Explanation                                                                  | English Explanation                                                   |
    | -------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
    | TRUEFRENCH or VFF          | Version Francophone Française (doublage réalisé en France)                          | Full French version (dubbing done in France)                          |
    | FRENCH or VF<sup>[1]</sup> | Version Francophone (normalement equivalent à la VFQ)                               | French version (normally equivalent to VFQ)                           |
    | VOF                        | Version Originale Française                                                         | Original French Version                                               |
    | VFI                        | Version Francophone Internationale                                                  | International French Version                                          |
    | VFQ                        | Version Francophone Québécoise (doublage réalisé au Quebec)                         | Canadian French Version (dubbing done in Quebec)                      |
    | VOQ                        | Version Original Québécoise (ex: Bon Cop, Bad Cop)                                  | Quebec Original Version (ex: Bon Cop, Bad Cop)                        |
    | VQ                         | Version Québécoise (accent Québécois important, ex: Les Simpsons le film)           | Quebec Version (strong Quebec accent, ex: The Simpsons movie)         |
    | VFB                        | Version Francophone Belge                                                           | Belgian French Version                                                |
    | VF[1-9] or FR[1-9]         | Indique le nombre de doublage présent (normalement VF2 soit VFF et VFQ)             | Indicates the number of dubs present (normally VF2 being VFF and VFQ) |
    | VOSTFR<sup>[2]</sup>       | Indique que l'audio est dans la langue originale, avec des sous-titres en français. | Indicates soundtrack in the original language, with French subtitles  |

    - *[1] VF is included under the VFQ Custom Format, but it should be noted that it was often mismatched with VFF instead of VFQ pre-2022.*
    - *[2] It should be noted that SUBFRENCH is included in this Custom Format.*
