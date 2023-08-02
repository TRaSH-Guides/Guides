??? abstract "Movie Versions - [Click to show/hide]"
    | Custom Format                                                                                                           |                                 Score                                 | Trash ID                                               |
    | ----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------: | ------------------------------------------------------ |
    | [{{ radarr['cf']['hybrid']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hybrid)                             |        {{ radarr['cf']['hybrid']['trash_scores']['default'] }}        | {{ radarr['cf']['hybrid']['trash_id'] }}               |
    | [{{ radarr['cf']['remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remaster)                         |       {{ radarr['cf']['remaster']['trash_scores']['default'] }}       | {{ radarr['cf']['remaster']['trash_id'] }}             |
    | [{{ radarr['cf']['4k-remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#4k-remaster)                   |     {{ radarr['cf']['4k-remaster']['trash_scores']['default'] }}      | {{ radarr['cf']['4k-remaster']['trash_id'] }}          |
    | [{{ radarr['cf']['criterion-collection']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#criterion-collection) | {{ radarr['cf']['criterion-collection']['trash_scores']['default'] }} | {{ radarr['cf']['criterion-collection']['trash_id'] }} |
    | [{{ radarr['cf']['masters-of-cinema']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#masters-of-cinema)       |  {{ radarr['cf']['masters-of-cinema']['trash_scores']['default'] }}   | {{ radarr['cf']['masters-of-cinema']['trash_id'] }}    |
    | [{{ radarr['cf']['vinegar-syndrome']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#vinegar-syndrome)         |   {{ radarr['cf']['vinegar-syndrome']['trash_scores']['default'] }}   | {{ radarr['cf']['vinegar-syndrome']['trash_id'] }}     |
    | [{{ radarr['cf']['special-edition']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#special-edition)           |   {{ radarr['cf']['special-edition']['trash_scores']['default'] }}    | {{ radarr['cf']['special-edition']['trash_id'] }}      |
    | [{{ radarr['cf']['imax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax)                                 |         {{ radarr['cf']['imax']['trash_scores']['default'] }}         | {{ radarr['cf']['imax']['trash_id'] }}                 |
    | [{{ radarr['cf']['imax-enhanced']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax-enhanced)               |    {{ radarr['cf']['imax-enhanced']['trash_scores']['default'] }}     | {{ radarr['cf']['imax-enhanced']['trash_id'] }}        |

    !!! tip "{{ radarr['cf']['imax-enhanced']['name'] }}"
        {{ radarr['cf']['imax-enhanced']['name'] }}: Get More Picture Instead of Black Bars.

        {{ radarr['cf']['imax-enhanced']['name'] }} exclusive expanded aspect ratio is 1:90:1, which offers up to 26% more picture for select sequences, meaning more of the action is visible on screen.

        If you don't prefer `{{ radarr['cf']['imax-enhanced']['name'] }}` then don't add it or use a score of `0`
