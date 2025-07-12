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
    - Website: [https://github.com/TheCaptain989/bazarr-cleansubs](https://github.com/TheCaptain989/bazarr-cleansubs)
    
    Automatically removes common annoying scene branding and attribution entries from subtitle files. Only .SRT format subtitles are supported.
    
    <a href="https://github.com/TheCaptain989/bazarr-cleansubs/raw/refs/heads/master/cleansubs.sh" download>Download</a> the script from GitHub and place in the `/config` directory of bazarr.

??? example "Script"

    Configure a custom script from the Bazarr *Settings* > *Subtitles* screen by pasting the following in the **Command** field under **Custom Post-Processing**: 
    
    ```sh
    /config/cleansubs.sh -f "{{subtitles}}" ;
    ```
