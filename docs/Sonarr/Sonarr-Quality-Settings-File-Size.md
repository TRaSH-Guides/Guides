# Quality Settings (File Size)

I often get the question "What's the best quality settings to use?"
Well, it's actually personal preference so I will show you my recommendations.

But before you continue to read, as with all my guides:

!!! danger ""
    **If you don't care about quality then stop reading and see if the other tutorials are helpful for you.**

These Quality Settings have been created and tested with info I got from others, and release comparisons from different sources.

I only do WEB-DL myself for TV shows because in my opinion WEB-DL is the sweet spot between quality and size and you often don't see big differences anyway for TV shows. (Except for shows like GOT, Vikings, etc)

??? question "FAQ"

    ## FAQ

    **Q: Why do you only show starting from HDTV720p?**

    A: With the big screens these days anything lower doesn't look watchable

    **Q: Why do you have some sizes set so high?**

    A: You probably didn't read the bold text above, I also need to keep in mind usenet releases that are often bigger than torrent releases.

    **Q: You noticed that some episodes don't grab because of these settings.**

    A: If you notice that some episodes won't be grabbed because of these size settings you can provide me a proof with a screenshot and the error it shows you when you do a interactive search (non redacted except the indexer/tracker if you want to).

    - I will only accept changes that are international releases. No multi, or dubbed language releases.
    - I won't accept mislabeled source releases like from MeGusta etc. (They should learn to name their stuff properly first)
    - I won't accept changes for micro sized releases.
    - Documentaries and cartoons are often much smaller so I probably won't edit those either.

------

## Sonarr Quality Definitions

| Quality                                                            | Minimum (Megabytes Per Minute)                                 | Maximum (Megabytes Per Minute)                                 |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------- |
| {{ sonarr['quality-size']['series']['qualities'][0]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][0]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][0]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][1]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][1]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][1]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][2]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][2]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][2]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][3]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][3]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][3]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][4]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][4]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][4]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][5]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][5]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][5]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][6]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][6]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][6]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][7]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][7]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][7]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][8]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][8]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][8]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][9]['quality'] }}  | {{ sonarr['quality-size']['series']['qualities'][9]['min'] }}  | {{ sonarr['quality-size']['series']['qualities'][9]['max'] }}  |
| {{ sonarr['quality-size']['series']['qualities'][10]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][10]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][10]['max'] }} |
| {{ sonarr['quality-size']['series']['qualities'][11]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][11]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][11]['max'] }} |
| {{ sonarr['quality-size']['series']['qualities'][12]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][12]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][12]['max'] }} |
| {{ sonarr['quality-size']['series']['qualities'][13]['quality'] }} | {{ sonarr['quality-size']['series']['qualities'][13]['min'] }} | {{ sonarr['quality-size']['series']['qualities'][13]['max'] }} |

------

### Sonarr Quality Definitions - Anime

| Quality                                                           | Minimum (Megabytes Per Minute)                                | Maximum (Megabytes Per Minute)                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| {{ sonarr['quality-size']['anime']['qualities'][0]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][0]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][0]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][1]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][1]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][1]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][2]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][2]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][2]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][3]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][3]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][3]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][4]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][4]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][4]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][5]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][5]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][5]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][6]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][6]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][6]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][7]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][7]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][7]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][8]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][8]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][8]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][9]['quality'] }}  | {{ sonarr['quality-size']['anime']['qualities'][9]['min'] }}  | {{ sonarr['quality-size']['anime']['qualities'][9]['max'] }}  |
| {{ sonarr['quality-size']['anime']['qualities'][10]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][10]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][10]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][11]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][11]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][11]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][12]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][12]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][12]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][13]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][13]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][13]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][14]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][14]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][14]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][15]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][15]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][15]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][16]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][16]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][16]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][17]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][17]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][17]['max'] }} |
| {{ sonarr['quality-size']['anime']['qualities'][18]['quality'] }} | {{ sonarr['quality-size']['anime']['qualities'][18]['min'] }} | {{ sonarr['quality-size']['anime']['qualities'][18]['max'] }} |

!!! note
    The reason why you don't see the `Preferred` score in the table above is because we want max quality anyway. So set it as high as possible.

    The highest preferred quality you can manually enter is 1 less than the Maximum quality. If you use the slider, the preferred quality can be up to 5 lesser than the Maximum quality.

    Make sure you have enabled 'Show Advanced' in Sonarr, if you don't see a provision to enter the scores, under the Quality settings.

--8<-- "includes/support.md"
