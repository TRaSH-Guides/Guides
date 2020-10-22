# Remote Path Mappings explained for Sonarr

Remote Path Mappings explained for Sonarr

# Description

Seems that allot of people don't understand how the remote path mapping works for Sonarr.
I will try to explain it with some screenshots and a short description.


# Do I need Remote Path Mappings ?

If your download client is on another system then Sonarr then you probably need to make use of Remote Path Mappings.

You will get a error that looks a little bit like the following screenshot.

![1549734726771](images/1549734726771.png)

So looking at this screenshot it seems we need to make use of Remote Path Mappings !!!

------

# How ?

First we navigate in Sonarr to the Settings => `Download Clients` Tab.

![1549734647618](images/1549734647618.png)

At the bottom you choose `Add new mapping`

![1549734986119](images/1549734986119.png)

A screen will popup with the following options.

![1549734928236](images/1549734928236.png)

1. `Host` => This is the hostname or IP you set in your download client settings.
2. `Remote Path` => The download path that you've set in your download client.
3. `Local Path` => The path Sonarr needs to access the same path.



------

# Now some screenshots with a examples that I use for this tutorial.

- [x] QBittorrent
- [ ] NZBGet
- [ ] other client ?

## Host:

To find what you need to put in your host you navigate in Sonarr to the Settings => Download Clients Tab.
There you open up the download client for this example I will be using QBittorrent

![1549734875590](images/1549734875590.png)

This is what you put in your Host in Remote Path Mapping.



## Remote Path:

To find what you need to put in your remote path you need to open up your download client and look what you've used there as download location.

In QBittorrent navigate to Tools => Options (or ALT+O) and navigate to the Download settings.

![1549735142149](images/1549735142149.png)



This is what you add in your Remote Path in Remote Path Mapping.



## Local Path:

To find what you need to put in in your local path you need to know how Sonarr is able to access the files your download client downloaded.
And this can be done in different ways.
Mounting/Network share what ever but Sonarr needs to have local access to it so you need to figure this one out your self what's the best way for Sonarr to access the download clients downloaded files.

The final result will look something like this.

![1549735082937](images/1549735082937.png)





