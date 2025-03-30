# NZBGet - Basic Setup

{! include-markdown "../../../includes/downloaders/basic-setup.md" !}

---

## Read This First

!!! note "Settings that aren't covered mean you can change them to your liking or simply leave them at default."

{! include-markdown "../../../includes/guides/screenshots-are-examples-warning.md" !}

---

## Paths

`Settings` => `PATHS`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

| Name         | Description                                 |
| :----------- | :------------------------------------------ |
| `${MainDir}` | Root directory for all tasks.               |
| `${AppDir}`  | Where NZBGet is installed.                  |
| `${DestDir}` | Destination directory for downloaded files. |

![!paths](images/paths.png)

### MainDir

Root directory for all tasks.

!!! success ""

    **Suggested:** If you use docker this should be set to `/config`.

### DestDir

Destination directory for downloaded files.

!!! success ""

    **Suggested:** `/data/usenet`.

### InterDir

Directory to store intermediate/temporary files.

*If this option is set (not empty) the files are downloaded into this directory first. After successful download of nzb-file (possibly after par-repair) the files are moved to destination directory (option DestDir). If download or unpack fail the files remain in intermediate directory.*

!!! success ""

    **Suggested:** `/data/usenet/intermediate` or `/data/usenet/incomplete`.

### NzbDir

Directory for incoming nzb-files.

!!! success ""

    **Suggested:** `Default`.

### QueueDir

Directory to store program state.

*This directory is used to save download queue, history, information about fetched RSS feeds, statistics, etc.*

!!! success ""

    **Suggested:** `Default`.

### ScriptDir

Directory with post-processing and other scripts.

!!! success ""

    **Suggested:** `Default`.

---

## News-Servers

`Settings` => `NEWS-SERVERS`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!newsservers](images/newsservers.png)

### ServerX.Active

Enable this news server.

!!! success ""

    **Suggested:** `Yes`.

### ServerX.Name

Name of your news server.

*The name is used in UI and for logging.*

!!! success ""

    **Suggested:** Your news server name.

### ServerX.Level

Level (priority) of your news server.

!!! success ""

    **Suggested:** Put your major download servers at level `0` and your fill servers at levels `1`, `2`, etc..

### ServerX.Optional

This is an optional non-reliable server.

*Marking server as optional tells NZBGet to ignore this server if a connection to this server cannot be established.*

!!! success ""

    **Suggested:** `No`

!!! info "Only switch to `Yes` if this news server is a non-reliable server."

### ServerX.Host

Host name of news server.

!!! success ""

    **Suggested:** The host name of your news server.

### ServerX.Encryption

Encrypted server connection (TLS/SSL).

*By changing this option you should also change the option Port accordingly because unsecure and encrypted connections use different ports.*

!!! success ""

    **Suggested:** `Yes`.

### ServerX.Port

News Server port

- `563` for a secure connection.
- `119` for an unsecured connection.

!!! success ""

    **Suggested:** Any secure port that your news server offers.

### ServerX.Username

User name to use for authentication.

!!! success ""

    **Suggested:** Your news server User name that is used for authentication.

### ServerX.Password

Password to use for authentication.

!!! success ""

    **Suggested:** Your news server Password that is used for authentication.

### ServerX.Connections

Maximum number of simultaneous connections to this server.

!!! success ""

    **Suggested:** Use the lowest possible number of connections to reach your max download speed `+1` connection.

### ServerX.Retention

Server retention time.

*How long the articles are stored on the news server.*

!!! success ""

    **Suggested:** Check your news server what their retention is.

---

## Categories

`Settings` => `CATEGORIES`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!categories](images/categories.png)

### CategoryX.Name

Category name.

!!! success ""

    **Suggested:** This should match what you use in Sonarr/Radarr categories (`tv`, `movies`, etc).

### Category1.DestDir

Destination directory for this category.

!!! success ""

    **Suggested:**

    - `${DestDir}/movies` for Radarr.
    - `${DestDir}/tv` for Sonarr.

{! include-markdown "../../../includes/downloaders/warning-path-location.md" !}

### CategoryX.Unpack

Unpack downloaded nzb-files.

!!! success ""

    **Suggested:** `Yes``.

### CategoryX.Extensions

List of extension scripts for this category.

!!! success ""

    **Suggested:** Depends if you need to run an extension script.

---

## Incoming Nzbs

`Settings` => `INCOMING NZBS`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!incoming](images/incoming.png)

### AppendCategoryDir

Create subdirectory with category-name in destination-directory.

!!! success ""

    **Suggested:** `Yes`.

### DupeCheck

Check for duplicate titles.

!!! success ""

    **Suggested:** `Yes`.

### Download Queue

`Settings` => `DOWNLOAD QUEUE`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!queue](images/queue.png)

### FlushQueue

Flush download queue to disk.

!!! success ""

    **Suggested:** `Yes`.

!!! tip
    You can disable this option if it negatively affects disk performance on your system. You should create backups of queue-directory (option QueueDir) in that case. Keep the option enabled if your system often crashes.

### ContinuePartial

Continue download of partially downloaded files.

!!! success ""

    **Suggested:** `Yes`.

!!! tip
    Disabling this option may slightly reduce disk access and is therefore recommended on fast connections.

### ArticleCache

Memory limit for article cache.

!!! success ""

    **Suggested:** `500`.

### DirectWrite

Write decoded articles directly into destination output file.

!!! success ""

    **Suggested:** `Yes`.

### WriteBuffer

Memory limit for per connection write buffer.

!!! success ""

    **Suggested:** `1024`.

!!! warning "If you're running low on memory, avoid setting this value too high."

### FileNaming

How to name downloaded files.

!!! success ""

    **Suggested:** `Auto`.

!!! info
    - `Article` - use file names stored in article metadata.
    - `Nzb` - use file names as defined in nzb-file.
    - `Auto` - prefer names from article metadata for obfuscated files use names from nzb-file.

### RenameAfterUnpack

Rename downloaded files after unpack.

*This option renames the extracted and obfuscated files using the NZB filename.*

!!! success ""

    **Suggested:** `Yes`.

### ReorderFiles

Reorder files within nzbs for optimal download order.

!!! success ""

    **Suggested:** `Yes`.

### PostStrategy

Post-processing strategy.

*Computer resources are in heavy demand when post-processing with simultaneous tasks - make sure the hardware is capable.*

!!! success ""

    **Suggested:** `Balanced`.

!!! info

    - `Balanced` - items that do not need par repair are post processed one at a time while par repair tasks may also run simultaneously one after another at the same time. This means that a post process par repair will not prevent another task from running, but at a cost of using more computer resource
    - `Aggressive` - will simultaneously post process up to three items including one par repair task
    - `Rocket` - will simultaneously post process up to six items including one or two par repair tasks.

### NzbCleanupDisk

Delete source nzb-file when it is not needed anymore.

!!! success ""

    **Suggested:** `Yes`.

---

## Check and Repair

`Settings` => `CHECK AND REPAIR`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!checkAndRepair](images/checkAndRepair.png)

### CrcCheck

Check CRC of downloaded and decoded articles.

Normally this option should be enabled for better detecting of download errors and for quick par-verification (option ParQuick).

!!! success ""

    **Suggested:** `Yes`.

!!! tip
    Setting this option to `No` could speed up your download and post-processing time.

### ParCheck

Whether and how par-verification must be performed.

!!! success ""

    **Suggested:** `Auto`.

!!! info
    - Auto - par-check is performed when needed. One par2-file is always downloaded. Additional par2-files are downloaded if needed for repair. Repair is performed if the option ParRepair is enabled
    - Always - check every download (even undamaged). One par2-file is always downloaded. Additional par2-files are downloaded if needed for repair. Repair is performed if the option ParRepair is enabled
    - Force - force par-check for every download (even undamaged). All par2-files are always downloaded. Repair is performed if the option ParRepair is enabled
    - Manual - par-check is skipped. One par2-file is always downloaded. If a damaged download is detected, all par2-files are downloaded but neither par-check nor par-repair take place. The download can be then repaired manually, eventually on another faster computer.

### ParRepair

Automatic par-repair after par-verification.

*If option ParCheck is set to "Auto" or "Force" this option defines if the download must be repaired when needed. The option can be disabled if a computer does not have enough CPU power, since repairing may consume too many resources and time on a slow computer.*

!!! success ""

    **Suggested:** `Yes`.

### ParScan

What files should be scanned during par-verification.

!!! success ""

    **Suggested:** `Extended`.

!!! info
    - Limited - scan only files belonging to par-set
    - Extended - scan files belonging to par-set first, scan other files until all missing files are found
    - Full - scan all files in destination directory. Can be very time consuming but may sometimes repair where Limited and Extended fail
    - Dupe - scan files belonging to par-set first, scan other files until repair is possible. Even files from other duplicate-downloads are scanned. Can be very time consuming but brings best results.

### ParQuick

Quick file verification during par-check.

*If the option is active the files are quickly verified using checksums calculated during download quick verification is very fast because it doesn't require the reading of files from disk, NZBGet knows checksums of downloaded files and quickly compares them with checksums stored in the par-file.*

!!! success ""

    **Suggested:** `Yes`.

!!! info "If the option is disabled the files are verified as usual. That's slow. Use this if the quick verification doesn't work properly."

### ParBuffer

Memory limit for par-repair buffer.

*Set the amount of RAM that the par-checker may use during repair. Having the buffer as big as the total size of all damaged blocks allows for the optimal repair speed. The option sets the maximum buffer size, the allocated buffer can be smaller.*

!!! success ""

    **Suggested:** `500`.

!!! tip
    - If you have a lot of RAM set the option to few hundreds (MB) for the best repair performance
    - If you're running low on memory, avoid setting this value too high.

### ParThreads

Number of threads to use during par-repair.

*On multi-core CPUs for the best speed set the option to the number of logical cores (physical cores + hyper-threading units). If you want to utilize the CPU to 100% you may need to add one or two additional threads to compensate for wait intervals used for thread synchronization.*

!!! success ""

    **Suggested:** Half of your logical cores are on your server, so it doesn't interfere with other processes on your server, such as video playback.

!!! info
    - On single-core CPUs use only one thread.
    - Set to `0` to automatically use all available CPU cores (may not work on old or exotic platforms).

!!! warning "Par2 repair can be very resource intensive, and it could slow down your system performance and even interfere with video playback"

### ParRename

Check for renamed and missing files using par-files.

*Par-rename restores original file names using information stored in par2-files. It also detects missing files (files listed in par2-files but not present on disk). When enabled the par-rename is performed as the first step of post-processing for every nzb-file.*

!!! success ""

    **Suggested:** `Yes`.

### RarRename

Check for renamed rar-files.

*Rar-rename restores original file names using information stored in rar-files. When enabled the rar-rename is performed as one of the first steps of post-processing for every nzb-file.*

*Rar-rename is useful for downloads not having par2-files or for downloads those files were renamed before creating par2-files. In both cases par-rename (option ParRename) can't rename files and the rar-rename makes it possible to unpack downloads which would fail otherwise.*

!!! success ""

    **Suggested:** `Yes`.

### DirectRename

Directly rename files during downloading.

*This is similar to par-renaming (option ParRename) but the files are renamed during downloading instead of post-processing stage. This requires some tricky handling of files and works only for healthy downloads.*

!!! success ""

    **Suggested:** `Yes`.

### HealthCheck

What to do if download health drops below critical health.

!!! success ""

    **Suggested:** `Delete`.

!!! info
    - Delete - delete nzb-file from queue, also delete already downloaded files
    - Park - move nzb-file to history, keep already downloaded files. Commands "Download remaining files" and "Retry failed articles" are available for this nzb
    - Pause - pause nzb-file
    - None - do nothing (continue download).

!!! tip "For automatic duplicate handling option must be set to `Delete`, `Park` or `None`. If it is set to "Pause" you will need to manually move another duplicate from history to queue. See also option DupeCheck."

### ParTimeLimit

Maximum allowed time for par-repair.

*If you use NZBGet on a very slow computer like NAS-device, it may be good to limit the time allowed for par-repair. NZBGet calculates the estimated time required for par-repair. If the estimated value exceeds the limit defined here, NZBGet cancels the repair.*

!!! success ""

    **Suggested:** `0`.

!!! info "Value `0` means unlimited."

### ParPauseQueue

Pause download queue during check/repair.

*Enable the option to give CPU more time for par-check/repair. That helps to speed up check/repair on slow CPUs with fast connection (e.g. NAS-devices).*

!!! success ""

    **Suggested:** `Yes`.

---

## Unpack

`Settings` => `UNPACK`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!unpack](images/unpack.png)

Pause download queue during check/repair.

*Enable the option to give CPU more time for par-check/repair. That helps to speed up check/repair on slow CPUs with fast connection (e.g. NAS-devices).*

### Unpack (Global)

Unpack downloaded nzb-files.

!!! success ""

    **Suggested:** `Yes`.

### DirectUnpack

Directly unpack files during downloading.

*When active the files are unpacked during downloading instead of post-processing stage. This works only for healthy downloads. Damaged downloads are unpacked as usual during post-processing stage after par-repair.*

!!! success ""

    **Suggested:** `Yes`.

!!! info
    - This option requires unpack to be enabled in general via option Unpack.
    - For best results also activate option DirectRename and option ReorderFiles.

!!! warning "`DirectUnpack` might lower your download speed but the overall time could be faster. (disable on low-powered devices)"

### UnpackPauseQueue

Pause download queue during unpack.

*Enable the option to give CPU more time for unpacking. That helps to speed up unpacking on slow CPUs.*

!!! success ""

    **Suggested:** `Yes`.

### UnpackCleanupDisk

Delete archive files after successful unpacking.

!!! success ""

    **Suggested:** `Yes`.

### UnrarCmd

Full path to unrar executable.

*The option can also contain extra switches to pass to unrar.*

### ExtCleanupDisk

Files to delete after successful download.

### UnpackIgnoreExt

Files to ignore during unpack.

#### Prevent unwanted extensions

!!! info "The Starr apps focus solely on media files and typically ignore all those extensions."

Add these extensions (*primarily for Windows users as they could potentially be abused or exploited*) to your `UnpackIgnoreExt`.

```none
ade, adp, app, application, appref-ms, asp, aspx, asx, bas, bat, bgi, cab, cer, chm, cmd, cnt, com, cpl, crt, csh, der, diagcab, exe, fxp, gadget, grp, hlp, hpj, hta, htc, inf, ins, iso, isp, its, jar, jnlp, js, jse, ksh, lnk, mad, maf, mag, mam, maq, mar, mas, mat, mau, mav, maw, mcf, mda, mdb, mde, mdt, mdw, mdz, msc, msh, msh1, msh2, mshxml, msh1xml, msh2xml, msi, msp, mst, msu, ops, osd, pcd, pif, pl, plg, prf, prg, printerexport, ps1, ps1xml, ps2, ps2xml, psc1, psc2, psd1, psdm1, pst, py, pyc, pyo, pyw, pyz, pyzw, reg, scf, scr, sct, shb, shs, theme, tmp, url, vb, vbe, vbp, vbs, vhd, vhdx, vsmacros, vsw, webpnp, website, ws, wsc, wsf, wsh, xbap, xll, xnk
```

!!! tip "If you are using NZBGet to download games and apps, this list shouldn't be used. You can either create a separate category, set it to download only, and manually extract the files, or use a separate app or instance for them."

---

## Extension Scripts

`Settings` => `EXTENSION SCRIPTS`

We will only cover the so-called most important and common settings. For the other settings, please refer to the descriptions provided in the application.

![!extScripts](images/extScripts.png)

### Extensions

List of active extension scripts for new downloads.

### ScriptOrder

Execution order for extension scripts.

### ScriptPauseQueue

Pause download queue during executing of postprocess-script

*Enable the option to give CPU more time for postprocess-script. That helps to speed up postprocess on slow CPUs with fast connection (e.g. NAS-devices).*

!!! success ""

    **Suggested:** `Yes`.

### ShellOverride

Shell overrides for script interpreters.

*By default extension scripts are executed as normal programs. The system finds an associated interpreter automatically. If for some reason that doesn't work properly you can provide shell overrides here.*

---

## Extension Manager

`Settings` => `EXTENSION SCRIPTS`

![!extScripts](images/extension-manager.png)

The Extension Manager is a tool for downloading, updating and deleting NZBGet extensions with backwards compatibility with extensions based on header configuration definition.

---

## Recommended Sonarr/Radarr Settings

The following settings are recommended for Sonarr/Radarr, else it could happen that Sonarr/Radarr will miss downloads that are still in the queue/history.
Being that Sonarr/Radarr only looks at the last xx amount in the queue/history.

### Sonarr

??? example "Sonarr"

    `Settings` => `Download Clients`

    ![!Sonarr: Settings => Download Clients](images/sonarr-settings-download-clients.png)

    Make sure you check both boxes under `Completed Download Handling` in step 3.

    Select NZBGet in step 4 and scroll down to the bottom of the new window where it says `Completed Download Handling` and check both boxes.

    ![!Sonarr: Download Clients - SABnzbd](images/sonarr-download-clients-nzbget.png)

### Radarr

??? example "Radarr"

    `Settings` => `Download Clients`

    ![!Radarr: Settings => Download Clients](images/radarr-settings-download-clients.png)

    Make sure you check both boxes under `Completed Download Handling` in step 3,

    and both boxes under `Failed Download Handling` in step 4.

--8<-- "includes/support.md"
