<style>
.indent-L1 {
    margin-left: 1em;
}
.indent-B1 {
    margin-bottom: 1em;
}
</style>
# Discord Notifier Basic Setup

Here you will see a basic setup for Discord Notifier.

------

## Login

First we're going to visit the [Discord Notifier](https://discordnotifier.com/index.php){:target="_blank"} site, if you don't have an account yet, click the link to signup.

 ![image-20201107173234502](images/image-20201107173234502.png)

1. Your Email address you used during signup.
1. Your Password you created during signup.
1. Login to the site and setup.
1. Password reset if you forgot your password.
1. Signup if you don't have an account.
1. Link to Discord Notifier Discord support channel.

------

## Profile

After you logged in you will be redirected to your profile screen where you need to do a few things.

 ![image-20201107184811997](images/image-20201107184811997.png)

1. Select your Country.
1. Select your Timezone.
1. Click on `Generate API Key` (This needs to be done).
1. Change your Time Format to your liking.
1. Don't forget to Save your Changes.

------

## Notification Setup

Here you will be able to setup the following things:

- Notifications Settings => Setup which notifications you want to receive.
- Discord Settings => Setup your discord channels and your reactions and invite the bot into your channel.

### Notification Settings

Setup which notifications you want to to receive from each option.

 ![image-20201107190759062](images/image-20201107190759062.png)

1. Click on the cog (settings) icon to configure what will be in your notification.

    #### Notification Settings Configuration
    ![image-20201117-121530](images/image-20201117-121530.png)

    1. Enable/Disable notification trigger
    1. Change color bar for notification trigger
    1. Expand trigger to enable/disable message fields
    1. Customize the layout for the notification (drag/drop editor to the right in the image)

### Discord Settings
<div class="indent-L1 indent-B1">
Setup your discord channels and your reactions and invite the bot into your channel.
</div>

#### Create the channels

<div class="indent-L1 indent-B1">
First thing to do is create a few channels where you receive your notifications.

!!! note:
    I won't be explaining how to setup a discord channel, that's up to you but google has plenty of references.

You can do it all from one channel or separate the notifications (granular) for each trigger if you want.
</div>

#### Simple channel setup
<div class="indent-L1">

`#media` => All the `*arr` notifications you setup in [Notification Settings](#notification-settings).

`#errors` => Health checks, network errors, etc.

`#plex` => Play, resume, etc. for Plex.
</div>
After you create the needed channels, it's time to add them to the `Setup the channels`

First we need to get the channel ID's from your server/channel

Open your User Settings -> Appearance -> Enable Developer Mode.

 ![image-20201107201431508](images/image-20201107201431508.png)

 Right click on the Discord text channel you want the bot to interact  with and press "Copy ID"

 ![image-20201107201209441](images/image-20201107201209441.png)

Paste the channel ID in the corresponding boxes.

 ![image-20201107201822743](images/image-20201107201822743.png)

1. Add the channel ID for the `#media` channel.
1. Add the channel ID for the `#errors` channel.
1. Add the channel ID for the `#plex` channel.
1. Use this option if you want to use separate channels for the notifications (see below).
1. Use this option if you want to use separate channels for the notifications.

![Image-20201117-145908](images/Image-20201117-145908.png)

### Invite the bot

It's time to invite the bot in to your Server/Channels by clicking on the following link.

 ![image-20201107203033357](images/image-20201107203033357.png)

You will get a screen that looks like the following screenshot.

 ![image-20201107203535642](images/image-20201107203535642.png)

1. Select the server the bot should join.
1. Click on `Authorize` to approve.

!!! note:
     You have to be an administrator of the Discord channel to invite bots. Make sure the bot has permissions to post.

??? summary "Bot Setup Help"
    Right click on your server > Server Settings > Roles

    If you have a Bot role you can skip this, otherwise click the + next to ROLES

    Name the role Bot and scroll down to Text Permissions.

    Enable `Send Messages`, `Embed Links` & `Add Reactions`

    Go back to your server, right click on the Media Bot and assign the role of Bot

#### Reactions

Here we will setup the Discord Notifier reactions(emoji's) that will be shown during a playback in plex, or during a download/import in Sonarr/Radarr.

![image-20201108084938027](images/image-20201108084938027.png) ![image-20201108085034607](images/image-20201108085034607.png)

This section exist of 2 parts.

1. *arr state (grab/failed) and play state of plex.
1. The Trackers/Indexers.

First we're going to download the emoji's and you can do that in 2 ways.

1. One by One - Right click -> save as for these emoji images.
1. Pack Download - Click [here](https://discordnotifier.com/setup.php?grab=reactions){:target="_blank"} to download a zip of all the current reaction images.

For this Example we will be using the Pack Download, that you need to unpack to your computer and then add them to your Discord Server

How to add your own Emoji's => [LINK](https://support.discord.com/hc/en-us/articles/360036479811-Custom-Emojis){:target="_blank"}

After you've added them to your Discord Server it's time to get the ID's from your emoji's, to do this go in to one of your channels and type:

```bash
\:emoji_name:
```

??? summary "Example"
    ![image-20201108092738752](images/image-20201108092738752.png)

    What results in to.

    ![image-20201108092827192](images/image-20201108092827192.png)

    So your ID would be `:grab:706535455876710461`.

Paste the ID results from your channel in to the corresponding boxes.

 ![image-20201108093201236](images/image-20201108093201236.png)

Do this for all the other boxes also including your Trackers/Indexers.

#### Trackers and Indexers

 ![image-20201108093947565](images/image-20201108093947565.png)

1. Paste here the the emoji ID.
1. The actual indexer name you're using in Sonarr/Radarr.

??? summary "Example"

    ![image-20201108094627415](images/image-20201108094627415.png)

    What will result in to.

    ![image-20201108094834791](images/image-20201108094834791.png)

    If you use a different name in Sonarr and Radarr just add them with a comma `BeyondHD - Jackett,BHD`.

Don't forget to click on `Save Changes` !!!

!!! note
    After pasting the Emoji's ID in to the box you will notice that the leading colon will disappear nothing to worry about that's per design

------

## Integrations

This is where we add all this to your *arr and Plex.

 ![image-20201108153748843](images/image-20201108153748843.png)

### Radarr, Readarr and Lidarr

Radarr, Readarr and Lidarr supports Discord Notifier native so that's a easy one to add.

`Settings` => `Connect` => click on ![image-20201108174654550.png](images/image-20201108174654550.png) and select `Discord Notifier` add your API key and you're done.

??? summary "Radarr Example"
    In Radarr go to `Settings` => `Connect` => Click on ![image-20201108174654550](images/image-20201108174654550.png) and select `DiscordNotifier.com`.

    ![image-20201108154540683](images/image-20201108154540683.png)

    Then add the following info.

    ![image-20201108172017406](images/image-20201108172017406.png)

    1. The name you want to use for the notification.
    2. Enable `On Grab`, `On Import`, `On Upgrade`, `On Health Issue` & `Include Health Warnings`.
    3. Add here you API key from Discord Notifier.
    4. Click on `Test` to see if it works.
    5. If everything is correct click on `Save`

### Sonarr

Sonarr doesn't have native support & will not get one per their devs.
That's why we're going to use the webhook method.

 ![image-20201108175840774](images/image-20201108175840774.png)

`Settings` => `Connect` > Click on ![image-20201108174654550.png](images/image-20201108174654550.png) and select `Webhook`.

Add the following info.

**Name**: Discord Notifier

**Enable:** `On Grab`, `On Import`, `On Upgrade`, `On Health Issue` & `Include Health Warnings`.

**URL:** The URL that you can copy/paste from the integrations page.

Click **Save**

??? summary "Sonarr Example"

    `Settings` => `Connect` > Click on ![image-20201108174654550.png](images/image-20201108174654550.png) and select `Webhook`.

    ![image-20201108181144356](images/image-20201108181144356.png)

    Add the following info.

    ![image-20201108181509164](images/image-20201108181509164.png)

    1. The name you want to use for the notification.
    2. Enable `On Grab`, `On Import`, `On Upgrade`, `On Health Issue` & `Include Health Warnings`.
    3. Add the URL that you can copy/paste from the integrations page.
    4. Make sure this is on `POST`.
    5. Click on `Test` to see if it works.
    6. If everything is correct click on `Save`

### Bazarr

For Bazarr you need to make use of JSON method.

 ![image-20201108183922518](images/image-20201108183922518.png)

`Settings` => `Notifications` => and select`JSON`

On the top click on ![image-20201108191244845](images/image-20201108191244845.png) `Edit` icon and Enable the notification type.

Add the JSON URL that you can copy/paste from the integrations page.

Scroll up and save

??? summary "Bazarr Example"

    `Settings` => `Notifications` => and select`JSON`

    ![image-20201108185518511](images/image-20201108185518511.png)

    On the top click on ![image-20201108191244845](images/image-20201108191244845.png) `Edit` icon and Enable the notification type.

    Add the following info.

    ![image-20201108190148938](images/image-20201108190148938.png)

    1. Enable the JSON Notification.
    2. Add the JSON URL that you can copy/paste from the integrations page.
    3. Click on `Test` to see if it works.
    4. If everything is correct click on `Ok`

    Don't forget to click on Save on the top of the Bazarr screen.

    ![image-20201108190622004](images/image-20201108190622004.png)

### Plex

#### URL Webhook

 ![image-20201108191708582](images/image-20201108191708582.png)

`Settings` => `Webhooks` => click on `ADD WEBHOOK` and add the URL that you can copy/paste from the integrations page and click on `SAVE CHANGES`

??? summary "Plex Example"

    `Settings` => `Webhooks` => click on `ADD WEBHOOK`

    On the top right click on the ![image-20201108194808693](images/image-20201108194808693.png) `Settings` icon, and on the left sidebar select `Webhooks`
    Click on the middle of the screen on ![image-20201108195006697](images/image-20201108195006697.png) and add the following info.

    ![image-20201108195139199](images/image-20201108195139199.png)

    1. Add the URL that you can copy/paste from the integrations page.
    2. Click on `SAVE CHANGES`

#### Python Webhook
<div class="indent-L1 indent-B1">
Python is required for this to work. Make sure your docker solution has it available if running docker.
</div>

##### All implementations
- Open the file and change the variables accordingly.
- There are links in the file comments to help as well
- You can test the script by typing python /path/to/script in your CLI. If the file has a shebang in it (#!python) then you do not need to specify python on the CLI.

##### Docker
- Cloudbox - Has python installed
- Hotio - Has python installed
- LSIO - Does not have python installed

##### Linux

##### Unraid

##### Windows
<div class="indent-L1 indent-B1">
Run the python file so it listens on the specific port.
</div>

### Testing

On the top of the integrations page you will now have the ability to test your settings. This only tests the connection between the notifier and your discord. You can use the Test in each *arr and that will test the everything (connection wise).

 ![image-20201108195808555](images/image-20201108195808555.png)

Click on the icons to test your notifications.
