# Replace copies with hardlinks

Have you recently switched to a setup that supports hardlinks and Instant Moves (Atomic-Moves), and would like to replace duplicate files with hardlinks?

If your Operating System supports it you could make use of [Jdupes](https://codeberg.org/jbruchon/jdupes).

## Usage

!!! info ""

    We won't cover every command :bangbang:

    If you want to know what else [Jdupes](https://codeberg.org/jbruchon/jdupes) can do please read the manual.

!!! tip

    This process can take a long time and a pretty big hit on your resources depending on the size of your library. We did notice the first time can take longer than the second time, this may be due to some sort of caching behavior on disk.

    - That's why we suggest doing it based on categories (Movies, TV, Music, etc).
    - We don't suggest using this on a cloud-based setup.

```bash
jdupes [options] DIR1 DIR2
```

Example: This will do a dry run and summarize at the end.

```bash
jdupes -rMX onlyext:mp4,mkv,avi "/mnt/user/data/torrents/movies/" "/mnt/user/data/media/movies"
```

!!! info "Folder paths should be changed to match what you're using in your setup"

Example: This will hard link all duplicate files without prompting.

```bash
jdupes -rLX onlyext:mp4,mkv,avi "/mnt/user/data/torrents/movies/" "/mnt/user/data/media/movies"
```

!!! info "Folder paths should be changed to match what you're using in your setup"

---

!!! bug "Windows allows a maximum of 1023 hard links per file"

!!! Warning "The `-Q` or `--quick` option only reads each file once, hashes it, and performs comparisons based solely on the hashes. There is a small but significant risk of a hash collision which is the purpose of the failsafe byte-for-byte comparison that this option explicitly bypasses. Do not use it on ANY data set for which any amount of data loss is unacceptable. You have been warned!"

{! include-markdown "../../includes/support.md" !}
