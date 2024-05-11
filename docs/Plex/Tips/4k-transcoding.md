# JBOPS 4K Transcode Stopping with Tautulli

## Introduction

The bane of Plex admins existence... 4K Transcodes. According to Plex's forum post [_The Rules of 4K_](https://forums.plex.tv/t/info-plex-4k-transcoding-and-you-aka-the-rules-of-4k/378203) the first three rules of collecting 4k content is don’t bother transcoding 4k.

This guide will walk you through getting started with Tautulli and JBOPS. By the end of this guide you'll be able to stop all 4K video transcodes on your server. Note that this does require a [Plex Pass](https://www.plex.tv/plex-pass/) to work.

## Getting Started

`git clone https://github.com/blacktwin/JBOPS` into the config dir of your tautulli instance (if dockerized)
Install requirements if needed (`pip install -r requirements.txt`)

Go to your tautulli and go to the settings menu. In the sidebar, open “Notification Agents”. Create a new Notification Agent.

## Configuration Tab

```plaintext
Script Folder: /config/JBOPS
Script File: killstream/kill_stream.py
Script Timeout: 30 (default)
Description (optional): 4K Transcode Stopper
```

## Triggers

```plaintext
☑️ Playback Start
☑️ Playback Resume
☑️ Transcode Decision Change
```

## Conditions

```plaintext
Condition {1}
Video Decision is transcode

Condition {2}
Video Resolution is 4k

Condition Logic
{1} and {2}
```

## Arguments

Under each: Playback Start, Playback Resume, Transcode Decision Change

```plaintext
--jbop stream --username {username} --sessionId {session_id} --killMessage 'Transcoding streams are not allowed for {video_resolution} streams.'
```
