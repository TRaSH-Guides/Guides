# How to setup FlareSolverr

[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr){:target="_blank" rel="noopener noreferrer"} is a proxy server to bypass Cloudflare and DDoS-GUARD protection.

!!! info

    - A FlareSolverr Proxy will only be used for requests if and only if Cloudflare is detected by Prowlarr
    - A FlareSolverr Proxy will only be used for requests if and only if the Proxy and the Indexer have matching tags
    - A Flaresolverr Proxy configured without any tags or has no indexers with matching tags it will be disabled.

## Install FlareSolverr

Please follow the installation instruction from [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr#installation){:target="_blank" rel="noopener noreferrer"}

## Add FlareSolverr to Prowlarr

`Settings` => `indexers`

![Settings => images](images/settings-indexers.png)

Click on the + sign and select `FlareSolverr`

![Add Indexers](images/add-indexer-proxy-flaresolverr.png)

Add the following info

![Add Proxy FlareSolverr](images/add-proxy-flaresolverr.png)

1. Name of the Proxy in Prowlarr.
1. The tags for this proxy.
1. The full host path (include http and the port) to your FlareSolverr instance.
1. The [FlareSolver Request maxTimeout value](https://github.com/FlareSolverr/FlareSolverr#-requestget){:target="_blank" rel="noopener noreferrer"} Prowlarr should use for FlareSolverr requests. Must be between `1` second and `180` seconds (Default: `60` seconds).
1. Test if your connection works.
1. If it works click on `Save`.

## Add FlareSolverr to your indexer

Select the indexer that you want to use with FlareSolverr

![Select Indexer](images/select-indexer.png)

Scroll down to the bottom and add the tag you've set up earlier at step 2.

![Add tag to indexer](images/add-tag-to-indexer-flaresolverr.png)

Click `Test` and `Save`.

Now the indexer should be using FlareSolverr.

--8<-- "includes/support.md"
