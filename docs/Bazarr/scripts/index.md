# Bazarr Scripts

A collection of community-provided and maintained scripts for Bazarr.

If you have a script you want to share, don't hesitate to create a [PR](https://github.com/TRaSH-Guides/Guides/blob/master/CONTRIBUTING.md) for it.

!!! warning "Because these scripts are community-provided and maintained we can't assure that they are still 100% working"

## 2 to 3 language code

??? info "2 to 3 language code"

    - Title: `2to3_language_code.sh`
    - Author(s): ???

    Changes the 2 iso code to 3 iso code.

??? example "Script"

    ```sh
    [[% filter indent(width=4) %]][[% include 'Bazarr/scripts/2to3-language-code/2to3_language_code.sh' %]][[% endfilter %]]
    ```

## Cleansubs

??? info "cleansubs"

    - Title: `cleansubs.sh`
    - Author: [TheCaptain989](https://github.com/TheCaptain989)
    - Website: https://github.com/TheCaptain989/bazarr-cleansubs
    
    A shell script to automatically remove common annoying scene branding and   attribution entries from subtitle files. Only .SRT format subtitles are   supported.
    
    [Download](https://raw.githubusercontent.com/TheCaptain989/bazarr-cleansubs/refs/heads/master/cleansubs.sh) from GitHub source and place in the `/config` directory of bazarr.

??? example "Script"

    Configure a custom script from the Bazarr *Settings* > *Subtitles* screen by typing the following in the **Post-processing command** field (Note the double quotes!): 
    
    `/config/cleansubs.sh -f "{{subtitles}}" ;`
