# Scripts you can use with NZBGet

## [Clean](Clean/README.md)

Cleans the NZB name by removing the retagged stuff (-Obfuscated, -postbox, etc).

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'NZBGet/scripts/Clean/Clean.py' %]][[% endfilter %]]
    ```

## [HashRenamer](HashRenamer/README.md)

Renames hashed media files to match the source NZB.

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'NZBGet/scripts/HashRenamer/HashRenamer.py' %]][[% endfilter %]]
    ```

## [WtFnZb-Renamer](WtFnZb-Renamer/README.md)

This extensions extracts obfuscated filenames from .nzb files

??? example "Script"

    ```python
    [[% filter indent(width=4) %]][[% include 'NZBGet/scripts/WtFnZb-Renamer/WtFnZb-Renamer.py' %]][[% endfilter %]]
    ```
