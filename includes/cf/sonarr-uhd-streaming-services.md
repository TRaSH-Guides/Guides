<!-- markdownlint-disable MD041-->
??? abstract "General Streaming Services (UHD) - [Click to show/hide]"

    | Custom Format                                                                                                                   |                                Score                                 | Trash ID                                              |
    | ------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------: | ----------------------------------------------------- |
    | [{{ sonarr['cf']['amzn']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#amzn)                                         |        {{ sonarr['cf']['amzn']['trash_scores']['default'] }}         | {{ sonarr['cf']['amzn']['trash_id'] }}                |
    | [{{ sonarr['cf']['atvp']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#atvp)                                         |        {{ sonarr['cf']['atvp']['trash_scores']['default'] }}         | {{ sonarr['cf']['atvp']['trash_id'] }}                |
    | [{{ sonarr['cf']['cc']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#cc)                                             |         {{ sonarr['cf']['cc']['trash_scores']['default'] }}          | {{ sonarr['cf']['cc']['trash_id'] }}                  |
    | [{{ sonarr['cf']['dcu']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dcu)                                           |         {{ sonarr['cf']['dcu']['trash_scores']['default'] }}         | {{ sonarr['cf']['dcu']['trash_id'] }}                 |
    | [{{ sonarr['cf']['dsnp']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#dsnp)                                         |        {{ sonarr['cf']['dsnp']['trash_scores']['default'] }}         | {{ sonarr['cf']['dsnp']['trash_id'] }}                |
    | [{{ sonarr['cf']['hmax']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hmax)                                         |        {{ sonarr['cf']['hmax']['trash_scores']['default'] }}         | {{ sonarr['cf']['hmax']['trash_id'] }}                |
    | [{{ sonarr['cf']['hbo']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hbo)                                           |         {{ sonarr['cf']['hbo']['trash_scores']['default'] }}         | {{ sonarr['cf']['hbo']['trash_id'] }}                 |
    | [{{ sonarr['cf']['hulu']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#hulu)                                         |        {{ sonarr['cf']['hulu']['trash_scores']['default'] }}         | {{ sonarr['cf']['hulu']['trash_id'] }}                |
    | [{{ sonarr['cf']['it']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#it)                                             |         {{ sonarr['cf']['it']['trash_scores']['default'] }}          | {{ sonarr['cf']['it']['trash_id'] }}                  |
    | [{{ sonarr['cf']['max']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#max)                                           |         {{ sonarr['cf']['max']['trash_scores']['default'] }}         | {{ sonarr['cf']['max']['trash_id'] }}                 |
    | [{{ sonarr['cf']['nf']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#nf)                                             |         {{ sonarr['cf']['nf']['trash_scores']['default'] }}          | {{ sonarr['cf']['nf']['trash_id'] }}                  |
    | [{{ sonarr['cf']['pmtp']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#pmtp)                                         |        {{ sonarr['cf']['pmtp']['trash_scores']['default'] }}         | {{ sonarr['cf']['pmtp']['trash_id'] }}                |
    | [{{ sonarr['cf']['pcok']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#pcok)                                         |        {{ sonarr['cf']['pcok']['trash_scores']['default'] }}         | {{ sonarr['cf']['pcok']['trash_id'] }}                |
    | [{{ sonarr['cf']['sho']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#sho)                                           |         {{ sonarr['cf']['sho']['trash_scores']['default'] }}         | {{ sonarr['cf']['sho']['trash_id'] }}                 |
    | [{{ sonarr['cf']['stan']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#stan)                                         |        {{ sonarr['cf']['stan']['trash_scores']['default'] }}         | {{ sonarr['cf']['stan']['trash_id'] }}                |
    | [{{ sonarr['cf']['syfy']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#syfy)                                         |  {{ sonarr['cf']['syfy']['trash_scores']['default'] }}         | {{ sonarr['cf']['syfy']['trash_id'] }}                |
    | :warning: [{{ sonarr['cf']['uhd-streaming-boost']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#uhd-streaming-boost) | {{ sonarr['cf']['uhd-streaming-boost']['trash_scores']['default'] }} | {{ sonarr['cf']['uhd-streaming-boost']['trash_id'] }} |
    | :warning: [{{ sonarr['cf']['uhd-streaming-cut']['name'] }}](/Sonarr/sonarr-collection-of-custom-formats/#uhd-streaming-cut)     |  {{ sonarr['cf']['uhd-streaming-cut']['trash_scores']['default'] }}  | {{ sonarr['cf']['uhd-streaming-cut']['trash_id'] }}   |

    !!! warning "UHD Streaming Boost and UHD Streaming Cut Custom Formats"

    Some streaming services have UHD releases that are generally better or worse than their HD counterparts. The UHD Streaming Boost and UHD Streaming Cut custom formats adjust those streaming services' scores appropriately for UHD releases.

    These two custom formats must be included in your profile for UHD releases to be scored correctly.
<!-- markdownlint-enable MD041-->
