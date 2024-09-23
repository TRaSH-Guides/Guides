<!-- markdownlint-disable MD041-->
## Why port-forwarding

To seed content effectively, it is necessary to have some form of port-forwarding enabled.
This can vary depending on whether you use a VPN or not and/or what router or firewall
you have.

### How to port-forward

=== "VPN Service"
    Please consult your VPN Service and/or your VPN container documentation for specifics.

    For Torguard we've created instructions on how to [setup port-forwarding](/Misc/How-to-setup-Torguard-for-port-forwarding/){:target="\_blank" rel="noopener noreferrer"}.

    #### How to Check if Your VPN is Working

    Download one of the test .torrents or magnet links from one of the following sites:

    - [ipleak.net](https://ipleak.net/){:target="\_blank" rel="noopener noreferrer"}
    - [TorGuard's “Check My Torrent IP”](https://torguard.net/checkmytorrentipaddress.php){:target="\_blank" rel="noopener noreferrer"}

    Add the magnet link to your torrent client and wait for the results. It should show you a different IP than your WAN IP number. Remember this IP because you will need it to [check if your port is open or closed](#how-to-check-if-a-port-is-open-or-closed).

=== "Router"
    Please consult your router manual for specifics or check if your router can be found on [Port Forward](https://portforward.com/router.htm){:target="\_blank" rel="noopener noreferrer"}.

#### How to Check if a Port is Open or Closed
<!-- markdownlint-disable MD051-->
Use the free online [Open Port Check Tool](https://canyouseeme.org/){:target="\_blank" rel="noopener noreferrer"} to check if your port is open. If you're using a VPN and have forwarded your port with the VPN service, then use the IP you got from [How to Check if Your VPN is Working](#how-to-check-if-your-vpn-is-working) and the port you used to forward. If you're not using a VPN service, use your WAN IP address and the port you used to forward.
<!-- markdownlint-enable MD041 MD051-->
