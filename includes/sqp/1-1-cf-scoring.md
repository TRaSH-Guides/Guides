#### Custom Formats and scores

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format                                                                             | Score                                   | Trash ID                             |
    | ----------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------ |
    | [{{ radarr['cf']['hq-webdl']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl) | {{ radarr['cf']['hq-webdl']['trash_score'] }} | {{ radarr['cf']['hq-webdl']['trash_id'] }} |
    | [{{ radarr['cf']['hq-remux']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq-remux) | 0                                       | {{ radarr['cf']['hq-remux']['trash_id'] }} |
    | [{{ radarr['cf']['hq']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hq)             | 0                                       | {{ radarr['cf']['hq']['trash_id'] }}       |

??? summary "BHDStudio - [CLICK TO EXPAND]"
    | Custom Format                                                                                                               | Score                                    | Trash ID                              |
    | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------- |
    | [{{ radarr['cf']['bhdstudio']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/bhdstudio.json) | {{ radarr['cf']['bhdstudio']['trash_score'] }} | {{ radarr['cf']['bhdstudio']['trash_id'] }} |

??? summary "Resolution - [CLICK TO EXPAND]"
    | Custom Format                                                                                                       | Score                                | Trash ID                          |
    | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------- |
    | [{{ radarr['cf']['720p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/720p.json)   | {{ radarr['cf']['720p']['trash_score'] }}  | {{ radarr['cf']['720p']['trash_id'] }}  |
    | [{{ radarr['cf']['1080p']['name'] }}](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/cf/1080p.json) | {{ radarr['cf']['1080p']['trash_score'] }} | {{ radarr['cf']['1080p']['trash_id'] }} |

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
