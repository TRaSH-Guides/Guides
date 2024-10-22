!!! warning "Informations concernant les audios HD"

    Il convient de noter que divers problèmes peuvent survenir avec ce profil si vous utilisez les formats personnalisés de l'audio HD, car :

    - Les règles de la Scène française stipulent que l'audio français doit être le premier audio (celui par défaut) dans une version MULTi.
    - Les règles stipulent que seul le meilleur son (qu'il soit original ou FR) doit être mentionné dans le titre.
    - Certains films (et séries, principalement de l'ère pré-streaming) ne disposent pas d'une piste audio FR équivalente à la piste la plus élevée de l'audio original.

    En conséquence, les situations ci-après peuvent être observées :

    - La qualité de l'audio dans le titre de la release pourrait ne pas être celle de la version française.
    - L'audio français pourrait être de moins bonne qualité que l'audio mentionné dans le titre.
    - Radarr n'évalue les fichiers audio pré-importation qu'en fonction du titre de la release. Après l'importation, il se base sur la première piste audio (par défaut) de la release (après ffprobe).
    - La note finale de la release peut être inférieure à celle obtenue avant l'importation.

    !!! tip

        Pour cette raison, les Formats Personnalisés de Groupes P2P existent ; ils tentent de regrouper les groupes qui ont tendance à fournir les meilleures pistes audio originales et françaises pour une release. Cependant, cette approche n'est pas infaillible et un film peut ne pas avoir une piste audio FR équivalente à la piste la plus élevée de l'audio original.
