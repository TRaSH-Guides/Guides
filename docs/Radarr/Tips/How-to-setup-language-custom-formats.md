# How to setup Language Custom Formats

Here we will explain how to setup your own preferred language Custom Format, with a few examples.

## Language Examples

Import the JSON in to your Custom Formats.

How ?

Follow the [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.

---

### Language: Original Only

<sub><sub>Language: Not Original</sub>

This is one of the most common one used besides the English only one.

With this Custom Format you will only get Movies/TV Shows in their original language.

For this we're going to make use of so called reverse scoring.

Add the following json to your Radarr/Sonarr with a score of `-10000`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-not-original.json' %]][[% endfilter %]]
    ```

---

### Language: English Only

<sub><sub>Language: Not English</sub>

With this Custom Format you will only get the Movie/TV Show in the English language.

!!! info "Replace the English condition with language of your choice."

For this we're going to make use of so called reverse scoring.

Add the following json to your Radarr/Sonarr with a score of `-10000`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-not-english.json' %]][[% endfilter %]]
    ```

---

### Language: Multiple Only

<sub><sub>Language: Not Dutch</sub>

In some case you need multiple languages in your Custom Format for different reasons,

in this example I will use Dutch and Flemish being a lot of Movies/TV Shows are collaborate made between the 2 countries/studio's.

With this Custom Format you will only get the Movie/TV Show with Dutch and/or Flemish Audio.

!!! info "Replace the Dutch/Flemish conditions with your preferred language(s)."

For this we're going to make use of so called reverse scoring.

Add the following json to your Radarr/Sonarr with a score of `-10000`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-not-dutch.json' %]][[% endfilter %]]
    ```

---

### Language: Prefer X but i'll take Y

<sub><sub>Language: Not Original or German</sub>
<sub><sub>Language: Prefer German</sub>

Let's say you want German, but if German is not available then fall back to Original language but don't accept any other translated languages.

!!! info "Replace the German conditions with your preferred language(s)."

Add the following json to your Radarr/Sonarr with a score of `-10000`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-not-original-or-german.json' %]][[% endfilter %]]
    ```

Add the following json to your Radarr/Sonarr with a score of `10`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-prefer-german.json' %]][[% endfilter %]]
    ```

---

### Language: Prefer Language X

<sub><sub>Language: Prefer German</sub>

Let's say you just want to prefer German and don't care if you get another random language(s).

!!! info "Replace the German conditions with your preferred language(s)."

Add the following json to your Radarr/Sonarr with a score of `10`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-prefer-german.json' %]][[% endfilter %]]
    ```

---

### Language: Prefer Multi Language

<sub><sub>Language: Prefer Dutch</sub>

In some case you may want prefer multiple languages in your Custom Format.

With this Custom Format you will only get the Movie/TV Show with either Preferred Language.

In this example I will use Dutch and Flemish since a lot of Movies/TV Shows since there is a lot of collaboration between the two countries/studio's.

!!! info "Replace the Dutch/Flemish conditions with your preferred language(s)."

Add the following json to your Radarr/Sonarr with a score of `10`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-prefer-dutch.json' %]][[% endfilter %]]
    ```

---

## FAQ & INFO

### What's reverse scoring

??? FAQ "What's reverse scoring? - [CLICK TO EXPAND]"

    With reverse scoring you add a Custom Format with a score of `-10000` and your preferred condition you negate.

    So in the case of the following Custom Format `Language: Original Only`, it will actually match all Not Original releases and give it a score of `-10000`.

### Prefer language X over language Y

??? FAQ "Prefer language X over language Y - [CLICK TO EXPAND]"

    If you want to prefer Prefer language X over language Y,

    you add for example: `Language: Prefer Language X` with a score of `10`, and add `Language: Prefer Language Y` with score of `9`.

    Which scores you should use depends on how important the language is compared to other Custom Formats you're using.

### What's Original Language

??? FAQ "What's Original Language? - [CLICK TO EXPAND]"

    Original Language is the language in which a Movie/TV Show was originally made.

### Where does Radarr get the Original Language from

??? FAQ "Where does Radarr get the Original Language from? - [CLICK TO EXPAND]"

    Radarr makes use of [The Movie Database (TMDB)](https://www.themoviedb.org/){:target="_blank" rel="noopener noreferrer"}.

    ![!The Movie Database (TMDB) Original Language](images/original-language-tmdb.png)

### Where does Sonarr get the Original Language from

??? FAQ "Where does Sonarr get the Original Language from? - [CLICK TO EXPAND]"

    Sonarr makes use of [TheTVDB](https://thetvdb.com/){:target="_blank" rel="noopener noreferrer"}.

    ![!TheTVDB Original Language](images/original-language-tvdb.png)

--8<-- "includes/support.md"
