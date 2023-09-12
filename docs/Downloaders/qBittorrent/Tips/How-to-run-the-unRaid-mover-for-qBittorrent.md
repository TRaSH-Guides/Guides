# How to run the unRaid mover for qBittorent seeding torrents

IF you try to use the unRaid cache drive for your `/data/torrents` share while the torrents in qBittorent are still seeding, the mover can't move files, because they are still in use.

Using the following instructions, you will be able to move the files with the use of the qBittorrent API.

!!! abstract "Workflow Rules - [CLICK TO EXPAND]"

    1. Pause torrents older than last x days.
    1. Run the mover.
    1. Resume the torrents once the mover is completed.

## Warning

!!! Danger "If you make use of the Seed Time/Ratio settings in your Indexers settings in the Starr apps[^1].<br> Make sure you're using `Post-Import Category` in your Starr apps Download clients settings.<br>Otherwise, when the torrents get paused, they could get removed by the Starr apps before the seeding goal is reached."

!!! warning
    These screenshots are just examples to show how it should look and where to place the needed data; they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

    - Always follow the data described in the guide.
    - If you have any questions or aren't sure, click the chat badge to join the Discord Channel, where you can ask your questions directly.

## Needed

### The Script

Download the following standalone script:

- [Script](https://raw.githubusercontent.com/StuffAnThings/qbit_manage/master/scripts/mover.py){:target="_blank" rel="noopener noreferrer"}

(Big "Thank you!" to [bobokun](https://github.com/bobokun){:target="_blank" rel="noopener noreferrer"}, Developer of [qBit Manage](https://github.com/StuffAnThings/qbit_manage){:target="_blank" rel="noopener noreferrer"}.)

### Plugins

Install the following Plugins:

- User Scripts
- Nerd Tools
  - python3 [^2]
  - python-setuptools [^2]
  - python-pip [^2]

------

## Setup

After installing the needed plugins, it's time to configure everything.

### qBit API

The script needs the qBit API to work, so we need to make sure it's installed when your unRaid server is booted or when the Array is started the first time.

You can choose from the following 2 options to install it, depending on your preference.

- [User scripts](#user-scripts)
- [Go File](#go-file)

#### User scripts

With this option, we're going to install the qBit API when the Array is started the first time.

Go to your unRaid Dashboard, to your settings tab, and select in the `User Utilities` section at the bottom the new plugin you installed under `User Scripts`.

![!User Scripts](images/Unraid-settings-user-scripts-icon.png)

Select at the bottom `ADD NEW SCRIPT`.

![!Add New Script](images/Unraid-user-scripts-add-new-script-icon.png)

A popup will appear where you can give it a name. For this example we're going to use `Install qBittorrent API` and then click `OK`.

![!Install qBittorrent API](images/Unraid-user-scripts-add-new-script-enter-name.png)

Click in the list on the cogwheel of the new user script you made.

![!Select user script](images/Unraid-settings-user-scripts-list-select-qbit-api.png)

Copy/Paste the following bash command in the new window that opens, followed by `SAVE CHANGES`.

```bash
#!/bin/bash
pip3 install qbittorrent-api
```

![!Bash script](images/Unraid-settings-user-scripts-qbit-api.png)

Select in the schedule list when the script should run, and choose `At First Array Start Only`.

![!Set Run Time](images/Unraid-settings-user-scripts-qbit-api-schedule.png)

Click on `RUN IN BACKGROUND` or restart your unRaid server so the qBit API is installed.

![!RUN IN BACKGROUND](images/Unraid-settings-user-scripts-qbit-api-run-background.png)

------

#### Go File

With this option, we're going to install the qBit API when the unRaid server is started.

On your USB stick/key navigate to `/boot/config` and open the `go` file with your favorite editor ([VSCode](https://code.visualstudio.com/){:target="_blank" rel="noopener noreferrer"}/[Notepad++](https://notepad-plus-plus.org/downloads/){:target="_blank" rel="noopener noreferrer"}) and copy/paste the following command:

```bash
pip3 install qbittorrent-api
```

Restart your unRaid Server or run the above command from the terminal.

------

### Script

Edit the script with your favorite editor ([VSCode](https://code.visualstudio.com/){:target="_blank" rel="noopener noreferrer"}/[Notepad++](https://notepad-plus-plus.org/downloads/){:target="_blank" rel="noopener noreferrer"}) you downloaded at the beginning of the guide [HERE](#the-script).

You only need to edit a few options in the script

```python
# --DEFINE VARIABLES--#
# Set Number of Days to stop torrents between two offsets
# days_from set to 0 will pause any torrents from todays date
# days_to will be the upper limit of how far you want to pause torrents to
days_from = 0
days_to = 2
qbt_host = "192.168.2.200:8080"
qbt_user = None
qbt_pass = None
# --DEFINE VARIABLES--#
```

- `days_from` => Set Number of Days to stop torrents **from** for the move.
- `days_to` => Set Number of Days to stop torrents **to** for the move.
- `qbt_host` => The URL you use to access qBittorrent locally. (*the* `"` *should remain*)
- `qbt_user` => Your used qBittorrent `User Name` if you have authentication enabled. Add `'` either side.
- `qbt_pass` => Your used qBittorrent `Password` if you have authentication enabled. Add `'` either side.

!!! danger "If you have authentication enabled. Add `'` on either side of your User/Password."

!!! warning ""
    Depending on whether or not you use the unRaid `Mover Tuning` app, You might need to change **line 68**:

    - If you *do not* use `Mover Tuning`, change **line 68** from `os.system('/usr/local/sbin/mover.old start')` to `os.system('/usr/local/sbin/mover start')`
    - If you *do* use `Mover Tuning` but **don't** want to use it for the script, do not change **line 68**
    - If you *do* use `Mover Tuning` and **do** want to use it for the script, change **line 68** from `os.system('/usr/local/sbin/mover.old start')` to `os.system('/usr/local/sbin/mover start')`. For this option, inside the `Mover Tuner` options you will also need to set `Move Now button follows plugin filters` to `Yes` and `Disable Mover running on a schedule` to `No`.

#### Copy The Script to your Preferred Location

Now it's time to place the script you just edited somewhere easy to access/remember.

Suggestions:

- `/mnt/user/appdata/qbittorrent/scripts` (you must create this folder yourself)
- `/mnt/user/data/scripts` (you must create this folder yourself)

#### Final Steps

Now it's time to setup the scheduler when the mover should run.

Go to your unRaid Dashboard, to your settings tab, and select in the `User Utilities` at the bottom the new plugin you installed `User Scripts`.

![!User Scripts](images/Unraid-settings-user-scripts-icon.png)

Select at the bottom `ADD NEW SCRIPT`.

![!Add New Script](images/Unraid-user-scripts-add-new-script-icon.png)

A popup will appear where you can give it a name. For this example we're going to use `qBittorrent Mover` and then click `OK`.

![!qBittorrent Mover](images/Unraid-user-scripts-add-new-script-enter-name-qbt.png)

Click in the list on the cogwheel of the new user script you made.

![!Select user script](images/Unraid-settings-user-scripts-list-select-qbit-mover.png)

Copy/Paste the following bash command in the new window that opens, followed by `SAVE CHANGES`.

```bash
#!/bin/bash
/usr/local/emhttp/plugins/dynamix/scripts/notify -s "qBittorrent Mover" -d "qBittorrent Mover starting @ `date +%H:%M:%S`."
echo executing script to pause torrents and run mover.
/usr/bin/python3 /mnt/user/data/scripts/mover.py
echo qbittorrent-mover completed and resumed all paused torrents.
/usr/local/emhttp/plugins/dynamix/scripts/notify -s "qBittorrent Mover" -d "qBittorrent Mover completed @ `date +%H:%M:%S`."
```

!!! info
    Replace the `/mnt/user/data/scripts/mover.py` path to the path where you placed your python script.

![!Bash script](images/Unraid-settings-user-scripts-qbit-mover.png)

Select in the schedule list when the script should run, and choose `Custom`

![!Set Run Time](images/Unraid-settings-user-scripts-qbit-mover-schedule.png)

After changing to `Custom`, you get on the right an extra option where you can setup your cron schedule (when it should be run).

For this example, we're going to let the script run a 4am at night: `0 4 * * *`

Setup your own schedule [HERE](https://crontab.guru/)

![!Set Run Time](images/Unraid-settings-user-scripts-qbit-mover-cron.png)

--8<-- "includes/support.md"

[^1]:
    Starr apps = Sonarr/Radarr etc. Doesn't Starr apps sound better then `The arr(s)` ?

[^2]:
    These needs to be installed from the Nerd Tools.
