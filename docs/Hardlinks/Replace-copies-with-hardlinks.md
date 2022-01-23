# Replace copies with hardlinks

You recently switched to a proper setup that supports Hardlinks and Instant Moves (Atomic-Moves).

And you would like to replace copies with hardlinks ?

If your Operating System supports it you could make use of [Jdupes](https://github.com/jbruchon/jdupes).

## Usage

!!! info ""
    I won't cover every command :bangbang:

    If you want to know what else [Jdupes](https://github.com/jbruchon/jdupes) can do please read the manual.

!!! tip
    This process can take a long time and a pretty big hit on your resources depending on how big your library is, I did notice the first time it takes longer then the second time. Not sure if this is a cache thing or something else.

    - That's why I suggest to do it based on categories (Movies, TV, Music etc).
    - I don't suggest to use this on a cloud based setup.

```bash
jdupes [options] DIR1 DIR2
```

This will print matches and --summarize at the end

```bash
jdupes -M -r "/data/torrents/movies/" "/data/media/movies"
```

This will hard link all duplicate files without prompting.

```bash
jdupes -L -r "/data/torrents/movies/" "/data/media/movies"
```

!!! bug ""
    Windows allows a maximum of 1023 hard links per file

!!! Warning
    The `-Q` or `--quick` option only reads each file once, hashes it, and performs comparisons based solely on the hashes. There is a small but significant risk of a hash collision which is the purpose of the failsafe byte-for-byte comparison that this option explicitly bypasses. Do not use it on ANY data set for which any amount of data loss is unacceptable. You have been warned!

--8<-- "includes/support.md"
