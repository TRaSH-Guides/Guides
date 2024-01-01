# Setup TorGuard for port forwarding

!!! note
    These settings are a recommendation if you want to choose other settings be my guest.

    If you want to support me, please use this [referral link](https://torguard.net/aff.php?aff=5575){:target="_blank" rel="noopener noreferrer"} and enter the following discount code:

    Get 50% Off ALL Plans (Anonymous VPN, Anonymous VPN Pro, Anonymous VPN Premium)

    ```
    TRaSH-Guides-2024
    ```

    [![torguard-FreeTrial-270x90](images/torguard/torguard-FreeTrial-728x90.gif)](https://torguard.net/aff.php?aff=5575){:target="_blank" rel="noopener noreferrer"}

    !!! bug ""
        As of 13 March Torguard Settles Piracy Lawsuit and has agreed to use commercially reasonable efforts to block BitTorrent traffic on its servers in the US using firewall technology. :bangbang:

        I Talked to several people and they are still able to use Torguard for Torrents, Perhaps because the connection is encrypted. And others just selected a server in another country.

        !!! warning "If the US server doesn't work for you use another country"

        [Source Torguard](https://torguard.net/blog/why-torguard-is-blocking-bittorrent-on-us-servers/){:target="_blank" rel="noopener noreferrer"}.

        [Source Torrentfreak](https://torrentfreak.com/torguard-settles-piracy-lawsuit-and-agrees-to-block-torrent-traffic-on-u-s-servers-220314/){:target="_blank" rel="noopener noreferrer"}.

------

## Login to your Client area

Login to your [Client Area](https://torguard.net/clientarea.php){:target="_blank" rel="noopener noreferrer"}.

??? success "Example - [Click to show/hide]"
    ![!Client Area Login](images/torguard/client-area-login.png)

### Create a user account

First we're going to create a [User Account](https://torguard.net/clientarea.php?action=changepw){:target="_blank" rel="noopener noreferrer"} for your VPN so we won't need to use your main account that you use to login to your account on the Torguard site.
This account will be used for authentication with your VPN Torrent client.

`Services` > `My Services` > `Manage` > `Manage Credentials`

??? success "Example - [Click to show/hide]"
    ![!Services > My Services](images/torguard/services-my-services.png)

    ![!Client Area Manage Credentials](images/torguard/client-area-manage-credentials.png)

Create a new username and choose a secure password or create a random username and password.

??? success "Example - [Click to show/hide]"
    ![!Create User Account](images/torguard/create_user_account.png)

------

## How to get the IP of your VPN server

Now it's time to get the IP of your VPN server you're going to use from the [Global VPN Network](https://torguard.net/network/){:target="_blank" rel="noopener noreferrer"}, From your Client Area.

`Servers` > `Global VPN Network`

??? success "Example - [Click to show/hide]"
    ![!Servers > Global VPN Network](images/torguard/servers-globalvpnnetwork.png)

### Global VPN Network

Then we're going to select which server we're going to use,

For the best speed it's recommended to choose the one nearest to your location.

!!! tip ""
    Sometimes you get better speeds if you use one of your neighboring countries.

!!! warning "If the US server doesn't work for you use another country"

Let's use for this example: `USA Miami` and copy/paste the Hostname `us-fl.torguard.org`.

![!Torguard Global VPN Network](images/torguard/globalvpnnetwork-list.png)

!!! tip
    Also check if your chosen server supports OpenVPN or Wireguard depending what you want to use.

### Get your VPN IP

Open a cmd window or something equal and type:

```bash
    ping us-fl.torguard.org
```

You will then get the IP of the server.
Remember that for later use.

??? success "Example - [Click to show/hide]"
    ![!ping](images/torguard/cmd-ping.png)

------

## How to setup Port forwarding

!!! note
    This section will consist of 2 parts depending if you want to use OVPN or WireGuard so make sure you choose your preferred VPN Tunnel type.

### Port Forward Request

From your Client Area go to your [My Services](https://torguard.net/clientarea.php?action=products){:target="_blank" rel="noopener noreferrer"}.

Then click on `Manage` and select `Port Forward Request`.

`Services` > `My Services` > `Manage` > `Port Forward Request`

??? success "Example - [Click to show/hide]"
    ![!Port Forward Request](images/torguard/req_port_fwd.png)

### VPN Tunnel Type

Choose your preferred VPN Tunnel type.

#### OVPN Request Port Forward

??? abstract "OVPN Request Port Forward"

    ![!Request New Port Forward OVPN](images/torguard/request-new-pfw-ovpn.png)

    1. That's the `IP` we found earlier.
    1. Select `UDP`.
    1. Select a `Port/Auth` I personally use `995|SHA1`.
    1. Select the `Protocol` `TCP`.
    1. I suggest to use a high `Port` number 10.000+ or a game port you don't use, don't use the default torrent ports 6881- 6889
        (This is also the port you will use in your torrent client).
    1. Click on the `+` sign and do the same with the `UDP` `Protocol`.
    1. Then click on `Submit Request`.

    If everything went according to plan you will see something like this.

    ![status](images/torguard/status.png)

    You will also receive a e-mail with the ports you forwarded.

    !!! Note
        Normally it doesn't take more then a few seconds/minutes to get the ports approved if it takes longer or you get `PENDING` I suggest to ping the server again (or choose another sever) and you often get a new IP and retry it again with the new IP.

#### WireGuard Request Port Forward

??? abstract "WireGuard Request Port Forward - [Click to show/hide]"

    ![!Request New Port Forward WireGuard](images/torguard/request-new-pfw-wireguard.png)

    1. That's the `IP` we found earlier.
    1. Select `UDP`. (:bangbang: **KEEP THIS ON UDP FOR WireGuard** :bangbang:)
    1. Select a `Port/Auth` and select `WireGuard`.
    1. Select the `Protocol` `TCP`.
    1. I suggest to use a high `Port` number 10.000+ or a game port you don't use, don't use the default torrent ports 6881- 6889
        (This is also the port you will use in your torrent client).
    1. Click on the `+` sign and do the same with the `UDP` `Protocol`.
    1. Then click on `Submit Request`.

    !!! warning "WARNING"
        :bangbang: DON'T CHANGE OPTION 2 `UDP` to `TCP` :bangbang:

    If everything went according to plan you will see something like this.

    ![status](images/torguard/status.png)

    You will also receive a e-mail with the ports you forwarded.

    !!! Note
        Normally it doesn't take more then a few seconds/minutes to get the ports approved if it takes longer or you get `PENDING` I suggest to ping the server again (or choose another sever) and you often get a new IP and retry it again with the new IP.

------

## How to create the config file

!!! note
    This section will consist of 2 parts depending if you want to use OVPN or WireGuard so make sure you choose your preferred VPN Tunnel type.

From your Client Area go to your [Config Generator](https://torguard.net/tgconf.php?action=vpn-openvpnconfig){:target="_blank" rel="noopener noreferrer"}.

`Tools` > `Config Generator`

??? success "Example Select Tools > Config Generator - [Click to show/hide]"
    ![!Tools - Config Generator](images/torguard/tools-config-generator.png)

### Config Generator

Choose your preferred VPN Tunnel type.

#### OVPN Config Generator

??? abstract "OVPN Config Generator - [Click to show/hide]"

    ![!OVPN Config Generator](images/torguard/config-generator-ovpn.png)

    1. Keep this on `Default`.
    1. Choose `OpenVPN`.
    1. Choose the `IP` we got earlier and used for the port forwarding.
    1. Choose `UDP`.
    1. Choose `995|SHA1` or what you selected during the port forwarding.
    1. Choose `AES-128-GCM`.
    1. Choose `2.4 and above`.
    1. Check `Require TLS 1.2`
    1. Click on `Generate Config`,

    Now you will download a `.conf` file with a random number.

    Rename the extension from `*.conf` to `*.ovpn` and copy it to your openvpn folder of your VPN torrent client.

#### WireGuard Config Generator

??? abstract "WireGuard Config Generator - [Click to show/hide]"

    ![!WireGuard Config Generator](images/torguard/config-generator-wireguard.png)

    1. Choose `WireGuard`.
    1. Choose the `IP` we got earlier and used for the port forwarding.
    1. Add your `VPN Username`.
    1. Only Change this if you know what you're doing :bangbang:
    1. Click on `Generate Config`

    Now you will download a `.conf` file with a random number.

    Rename the file from `*.conf` to `wg0.conf` and copy it to your wireguard folder of your VPN torrent client.

------

Thanks:

A big Thanks to [mrhotio](https://github.com/mrhotio) for his excellent instructions on how to setup WireGuard for TorGuard.

{! include-markdown "../../includes/support.md" !}
<!-- --8<-- "includes/support.md" -->
