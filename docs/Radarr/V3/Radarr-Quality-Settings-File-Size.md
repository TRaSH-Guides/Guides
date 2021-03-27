# Quality Settings (File Size)

I often get the question what's the best Quality Settings to use,
Well it's actually personal preference so I will show you a recommended Quality Settings.
But before you continue to read, as with all my guides:

!!! question ""
    **If you don't care about quality then stop reading and see if the other tutorials are helpful for you.**

This Quality Settings has been created and tested with info I got from others, and release comparisons from different sources.

??? question "FAQ"

    ## FAQ

    **Q: Why do you only show starting from HDTV720p?**

    A: With the big screens these days anything lower doesn't look watchable

    **Q: Why do you have some sized set to max?**

    A: You probably didn't read the bold text above

    **Q: When I set Bluray to MAX size I get often ISO's/ Bluray folder structure.**

    A: You probable have configured your Quality Profiles wrong and enabled BR-DISK and didn't add the recommended Custom Profile to help Radarr to block/ignore it. [BR-DISK](/Radarr/V3/Radarr-collection-of-custom-formats/#br-disk){:target="_blank" rel="noopener noreferrer"}

    **Q: Some movies won't be grabbed because of these settings.**

    A: If you notice that some movies won't be grabbed because of these size settings you can provide me a proof with a screenshot and the error it shows you when you do a interactive search (non redacted except the indexer/tracker if you want to).

    - I will only accept changes that are International releases no multi, or dubbed language releases.
    - I won't accept mislabeled source releases like from MeGusta, etc (they should learn to name their stuff decent first).
    - I won't accept changes for micro sized releases.
    - Documentaries and cartoons are often much smaller so I probably won't edit those either.

------

## Radarr Quality Definitions

| Quality      | Minimum | Maximum |
| ------------ | ------- | ------- |
| HDTV-720p    | 17.1    | 400     |
| WEBDL-720p   | 17.1    | 400     |
| WEBRip-720p  | 17.1    | 400     |
| Bluray-720p  | 25.7    | 400     |
| HDTV-1080p   | 33.7    | 400     |
| WEBDL-1080p  | 33.7    | 400     |
| WEBRip-1080p | 33.7    | 400     |
| Bluray-1080p | 50.8    | 400     |
| Remux-1080p  | 136.8   | 400     |
| HDTV-2160p   | 85      | 400     |
| WEBDL-2160p  | 85      | 400     |
| WEBRip-2160p | 85      | 400     |
| Bluray-2160p | 102     | 400     |
| Remux-2160p  | 221.5   | 400     |

!!! note
    The reason why you don't see the preferred score in the Table is because we want max quality anyway so as high as possible.
