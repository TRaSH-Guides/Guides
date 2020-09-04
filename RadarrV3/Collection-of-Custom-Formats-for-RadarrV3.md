## Collection of Custom Formats for Radarr V3 (Aphrodite)

Here I will try to collect a collection of most needed/used Custom Formats.
That I've found on discord or created myself with the help of others.

> Keep in mind Custom Formats are made to fine tune your Quality Profile !!!
>
> Meaning: Quality Profile trumps Custom Formats !!!

With the coming of Radarr V3 Custom Formats are much more advanced/powerful than with v0.2, althrough this also means a Custom Format is much more complicated to setup.
So I decided to use more screenshots for the basic setups to make it as easy as possible.

------

| Audio                                    | Video                               | Misc                                    |
| :--------------------------------------- | ----------------------------------- | --------------------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [Single Layer DV](#single-layer-dv) | [BR-DISK](#br-disk)                     |
| [DTS-HD/DTS:X](#dts-hd-dts-x)            |                                     | [EVO except WEB-DL](#evo-except-web-dl) |
| [DDP (non-Atmos)](#ddp-non-atmos)        |                                     | [Special Edition](#special-edition)     |



------

### BR-DISK

This is a custom format to help Radarr to recognize & ignore BR-DISK (ISO's and Blu-ray folder structure). 

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

 ![image-20200823155946642](images/image-20200823155946642.png)

Release Title: `(avc|vc-1|hevc)` 
Negate: `False` 
Required: `True`

 ![image-20200823160216479](images/image-20200823160216479.png)

Quality Modifier: `Remux` 
Negate: `True`
Required: `False`

 ![image-20200823160329429](images/image-20200823160329429.png)

Source: `WEBDL`
Negate: `True`
Required: `False`

 ![image-20200823160419447](images/image-20200823160419447.png)

Release Title: `^((?!x265).)*$`
Negate: `True`
Required: `False`

 ![image-20200823160456561](images/image-20200823160456561.png)

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

 ![image-20200823160627512](images/image-20200823160627512.png)

Release Title: `\b-EVO\b`
Negate: `False`
Required: `False`

 ![image-20200823160801588](images/image-20200823160801588.png)

Source: `WEBDL`
Negate: `True`
Required: `True`


 ![image-20200823162547299](images/image-20200823162547299.png)

------

------

### Dolby TrueHD/ATMOS

If you prefer TrueHD|Atmos audio tracks.



 ![image-20200823144556484](images/image-20200823144556484.png)



Release Title: `truehd|atmos`
Negate: `False`
Required: `True`

 ![image-20200823144701236](images/image-20200823144701236.png)

------

------

### DTS-HD/DTS:X

If you prefer DTS-HD/DTS:X audio tracks.

 ![image-20200823151557625](images/image-20200823151557625.png)

Release Title: `dts.?(hd|es|x(?!\d))`
Negate: `False`
Required: `True`

 ![image-20200823151639099](images/image-20200823151639099.png)

------

------

### Single Layer DV

Custom Format for Single Layer Dolby Vision releases.


 ![image-20200823152059999](images/image-20200823152059999.png)

Release Title: `sl.?dv|single.?layer.?dovi` 
Negate: `False` 
Required: `True`

 ![image-20200823152225653](images/image-20200823152225653.png)

Quality Modifer: `Remux` 
Negate: `False`
Required: `True`

 ![image-20200823152302737](images/image-20200823152302737.png)

------

------

### Special Edition

Custom format for several Special Editions

 ![image-20200904212829258](images/image-20200904212829258.png)

Edition: `extended|uncut|director|special|unrated|uncensored|\.cut[\.|-]`
Negate: `False`
Required: `True`

 ![image-20200904212930373](images/image-20200904212930373.png)

------

------

### DDP (non-Atmos)

 ![](images/image-20200904215047871.png)

Release Title: `dd(p|\+)|eac3`
Negate: `False`
Required: `True`

 ![](images/image-20200904215205552.png)

Release Title `TrueHD|ATMOS`
Negate: `True`
Required: `True`

 ![](images/image-20200904215249279.png)

------

------

