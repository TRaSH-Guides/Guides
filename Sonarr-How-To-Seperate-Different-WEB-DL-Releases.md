# Sonarr-How-To-Seperate-Different-WEB-DL-Releases
Sonarr How To Seperate Different WEB-DL Releases (iTunes.WEB-DL, AMZN.WEB-DL, NF.WEB-DL)

# Description

This will show you How To Seperate Different WEB-DL Releases (iTunes.WEB-DL, AMZN.WEB-DL, NF.WEB-DL) in Sonarr.

------

# Screenshots

![Seperate WEB-DL](http://my.jetscreenshot.com/13737/20180325-yrzv-14kb.png)

------

## HowTo :

Add the following to your Settings => Indexers => "Add new restriction".

Keep a eye on the tags you're using because you need to add them also to your shows when you want them as a certain release.

![Add in Show](http://my.jetscreenshot.com/13737/20180325-dzdf-24kb.png)



#### NOTE:

The reason why  i've added "RARBG" as "Must not contain" is because I dislike retagged releases,

### AMZN.WEB-DL

- Must contain: AMZN.WEB-DL
- Must not contain: RARBG, -BAMBOOZLE
- Tags: amzn-webdl 

![AMZN.WEB-DL](http://my.jetscreenshot.com/13737/20180325-vgf2-12kb.png)



### NF.WEB-DL

- Must contain: NF.WEB-DL
- Must not contain: RARBG, -BAMBOOZLE
- Tags: nf-webdl 

![NF.WEB-DL](http://my.jetscreenshot.com/13737/20180325-poqf-12kb.png)



### WEB-DL

- Must contain: WEB-DL 
- Must not contain: WEBRip, -focus, x264, AMZN, -CTL, -PLAYREADY, Amazon.WEB DL, Amazon, -QoQ, -TBS, -STRiFE 
- Tags: web-dl 

![WEB-DL](http://my.jetscreenshot.com/13737/20180920-m7bx-24kb.png)

#### NOTE:

The "Must not contain" names/groups are there because they don't release iTunes WEB-DL or the ones you find are mislabeld or stripped/re-encoded like the -TBS releases.



