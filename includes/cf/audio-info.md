??? info "I've a AppleTV - [Click to show/hide]"

    ![!Audio Formats Flowchart](/Radarr/images/plex-audio-atv.png)

    - Passthrough: The preferred method if you have an audio setup (AVR/Soundbar). This mode will send the audio signals without any alteration or processing.
    - Direct Play: The client supports the container, video stream, and audio stream natively. The Plex server simply sends the media file as-is to the client. This uses very little CPU power.
    - Transcode: The client does not support the video stream and/or the audio stream. The Plex server re-encodes the video, audio, or both into a compatible format. Transcoding video uses a lot of CPU power, but transcoding audio uses little to moderate CPU power.
    - Decodes: Decompresses the audio before sending it to your AVR/Soundbar.

    *partial used source: [Infuse FAQ](https://support.firecore.com/hc/en-us/articles/217735707-Audio-Options-tvOS#h_01HE1Z5XNJZK5YTF1SVTPS0MTR){:target="_blank" rel="noopener noreferrer"}*

??? info "Am I losing any quality by using LPCM? - [Click to show/hide]"

    - No. Since LPCM is a lossless format, using it will result in no loss of quality. What your ears hear will be exactly the same. The only difference is your receiver will recognize the audio stream as PCM instead of Dolby/DTS.
    - LPCM will discard object and spatial metadata. (TrueHD Atmos, DTS-X)

    *source: [Infuse FAQ](https://support.firecore.com/hc/en-us/articles/217735707-Audio-Options-tvOS#h_01HE1Z5XNJZK5YTF1SVTPS0MTR){:target="_blank" rel="noopener noreferrer"}*

??? info "Should I block certain audio formats because something in my setup doesn't support it? - [Click to show/hide]"

    If you have chosen a profile that includes Audio Formats, it's somewhat pointless to lower the scores or block certain audio formats since 95% of the Remuxes and UHD Encodes provide HD audio formats such as TrueHD Atmos, TrueHD, and DTS-X.

    So you have 2 options.

    1. Choose another quality profile that doesn't include audio formats such as `HD Bluray + WEB` or `2160p WEB-DL`.
    1. Accept the limitations of your audio setup (AVR/Soundbar) and/or your hardware media player device.
