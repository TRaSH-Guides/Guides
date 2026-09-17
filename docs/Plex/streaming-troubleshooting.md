# Streaming and Buffering Troubleshooting

Buffering, stuttering, or a stream that keeps dropping quality almost always has one of a
handful of causes: the client's connection, a forced transcode, server resources, or the
remote-access path. [Tautulli](https://tautulli.com/){:target="_blank" rel="noopener noreferrer"}
and [Tracearr](https://tracearr.com/){:target="_blank" rel="noopener noreferrer"} both show you
what a stream is actually doing, which turns "it's buffering" into a specific, fixable cause.

This page explains what each tool shows and how to read it. It links to Plex's own
troubleshooting articles, and ends with an FAQ table of common causes and fixes.

!!! info "Jellyfin/Emby"

    Tracearr also monitors Jellyfin and Emby. The same reasoning applies: check the stream's
    decision (direct play vs transcode) and bandwidth before assuming a server or network
    problem.

## Reading Tautulli

[Tautulli](https://tautulli.com/){:target="_blank" rel="noopener noreferrer"}
([docs](https://docs.tautulli.com/){:target="_blank" rel="noopener noreferrer"}) is a monitoring
and tracking tool for a single Plex Media Server. Its **Activity** tab (and the **History** tab
for past sessions) is the first place to look at a stream in trouble.

For each active stream, Tautulli shows:

- **Decision** - `Direct Play`, `Direct Stream`, or `Transcode`. This is the single most useful
    field: `Direct Play` sends the file as-is, no server work involved. `Direct Stream` remuxes
    the container and can transcode audio and other non-video components, so it is still some
    server work even though the video itself isn't re-encoded. `Transcode` converts the video
    (and/or audio) to a format the client can play. See Plex's
    [Direct Play and Direct Stream](https://support.plex.tv/articles/200250387-streaming-media-direct-play-and-direct-stream/){:target="_blank" rel="noopener noreferrer"}
    and [Transcoding Media](https://support.plex.tv/articles/200250377-transcoding-media/){:target="_blank" rel="noopener noreferrer"}
    articles for the full breakdown.
- **Transcode reason** - Hovering or expanding the stream shows *why* Plex chose to transcode
    (video codec, audio codec, subtitle burn-in, bitrate too high for the set quality, etc).
- **Bandwidth** - Total stream bandwidth, split into LAN and WAN where relevant.
- **Location** - `LAN` or `WAN`, and whether the connection is relayed (secure/direct vs relay).
- **User / Player / Platform / IP** - Who is watching, on what app and device, and from where.
- **Quality profile** - The bitrate/resolution ceiling the client (or a manual override) has
    requested.

!!! tip "Read the stream stats before assuming the cause"

    - `Direct Play` with low bandwidth on a LAN device points at the client or its Wi-Fi, not the server.
    - `Transcode` with high CPU usage points at the server or a client compatibility gap.
    - `WAN` with a `relay` connection points at remote access.

## Reading Tracearr

[Tracearr](https://tracearr.com/){:target="_blank" rel="noopener noreferrer"}
([docs](https://docs.tracearr.com/){:target="_blank" rel="noopener noreferrer"}) is a
multi-server monitoring platform covering Plex, Jellyfin, and Emby from one dashboard. It covers
the same ground as Tautulli, plus fleet-wide analytics:

- **Session tracking** - Who watched what, when, where, and on which device, per server.
- **Stream analytics** - Direct play vs transcode breakdown, bandwidth usage, and per-stream
    codec/resolution/device-compatibility scores.
- **Server health** - Live CPU, memory, and bandwidth charts per server, useful for confirming
    whether a transcode is actually starving the server of resources.
- **Stream map** - Geolocation of where streams originate, useful for spotting an unexpectedly
    remote or relayed connection.
- **Automations** - Rules that fire on a condition (for example, too many concurrent streams
    from one account) and notify a destination (Discord, ntfy, webhook, email, mobile push, etc)
    or stop the stream outright.

Use Tracearr the same way as Tautulli for a single stream: check the decision and bandwidth
first. Lean on Tracearr over Tautulli when the fleet has more than one media server, or when you
want an automated notify/kill rule instead of checking manually.

!!! note "Gap"

    This page describes Tracearr's monitoring and stop-stream automation action as documented by
    the project. If your specific automation setup or notification routing behaves differently,
    check [docs.tracearr.com](https://docs.tracearr.com/){:target="_blank" rel="noopener noreferrer"}
    rather than assuming this page covers your configuration.

## Plex's own troubleshooting articles

Plex maintains its own support articles that go deeper on how streaming decisions and transcoding
work:

- [Why Is My Video Stream Buffering?](https://support.plex.tv/articles/201575036-why-is-my-video-stream-buffering/){:target="_blank" rel="noopener noreferrer"}
- [Streaming Overview](https://support.plex.tv/articles/200430303-streaming-overview/){:target="_blank" rel="noopener noreferrer"}
- [Streaming Media: Direct Play and Direct Stream](https://support.plex.tv/articles/200250387-streaming-media-direct-play-and-direct-stream/){:target="_blank" rel="noopener noreferrer"}
- [Transcoding Media](https://support.plex.tv/articles/200250377-transcoding-media/){:target="_blank" rel="noopener noreferrer"}
- [Using Hardware-Accelerated Streaming](https://support.plex.tv/articles/115002178853-using-hardware-accelerated-streaming/){:target="_blank" rel="noopener noreferrer"}
- [How Do Streaming Quality Selections Work?](https://support.plex.tv/articles/203810306-how-do-streaming-quality-selections-work/){:target="_blank" rel="noopener noreferrer"}
- [Server Settings: Bandwidth and Transcoding Limits](https://support.plex.tv/articles/227715247-server-settings-bandwidth-and-transcoding-limits/){:target="_blank" rel="noopener noreferrer"}
- [Troubleshooting Remote Access](https://support.plex.tv/articles/200931138-troubleshooting-remote-access/){:target="_blank" rel="noopener noreferrer"}

## Speed tests

A speed test tells you what a connection can actually do right now, separate from anything
Tautulli or Tracearr report about the stream itself. Where you run it matters:

- Run it **on the Plex server's connection** to check upload. Upload is the number that limits a
    remote (WAN) stream, since the server is uploading the stream out to the remote client.
- Run it **on the client's connection** to check download, since that's what limits how fast the
    client can pull the stream in.

- [Speedtest by Ookla](https://www.speedtest.net/){:target="_blank" rel="noopener noreferrer"} -
    the most common test; reports upload, download, latency, and jitter against a nearby server.
- [Cloudflare Speed Test](https://speed.cloudflare.com/){:target="_blank" rel="noopener noreferrer"} -
    runs against Cloudflare's network. Useful as a second data point if Ookla's result looks off.
- [fast.com](https://fast.com/){:target="_blank" rel="noopener noreferrer"} (Netflix) -
    download-focused, a quick sanity check on the client side.
- [Troubleshooting Remote Access](https://support.plex.tv/articles/200931138-troubleshooting-remote-access/){:target="_blank" rel="noopener noreferrer"}
    covers what Plex itself checks on the server side for remote access and bandwidth.

### Speed test commands

```bash
# Ookla CLI (official) - run on the server for upload, on the client for download
speedtest

# Python speedtest-cli (community, useful where the Ookla CLI isn't packaged)
pip install speedtest-cli
speedtest-cli

# LAN throughput between two hosts, isolates a weak Wi-Fi/LAN link from an ISP problem
# on the server (or another wired LAN host):
iperf3 -s
# on the client, replace with the server's LAN IP:
iperf3 -c 192.168.1.10

# quick one-off throughput check against a public test file
curl -o /dev/null -w 'Speed: %{speed_download} bytes/sec\n' https://proof.ovh.net/files/100Mb.dat
```

If `iperf3` between the server and client is fast on the LAN but a Plex stream still buffers, the
cause is the ISP connection or Plex's own bandwidth limit, not the LAN. If `iperf3` itself is
slow, the LAN or Wi-Fi link is the problem, before the ISP even enters the picture.

## FAQ: Common causes and fixes

| Symptom | Likely cause | How to confirm (Tautulli/Tracearr) | Fix |
| --- | --- | --- | --- |
| Buffers or stutters on one specific device, others are fine | Weak client Wi-Fi (2.4GHz congestion, TV far from the access point, wall/floor obstruction) | Stream shows `Direct Play`/`Direct Stream` (not a transcode) with low or fluctuating bandwidth. `LAN` only confirms the Plex connection path is local, not that the client's own Wi-Fi link is healthy, so treat this as pointing at the client side rather than definitive proof | Move the AP closer, switch the TV/device to 5GHz or wired Ethernet, or add an access point. See [What does my media player support](/Plex/what-does-my-media-player-support/) for devices with reliable wired/Wi-Fi track records |
| Plays fine on some apps, transcodes on others for the same file | The client cannot direct play/direct stream the media (unsupported codec/container), or its quality setting requires a lower bitrate. Only genuinely "a transcode it doesn't need" when another compatible client plays the same file without transcoding | Tautulli/Tracearr `Decision` shows `Transcode` with a stated reason (video/audio codec, subtitle) even though the file plays natively elsewhere | Check the client's supported codecs, use a client/app known to direct play the format (see [What does my media player support](/Plex/what-does-my-media-player-support/)), or fix the file's audio/subtitle track |
| Multiple simultaneous streams buffer, single streams are fine | Server CPU/GPU can't keep up with concurrent transcodes | Tracearr shows CPU utilization, and GPU utilization where the platform reports it, climbing as concurrent transcodes stack up; Tautulli shows multiple `Transcode` sessions at once with degraded transcode speed/health | Reduce concurrent transcodes (lower `Maximum simultaneous video transcode`), add/upgrade hardware transcoding, or get clients to direct play instead |
| Remote (away from home) streams buffer, home streams are fine | Combined WAN stream bandwidth exceeds the server's effective upload capacity, or the remote client's own download bandwidth is the bottleneck | Tautulli/Tracearr bandwidth for all concurrent WAN sessions combined approaches or exceeds the server's set upload limit, and/or the remote client's own connection can't sustain the stream's bitrate | Raise or correctly set the upload speed limit in Plex ([Server Settings: Bandwidth and Transcoding Limits](https://support.plex.tv/articles/227715247-server-settings-bandwidth-and-transcoding-limits/){:target="_blank" rel="noopener noreferrer"}), lower the remote stream's quality, or upgrade upload bandwidth |
| A particular subtitle track causes transcoding, other tracks (or no subtitles) direct play/stream | Incompatible subtitles requiring burn-in (a format or track the client can't render natively) force a video transcode; a compatible subtitle format can direct play/stream without one | Tautulli/Tracearr shows `Transcode` with the reason tied to that specific subtitle track/format | Use a client with native subtitle support, convert subtitles to a supported format, or accept the transcode cost |
| Remote streams always look worse than expected | Remote/mobile quality cap set too low in the app or account settings | Tautulli/Tracearr quality profile for the session shows a lower resolution/bitrate than the source | Raise the app's remote streaming quality setting; see [How Do Streaming Quality Selections Work?](https://support.plex.tv/articles/203810306-how-do-streaming-quality-selections-work/){:target="_blank" rel="noopener noreferrer"} |
| Buffering happens at specific times of day, on a specific ISP | ISP throttling or local congestion (peak-hour contention, streaming/BitTorrent traffic shaping) | Symptom correlates with time of day rather than any Tautulli/Tracearr stream data; direct play with adequate bandwidth still buffers | Test with a wired connection at the same time and run a speed test during the issue. Degraded results point at a connectivity problem but don't by themselves prove throttling; bring the data to the ISP if the pattern persists |
| Remote streams are slow, but home streams are fast | Indirect (relayed) connection instead of a direct one | Tautulli/Tracearr shows the session as relayed rather than a secure/direct WAN connection | Try to get remote access connecting directly (port forwarding, correct public IP/port). If the ISP uses CGNAT or otherwise blocks inbound connections, a relay may be unavoidable regardless of port forwarding; see [Troubleshooting Remote Access](https://support.plex.tv/articles/200931138-troubleshooting-remote-access/){:target="_blank" rel="noopener noreferrer"} |

## Jellyfin and Kodi

This page is written for Plex, but the same direct-play-vs-transcode diagnostic applies to
[Jellyfin](https://jellyfin.org/docs/){:target="_blank" rel="noopener noreferrer"}. Kodi needs a
different approach since it's a client, not a server.

**Jellyfin** - the Dashboard's
[active devices/playback view](https://jellyfin.org/docs/general/server/devices/){:target="_blank" rel="noopener noreferrer"}
shows the same play method (Direct Play, Direct Stream, or Transcode) as Tautulli, plus the reason
a stream transcoded. Read it the same way as the Tautulli section above, and check the
[Jellyfin FAQ](https://jellyfin.org/docs/general/faq/){:target="_blank" rel="noopener noreferrer"}
for common causes. Tracearr already monitors Jellyfin (see the note near the top of this page), so
a fleet running both Plex and Jellyfin doesn't need a separate tool for this.

**Kodi** - Kodi is a client only; it has no server-side transcoding of its own. Buffering is
almost always the client's own network (weak Wi-Fi, same as the first FAQ row above) or its cache
settings, not a server problem. Kodi's
[advancedsettings.xml](https://kodi.wiki/view/Advancedsettings.xml){:target="_blank" rel="noopener noreferrer"}
controls buffer size and mode via the `<cache>` settings; see the wiki's
[video cache how-to](https://kodi.wiki/view/HOW-TO:Modify_the_video_cache){:target="_blank" rel="noopener noreferrer"}
for tuning them. A wired connection or a larger buffer clears most occasional stutter. Whether
Kodi can direct play a file at all still depends on the playback device's own codec and container
support, same as any other client.

## Related guides

- [What does my media player support](/Plex/what-does-my-media-player-support/) - community-tested
    device data (HDR/audio passthrough support), useful when a device keeps forcing a transcode
    or a Wi-Fi-only device is the recurring culprit
- [Optimal Plex Client Settings](/Plex/Tips/Optimal-plex-client-settings/) - per-client setting
    recommendations
- [Stop 4k Video Transcoding](/Plex/Tips/4k-transcoding/) - using Tautulli notification agents to
    kill unwanted 4K transcodes automatically
- [Suggested Plex Media Server Settings](/Plex/Tips/Plex-media-server/) - server-side settings
    that affect transcoding and bandwidth

--8<-- "includes/support.md"
