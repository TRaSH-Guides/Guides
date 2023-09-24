# How to run the unRaid mover for qBittorent seeding torrents

When you make use of the unRaid cache drive for your `/data/torrents` share and the torrents in qBittorent are still seeding then the mover can't move files, because they are still in use.

Using the following instructions you will be able to move the files with the use of the qBittorrent API.

!!! abstract "Workflow Rules - [Click to show/hide]"

    1. Pause torrents older than last x days.
    1. Run the mover.
    1. Resume the torrents once the mover is completed.

!!! warning

    The screenshots are just examples to show you how it should look and where you need to place the data that you need to add, they aren't always a 100% reflection of the actual data and not always 100% up to date with the actual data you need to add.

    - Always follow the data described in the guide.
    - If you got any questions or aren't sure just click the chat badge to join the Discord Channel where you can ask your questions directly.

## Needed

### The Script

Download the following standalone script.

- [Script (mover.py)](https://raw.githubusercontent.com/StuffAnThings/qbit_manage/master/scripts/mover.py){:target="_blank" rel="noopener noreferrer"}

Big Thnx to [bobokun](https://github.com/bobokun){:target="_blank" rel="noopener noreferrer"} Developer of [qBit Manage](https://github.com/StuffAnThings/qbit_manage){:target="_blank" rel="noopener noreferrer"}

### Plugins

Install the following Plugins.

- User Scripts
- NerdTools
      - python3 <sup>(*1*)</sup>
      - python-setuptools <sup>(*1*)</sup>
      - python-pip <sup>(*1*)</sup>

!!! info "<sup>(*1*)</sup> These needs to be installed from the NerdTools."

------

## Setup

After you installed the needed Plugins it's time to configure everything.

### qBit API

The script needs the qBit API to work, so we need to make sure it's installed when your unRaid server is booted or when the Array is started the first time.

You can choose from the following 3 options how you want to install it, depending what you preference.

- [User scripts](#user-scripts)
- [Go File](#go-file)
- [Python venv](#python-venv)

#### User scripts

With this option we're going to install the qBit API when the Array is started the first time.

Go to your unRaid Dashboard to your settings tab and select in the `User Utilities` at the bottom the new plugin you installed `User Scripts`.

![!User Scripts](images/Unraid-settings-user-scripts-icon.png)

Select at the bottom `ADD NEW SCRIPT`.

![!Add New Script](images/Unraid-user-scripts-add-new-script-icon.png)

A popup will appear where you can give it a name, for this example we're going to use `Install qBittorrent API` and then click on `OK`.

![!Install qBittorrent API](images/Unraid-user-scripts-add-new-script-enter-name.png)

Click in the list on the cogwheel of the new user scrip you made.

![!Select user script](images/Unraid-settings-user-scripts-list-select-qbit-api.png)

Copy/Paste in the new windows that opens the following bash command followed by `SAVE CHANGES`.

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

With this option we're going to install the qBit API when the unRaid server is started.

On your USB stick/key go to `/boot/config` and open the `go` file with your favorite editor ([VSCode](https://code.visualstudio.com/){:target="_blank" rel="noopener noreferrer"}/[Notepad++](https://notepad-plus-plus.org/downloads/){:target="_blank" rel="noopener noreferrer"}) and copy/paste the following command.

```bash
pip3 install qbittorrent-api
```

Restart your unRaid Server, or run the above command from the terminal.

------

#### Python venv

With this option we're going to create a [Python virtual environment](https://docs.python.org/3/library/venv.html) on our disks to run and store isolated dependencies for this specific environment.

By doing so, we **only need to setup this step once** and it will be persistent after reboots _(this differs from the previous steps)_.

First, you need to choose a location to start a clear python environment.

!!! info
    In the next steps, you will be ask to choose a [location to place the script](#copy-script-to-your-preferred-location), try to be consistent.

Suggestions:

- `/mnt/user/appdata/qbittorrent/scripts/.venv`
- `/mnt/user/data/scripts/.venv`

Run the following command on Unraid terminal within the location you chose:

```bash
python3 -m venv --clear /mnt/user/data/scripts/.venv
```

We now need to enter into this new environment to install our dependencies (`qbittorrent-api`) on there, run:

```bash
source /mnt/user/data/scripts/.venv/bin/activate
pip3 install qbittorrent-api
deactivate # to leave the environment
```

!!! info
    Replace the `/mnt/user/data/scripts/.venv` to the chosen path before.

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

!!! danger "If you have authentication enabled. Add `'` either side of your User/Password."

!!! warning ""
    Depending on whether you use the unRaid `Mover Tuning` app, You might need to change **line 68**:

    - If you do not use `Mover Tuning`, change **line 68** from `os.system('/usr/local/sbin/mover.old start')` to `os.system('/usr/local/sbin/mover start')`
    - If you use `Mover Tuning` but **don't** want to use it for the script, do not change **line 68**
    - If you use `Mover Tuning` and **do** want to use it for the script, change **line 68** from `os.system('/usr/local/sbin/mover.old start')` to `os.system('/usr/local/sbin/mover start')`. For this option, inside the `Mover Tuner` options you will also need to set `Move Now button follows plugin filters` to `Yes` and `Disable Mover running on a schedule` to `No`.

#### Copy script to your preferred location

Now it's time to place the script you just edited somewhere easy to access/remember.

Suggestions:

- `/mnt/user/appdata/qbittorrent/scripts/mover.py`
- `/mnt/user/data/scripts/mover.py`

#### Final steps

Now it's time to setup the scheduler when the mover should run.

Go to your unRaid Dashboard to your settings tab and select in the `User Utilities` at the bottom the new plugin you installed `User Scripts`.

![!User Scripts](images/Unraid-settings-user-scripts-icon.png)

Select at the bottom `ADD NEW SCRIPT`.

![!Add New Script](images/Unraid-user-scripts-add-new-script-icon.png)

A popup will appear where you can give it a name, for this example we're going to use `qBittorrent Mover` and then click on `OK`.

![!qBittorrent Mover](images/Unraid-user-scripts-add-new-script-enter-name-qbt.png)

Click in the list on the cogwheel of the new user scrip you made.

![!Select user script](images/Unraid-settings-user-scripts-list-select-qbit-mover.png)

Copy/Paste in the new windows that opens the following bash command followed by `SAVE CHANGES`.

```bash
#!/bin/bash
#source /mnt/user/data/scripts/.venv/bin/activate
/usr/local/emhttp/plugins/dynamix/scripts/notify -s "qBittorrent Mover" -d "qBittorrent Mover starting @ `date +%H:%M:%S`."
echo "executing script to pause torrents and run mover."
python3 /mnt/user/data/scripts/mover.py
echo "qbittorrent-mover completed and resumed all paused torrents."
/usr/local/emhttp/plugins/dynamix/scripts/notify -s "qBittorrent Mover" -d "qBittorrent Mover completed @ `date +%H:%M:%S`."
```

!!! info
    Replace the `/mnt/user/data/scripts/mover.py` path to the path where you placed your python script.

!!! danger

    **Only** if you are using the [Python venv](#python-venv) method:

      - Uncomment **line 2** (remove just the `#` character)
      - Replace the `/mnt/user/data/scripts/.venv` part to the path where you created the python env, **keep the rest**

![!Bash script](images/Unraid-settings-user-scripts-qbit-mover.png)

Select in the schedule list when the script should run, and choose `Custom`

![!Set Run Time](images/Unraid-settings-user-scripts-qbit-mover-schedule.png)

After changing to `Custom` you get on the right a extra option where you can setup your cron schedule when it should be run.

For this example we're going to let the script run a 4am at night. `0 4 * * *`

Setup your own schedule [HERE](https://crontab.guru/)

![!Set Run Time](images/Unraid-settings-user-scripts-qbit-mover-cron.png)

--8<-- "includes/support.md"
