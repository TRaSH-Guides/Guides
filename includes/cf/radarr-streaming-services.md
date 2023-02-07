??? abstract "Streaming Services - [CLICK TO EXPAND]"
    | Custom Format                                                                             | Score                                      | Trash ID                                |
    | ----------------------------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------- |
    | [{{ radarr['cf']['amzn']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#amzn)   | 0                                          | {{ radarr['cf']['amzn']['trash_id'] }}  |
    | [{{ radarr['cf']['atvp']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#atvp)   | 0                                          | {{ radarr['cf']['atvp']['trash_id'] }}  |
    | [{{ radarr['cf']['bcore']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#bcore) | {{ radarr['cf']['bcore']['trash_score'] }} | {{ radarr['cf']['bcore']['trash_id'] }} |
    | [{{ radarr['cf']['dsnp']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#dsnp)   | 0                                          | {{ radarr['cf']['dsnp']['trash_id'] }}  |
    | [{{ radarr['cf']['hbo']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hbo)     | 0                                          | {{ radarr['cf']['hbo']['trash_id'] }}   |
    | [{{ radarr['cf']['hmax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hmax)   | 0                                          | {{ radarr['cf']['hmax']['trash_id'] }}  |
    | [{{ radarr['cf']['hulu']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hulu)   | 0                                          | {{ radarr['cf']['hulu']['trash_id'] }}  |
    | [{{ radarr['cf']['ma']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#ma)       | {{ radarr['cf']['ma']['trash_score'] }}    | {{ radarr['cf']['ma']['trash_id'] }}    |
    | [{{ radarr['cf']['nf']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#nf)       | 0                                          | {{ radarr['cf']['nf']['trash_id'] }}    |
    | [{{ radarr['cf']['pathe']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pathe) | 0                                          | {{ radarr['cf']['pathe']['trash_id'] }} |
    | [{{ radarr['cf']['pcok']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pcok)   | 0                                          | {{ radarr['cf']['pcok']['trash_id'] }}  |
    | [{{ radarr['cf']['pmtp']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#pmtp)   | 0                                          | {{ radarr['cf']['pmtp']['trash_id'] }}  |
    | [{{ radarr['cf']['stan']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#stan)   | 0                                          | {{ radarr['cf']['stan']['trash_id'] }}  |

    ------
    Breakdown and Why

    - These reason why these Custom Formats have a score of `0` is because they are mainly used for the naming scheme and other variables should decide for movies if a certain release if preferred.
    - `MA` is the only one with a score because of their higher bitrate and quality compared to other streaming services.
