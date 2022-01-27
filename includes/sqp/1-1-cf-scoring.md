#### Custom Formats and scores

??? summary "HQ Source Groups - [CLICK TO EXPAND]"
    | Custom Format        | Score | LINK |
    | -------------------- | ----- | ---- |
    | HQ-WEBDL             | 1750  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-webdl){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ-Remux             |    0  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq-remux){: .header-icons target=_blank rel="noopener noreferrer" } |
    | HQ                   |    0  | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#hq){: .header-icons target=_blank rel="noopener noreferrer" } |

??? summary "BHDStudio - [CLICK TO EXPAND]"
    | Custom Format        | Score | LINK |
    | -------------------- | ----- | ---- |
    | BHDStudio            | 1800  | [:octicons-link-external-16:](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/bhdstudio.json){: .header-icons target=_blank rel="noopener noreferrer" } |

??? summary "Misc - [CLICK TO EXPAND]"
    | Custom Format        | Score | LINK |
    | -------------------- | ----- | ---- |
    | 720p                 |     5 | [:octicons-link-external-16:](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/720p.json){: .header-icons target=_blank rel="noopener noreferrer" } |
    | 1080                 |    25 | [:octicons-link-external-16:](https://raw.githubusercontent.com/TRaSH-/Guides/master/docs/json/radarr/1080p.json){: .header-icons target=_blank rel="noopener noreferrer" } |
    | Repack/Proper        |     1 | [:octicons-link-external-16:](/Radarr/Radarr-collection-of-custom-formats/#repack-proper){: .header-icons target=_blank rel="noopener noreferrer" } |

--8<-- "includes/cf/unwanted.md"

### Quality Size

`Settings` => `Quality`

Change the 1080p Quality Size to the range BHDStudio uses ( I searched BHD to check what was their smallest and biggest release, so this can change later if needed)

If you notice issues with the sizes please report it.

| Quality        | Min   | Preferred | Max   |
| -------------- | ----- | --------- | ----- |
| WEBDL-1080p    |  25.2 |      84.7 |  85.7 |
| WEBRip-1080p   |  25.2 |      84.7 |  85.7 |
| Bluray-720p    |  25.2 |     101   | 102   |
| Bluray-1080p   |  33.8 |     135.9 | 136.9 |

??? check "example - [CLICK TO EXPAND]"
    ![!Quality Size](images/quality-size.png)

    !!! attention
        These screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

        - Always follow the data described in the guide.
        - If you got any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.
