??? summary "Movie Versions - [CLICK TO EXPAND]"
    | Custom Format                                                                                                     | Score                                               | Trash ID                                         |
    | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ |
    | [{{ radarr['hybrid']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#hybrid)                             | {{ radarr['hybrid']['trash_score'] }}               | {{ radarr['hybrid']['trash_id'] }}               |
    | [{{ radarr['remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#remaster)                         | {{ radarr['remaster']['trash_score'] }}             | {{ radarr['remaster']['trash_id'] }}             |
    | [{{ radarr['4k-remaster']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#4k-remaster)                   | {{ radarr['4k-remaster']['trash_score'] }}          | {{ radarr['4k-remaster']['trash_id'] }}          |
    | [{{ radarr['criterion-collection']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#criterion-collection) | {{ radarr['criterion-collection']['trash_score'] }} | {{ radarr['criterion-collection']['trash_id'] }} |
    | [{{ radarr['special-edition']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#special-edition)           | {{ radarr['special-edition']['trash_score'] }}      | {{ radarr['special-edition']['trash_id'] }}      |
    | [{{ radarr['imax']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax)                                 | {{ radarr['imax']['trash_score'] }}                 | {{ radarr['imax']['trash_id'] }}                 |
    | [{{ radarr['imax-enhanced']['name'] }}](/Radarr/Radarr-collection-of-custom-formats/#imax-enhanced)               | {{ radarr['imax-enhanced']['trash_score'] }}        | {{ radarr['imax-enhanced']['trash_id'] }}        |

    !!! tip "{{ radarr['imax-enhanced']['name'] }}"
        {{ radarr['imax-enhanced']['name'] }}: Get More Picture Instead of Black Bars.

        {{ radarr['imax-enhanced']['name'] }} exclusive expanded aspect ratio is 1:90:1, which offers up to 26% more picture for select sequences, meaning more of the action is visible on screen.

        If you don't prefer `{{ radarr['imax-enhanced']['name'] }}` then don't add it or use a score of `0`
