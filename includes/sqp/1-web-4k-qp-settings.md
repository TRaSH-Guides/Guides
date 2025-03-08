<!-- markdownlint-disable MD041-->
#### Quality Profile Settings

- **Enable:** `Upgrades Allowed`
- **Upgrade Until Quality:** `{{ radarr['quality-profiles']['sqp-1-web-2160p']['cutoff'] }}`
- **Minimum Custom Format Score:** `{{ radarr['quality-profiles']['sqp-1-web-2160p']['minFormatScore'] }}` <sup>(_1_)</sup>
- **Upgrade Until Custom Format Score:** `{{ radarr['quality-profiles']['sqp-1-web-2160p']['cutoffFormatScore'] }}`

!!! info "<sup>(_1_)</sup> If you're limited to public indexers, or are searching for content that is more rare, you might want to lower the `Minimum Custom Format Score` to 10."
<!--
??? success "example - [Click to show/hide]"

    ![!Quality Profile Settings](/SQP/images/1-web-qp-settings.png)

    !!! warning

        These screenshots are merely examples to demonstrate how it should look and where to place the data you need to add, they don't always reflect the actual data and may not always be completely up-to-date with the information you need to add.

        - Always follow the data described in the guide.
        - If you have any questions or aren't sure, just click the chat badge to join the Discord channel where you can ask your questions directly.
-->
<!-- markdownlint-enable MD041-->
