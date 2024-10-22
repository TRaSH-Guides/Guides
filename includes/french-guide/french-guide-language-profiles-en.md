### Getting the Right Language Profile

- **Want Original with subs**, or **VOSTFR**: You only want `Original` audio (`English`, `Spanish`, `Korean`, etc.) and `French` subtitles.
- **Want MULTi but will take French if not available**, or **MULTi.VF**: You want `Original` + `French` audio tracks, with a fallback to `French` audio if both are not available.
- **Want MULTi but will take Original if not available**, or **MULTi.VO**: You want `Original` + `French` audio tracks, with a fallback to `Original` audio if both are not available..

| Profile  | Both `Original` + `French` audio | Only `Original` Audio | Only `French` Audio | `English` Subs |   `French` Subs    |
|----------|:--------------------------------:|:---------------------:|:-------------------:|:--------------:|:------------------:|
| VOSTFR   |           :cross-mark:           |  :heavy_check_mark:   |    :cross-mark:     |   :warning:    | :heavy_check_mark: |
| MULTi.VF |        :heavy_check_mark:        |     :cross-mark:      | :heavy_check_mark:  |   :warning:    |     :warning:      |
| MULTi.VO |        :heavy_check_mark:        |  :heavy_check_mark:   |    :cross-mark:     |   :warning:    |     :warning:      |

:heavy_check_mark: What the profile is trying to get
:cross-mark: What the profile is trying to avoid
:warning: Not the main purpose of the profile but can happen

!!! tip "For the VOSTFR profile, it is recommended to get Bazarr up and running"
    To do so, follow the [Bazarr Setup Guide](/Bazarr/Setup-Guide). Bazarr will help you get `French` subtitles when no VOSTFR releases are available.
