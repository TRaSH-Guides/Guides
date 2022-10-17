# Setup proxy for certain indexers

It's not recommend to run the Starr apps though a VPN,  what can happen is that the Starr apps doesn't update the posters or metadata or you can't add new movies/tv shows, it doesn't need to happen right away. but sooner or later it can and probably will happen.

Just run VPN on the apps that actually need it, like your torrent client, and perhaps in some cases certain indexers because of region/ISP restriction.

!!! warning
    Please check the indexers rules if you're allowed to use a VPN/Proxy to access their site, being that VPN services often use shared IP it could be recognized as account sharing.

    This isn't the same as the tracker, the API/Website scraping happens on the actual site and some indexers don't allow VPN usage on their site.

In this guide i will try to explain how to setup Prowlarr to use your VPN from your torrent client.

## Enable privoxy

If you use docker you need to enable enable privoxy in you torrent client so you can use it to passthrough traffic.

Please check your used docker image how to enable privoxy.

## Add privoxy to Prowlarr

`Settings` => `indexers`

![Settings => images](images/settings-indexers.png)

Click on the + sign and select `http`

![!Add Indexers](images/add-indexer-proxy-http.png)

Add the following info

![!Add Proxy http](images/add-proxy-http.png)

1. Name of the Proxy in Prowlarr.
1. The tags for this proxy. Proxies apply to all matching (same tag) indexers. If blank this proxy applies to all indexers.
1. Host name to your torrent client.
1. Used port for privoxy (default for privoxy: 8118).
1. User name for your torrent client.
1. Password for your torrent client.
1. Test if your connection works.
1. If it works click on `Save`.

## Add privoxy to your indexer

Select the indexer that you want to use with Privoxy

![!Select Indexer](images/select-indexer.png)

Scroll down to the bottom and add the tag you've set up earlier at step 2.

![!Add tag to indexer](images/add-tag-to-indexer-privoxy.png)

Click `Test` and `Save`.

Now the indexer should be using the VPN of your torrent client.
