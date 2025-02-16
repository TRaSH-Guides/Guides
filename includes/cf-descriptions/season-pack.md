<!-- markdownlint-disable MD041-->
**Season Pack**<br>

!!! danger "This CF utilizes functionality only available starting in Sonarr v4.0.2.1262."

This Custom Format can be used to prefer or exclude season packs

- Give it a score of `10` if you prefer a season pack.
- Give it a score of `-10000` if you prefer to not download season packs.
- Utilizes the "Release Type" custom format condition added in v4.0.2.1262, Season Pack source status is now persistently stored alongside episodes.

!!! info

    - This Custom Format could previously result in download loops. The new "Release Type" custom format condition now prevents this undesired behavior. :bangbang:
    - This will upgrade your already downloaded single episodes :bangbang:
<!-- markdownlint-enable MD041-->
