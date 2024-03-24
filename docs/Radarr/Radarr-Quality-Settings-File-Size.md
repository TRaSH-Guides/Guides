# Quality Settings (File Size)

I often get the question "What's the best quality settings to use?"
Well, it's actually personal preference so I will show you my recommendations.

But before you continue to read, as with all my guides:

!!! danger ""
    **If you don't care about quality then stop reading and see if the other tutorials are helpful for you.**

These Quality Settings have been created and tested with info I got from others, and release comparisons from different sources.

??? question "FAQ - [Click to show/hide]"

    ## FAQ

    **Q: Why do you only show starting from HDTV720p?**

    A: With the big screens these days anything lower doesn't look watchable

    **Q: Why do you have some sizes set to max?**

    A: You probably didn't read the bold text above

    **Q: When I set Bluray to MAX size I often get ISO's/ Bluray folder structure.**

    A: You probably have configured your Quality Profiles wrong and enabled BR-DISK and didn't add the recommended Custom Profile to help Radarr to block/ignore it. [BR-DISK](/Radarr/Radarr-collection-of-custom-formats/#br-disk){:target="_blank" rel="noopener noreferrer"}

    **Q: Some movies won't be grabbed because of these settings.**

    A: If you notice that some movies won't be grabbed because of these size settings, you can provide me proof with a screenshot and the error it shows you when you do an interactive search (non redacted except the indexer/tracker if you want to).

    - I will only accept changes that are international releases. No multi, or dubbed language releases.
    - I won't accept mislabeled source releases like from MeGusta etc. (They should learn to name their stuff properly first)
    - I won't accept changes for micro sized releases.
    - Documentaries and cartoons are often much smaller so I probably won't edit those either.

------

## Radarr Quality Definitions

- Note that `400` is the displayed value for Unlimited

| Quality                                                           | Minimum (Megabytes Per Minute)                                | Maximum (Megabytes Per Minute)                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| {{ radarr['quality-size']['movie']['qualities'][0]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][0]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][0]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][1]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][1]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][1]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][2]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][2]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][2]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][3]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][3]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][3]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][4]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][4]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][4]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][5]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][5]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][5]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][6]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][6]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][6]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][7]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][7]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][7]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][8]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][8]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][8]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][9]['quality'] }}  | {{ radarr['quality-size']['movie']['qualities'][9]['min'] }}  | {{ radarr['quality-size']['movie']['qualities'][9]['max'] }}  |
| {{ radarr['quality-size']['movie']['qualities'][10]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][10]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][10]['max'] }} |
| {{ radarr['quality-size']['movie']['qualities'][11]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][11]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][11]['max'] }} |
| {{ radarr['quality-size']['movie']['qualities'][12]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][12]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][12]['max'] }} |
| {{ radarr['quality-size']['movie']['qualities'][13]['quality'] }} | {{ radarr['quality-size']['movie']['qualities'][13]['min'] }} | {{ radarr['quality-size']['movie']['qualities'][13]['max'] }} |

!!! note
    The reason why you don't see the `Preferred` score in the table above is because we want max quality anyway. So set it as high as possible.

    The highest preferred quality you can manually enter is 1 less than the Maximum quality. If you use the slider, the preferred quality can be up to 5 lesser than the Maximum quality.

    Make sure you have enabled 'Show Advanced' in Radarr, if you don't see a provision to enter the scores, under the Quality settings.

{! include-markdown "../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
