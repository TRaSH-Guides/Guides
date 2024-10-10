### Getting the right Language Profile

- **Want Original with subs**, or **VOSTFR**: You only want `Original` audio (`English`, `Spanish`, `Korean`, etc.) and `French` subs.
- **Want MULTi but will take French if not available**, or **MULTi.VF**: You want `Original` + `French` audios, with fallback to `French` audio.
- **Want MULTi but will take Original if not available**, or **MULTi.VO**: You want `Original` + `French` audios, with fallback to `Original` audio.

| Profile  | Both `Original` + `French` audio | Only `Original` Audio | Only `French` Audio | `English` Subs |   `French` Subs    |
|----------|:--------------------------------:|:---------------------:|:-------------------:|:--------------:|:------------------:|
| VOSTFR   |           :cross-mark:           |  :heavy_check_mark:   |    :cross-mark:     |   :warning:    | :heavy_check_mark: |
| MULTi.VF |        :heavy_check_mark:        |     :cross-mark:      | :heavy_check_mark:  |   :warning:    |     :warning:      |
| MULTi.VO |        :heavy_check_mark:        |  :heavy_check_mark:   |    :cross-mark:     |   :warning:    |     :warning:      |

:heavy_check_mark: What the profile is trying to get
:cross-mark: What the profile is trying to avoid
:warning: Not the main purpose of the profile but can happen

!!! tip "For the VOSTFR profile it is recommended to get Bazarr up and working"
    To do so follow the [Bazarr Setup Guide](/Bazarr/Setup-Guide). Bazarr will help you getting `French` subs when no VOSTFR releases are available.
