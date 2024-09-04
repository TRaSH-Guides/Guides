# Installing

## Introduction

Deluge is an open-source cross-platform torrent client written in Python. It has been around since 2006 and offers many features that, while niche, many consider to be critical to their setups.

---

## Installation

Information sourced mostly from [Deluge's Downloads Page](https://dev.deluge-torrent.org/wiki/Download)

### Windows

You can find the latest Windows installers [here](https://ftp.osuosl.org/pub/deluge/windows/?C=M;O=D)

!!! note

    `lt2.0` in the filename means the installer includes libtorrent 2.0.x instead of the older 1.2.x

### Linux (Native)

Due to most default OS repositories being outdated, we recommend using Deluge's repositories to install the latest version.

Using `apt-get` to install

        sudo add-apt-repository ppa:deluge-team/stable
        sudo apt-get update
        sudo apt-get install deluge

Using `pip3` to install (included in the Python package)

        pip3 install deluge

!!! info

    You can find this project's pip repo @ [pypi.org/project/deluge/](https://pypi.org/project/deluge/)

!!! Advanced

    If you want to install deluged as a service, documentation can be found [here](https://deluge.readthedocs.io/en/latest/how-to/systemd-service.html)

### Docker Containers

[LinuxServer.io](https://hub.docker.com/r/linuxserver/deluge)

[BinHex](https://hub.docker.com/r/binhex/arch-deluge)

[BinHex VPN](https://hub.docker.com/r/binhex/arch-delugevpn)

--8<-- "includes/support.md"
