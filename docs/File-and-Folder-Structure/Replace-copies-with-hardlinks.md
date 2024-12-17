# Replace copies with hardlinks

Have you recently switched to a setup that supports hardlinks and Instant Moves (Atomic-Moves), and would like to replace duplicated files with hardlinks?

If your Operating System supports it you could make use of [jdupes](https://codeberg.org/jbruchon/jdupes/releases).

The latest version's binaries are available for Windows at the link above. You can use a package manager, such as [homebrew](https://formulae.brew.sh/formula/jdupes), `apt`, or `pacman`, to install the latest available version for Mac or your flavor of Linux.

## Usage

!!! info ""

    We won't cover every command :bangbang:

    If you want to know what else [jdupes](https://codeberg.org/jbruchon/jdupes) can do please [read the usage manual](https://codeberg.org/jbruchon/jdupes#usage).

!!! tip

    This process can put a significantly large load on your system resources for an extended period of time depending on the size of your library. As duplicates are discovered, and hardlinks are made, the process becomes more efficient - as linked and different-sized files are not repeatedly checked against eachother. This leads to subsequent runs potentially finishing faster.

    To speed this process up _significantly_ more, you can leverage a hash database. This will store information about the files, including their signatures, across runs of `jdupes` - vastly increasing the speed at which runs are finished.

    Simply use the following additional option _BEFORE YOUR DIRECTORIES_ with a path that is always available and persistent:

        -y "/mnt/user/appdata/scripts/media_hash.db"

    - We don't suggest using `jdupes` on a cloud-based setup.

The following is a basic usage template:

```bash
jdupes [options] DIR1 DIR2
```

The example below will do a dry run and summarize at the end.
!!! info "Folder paths should be adjusted to match your directory structure"

=== "Without Hash Database"

    ```bash
    jdupes -rMX onlyext:mp4,mkv,avi "/mnt/user/data/torrents/movies/" "/mnt/user/data/media/movies"
    ```

=== "With Hash Database"

    ```bash
    jdupes -rMX onlyext:mp4,mkv,avi -y "/mnt/user/appdata/scripts/media_hash.db" "/mnt/user/data/torrents/movies/" "/mnt/user/data/media/movies"
    ```

---

The example below will hard link all duplicate files without prompting.
!!! info "Folder paths should be adjusted to match your directory structure"

=== "Without Hash Database"

    ```bash
    jdupes -rLX onlyext:mp4,mkv,avi "/mnt/user/data/torrents/movies/" "/mnt/user/data/media/movies"
    ```

=== "With Hash Database"

    ```bash
    jdupes -rLX onlyext:mp4,mkv,avi -y "/mnt/user/appdata/scripts/media_hash.db" "/mnt/user/data/torrents/movies/" "/mnt/user/data/media/movies"
    ```

---

!!! bug "Windows only allows a maximum of 1023 hard links per file"

!!! Warning "The `-Q` or `--quick` option only reads each file once, hashes it, and performs comparisons based solely on the hashes. There is a small but significant risk of a hash collision which is the purpose of the failsafe byte-for-byte comparison that this option explicitly bypasses. Do not use it on ANY data set for which any amount of data loss is unacceptable. You have been warned!"

--8<-- "includes/support.md"
