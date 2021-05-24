# Deluge - Basic Setup

This basic example is based on the use of docker images

!!! note ""
    Keep in mind I've setup my paths so it works with hardlinks and you get instant moves.

!!! attention ""
    The default path setup recommended by some docker developers that encourages people to use mounts like `/movies`, `/tv` and `/downloads` is very suboptimal. It is the easiest way to get started. While easy to use, it has a major drawback. Mainly losing the ability to hardlink or instant move.

    But you're able to change this, by not using the pre-defined/recommended paths like:

    - `/downloads` => `/data/downloads`
    - `/movies` => `/data/media/movies`
    - `/tv` => `/data/media/tv`.

------

## Soon
