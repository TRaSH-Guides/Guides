# How to setup Language Custom Formats

Here we will try to explain how to setup your own preferred language Custom Format, with a few examples.

## Language Examples

Import the JSON in to your Custom Formats.

How ?

Follow the [How to import Custom Formats](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.

---

### Language: Original Only

<sub><sub>Language: Not Original</sub>

This is one of the most common one used besides the English only one.

With this Custom Format you will get only the Movie/TV Show with the original language.

For this we're going to make use of so called reverse scoring.

Add the following json to your Radarr/Sonarr with a score of `-10000`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-not-original.json' %]][[% endfilter %]]
    ```

---

### Language: English Only

<sub><sub>Language: Not English</sub>

With this Custom Format you will get only the Movie/TV Show in the English language.

!!! info "Replace the English condition with your preferred language."

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

With this Custom Format you will get only the Movie/TV Show with Dutch and/or Flemish Audio.

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

Let's say you want German, but you take the Original language if no German is available, but don't want any other translated languages.

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

Let's say you just want to prefer Dutch (That uses multiple language conditions as described earlier) and don't care if you get another random language(s).

!!! info "Replace the Dutch/Flemish conditions with your preferred language(s)."

Add the following json to your Radarr/Sonarr with a score of `10`.

??? example "JSON - [CLICK TO EXPAND]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/language-prefer-dutch.json' %]][[% endfilter %]]
    ```

---

## FAQ

