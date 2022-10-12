### Quality Size

`Settings` => `Quality`

| Quality                                                            | Min                                                            | Max                                                            |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------- |
| {{ radarr['quality-size']['sqp-uhd']['qualities'][0]['quality'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][0]['min'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][0]['max'] }} |
| {{ radarr['quality-size']['sqp-uhd']['qualities'][1]['quality'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][1]['min'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][1]['max'] }} |
| {{ radarr['quality-size']['sqp-uhd']['qualities'][2]['quality'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][2]['min'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][2]['max'] }} |
| {{ radarr['quality-size']['sqp-uhd']['qualities'][4]['quality'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][4]['min'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][4]['max'] }} |
| {{ radarr['quality-size']['sqp-uhd']['qualities'][5]['quality'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][5]['min'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][5]['max'] }} |
| {{ radarr['quality-size']['sqp-uhd']['qualities'][6]['quality'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][6]['min'] }} | {{ radarr['quality-size']['sqp-uhd']['qualities'][6]['max'] }} |

The reason why you don't see the `Preferred` score in the table above is because we want max quality anyway. So set it as high as possible.

The highest preferred quality you can manually enter is 1 less than the Maximum quality. If you use the slider, the preferred quality can be up to 5 lesser than the Maximum quality.

Make sure you have enabled `Show Advanced` in Radarr, if you don't see a provision to enter the scores, under the Quality settings.
