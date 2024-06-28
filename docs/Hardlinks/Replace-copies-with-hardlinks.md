# Replace copies with hardlinks

You recently switched to a proper setup that supports Hardlinks and Instant Moves (Atomic-Moves).

And you would like to replace copies with hardlinks ?

If your Operating System supports it you could make use of [Jdupes](https://codeberg.org/jbruchon/jdupes).

## Usage

!!! info ""

    We won't cover every command :bangbang:

    If you want to know what else [Jdupes](https://codeberg.org/jbruchon/jdupes) can do please read the manual.

!!! tip

    This process can take a long time and a pretty big hit on your resources depending on the size of your library. We did notice the first time can take longer than the second time, this may be due to some sort of caching behavior on disk.

    - That's why we suggest doing it based on categories (Movies, TV, Music etc).
    - We don't suggest using this on a cloud-based setup.

```bash
jdupes [options] DIR1 DIR2
```

This will do a dry run and summarize at the end.

```bash
jdupes -rMX onlyext:mp4,mkv,avi "/data/torrents/movies/" "/data/media/movies"
```

This will hard link all duplicate files without prompting.

```bash
jdupes -rLX onlyext:mp4,mkv,avi "/data/torrents/movies/" "/data/media/movies"
```

!!! bug ""

    Windows allows a maximum of 1023 hard links per file

!!! Warning

    The `-Q` or `--quick` option only reads each file once, hashes it, and performs comparisons based solely on the hashes. There is a small but significant risk of a hash collision which is the purpose of the failsafe byte-for-byte comparison that this option explicitly bypasses. Do not use it on ANY data set for which any amount of data loss is unacceptable. You have been warned!

{! include-markdown "../../includes/support.md" !}
