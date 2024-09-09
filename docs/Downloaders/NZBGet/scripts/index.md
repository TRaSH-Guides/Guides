# NZBGet Scripts

!!! note "NZBGet development has been picked up again by new developers over at [github](https://github.com/nzbgetcom/nzbget){:target="\_blank" rel="noopener noreferrer"}!"

A collection of community-provided and maintained scripts for NZBGet.

If you have a script you want to share, don't hesitate to create a [PR](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md) for it.

!!! warning "Because these scripts are community-provided and maintained we can't assure that they are still 100% working"

## Clean

??? info "Clean NZB name"

    - Title: `Clean.py`
    - Author(s): ???

    Removes the following suffixes from NZB name:
    NZBgeek / Obfuscated / BUYMORE / Scrambled /etc...
    Cleans the NZB name by removing the retagged stuff (-Obfuscated, -postbox, etc).

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/NZBGet/scripts/Clean/Clean.py' %]][[% endfilter %]]
    ```

## HashRenamer

??? info "Renames hashed media files to match the source NZB"

    - Title: `HashRenamer.py`
    - Author(s): l3uddz
    - URL: [github.com/cloudbox/cloudbox](https://github.com/cloudbox/cloudbox){:target="_blank" rel="noopener noreferrer"}

    Part of the Cloudbox project: [https://cloudbox.works](https://cloudbox.works)
    Built on top of the NZBGet scripts template created by [Clinton Hall](https://github.com/clinton-hall){:target="_blank" rel="noopener noreferrer"}.
    Released under GNU General Public License v2.0

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/NZBGet/scripts/HashRenamer/HashRenamer.py' %]][[% endfilter %]]
    ```

## replace_for

??? info "Replaces underscores with dots"

    - Title: `replace_for.py`
    - Author: miker

    Replaces underscores with dots in downloaded filename to prevent download loops with poorly named releases on some indexers (often HONE releases).

    Install Instructions:

        1. Copy script to NZBGet's script folder
        1. Run: `sudo chmod +x replace_for.py`
        1. In NZBGet go to `Settings` => `Extension Scripts`
        1. Enable `replace_for.py` in the `Extensions` setting.

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/NZBGet/scripts/replace_for/replace_for.py' %]][[% endfilter %]]
    ```

## WtFnZb-Renamer

??? info "Renames hashed media files to match the source NZB"

    - Title: `WtFnZb-Renamer.py`
    - Author(s): WtFnZb
    - URL: ??

    NZBGET SCAN SCRIPT

    Extract filenames from subjects containing [PRiVATE]-[WtFnZb]

    This extensions extracts obfuscated filenames from .nzb files

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/NZBGet/scripts/WtFnZb-Renamer/WtFnZb-Renamer.py' %]][[% endfilter %]]
    ```

!!! tip

    This script doesn't always work and is often needed if you use a certain indexer.

    It might be better to use the following Sonarr Regex in your release profile

    [su season pack issue](/Sonarr/Sonarr-Release-Profile-RegEx/#su-season-pack-issue)
