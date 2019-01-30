# Remote-Path-Mappings-explained-for-Sonarr-Radarr

Remote Path Mappings explained for Sonarr/Radarr

# Description

Seems that allot of people are having to understand how the remote path mapping works for Sonarr/Radarr.
I will try to explain it with some screenshots and a short description,
for this I will use screenshots used from Radarr.



# Do I need Remote Path Mappings ?

If you download client is on another system then Radarr/Sonarr then you probably need to make use of Remote Path Mappings.

You will get a error that looks a little bit like the following screenshot.

![OH NO!!!](http://my.jetscreenshot.com/13737/20190126-oiao-44kb.png)

So looking at this screenshot it seems we need to make use of Remote Path Mappings !!!

------

# How ?

First we navigate in Radarr to the Settings => `Download Client` Tab.

![Download Client Tab](http://my.jetscreenshot.com/13737/20190126-5k5d-31kb.png)

At the bottom you choose `Add new mapping`

![add new mapping](http://my.jetscreenshot.com/13737/20190126-gsm6-11kb.png)

A screen will popup with the following options.

![Add Mapping](http://my.jetscreenshot.com/13737/20190126-0srw-12kb.png)

1. `Host` => This is the hostname or IP you set in your download client settings.
2. `Remote Path` => The download path that you've set in your download client.
3. `Local Path` => The path Sonarr/Radarr needs to access the same path.



------

# Now some screenshots with a examples that I use for this tutorial.

- Qbittorrent
- NZBGet

## Host:

To find what you need to put in your host you navigate in Radarr to the Settings => Download Client Tab.
There you open up the download client for this example I will be using Qbittorrent

![Qbittorrent Client](http://my.jetscreenshot.com/13737/20190126-heqh-6kb.png)

This is what you put in your Host in Remote Path Mapping.



## Remote Path:

To find what you need to put in your remote path you need to open up your download client and look what you've used there as download location.

In Qbittorrent navigate to Tools => Options (or ALT+O) and navigate to the Download settings.

![Qbittorrent Download Settings](http://my.jetscreenshot.com/13737/20190126-3wa7-61kb.png)



This is what you add in your Remote Path in Remote Path Mapping.



## Local Path:

To find what you need to put in in your local path you need to know how Radarr is able to access the files your download client downloaded.
And this can be done in different ways.
Mounting/Networkshare what ever but Radarr needs to have local access to it so you need to figure this one out your self what's the best way for Radarr to access the download clients downloaded files.

The final result will look like this.

![Qbittorrent Final Result](http://my.jetscreenshot.com/13737/20190126-ngqk-13kb.png)





