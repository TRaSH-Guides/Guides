# How To Set Up

This section will show several how-to guides for installing the Starr Apps.
This is all done in a way to achieve [Hardlinks and Instant Moves (Atomic-Moves)](/File-and-Folder-Structure/Hardlinks-and-Instant-Moves/).

## Folder Setup

Before you proceed to setup in either of these installation methods, having a folder on your drive would be good to have.

## Linux/MacOS

Here's a quick one-liner that replicates the folder structure mentioned in this guide:

```bash
mkdir -p data/{torrents/{books,movies,music,tv},usenet/{incomplete,complete/{books,movies,music,tv}},media/{books,movies,music,tv}}
```

## Windows (Not Recommended)

you can use a powershell script to do this:

```powershell
New-Item -ItemType Directory -Force -Path `
"D:\data\torrents\books",
"D:\data\torrents\movies",
"D:\data\torrents\music",
"D:\data\torrents\tv",
"D:\data\usenet\incomplete",
"D:\data\usenet\complete\books",
"D:\data\usenet\complete\movies",
"D:\data\usenet\complete\music",
"D:\data\usenet\complete\tv",
"D:\data\media\books",
"D:\data\media\movies",
"D:\data\media\music",
"D:\data\media\tv"
```

Just replace your path with the paths you would like to have.

## Installing the *arr stack

Select your desired method of installation:

- [Docker](/File-and-Folder-Structure/How-to-set-up/Docker/)
- [Dockstarter](/File-and-Folder-Structure/How-to-set-up/Dockstarter/)
- [Native](/File-and-Folder-Structure/How-to-set-up/Native/)
- [Synology](/File-and-Folder-Structure/How-to-set-up/Synology/)
- [TrueNAS Core](/File-and-Folder-Structure/How-to-set-up/TrueNAS-Core/)
- TrueNAS Scale users can follow the same concepts as the Docker method until someone provides a guide and is willing to maintain and support it in the Guide Discord.
- [Unraid](/File-and-Folder-Structure/How-to-set-up/Unraid/)
- [Windows](/File-and-Folder-Structure/How-to-set-up/Windows/)

--8<-- "includes/support.md"
