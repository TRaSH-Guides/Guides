# Port Forwarding Troubleshooting

Is your torrent client **not connectable** — or barely uploading and seeding? That almost
always means the internet can't reach your client on its port. This page walks you through
finding and fixing it, one step at a time.

It does **not** repeat the per-client setup steps — for those, see the setup guides for
[qBittorrent](/Downloaders/qBittorrent/Port-forwarding/) and
[Deluge](/Downloaders/Deluge/Port-Forwarding/).

!!! info "Usenet users"

    Port forwarding is a **BitTorrent** concern. Usenet (SABnzbd/NZBGet) downloads over
    outbound connections only and never needs an inbound forwarded port.

## Why it matters

If other peers can't connect **to** you, your client can only reach **out** — so it misses most
of the swarm, grabs from fewer sources, and can barely seed. Fixing this is what gets your
speeds and ratio up.

Under the hood, the BitTorrent protocol treats "can't receive inbound connections" as a named
condition: the
[Holepunch extension (BEP 55)](https://www.bittorrent.org/beps/bep_0055.html){:target="_blank" rel="noopener noreferrer"}
exists specifically to work around *"peers that cannot receive inbound connections."*
qBittorrent reports it as a **firewalled** / not-connectable status.

!!! tip "The golden rule"

    The port your client **listens** on and the port **forwarded** at your router (or VPN
    server) must be the **same number**. If they differ, the client advertises the wrong port
    to trackers and DHT and receives no incoming connections.

## Step 1 — Confirm the client is actually listening

Before blaming the network, confirm the client is bound and listening on the expected port.

=== "Linux"

    ```bash
    sudo ss -tlnp | grep <port>
    ```

=== "Windows"

    ```bat
    netstat -ab
    ```

If the port is not listed, fix the client's own configuration (or host firewall, below)
first — the external path cannot work if nothing is listening locally.

## Step 2 — Test the port from outside

Use [canyouseeme.org](https://canyouseeme.org/){:target="_blank" rel="noopener noreferrer"},
*"a free utility for remotely verifying if a port is open or closed … useful for users who
wish to verify port forwarding."* Enter your forwarded port.

!!! warning "Testing while on a VPN"

    When connected to a VPN, your public IP is the **VPN's exit IP**, not your home IP. The
    test must check the port on that exit IP — test it while the VPN is connected, using the
    port your VPN provider forwarded.

## Step 3 — Allow the port on the host firewall

The download client's host must permit inbound traffic on the listening port.

| Environment | Where to allow the port |
| --- | --- |
| **Native Ubuntu / Linux** | `ufw` / `firewalld` (or the distro's firewall) — allow the listening port |
| **Windows** | Windows Defender Firewall → Inbound Rules → allow the listening port |
| **unRAID** | Containers publish the port via the Docker template; confirm the host port mapping matches the client's listening port |

## Step 4 — Forward the port through your network

Where you forward the port depends on the hardware between your client and the internet. First,
identify what you have:

- **Modem** — converts the ISP signal to Ethernet and nothing else; it performs no NAT, so there is nothing to forward on a pure modem.
- **Router** — performs NAT, firewall, and DHCP. Port forwards always live on a router.
- **ISP gateway** (combo unit) — a modem and router in one box, common with ISP-supplied equipment. It performs NAT, so forwards happen on it unless you bridge it.

In every case the *golden rule* holds: forward the **single** listening port (TCP, plus UDP if
your client uses it) to the host running the client, and never use UPnP or DMZ (see below).
[portforward.com](https://portforward.com/){:target="_blank" rel="noopener noreferrer"} has
model-specific steps for most routers and gateways.

### Your own router behind a pure modem

The simplest case — a single NAT. Forward the listening port on your router to the client's
host. A pure modem needs no configuration.

### ISP gateway (combo unit), no second router

Your ISP's box performs the NAT, so forward the listening port on the gateway's own admin page
to the client's host.

### ISP gateway *and* your own router (double-NAT)

Two devices perform NAT in series, so a forward on your router alone never receives traffic.
**Detect it** by checking your router's **WAN IP**: if it is a private
[RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918){:target="_blank" rel="noopener noreferrer"}
address (`10.x.x.x`, `172.16–31.x.x`, or `192.168.x.x`), the gateway upstream is doing NAT too.

**Preferred fix:** put the ISP gateway in **bridge mode** (sometimes called *IP passthrough*).
This disables its NAT/DHCP/routing and passes the public IP straight to your router, collapsing
the two NATs into one — then forward on your router exactly as in the first scenario.

If the gateway offers no bridge mode, you must forward **twice**: on the gateway, forward the
port to your router's WAN IP; then on your router, forward it on to the client. Bridge mode is
strongly preferred — it removes a NAT layer and a point of failure.

!!! note

    Bridge mode is a network-configuration concept rather than a security topic, so it is
    documented by ISP and router vendors rather than by a standards body; the exact name and
    steps vary per device. Consult your ISP's documentation.

### Behind CGNAT (Carrier-Grade NAT)

If your ISP places you behind CGNAT, **inbound port forwarding is impossible** — your gateway's
public-facing address is itself inside the ISP's NAT, so a forward never reaches you.

**Detect it:** compare the WAN IP shown on your router or gateway to your public IP (from any
*"what is my IP"* service). If they differ you are behind an upstream NAT; if the WAN IP falls
in **`100.64.0.0`–`100.127.255.255`**, that is the
[RFC 6598](https://datatracker.ietf.org/doc/html/rfc6598){:target="_blank" rel="noopener noreferrer"}
*Shared Address Space* reserved for CGNAT — a definitive sign.

**Options:** ask your ISP for a non-CGNAT / static public IP (often available, sometimes for a
fee), or use a VPN that supports port forwarding (below).

!!! danger "Never use UPnP or DMZ to do this"

    Forward **one specific port**. Do **not** use UPnP or the router's DMZ host as a shortcut.

    - **UPnP** lets any device on your network open inbound ports with **no authentication**. CISA advises users to *"disable UPnP"* on home networks, and it has a history of serious flaws — [CVE-2020-12695 "CallStranger"](https://nvd.nist.gov/vuln/detail/CVE-2020-12695){:target="_blank" rel="noopener noreferrer"} (CVSS 7.5) and [CERT/CC VU#357851](https://www.kb.cert.org/vuls/id/357851){:target="_blank" rel="noopener noreferrer"} (routers accepting UPnP requests from the internet, CVSS 9.4).
    - **DMZ host** forwards **all** unsolicited inbound ports to one device, bypassing the firewall entirely. Router vendors say so plainly: NETGEAR warns it *"removes all of your router's firewall protection for a device"* and to instead use [port forwarding so *"only the specific ports that are needed are opened"*](https://kb.netgear.com/25891/What-is-the-De-Militarized-Zone-DMZ-feature-on-my-NETGEAR-router){:target="_blank" rel="noopener noreferrer"}; [TP-Link](https://www.tp-link.com/us/support/faq/28/){:target="_blank" rel="noopener noreferrer"} describes the DMZ host as *"totally exposed to the internet … with all ports opened."*

## Using a VPN

If you route your client through a VPN, the port must be forwarded **by the VPN provider**, and
not all providers offer this:

- **ProtonVPN** supports it on its P2P servers; note that [*"the port number usually changes when you reconnect … you'll need to update your torrent client"*](https://protonvpn.com/support/port-forwarding){:target="_blank" rel="noopener noreferrer"}.
- **AirVPN** supports it via its Client Area → Ports menu.
- **Mullvad removed port-forwarding support**, with all forwards [discontinued as of 1 July 2023](https://mullvad.net/en/blog/removing-the-support-for-forwarded-ports){:target="_blank" rel="noopener noreferrer"}.

Bind the client to the VPN so it cannot leak or connect when the VPN drops. The
[qBittorrent guide](https://github.com/qbittorrent/qBittorrent/wiki/How-to-bind-your-vpn-to-prevent-ip-leaks){:target="_blank" rel="noopener noreferrer"}
recommends selecting *"the name of the VPN's adapter under the Network Interface drop down box."*

!!! warning "About ISP port throttling"

    A common belief is that ISPs throttle the default BitTorrent ports `6881`–`6889` by number,
    so changing your port speeds things up. The documented cases of ISP interference (e.g. the
    2007–2008 Comcast/FCC case) used **protocol inspection**, not port-number blocking — so
    changing your port is **not** a reliable fix for throttling, even though using a
    non-default port is reasonable practice.

--8<-- "includes/support.md"
