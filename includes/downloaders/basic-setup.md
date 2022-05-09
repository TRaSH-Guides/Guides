This basic example is based on the use of docker images

!!! tip ""
    Keep in mind the path are setup so it works with hardlinks and instant moves.

    More info [HERE](/Hardlinks/Hardlinks-and-Instant-Moves/){:target="_blank" rel="noopener noreferrer"}

!!! attention ""
    The default path setup suggested by some docker developers that encourages people to use mounts like `/movies`, `/tv` and `/downloads` is very suboptimal because it makes them look like two or three file systems, even if they aren’t. It is the easiest way to get started. While easy to use, it has a major drawback. Mainly losing the ability to hardlink or instant move, resulting in a slower and more I/O intensive copy + delete is used.

    But you're able to change this, by not using the pre-defined/recommended paths like:

    - `/downloads` => `/data/downloads`, `/data/usenet`, `/data/torrents`
    - `/movies` => `/data/media/movies`
    - `/tv` => `/data/media/tv`
