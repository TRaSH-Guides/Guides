#### Custom Formats and scores

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                    | Score                                   | LINK                                                                                                                                           |
    | -------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
    | {{ radarr['hq-webdl']['name'] }} | {{ radarr['hq-webdl']['trash_score'] }} | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |
    | {{ radarr['hq-remux']['name'] }} | 0                                       | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-remux){: .header-icons target=_blank rel="noopener noreferrer" } |
    | {{ radarr['hq']['name'] }}       | 0                                       | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq){: .header-icons target=_blank rel="noopener noreferrer" }       |

??? summary "BHDStudio - [CLICK TO EXPAND]"
    | Custom Format                     | Score                                    | LINK                                                                                                                                                                            |
    | --------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | {{ radarr['bhdstudio']['name'] }} | {{ radarr['bhdstudio']['trash_score'] }} | [:octicons-link-external-16:](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/bhdstudio.json){: .header-icons target=_blank rel="noopener noreferrer" } |

??? summary "Resolution - [CLICK TO EXPAND]"
    | Custom Format                 | Score                                | LINK                                                                                                                                                                        |
    | ----------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | {{ radarr['720p']['name'] }}  | {{ radarr['720p']['trash_score'] }}  | [:octicons-link-external-16:](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/720p.json){: .header-icons target=_blank rel="noopener noreferrer" }  |
    | {{ radarr['1080p']['name'] }} | {{ radarr['1080p']['trash_score'] }} | [:octicons-link-external-16:](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/1080p.json){: .header-icons target=_blank rel="noopener noreferrer" } |

{! include-markdown "../../includes/cf/misc.md" !}
<!-- --8<-- "includes/cf/misc.md" -->

{! include-markdown "../../includes/cf/unwanted.md" !}
<!-- --8<-- "includes/cf/unwanted.md" -->

### Quality Size

`Settings` => `Quality`

Change the 1080p Quality Size to the range BHDStudio uses ( I searched BHD to check what was their smallest and biggest release, so this can change later if needed)

If you notice issues with the sizes please report it.

| Quality      | Min  | Preferred | Max   |
| ------------ | ---- | --------- | ----- |
| WEBDL-1080p  | 25.2 | 84.7      | 85.7  |
| WEBRip-1080p | 25.2 | 84.7      | 85.7  |
| Bluray-720p  | 25.2 | 101       | 102   |
| Bluray-1080p | 33.8 | 135.9     | 136.9 |

??? check "example - [CLICK TO EXPAND]"
    ![!Quality Size](/SQP/images/quality-size.png)

    !!! attention
        These screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

        - Always follow the data described in the guide.
        - If you got any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.
