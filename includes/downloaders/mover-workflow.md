<!-- markdownlint-disable MD041-->
## What the mover script does

1. Pause torrents in a specified age range that reside on your cache drive.
1. Run/Trigger the unRAID mover.
1. Resume the torrents after the unRaid mover has completed.

!!! tip

    - You cannot disable the mover from `Settings` => `Scheduler` => `Mover Settings`. So, you could set the mover to run once a month, and one minute after you run the script. The mover shouldn't run because it's already running.
    - If you're also using Mover Tuning, do not disable the mover running on a schedule; it could completely disable the mover.
    - It's recommended to use Mover Tuning, and if you do, make sure the `Move files that are greater than this many days old:` is set to the same number of days you have in the script.
<!-- markdownlint-enable MD041-->
