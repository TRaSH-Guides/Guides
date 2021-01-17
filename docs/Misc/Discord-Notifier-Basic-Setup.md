<style>
.indent-L1 {
    margin-left: 1em;
}
.indent-B1 {
    margin-bottom: 1em;
}
</style>

# Discord Notifier (Notifiarr) Basic Setup

------

## Login

First we're going to visit the [Notifiarr](https://discordnotifier.com/index.php){:target="_blank" rel="noopener noreferrer"} site, if you don't have an account yet, click the link to signup.

 ![dn-login](images/dn-login.png)

1. Your Email address you used during signup.
1. Your Password you created during signup.
1. Login to the site and setup.
1. Password reset if you forgot your password.
1. Signup if you don't have an account.
1. Link to Notifiarr Discord support channel.

------

## Profile

After you have logged in, you will be redirected to your profile screen.

 ![dn-profile](images/dn-profile.png)

1. Select your `Country`.
1. Select your `Timezone`.
1. Click on `Generate API Key` (This needs to be done).
1. Select your `Notification Language`.
1. Change your `Time Format` to your liking.
1. Don't forget to Save your Changes.

------

## Integration Setup

- Enable the integrations you want to use
- Setup your discord server (required), invite the bot (required) and reactions (optional).

### Integration Settings

![dn-manage-integration-open](images/dn-manage-integration-open.png)

First, click on  `Manage Integrations` so you can enable what you want to receive notifications for.

![dn-manage-integration](images/dn-manage-integration.png)

A screen will popup and here you're able to select from which application/service you receive a notification.

When you enabled the ones you want click on `Save`

Setup which notifications you want to to receive from each option.

 ![dn-notifcation-settings-radarr](images/dn-notifcation-settings-radarr.png)

1. Cog wheel, this opens the integration settings
1. External link, this opens the website for the integration
1. WIKI link, this opens any extra wiki information available for the integration
1. Trigger, this enables/disables a specific trigger for the integration
1. Channels, this sets the channel in your server to post to for the integration

??? example "Integration Settings (Cog wheel))"

    #### Notification Settings Configuration

    ![dn-integration-settings](images/dn-integration-settings.png)

    1. [Instructions how to setup the integration](#integrations)
    1. Enable/Disable notification trigger
    1. Change color bar for notification trigger
    1. Expand trigger to enable/disable message fields
    1. Customize the layout for the notification (drag/drop editor to the right in the image)
    1. Enable so each notification is unique and wont update existing ones.
    1. Here you can edit the layout

### Discord Settings

<div class="indent-L1 indent-B1">
Setup your discord server, shared channels, reactions and invite the bot into your server.
</div>

#### Create the channels

<div class="indent-L1 indent-B1">
First thing to do is create a few channels (in your discord server) where you receive your notifications.

!!! note:
    I won't be explaining how to setup a discord channel, that's up to you but google has plenty of references.

You can do it all from one channel or separate the notifications (granular) for each trigger if you want.
</div>

#### Simple channel setup

`#media` => All the `*arr` notifications you setup in [Notification Settings](#notification-settings).

`#errors` => Health checks, network errors, etc.

`#plex` => Play, resume, etc. for Plex.

After you create the needed channels, it's time to add them to the `Setup the channels`

First we need to get the server ID

Open your User Settings -> Appearance -> Enable Developer Mode.

 ![dn-discord-dev-mode](images/dn-discord-dev-mode.png)

 Right click on the server name at the top of your discord and press "Copy ID"

 ![dn-channel-paste](images/dn-channel-paste.png)

1. Add your server ID
1. Select the channel ID for the `#media` channel.
1. Use this option if you want to use separate channels for the notifications (see below).
1. Select the channel ID for the `#errors` channel.
1. Select the channel ID for the `#plex` channel.
1. Use this option if you want to use separate channels for the notifications (see below).

??? example "Granular arr setup"

    ##### Granular arr setup

    ![dn-granular-arr-setup](images/dn-granular-arr-setup.png)

??? example "Granular media setup"

    ##### Granular media setup

    ![dn-granular-media-setup](images/dn-granular-media-setup.png)

### Invite the bot

It's time to invite the bot in to your Server/Channels by clicking on the following link.

 ![dn-invite-bot-here](images/dn-invite-bot-here.png)

You will get a screen that looks like the following screenshot.

 ![dn-invite-bot-discord](images/dn-invite-bot-discord.png)

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

![dn-reaction-1](images/dn-reaction-1.png) ![dn-reaction-2](images/dn-reaction-2.png)

This section exist of 2 parts.

1. *arr state (grab/failed) and play state of plex.
1. The Trackers/Indexers.

First we're going to download the emoji's and you can do that in 2 ways.

1. 1 at a time - Right click -> Save As... - for these emoji images to some location on your computer.
1. Pack Download - Click [here](https://discordnotifier.com/setup.php?grab=reactions){:target="_blank" rel="noopener noreferrer"} to download a zip of all the current reaction images.

For this example, we will be using Pack Download.  You'll need download the file and then unpack it somewhere on your computer.  After which, you can then add the emoji's to your Discord Server easily.

How to add your own Emoji's => [LINK](https://support.discord.com/hc/en-us/articles/360036479811-Custom-Emojis){:target="_blank" rel="noopener noreferrer"}

After you've added them to your Discord Server it's time to get the ID's from your emoji's, to do this go in to one of your channels and type:

```bash
\:emoji_name:
```

??? example "Example"
    ![dn-emoji-example](images/dn-emoji-example.png)

    What results in to.

    ![dn-emoji-result](images/dn-emoji-result.png)

    So your ID would be `:grab:706535455876710461`.

Paste the ID results from your channel in to the corresponding boxes.

 ![dn-reaction-paste](images/dn-reaction-paste.png)

Do this for all the other boxes also including your Trackers/Indexers.

#### Trackers and Indexers

 ![dn-reaction-indexers](images/dn-reaction-indexers.png)

1. Paste here the the emoji ID.
1. The actual indexer name you're using in Sonarr/Radarr.

??? example "Example"

    ![dn-indexer-torznab](images/dn-indexer-torznab.png)

    What will result in to.

    ![dn-indexer-torznab-result](images/dn-indexer-torznab-result.png)

    If you use a different name in Sonarr and Radarr just add them with a comma `BeyondHD - Jackett,BHD`.

Don't forget to click on `Save Changes` !!!

!!! note
    After pasting the Emoji's ID in to the box you will notice that the leading colon will disappear nothing to worry about that's per design

------

## Integrations

Here we will explain how to we add all this to your *arr and Plex.

 ![dn-integration-settings-link](images/dn-integration-settings-link.png)

### Radarr, Readarr and Lidarr

Radarr, Readarr and Lidarr supports Discord Notifier natively so that's an easy one to add.

`Settings` => `Connect` => click on ![dn-arr-add-plus.png](images/dn-arr-add-plus.png) and select `Discord Notifier` add your API key and you're done.

??? example "Radarr Example"
    In Radarr go to `Settings` => `Connect` => Click on ![dn-arr-add-plus](images/dn-arr-add-plus.png) and select `DiscordNotifier.com`.

    ![dn-arr-add-notification](images/dn-arr-add-notification.png)

    Then add the following info.

    ![dn-arr-settings-notification](images/dn-arr-settings-notification.png)

    1. The name you want to use for the notification.
    1. Enable `On Grab`, `On Import`, `On Upgrade`, `On Health Issue` & `Include Health Warnings`.
    1. Add here you API key from Discord Notifier.
    1. Click on `Test` to see if it works.
    1. If everything is correct click on `Save`

### Sonarr

Sonarr doesn't have native support & will not get one per their devs.
That's why we're going to use the webhook method.

 ![dn-sonarr-instruction](images/dn-sonarr-instructions.png)

`Settings` => `Connect` > Click on ![dn-arr-add-plus](images/dn-arr-add-plus.png) and select `Webhook`.

Add the following info:

**Name**: Discord Notifier

**Enable:** `On Grab`, `On Import`, `On Upgrade`, `On Health Issue` & `Include Health Warnings`.

**URL:** The URL that you can copy/paste from the integrations page.

Click **Save**

??? example "Sonarr Example"

    `Settings` => `Connect` > Click on ![dn-arr-add-plus.png](images/dn-arr-add-plus.png) and select `Webhook`.

    ![dn-sonarr-add-webhook](images/dn-sonarr-add-webhook.png)

    Add the following info.

    ![dn-sonarr-settings-webhook](images/dn-sonarr-settings-webhook.png)

    1. The name you want to use for the notification.
    1. Enable `On Grab`, `On Import`, `On Upgrade`, `On Health Issue` & `Include Health Warnings`.
    1. Add the URL that you can copy/paste from the integrations page.
    1. Make sure this is on `POST`.
    1. Click on `Test` to see if it works.
    1. If everything is correct click on `Save`

### Bazarr

For Bazarr you need to make use of JSON method.

 ![dn-bazarr-instruction](images/dn-bazarr-instruction.png)

`Settings` => `Notifications` => and select`JSON`

On the top click on ![dn-bazarr-edit-icon](images/dn-bazarr-edit-icon.png) icon and Enable the notification type.

Add the JSON URL that you copy/pasted from the integrations page.

Scroll up and save

??? example "Bazarr Example"

    `Settings` => `Notifications` => and select`JSON`

    ![dn-bazarr-add-json](images/dn-bazarr-add-json.png)

    On the top click on ![dn-bazarr-edit-icon](images/dn-bazarr-edit-icon.png) `Edit` icon and Enable the notification type.

    Add the following info.

    ![dn-bazarr-settings-json](images/dn-bazarr-settings-json.png)

    1. Enable the JSON Notification.
    1. Add the JSON URL that you copy/pasted from the integrations page.
    1. Click on `Test` to see if it works.
    1. If everything is correct click on `Ok`

    Don't forget to click on Save on the top of the Bazarr screen.

    ![dn-bazarr-save-json](images/dn-bazarr-save-json.png)

### Plex

#### URL Webhook

 ![dn-plex-instructions](images/dn-plex-instructions.png)

`Settings` => `Webhooks` => click on `ADD WEBHOOK` and add the URL that you can copy/paste from the integrations page and click on `SAVE CHANGES`

??? example "Plex Example"

    `Settings` => `Webhooks` => click on `ADD WEBHOOK`

    On the top right click on the ![dn-plex-settings-icon](images/dn-plex-settings-icon.png) `Settings` icon, and on the left sidebar select `Webhooks`
    Click on the middle of the screen on ![dn-plex-webhook-icon](images/dn-plex-webhook-icon.png) and add the following info.

    ![dn-plex-settings-webhook](images/dn-plex-settings-webhook.png)

    1. Add the URL that you can copy/paste from the integrations page.
    2. Click on `SAVE CHANGES`

??? info "Advanced Plex Settings"

    ### Advanced Plex Settings

    ![dn-plex-advanced](images/dn-plex-advanced.png)

    #### Python Webhook

    <div class="indent-L1 indent-B1">
    Python is required for this to work. Make sure your docker solution has it available if running docker.
    </div>

    #### All implementations

    - Open the file and change the variables accordingly.
    - There are links in the file comments to help as well
    - You can test the script by typing python /path/to/script in your CLI. If the file has a shebang in it (#!python) then you do not need to specify python on the CLI.

    ##### Docker

    - Cloudbox - Has python installed
    - Hotio - Has python installed
    - LSIO - Does not have python installed

    ##### Linux

    placeholder

    ##### Unraid

    placeholder

    ##### Windows

    placeholder

    <div class="indent-L1 indent-B1">
    Run the python file so it listens on the specific port.
    </div>

### Testing

On the bottom of all the instruction you will now have the ability to test your settings. This only tests the connection between the notifier and your discord. You can use the Test in each *arr and that will test the everything (connection wise).

 ![dn-test-icons-bar](images/dn-test-icons-bar.png)

Click on the icons to test your notifications.
After going through this tutorial and you still aren't getting notifications in your discord channel from the respective logos, then retry the steps outlined above.  If there is still an issue, try asking in the Discord Notifier [discord channel](https://discord.gg/AURf8Yz){:target="_blank" rel="noopener noreferrer"} for additional support.
