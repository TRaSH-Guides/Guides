# Permissions

This can be a struggle depending on how you have your server setup. If you want to do a simple test and see if you have permission issues, set the role your bot is included in to have admin permission and test. If everything works, this means you simply need to adjust permissions for the role so you do not need to make it an admin role if you dont want to.

---

I will work on the assumption you have created a role called **Bots** already with this and assigned the Notifiarr bot to it. With that said, right click on your server name at the top and pick `Server Settings > Roles`. Click on the Bots role so the permissions list loads.

> Yes I am aware that adding the bot automatically creates a **Notifiarr** role but most will rather leave that one hidden and use an existing role. If you want to use that one, make sure all the same permissions are applied to it.

## **Required permissions**

1. `View Channels`
    - The bot needs this role to generate a channel list so you can assign which notifications go to which channels on your server. If the channel is a private channel, you may also need to adjust channel specific permissions.
1. `Send Messages`
    - This one is obvious, without it the bot role can not add messages to channels
1. `Embed Links`
    - Many notifications have links (such as TMDb, TVDb, IMDb, Website links, etc)
1. `Add Reactions`
    - *arr and Plex notifications add reactions to notifications to signify things such as the indexer, manual or rss grab, imported, failed, unpacked, subtitles, etc
1. `Use External Emojis`
    - Only required if the reactions you use are from another server
1. `Mention @everyone, @here and All Roles`
    - Needed if you have alerts setup with Snapshots or Media Request integrations so the proper user/role can be @mentioned
1. `Manage Messages`
    - This is used for the Media Request integration so the bot can remove all the back and forth posts when adding new things to leave a clean channel history
1. `Read Message History`
    - This is used for the Media Request integration so the bot can get the user interactions and is also used to place reactions on existing messages

---

If you manage your channels with individual permissions **plus** bot permissions, you will need to adjust them accordingly so the bot can do its job. If you have permissions mis-configured then the site will auto disable the integration after 25 Discord API errors. If you are using reactions and get API errors, the site will auto remove the reaction. If you are using the bot and have cleanup history enabled and get API errors, the site will auto disable that.

You will know when the site does this with a big red notice on top of the setup page that explains the error that Discord reported and what action was taken. All you have to do is fix the issue and re-enable what the site disabled from that point.
