## Collection of Custom Formats for Radarr V3 (Aphrodite)

Here I will try to collect a collection of most needed/used Custom Formats.
That I've found on discord or created myself with the help of others.

> Keep in mind Custom Formats are made to fine tune your Quality Profile !!!
>
> Meaning: Quality Profile trumps Custom Formats !!!

With the coming of Radarr V3 Custom Formats are much more advanced/powerful than with v0.2, although this also means a Custom Format is much more complicated to setup.


------

| Audio                                    | Video                               | Misc                                    |
| :--------------------------------------- | ----------------------------------- | --------------------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [Single Layer DV](#single-layer-dv) | [BR-DISK](#br-disk)                     |
| [DTS-HD/DTS:X](#dts-hd-dts-x)            | [x264](#x264)                       | [EVO except WEB-DL](#evo-except-web-dl) |
| [DDP (non-Atmos)](#ddp-non-atmos)        | [x265](#x265)                       | [Special Edition](#special-edition)     |
|                                          |                                     | [Low Quality Releases](#low-quality-releases)     |


------

### BR-DISK

This is a custom format to help Radarr to recognize & ignore BR-DISK (ISO's and Blu-ray folder structure). 

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

 ![image-20200905193701986](images/image-20200905193701986.png)

Release Title: `avc|vc-1|hevc`
Negate: `False`
Required: `True`

Quality Modifier: `Remux` 
Negate: `True`
Required: `False`

Source: `WEBDL`
Negate: `True`
Required: `False`

Release Title: `^((?!x265).)*$`
Negate: `True`
Required: `True`

#### **NOTE:**

> Depending on your renaming scheme it could happen that Radarr will match renamed files after they are downloaded and imported as `BR-DISK`,
> This is a cosmetic annoyance till I come up for another way to solve this,
> being that this Custom Format is used to not download BR-DISK it does its purpose as intended.
> Several reasons why this is happening:
>
> - Blame the often wrongly used naming of x265 encodes.
> - Radarr v3 uses dynamic custom formats 

------

------

### EVO except WEB-DL

This group is often banned for the low quality Blu-ray releases but their WEB-DL are okay.

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

 ![image-20200905223125338](images/image-20200905223125338.png)

Release Title: `\bEVO\b`
Negate: `False`
Required: `False`

Source: `WEBDL`
Negate: `True`
Required: `False`

------

------

### Dolby TrueHD/ATMOS

If you prefer TrueHD|Atmos audio tracks.

 ![image-20200905223224099](images/image-20200905223224099.png)

Release Title: `truehd|atmos`
Negate: `False`
Required: `False`

------

------

### DTS-HD/DTS:X

If you prefer DTS-HD/DTS:X audio tracks.

 ![image-20200905223324883](images/image-20200905223324883.png)

Release Title: `dts.?(hd|es|x(?!\d))`
Negate: `False`
Required: `False`

------

------

### Single Layer DV

Custom Format for Single Layer Dolby Vision releases.

 ![image-20200905223433265](images/image-20200905223433265.png)

Release Title: `sl.?dv|single.?layer.?dovi` 
Negate: `False` 
Required: `False`

Quality Modifer: `Remux` 
Negate: `False`
Required: `True`

------

------

### Special Edition

Custom format for several Special Editions

 ![image-20200904233909845](images/image-20200904233909845.png)

Edition: `extended|uncut|director|special|unrated|uncensored|\bCut\b|\bVersion\b`
Negate: `False`
Required: `True`

Edition: `theatrical`
Negate: `True`
Required: `True`

------

------

### DDP (non-Atmos)

 ![](images/image-20200904215047871.png)

Release Title: `dd(p|\+)|eac3`
Negate: `False`
Required: `True`

Release Title `TrueHD|ATMOS`
Negate: `True`
Required: `True`

------

------

### x264

 ![image-20200905194336459](images/image-20200905194336459.png)

Release Title: `(x|h)\.?264`
Negate: `False`
Required: `False`

------

------

### x265

 ![image-20200905194401001](images/image-20200905194401001.png)

Release Title: `(x|h)\.?265`
Negate: `False`
Required: `False`

------


------

### Low Quality Releases

 IMG Needed
#### Low-Quality Releases (often banned groups)[BLOCK1]
Release Title: /b-aXXo|-CrEwSaDe|-DEViSE|-FaNGDiNG0|-FLAWL3SS|-FZHD|-FRDS|-HDTime|-IMAGINE|-iPlanet|-KingBen|-KiNGDOM|-KLAXXON|-Leffe|-LTRG|-mHD|-mSD|-NhaNc3|-nHD|-nikt0|-nSD|-PrisM|-PRODJi|-Rx|-RDN|-SANTi|-ViSION|-WAF|-WHiiZz|-x0r|-YIFY|-YTS|-STUTTERSHIT/b
Negate: `False`
Required: `True`

#### Another Small list of often banned groups.[BLOCK2]
Release Title: /b-CDDHD|-EuReKA|-DDR|-DNL|-BARC0DE/b
Negate: `False`
Required: `True`

#### And Another list.[BLOCK3]
Release Title: /b-RARBG|-FGT|-BReWeRS|-Grym|-LiGaS|-Zeus|-Tigole/b
Negate: `False`
Required: `True`

### Rips from Scene and quick-to-release P2P groups while adequate, are not considered high quality.[BLOCK4]
Release Title: /b-beAst|-CHD|-EVO|-HDWinG|-MTeam|-MySiLU|-WiKi/b
Negate: `False`
Required: `True`

>NOTE:
>
>- EVO (except WEB-DL)
------

------

