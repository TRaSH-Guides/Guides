# Recommended naming scheme

--8<-- "includes/starr/renaming-description-faq.md"

---

## Preparation

Go to `Settings` => `Media Management` and make sure that `Show Advanced` at the top is enabled.

![Enable Advanced](images/radarr-show-adavanced.png)

Once you've clicked on the button it should look like this and you should see all the advanced options.

![Unhide Advanced](images/unhide-advanced.png)

Finally, enable `Rename Movies` to reveal the movie renaming options.

![Enable Rename Movies](images/radarr-enable-rename.png)

## Standard Movie Format

--8<-- "includes/radarr/imdb-vs-tmdb.md"

=== "Standard"

    ```none
    {{ radarr['naming']['radarr-naming']['file']['standard'] }}
    ```

    <sub><sup>**Movie**: `The Movie Title (2010) {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

=== "Plex"

    This naming scheme is made to be used with the [New Plex Agent](https://forums.plex.tv/t/new-plex-media-server-movie-scanner-and-agent-preview/593269/517){:target="\_blank" rel="noopener noreferrer"},

    !!! danger "If you use the `{edition-{Edition Tags}}` part of the recommended file name, then Plex will recognize the edition of the movie and add it the the Plex UI - e.g., Directors Cut.<br><br>However, this means that if you have two copies of a movie with different editions in a single merged library - for example, a 1080p Directors Cut and a 2160p Theatrical Edition - then these will show as two separate items in Plex.<br><br>If you only want a movie to appear once per library, where you keep more than one copy of a movie, then replace: `{edition-{Edition Tags}}` with `{Edition Tags}`."

    === "Plex (IMDb)"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['plex-imdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) {imdb-tt0066921} {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

    === "Plex (TMDb)"

        ```none
        {{ radarr['naming']['radarr-naming']['file']['plex-tmdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) {tmdb-345691} {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

    === "Plex Anime (IMDb)"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['plex-anime-imdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) {imdb-tt0066921} {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`</sup></sub>

    === "Plex Anime (TMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['plex-anime-tmdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) {tmdb-345691} {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`</sup></sub>

=== "Emby"

    Source: [Emby Wiki/Docs](https://emby.media/support/articles/Movie-Naming.html#id-tags-in-folder--file-names){:target="\_blank" rel="noopener noreferrer"}

    === "Emby (IMDb)"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['emby-imdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [imdbid-tt0066921] - {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

    === "Emby (TMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['emby-tmdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [tmdbid-tt0066921] - {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

    === "Emby Anime (IMDb)"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['emby-anime-imdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [imdbid-tt0066921] - {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`</sup></sub>

    === "Emby Anime (TMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['emby-anime-tmdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [tmdbid-tt0066921] - {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`</sup></sub>

=== "Jellyfin"

    Source: [Jellyfin Wiki/Docs](https://jellyfin.org/docs/general/server/media/movies){:target="\_blank" rel="noopener noreferrer"}

    === "Jellyfin (IMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['jellyfin-imdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [imdbid-tt0106145] - {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

    === "Jellyfin (TMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['jellyfin-tmdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [tmdbid-65567] - {edition-Ultimate Extended Edition} [IMAX HYBRID][Bluray-1080p Proper][3D][DV HDR10][DTS 5.1][x264]-EVOLVE`</sup></sub>

    === "Jellyfin Anime (IMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['jellyfin-anime-imdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [imdbid-tt0106145] - {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`</sup></sub>

    === "Jellyfin Anime (TMDb)"

        ```bash
        {{ radarr['naming']['radarr-naming']['file']['jellyfin-anime-tmdb'] }}
        ```

        <sub><sup>**Movie**: `The Movie Title (2010) [tmdbid-65567] - {edition-Ultimate Extended Edition} [Surround Sound x264][Bluray-1080p Proper][3D][DTS 5.1][DE][10bit][AVC]-EVOLVE`</sup></sub>

---

## Original Title vs Original Filename

### Original Title

Another option is to use `{Original Title}` rather than the recommended naming scheme outlined above. `{Original Title}` will use the title of the release which will contain all of the information included in the release itself. The benefit of this naming scheme is to prevent download loops which can occur on import when there is a discrepancy in the release title compared to the contents of the file itself (for example, if the release title says DTS-ES but the contents are actually DTS). The downside is less flexibility with how the files are named.

If using this alternate naming scheme I suggest using `{Original Title}` over `{Original Filename}`

Why?

The filename can be Obscured where the Release naming isn't, especially when you use Usenet.

`{Original Title}` => `The.Movie.Title.2010.REMASTERED.1080p.BluRay.x264-GROUP`

`{Original Filename}` => `group-karatekid-1080p` or `lchd-tkk1080p` or `t1i0p3s7i8yuti`

---

## Movie Folder Format

--8<-- "includes/radarr/imdb-vs-tmdb.md"

!!! warning "Please note that folder names are created in the database whenever the movie is added to Radarr and it may be missing or incorrect at that time, resulting in your folder having a blank ID.:bangbang:<br><br>If you instead add it to the filename, the IMDb/TMDb ID will be freshly pulled for any download or upgrade."

=== "Standard Folder"

    Minimum needed and recommended

    ```bash
    {{ radarr['naming']['radarr-naming']['folder']['default'] }}
    ```

    <sub><sup>**Example**: `The Movie Title (2010)`</sup></sub>

=== "Optional Plex"

    --8<-- "includes/radarr/radarr-folder-name-after-year-info.md"

    === "Plex Folder IMDb"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['folder']['plex-imdb'] }}
        ```

        <sub><sup>**Example**: `The Movie Title (2010) {imdb-tt1520211}`</sup></sub>

    === "Plex Folder TMDb"

        ```bash
        {{ radarr['naming']['radarr-naming']['folder']['plex-tmdb'] }}
        ```

        <sub><sup>**Example**: `The Movie Title (2010) {tmdb-1520211}`</sup></sub>

=== "Optional Emby"

    --8<-- "includes/radarr/radarr-folder-name-after-year-info.md"

    === "Emby Folder IMDb"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['folder']['emby-imdb'] }}
        ```

        <sub><sup>**Example**: `The Movie Title (2010) [imdb-tt1520211]`</sup></sub>

    === "Emby Folder TMDb"

        ```bash
        {{ radarr['naming']['radarr-naming']['folder']['emby-tmdb'] }}
        ```

        <sub><sup>**Example**: `The Movie Title (2010) [tmdb-1520211]`</sup></sub>

=== "Optional Jellyfin"

    --8<-- "includes/radarr/radarr-folder-name-after-year-info.md"

    === "Jellyfin Folder IMDb"

        --8<-- "includes/radarr/tmdb-imdb-info.md"

        ```bash
        {{ radarr['naming']['radarr-naming']['folder']['jellyfin-imdb'] }}
        ```

        <sub><sup>**Example**: `The Movie Title (2010) [imdbid-tt1520211]`</sup></sub>

    === "Jellyfin Folder TMDb"

        ```bash
        {{ radarr['naming']['radarr-naming']['folder']['jellyfin-tmdb'] }}
        ```

        <sub><sup>**Example**: `The Movie Title (2010) [tmdbid-1520211]`</sup></sub>

---

--8<-- "includes/support.md"
