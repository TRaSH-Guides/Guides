# How to make sure Radarr doesn't snatch Full Blurays (ISO/BDMV)

Radarr has problems to separate full Blurays from Bluray-Rips,
after some researching and  testing I found a way to solve this issue.
To make this work we need to make use of Custom Formats,
and make sure the used profile is making use of it (or better said not).

------

`Navigate to Settings => Custom Formats`

![Custom Formats](http://my.jetscreenshot.com/13737/20190130-ulr4-17kb.png)

Then click on the ![Add Custom Formats](http://my.jetscreenshot.com/13737/20190130-sjz2-0kb.png) to add a new Custom Format.

On the new popup at the bottom you have the option `Advanced` and click on `Custom`

![Advanced](http://my.jetscreenshot.com/13737/20190130-o3hd-5kb.png)

Again a new popup will appear.

Enter the following info

`Name` => `bluray`

`Format Tags` => `C_RXRQ_(AVC|VC-1|HEVC)` `M_N_REMUX`

![bluray](http://my.jetscreenshot.com/13737/20190130-n0d7-13kb.png)

**!!! NOTE: make sure the 2 tags are entered separate !!!**

Then we're going to create a profile that we're going to use,
for this example we will create a profile for Bluray-Rips 720p/1080p.

`Navigate to Settings => Profiles`

Click on the ![plus sign](http://my.jetscreenshot.com/13737/20190130-sjz2-0kb.png) to create a new profile.

`Name` => `Bluray-Rips`

`Qualities` = > check `Bluray-720p` and `Bluray-1080p`

`Cutoff` => `Bluray-1080p` **(1)**

![bluray-profile](http://my.jetscreenshot.com/13737/20190130-ynbs-19kb.png)

Scroll down to the `Custom Formats` settings.

check `None` **(1)** and make sure you didn't check `bluray` and press on `Save`.

![bluray-profile](http://my.jetscreenshot.com/13737/20190130-r0ub-9kb.png)

Now add a movie or go to a added movie and edit the wanted profile to Bluray-Rip.
When changed/saved do a manual search and you will see the full bluray's will be ignored.

------

**(1)** When you make use of other custom formats and want that the custom formats will be preferred please choose `Custom Format Cutoff` of you own custom formats and make sure you don't choose `None` at the bottom but your own custom format.

