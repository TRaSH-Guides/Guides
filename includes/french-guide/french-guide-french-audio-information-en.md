Those are all optional and only there to rename your release or to avoid getting a certain type of French audio. Examples:

- You prefer to have both VFF and VFQ, known as VF2 audio; in this case, you will score VF2 at `101` and keep the others at `0` (default).
- You prefer VFF over VFQ; in this case, you will score VFF and VF2 at `101`, set VFI to `0` (default), and VFQ to `-101`.
- You prefer VFQ over VFF; in this case you will score VFQ and VF2 at `101`, set VFI to `0` (default), and VFF to `-101`.
- You absolutely do not want VQ audio; in this case, you will set it to `-10000`.

!!! tip "Indexers"
    Not all indexers report the type of **French Audio** a release has. Therefore, you can still get unwanted French audio.
    Scoring these CFs can also create download loops; please read the warning below.

!!! warning "Attention"
    It has been proven that raising the score of an audio to more than `101` (except for `VOSTFR`) has a higher chance to lead to download loops and therefore is not recommended.
    Similarly, lowering the score of an audio to less than `-101` (unless absolutely not wanted as in the example) has a higher chance to lead to download loops and therefore is not recommended.

??? abstract "Explanation - [Click to show/hide]"

    | Acronyms                   | French Explanation                                                                  | English Explanation                                                   |
    |----------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
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

    - *[1] VF is included under the VFQ Custom Format, but it should be noted that it was often mismatched with VFF instead of VFQ pre-2022.*
    - *[2] It should be noted that SUBFRENCH is included in this Custom Format.*
