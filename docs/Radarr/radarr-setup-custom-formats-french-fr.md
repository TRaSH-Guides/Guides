# Comment configurer les Formats Personnalisés

!!! note
    Ce guide a été créé et est maintenu par [Someone said "Nice"?](https://github.com/NiceTSY)

Quelle est la meilleure façon de configurer les Formats Personnalisés (ou Custom Formats) et lesquels utiliser avec quel score pour obtenir une release avec un audio français et un anglais ?

Gardez à l'esprit que la plupart des sorties sont MULTi (comprenez double audio, original et français) et qu'il sera difficile d'avoir uniquement l'audio français, à moins que vous ne soyez prêt à obtenir du 720p, ou que vous ne recherchiez que des films français.

Par conséquent, vous aurez besoin d'un format personnalisé MULTi légèrement modifié par rapport à celui qui se trouve dans le guide original. Celui-ci reconnaît également les tags VO et VFF dans le nom et renomme le fichier durant l'importation. Ceci est important pour que le score corresponde avant et après l'importation et ainsi éviter une boucle où une release serait téléchargé de multiple fois.

--8<-- "includes/cf/score-attention.md"

------

## Notions de base

Il est très important que vous respectiez et compreniez ce qui est proposé par le guide de Trash (en anglais seulement) :

- L'ajout de Formats Personnalisés, comme expliqué dans [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.
- La configuration d'un profil de qualité pour utiliser les formats personnalisés, comme expliqué dans la section [How to setup Custom Formats | Basics section](/Radarr/Radarr-setup-custom-formats/#basics){:target="_blank" rel="noopener noreferrer"}.

------

!!! warning "Impératif"

    La seule modification nécessaire et **indispensable** pour que les formats personnalisés français fonctionnent, est de définir le profil de langue sur `Any`.

    ??? check "Exemple - [CLICK TO EXPAND]"
        ![!cf-quality-profile-cf](images/cf-french-profile-language.png)

    !!! info
        `Any` est choisit sinon un film anglais identifié avec un son français dans Radarr ne sera pas récupéré et vice-versa.

------

## Je ne suis intéressé que par des films sous-titrés en français (VOSTFR)

Deux options s'offre à vous :

### En utilisant le guide de Trash et Bazarr

!!! tip "Il s'agit de la méthode à privilégier."

- Allez voir ces exemples : [How to setup Custom Formats | Examples section](/Radarr/Radarr-setup-custom-formats/#examples)
- Configurez [Bazarr](../Bazarr/Setup-Guide.md). Il permet d'obtenir des sous-titres pour tous les films.
- Profitez de vos films avec les sous-titres.
- (Facultatif) Ajoutez le Format Personnalisé [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) avec un score de `1000`.

### En utilisant les exemples suivants et le Format Personnalisé VOSTFR

- Continuez sur cette page.
- Ignorez toute mention des **Formats Personnalisés MULTi**.
- Ajoutez le Format Personnalisé [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr) avec un score de `1000`.

------

## Usages

Il y a deux façons d'aborder les exemples ci-dessous. En utilisant ou non les Formats Personnalisés de Groupes P2P du Guide original (qui peuvent être trouvés ici : [Collection of Custom Formats](/Radarr/Radarr-collection-of-custom-formats/){:target="_blank" rel="noopener noreferrer"}).
Afin d'illustrer ce principe, vous verrez une section **"Original mix (optional)"** dans chacun des exemples ci-dessous. Vous devez comprendre que si vous ajoutez les Formats Personnalisés de cette section optionnelle, si Radarr ne trouve pas de MULTi, vous aurez toujours un bon score pour l'audio anglais.

!!! warning "Attention"
    Si vous utilisez le **"Original mix (optional)"**. Vous devez comprendre que même si l'objectif principal de ces Formats Personnalisés est de travailler en parallèle avec les formats du guide original.
    Vous pouvez vous retrouver avec une seule version audio alors qu'il existe une version MULTi. La raison est qu'elle n'a pas été notée assez haut pour l'emporter sur les autres scores.

------

## Exemples

--8<-- "includes/cf/score-attention.md"

------

### Type de versions françaises

Ces Formats sont optionnels et ne sont là que pour renommer votre fichier ou pour éviter un certain type de version française. Exemples :

- Vous ne voulez pas de VFQ ou VQ, dans ce cas, vous leur attribuerez un score de `-10000` au lieu de `0`.
- Vous souhaitez seulement du VOSTFR, dans ce ce cas, ignorez toute mention des **Formats Personnalisés MULTi** et donnerez un score de `1000` au Format Personnalisé [{{ radarr['cf']['french-vostfr']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vostfr).

{! include-markdown "../../includes/french-guide/radarr-french-audio-version.md" !}

------

### Les releases à éviter

Selon moi, ces Formats sont indispensables pour tous les Profils de Qualité que vous utilisez. Ils vous assurent de ne pas avoir de releases de faible qualité.

{! include-markdown "../../includes/french-guide/radarr-french-unwanted.md" !}

------

#### Encodages HQ-1080p

{! include-markdown "../../includes/french-guide/radarr-french-example-hd-encodes.md" !}

------

#### Remux-1080p

{! include-markdown "../../includes/french-guide/radarr-french-example-1080p-remuxes.md" !}

------

#### Encodages HQ-2160p

{! include-markdown "../../includes/french-guide/radarr-french-example-uhd-encodes.md" !}

------

#### Remux-2160p

{! include-markdown "../../includes/french-guide/radarr-french-example-2160p-remuxes.md" !}

------

## Remerciements

- Un grand merci à toutes les personnes qui m'ont aidé à tester ces Profils et Formats (et qui continuent à le faire).
- Une mention spéciale à MySuperChef et PrL pour leur temps et leurs explications.
- Une mention spéciale pour Piou et Wikoul qui sont potentiellement tous les deux maintenant dans des asiles en raison de la quantité de tests effectués.
- [TRaSH](https://trash-guides.info/), pour m'avoir accordé un petit espace sur son guide, ses connaissances, et sa gentillesse.

--8<-- "includes/support.md"
