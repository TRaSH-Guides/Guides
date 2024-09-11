# SABnzbd Scripts

A collection of community-provided and maintained scripts for SABnzbd.

If you have a script you want to share, don't hesitate to create a [PR](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md) for it.

!!! warning "Because these scripts are community-provided and maintained we can't assure that they are still 100% working"

## Clean

??? info "Clean NZB name"

    - Title: `Clean.py`
    - Author(s): ???
    - Made compatible for SABnzbd: AlexK

    Removes the following suffixes from NZB name:
    NZBgeek / Obfuscated / BUYMORE / Scrambled /etc...
    Cleans the NZB name by removing the retagged stuff (-Obfuscated, -postbox, etc).

    Install Instructions:

        1. Copy script to SABnzbd's script folder
        1. run: `sudo chmod +x Clean.py`
        1. in SABnzbd go to `Settings` => `Switches`
        1. Change Pre-queue user script and select: `Clean.py`

    ![!Enable Clean.py](/Downloaders/SABnzbd/images/sabnzbd-switches-queue-clean.png)

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/SABnzbd/scripts/Clean/Clean.py' %]][[% endfilter %]]
    ```

## replace_for

??? info "Replaces underscores with dots"

    - Title: `replace_for.py`
    - Author: miker

    Replaces underscores with dots in downloaded filename to prevent download loops with poorly named releases on some indexers (often HONE releases).

    Install Instructions:

        1. Copy script to SABnzbd's script folder
        1. run: `sudo chmod +x replace_for.py`
        1. in SABnzbd go to `Settings` => `Categories`
        1. Change script for required categories and select: `replace_for.py`

    ![!Enable replace_for.py](/Downloaders/SABnzbd/images/sabnzbd-categories-replace_for.png)

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'Downloaders/SABnzbd/scripts/replace_for/replace_for.py' %]][[% endfilter %]]
    ```
