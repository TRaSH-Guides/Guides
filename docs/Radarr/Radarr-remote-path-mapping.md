# Remote Path Mappings

Seems that allot of people don't understand how the remote path mapping works for Radarr. I will try to explain it with some screenshots and a short description.

Remote Path Mapping acts as a dumb find `Remote Path` and replace with `Local Path`

## Do I need Remote Path Mappings

- If Radarr and your download client are not on the same server/system.
- If you use either merged local/remote setups using mergerfs or similar
- You run dockers and **DON'T** have Consistent and well planned paths.

!!! note
    If you run dockers it would be smarter to fix the problem at the source what's causing the actual issue.

    - [Radarr Wiki Servarr - Docker Guide](https://wiki.servarr.com/Docker_Guide#Consistent_and_well_planned_paths)

    - [TRaSH Guides](/Misc/how-to-set-up-hardlinks-and-atomic-moves/)

------

## How do I recognize that I need remote path mappings

Your download stays in your download client and Radarr doesn't want to import it.

Go to `Activity` => `Queue`

You will see a orange download icon, hover with your mouse over it and you will get a error that looks a bit like this.

![!rpm-activity-waiting-for-import](images/rpm-activity-waiting-for-import.png)

Go to `System` => `Events`

You will see somewhere a error that looks a bit like this.

![!rpm-system-events](images/rpm-system-events.png)

The following error could also mean that you need remote path mapping

![!rpm-health-issue](images/rpm-health-issue.png)

So looking at these screenshot it seems you need to make use of Remote Path Mappings.

------

## How do I setup remote path mappings

Go to `Settings` => `Download Clients`

Scroll all the way down where you see `Remote Path Mappings` and click on the right on the plus sign.

![!rpm-settings-download-clients](images/rpm-settings-download-clients.png)

A screen will popup with the following options.

![!rpm-add-rpm](images/rpm-add-rpm.png)

1. `Host` => This is the hostname or IP you set in your download client settings.
1. `Remote Path` => The download path that you've set in your download client.
1. `Local Path` => The path Radarr needs to access the same path.

### Host

To find what you need to put in your host

Go to `Settings` => `Download Clients`

There you open up the download client for this example I will be using SABnzbd

​    ![!rpm-sabnzbd-host](images/rpm-sabnzbd-host.png)

This is what you put in your Host in Remote Path Mapping.
This could be a `hostname`, `container name` or a `IP Address`

??? examples "Example what to add in Add Remote Path Mapping"

    ![!rpm-add-rpm-select-sabnzbd](images/rpm-add-rpm-select-sabnzbd.png)

### Remote Path

To find what you need to put in your remote path you need to open up your download client and look what you've used there as download location.

In SABnzbd go to `settings` => `Folders`

![!rpm-sabnzbd-folders-cdf](images/rpm-sabnzbd-folders-cdf.png)

??? examples "Example what to add in Add Remote Path Mapping"

    ![!rpm-add-rpm-remote-path](images/rpm-add-rpm-remote-path.png)

### Local Path

To find what you need to put in in your local path you need to know how Radarr is able to access the files your download client downloaded. And this can be done in different ways. Mounting/Network share what ever but Radarr needs to have local access to it so you need to figure this one out your self what's the best way for Radarr to access the download clients downloaded files.

Click on the browse button and browse to the location where the files are accessible for Radarr.

??? examples "Example what to add in Add Remote Path Mapping"

    ![!rpm-add-local-path](images/rpm-add-local-path.png)

The final result will look something like this.

![!rpm-final-results](images/rpm-final-results.png)

After these changes the file should be able to be imported by Radarr.
