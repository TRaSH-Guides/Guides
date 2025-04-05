# NZBGet Scripts

!!! danger "USE THESE SCRIPTS ONLY IF YOU HAVE A PARTICULAR REQUIREMENT FOR THEM."

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

## replace_for

??? info "Replaces underscores with dots"

    - Title: `replace_for.py`
    - Author: miker

    Replaces underscores with dots in downloaded filename to prevent download loops with poorly named releases on some indexers (often HONE releases).

    Install Instructions:

        1. Copy script to NZBGet's script folder
        2. Run: `sudo chmod +x replace_for.py`
        3. Run: `dos2unix replace_for.py`
        4. In NZBGet go to `Settings` => `Extension Scripts`
        5. Enable `replace_for.py` in the `Extensions` setting.

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/NZBGet/scripts/replace_for/replace_for.py' %]][[% endfilter %]]
    ```
