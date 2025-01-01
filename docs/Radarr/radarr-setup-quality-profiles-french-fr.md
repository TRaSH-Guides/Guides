# Comment configurer ses Profiles (French Profile)

*aka Comment configurer les Formats Personnalisés pour obtenir un audio et/ou des sous-titres en français ?*<br><br>

!!! note "Ce guide a été créé et est maintenu par [Someone Said "Nice"?](https://github.com/NiceTSY)"

---

## Notions de base

Il est important que vous suiviez et compreniez ce qui est prévu par le guide de TRaSH :

- Ajouter des Formats Personnalisés, comme expliqué dans [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"} (anglais seulement).
- Configurer un Profil de Qualité pour utiliser les Formats Personnalisés, comme expliqué dans [How to setup Quality Profiles | Basics section](/Radarr/radarr-setup-quality-profiles/#basics){:target="_blank" rel="noopener noreferrer"} (anglais seulement).

!!! warning "Veuillez lire ces deux sections avant de continuer le guide, car elles contiennent des informations importantes. Le reste de ce guide part du principe que vous l'avez fait."

!!! tip
    TRaSH a créé un [organigramme](/Radarr/Radarr-setup-custom-formats/#which-quality-profile-should-you-choose){:target="\_blank" rel="noopener noreferrer"} pour faciliter vos décisions. N'oubliez pas que ce schéma n'inclut aucun des formats personnalisés suivants et que vous devrez toujours lire ce guide pour obtenir des versions MULTi.

---

## FAQ

!!! info "Je ne suis pas Français de France mais du Canada, est-ce que le guide fonctionne toujours ?"
    Oui, le guide s'adapte à tous les types de français : VFF, VFQ et VFB (même si ce dernier est assez rare). Assurez-vous simplement de vérifier le scoring dans la section [Versions Audio Françaises](#versions-audio-francaises) section.

!!! info "Je suis seulement intéressé par les sous-titres français (VOSTFR)"
    Veuillez suivre le profil **Original avec sous-titres** (**VOSTFR**).

!!! info "Puis-je obtenir des HDLight ou 4KLight ?"
    Pas vraiment, ce guide n'est pas prévu pour cela. Toutefois, si l'espace disque est un problème pour vous, préférez les versions Web-DL ou les releases Blu-ray 720p.

!!! info "FlareSolverr ?"
    Il existe une section en anglais : [How to set up FlareSolverr](/Prowlarr/prowlarr-setup-flaresolverr/){:target="\_blank" rel="noopener noreferrer"}.

---

## Paramètres spécifiques à Prowlarr

!!! abstract "Indexers - Remplacer MULTi par une autre langue dans le nom de la release (Replace MULTi by another language in release name)"
    Prowlarr permet de remplacer MULTi par une autre langue. Cette option semble excellente mais entraînera des faux positifs concernant les CF audio français.
    Veuillez préférer l'utilisation de l'option "Indexeurs - Option Multi Langues" dans Radarr (voir ci-dessous).

!!! abstract "Indexers - Remplacer VOSTFR et SUBFRENCH par ENGLISH (Replace VOSTFR and SUBFRENCH with ENGLISH)"
    Cette option ne devrait pas être utilisée, principalement parce que vous perdez des informations concernant la release.
    De plus, `VOSTFR` ne signifie pas que l'audio est en `Anglais` mais plutôt qu'il s'agit de l'audio `Original`, ce qui peut correspondre à de l'`Espagnol`, du `Coréen`, etc.

!!! abstract "Indexers - Remplacer VFQ par FRENCH (Replace VFQ with FRENCH)"
    Comme pour l'option MULTi, cela entraînera des faux positifs concernant les CF audio français. Gardez-la désactivée.

??? success "Capture d'écran - [Cliquez pour afficher/masquer]"
    ![French Prowlarr specific settings](images/french-prowlarr-settings.png)

---

## Paramètres spécifiques à Radarr

!!! abstract "Media Management - Format Standard du Film et Format du Dossier du Film (Standard Movie Format and Movie Folder Format)"
    Veuillez consulter ceci : [Recommended naming scheme](/Radarr/Radarr-recommended-naming-scheme/){:target="_blank" rel="noopener noreferrer"} (anglais seulement).

    !!! tip "Format du film/dossier avec le nom du film en français"
        Radarr supporte la convention de nommage ISO-2 pour nommer un film, donc en remplaçant `{Movie CleanTitle}` par `{Movie CleanTitle:fr}`, cela changera le nom pour sa version française.

!!! abstract "Indexers - Multi Languages option"
    Dans Radarr, vous pouvez indiquer que MULTi pour un indexeur signifie qu'une release possède au moins certains audios. Pour les besoins de ce guide, vous sélectionnerez `Original` et `French`.
    Cette option ne devrait être utilisée que pour les indexeurs français. L'appliquer sur des indexeurs plus "internationaux" peut créer des faux positifs avec les CF audio français.

    Si vous ne voyez pas l'option, pensez à activer les "Options Avancées" de Radarr.

    ??? success "Capture d'écran - [Cliquez pour afficher/masquer]"
        ![French Radarr MULTi settings](images/french-starr-multi-settings.png)

---

## Logique de scoring (anglais seulement)

--8<-- "includes/cf/score-attention.md"

---

## Profils de Qualité

{! include-markdown "../../includes/french-guide/french-guide-language-profiles-fr.md" !}

---

### Versions Audio Françaises

{! include-markdown "../../includes/french-guide/french-guide-french-audio-information-fr.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-audio-version-fr.md" !}

---

### HD Bluray + WEB (1080p)

!!! tip "Paramètres de base"
    Assurez-vous de fusionner les qualités Bluray et WEB en un seul groupe dans les qualités de votre Profil de Qualité. Cela est dû au fait que les releases potentielles avec un audio `Français` peuvent ne pas exister en WEB.
    La raison pour laquelle nous n'avons pas sélectionné le WEB-DL 720p est que vous trouverez difficilement des releases qui ne sont pas en 1080p WEB-DL.

    ??? success "Capture d'écran pour les profiles VOSTFR + MULTi.VO - [Cliquez pour afficher/masquer]"
        ![HD Bluray + WEB for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-bluray-webdl-hd-vo.png)

    ??? success "Capture d'écran pour le profile MULTi.VF - [Cliquez pour afficher/masquer]"
        ![HD Bluray + WEB for MULTi.VF Profile](images/french-radarr-qp-bluray-webdl-hd-vf.png)

!!! warning "Assurez-vous de ne pas cocher l'option BR-DISK."

{! include-markdown "../../includes/french-guide/starr-move-quality-to-top-fr.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**Les Formats Personnalisés suivants sont requis :**

{! include-markdown "../../includes/french-guide/radarr-cf-french-hd-bluray-web-scoring-fr.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-fr.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**Les Formats Personnalisés suivants sont facultatifs :**

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe-noremux.md" !}

Note: Les Formats Personnalisés `Advanced Audio` ne sont pas utilisés dans le profil, car les WEB-DL contiennent rarement de l'audio HD (la plupart des nouveaux WEB-DL contiennent cependant de l'Atmos avec perte). Si vous voulez de l'audio HD, nous vous suggérons d'utiliser des Remuxes ou des encodages UHD.

---

### HD Remux (1080p)

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-fr.md" !}

!!! tip "Paramètres de base"
    Assurez-vous de fusionner les qualités Bluray et WEB en un seul groupe dans les qualités de votre Profil de Qualité. Cela est dû au fait que les releases potentielles avec un audio `Français` peuvent ne pas exister en WEB.
    La raison pour laquelle nous n'avons pas sélectionné le WEB-DL 720p est que vous trouverez difficilement des releases qui ne sont pas en 1080p WEB-DL.

    ??? success "Capture d'écran pour les profiles VOSTFR + MULTi.VO - [Cliquez pour afficher/masquer]"
        ![HD Remux for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-remux-hd-vo.png)

    ??? success "Capture d'écran pour le profile MULTi.VF - [Cliquez pour afficher/masquer]"
        ![HD Remux for MULTi.VF Profile](images/french-radarr-qp-remux-hd-vf.png)

!!! warning "Assurez-vous de ne pas cocher l'option BR-DISK."

{! include-markdown "../../includes/french-guide/starr-move-quality-to-top-fr.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**Les Formats Personnalisés suivants sont requis :**

{! include-markdown "../../includes/french-guide/radarr-cf-french-remux-web-scoring-fr.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-fr.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**Les Formats Personnalisés suivants sont facultatifs :**

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe.md" !}

---

### UHD Bluray + WEB (2160p)

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-fr.md" !}

!!! tip "Paramètres de base"
    Assurez-vous de fusionner les qualités Bluray et WEB en un seul groupe dans les qualités de votre Profil de Qualité. Cela est dû au fait que les releases potentielles avec un audio `Français` peuvent ne pas exister en WEB.

    ??? success "Capture d'écran pour les profiles VOSTFR + MULTi.VO - [Cliquez pour afficher/masquer]"
        ![UHD Bluray + WEB for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-bluray-webdl-uhd-vo.png)

    ??? success "Capture d'écran pour le profile MULTi.VF - [Cliquez pour afficher/masquer]"
        ![UHD Bluray + WEB for MULTi.VF Profile](images/french-radarr-qp-bluray-webdl-uhd-vf.png)

!!! warning "Assurez-vous de ne pas cocher l'option BR-DISK."

{! include-markdown "../../includes/french-guide/starr-move-quality-to-top-fr.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**Les Formats Personnalisés suivants sont requis :**

{! include-markdown "../../includes/french-guide/radarr-cf-french-uhd-bluray-web-scoring-fr.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-hdr-format-information-fr.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-fr.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**Les Formats Personnalisés suivants sont facultatifs :**

{! include-markdown "../../includes/french-guide/french-guide-optional-format-information-fr.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-misc-uhd-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe-noremux.md" !}

---

### UHD Remux (2160p)

{! include-markdown "../../includes/french-guide/radarr-french-advanced-audio-information-fr.md" !}

!!! tip "Paramètres de base"
    Assurez-vous de fusionner les qualités Bluray et WEB en un seul groupe dans les qualités de votre Profil de Qualité. Cela est dû au fait que les releases potentielles avec un audio `Français` peuvent ne pas exister en WEB.

    ??? success "Capture d'écran pour les profiles VOSTFR + MULTi.VO - [Cliquez pour afficher/masquer]"
        ![UHD Remux for VOSTFR or MULTi.VO Profile](images/french-radarr-qp-remux-uhd-vo.png)

    ??? success "Capture d'écran pour le profile MULTi.VF - [Cliquez pour afficher/masquer]"
        ![UHD Remux for MULTi.VF Profile](images/french-radarr-qp-remux-uhd-vf.png)

!!! warning "Assurez-vous de ne pas cocher l'option BR-DISK."

{! include-markdown "../../includes/french-guide/starr-move-quality-to-top-fr.md" !}

{! include-markdown "../../includes/cf/radarr-suggest-attention.md" !}

**Les Formats Personnalisés suivants sont requis :**

{! include-markdown "../../includes/french-guide/radarr-cf-french-remux-web-scoring-fr.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-hdr-format-information-fr.md" !}

{! include-markdown "../../includes/cf/radarr-misc-required.md" !}

{! include-markdown "../../includes/french-guide/radarr-french-unwanted-fr.md" !}

{! include-markdown "../../includes/cf/radarr-streaming-services.md" !}

**Les Formats Personnalisés suivants sont facultatifs :**

{! include-markdown "../../includes/french-guide/french-guide-optional-format-information-fr.md" !}

{! include-markdown "../../includes/cf/radarr-audio.md" !}

{! include-markdown "../../includes/cf/radarr-misc-optional.md" !}

{! include-markdown "../../includes/cf/radarr-misc-uhd-optional.md" !}

{! include-markdown "../../includes/cf/radarr-movie-versions-imaxe.md" !}

---

### Formats audio avancés et HDR

TRaSH fournit d'excellents guides et explications à leur sujet dans les liens suivants (*en anglais uniquement*) :

- [Advanced Audio](/Radarr/radarr-setup-quality-profiles/#advanced-audio){:target="\_blank" rel="noopener noreferrer"}
- [HDR Formats](/Radarr/radarr-setup-quality-profiles/#hdr-formats){:target="\_blank" rel="noopener noreferrer"}

---

## Autres Informations

Une FAQ répondant à la plupart des questions que vous pourriez vous poser est fournie par TRaSH (*en anglais uniquement*) : [FAQ & Info](/Radarr/radarr-setup-quality-profiles/#faq-info){:target="\_blank" rel="noopener noreferrer"}

---

## Remerciements

- Un grand merci à toutes les personnes qui m'ont aidé à créer et tester ces Profils et Formats (et qui continuent à le faire).
- Une mention spéciale à MySuperChef et PrL pour leur temps et leurs explications.
- Une mention spéciale pour Piou et Wikoul qui sont potentiellement tous les deux maintenant dans des asiles en raison de la quantité de tests effectués.
- [TRaSH](https://trash-guides.info/), pour m'avoir accordé un petit espace sur son guide, ses connaissances, et sa gentillesse.

--8<-- "includes/support.md"
