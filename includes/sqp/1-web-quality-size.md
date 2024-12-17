<!-- markdownlint-disable MD041 MD052-->
### Quality Size

`Settings` => `Quality`

| Quality                                                                  | Min                                                                  | Max                                                                  |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| {{ radarr['quality-size']['sqp-streaming']['qualities'][2]['quality'] }} | {{ radarr['quality-size']['sqp-streaming']['qualities'][2]['min'] }} | {{ radarr['quality-size']['sqp-streaming']['qualities'][2]['max'] }} |
| {{ radarr['quality-size']['sqp-streaming']['qualities'][3]['quality'] }} | {{ radarr['quality-size']['sqp-streaming']['qualities'][3]['min'] }} | {{ radarr['quality-size']['sqp-streaming']['qualities'][3]['max'] }} |
| {{ radarr['quality-size']['sqp-streaming']['qualities'][5]['quality'] }} | {{ radarr['quality-size']['sqp-streaming']['qualities'][5]['min'] }} | {{ radarr['quality-size']['sqp-streaming']['qualities'][5]['max'] }} |

The reason why you don't see the `Preferred` score in the table above is because we want max quality anyway. So set it as high as possible.

The highest preferred quality you can manually enter is 1 less than the Maximum quality. If you use the slider, the preferred quality can be up to 5 lesser than the Maximum quality.

Make sure you have enabled `Show Advanced` in Radarr, if you don't see a provision to enter the scores, under the Quality settings.
<!-- markdownlint-enable MD041 MD052-->
