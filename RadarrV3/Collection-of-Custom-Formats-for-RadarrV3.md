## Collection of Custom Formats for Radarr V3 (Aphrodite)

Here I will try to collect a collection of most needed/used Custom Formats.
That I've found on discord or created myself with the help of others.

> Keep in mind Custom Formats are made to fine tune your Quality Profile !!!
>
> Meaning: Quality Profile trumps Custom Formats !!!

With the coming of Radarr v3 the Custom Formats is much more advanced/powerful then with v2 this also means it's much more complicated  to setup.
So I decided to use more screenshots for the basic setups to make it as easy as possible.

First a few regex basics (work in progress!!!):

`/b` = word break	

`/i` = case insensitive

`.?` = dot or space

------

| Audio                                    | Video                               | Misc                                    |
| :--------------------------------------- | ----------------------------------- | --------------------------------------- |
| [Dolby TrueHD/ATMOS](#dolby-truehdatmos) | [Single Layer DV](#single-layer-dv) | [BR-DISK](#br-disk)                     |
| [DTS-HD/DTS:X](#dts-hd-dts-x)            |                                     | [EVO except WEB-DL](#evo-except-web-dl) |
|                                          |                                     | [Special Edition](#special-edition)     |



------

### BR-DISK

This is a custom format to help Radarr to recognize & ignore BR-DISK (ISO's and Blu-ray folder structure). 

You will need to add the following to your new Custom Format when created in your Quality Profile (`Setting` => `Profiles`) and then set the score to `-1000`

 ![image-20200823155946642](images/image-20200823155946642.png)

`(avc|vc-1|hevc)`

 ![image-20200823160216479](images/image-20200823160216479.png)

`Remux`

 ![image-20200823160329429](images/image-20200823160329429.png)

`WEBDL`

 ![image-20200823160419447](images/image-20200823160419447.png)

`^((?!x265).)*$`

 ![image-20200823160456561](images/image-20200823160456561.png)

#### **NOTE:**

> Depending on your rename scheme it could happen that it will match renamed files after download as BR-DISK,
> This is a cosmetic annoyance till I come up for another way to solve this,
> being that this Custom Format is used to not download BR-DISK it does it purpose as intended.
> Several reasons why this is happening:
>
> - Blame the often wrongly used naming of x265 encodes.
> - Radarr v3 uses dynamic custom formats 

------

------

### EVO except WEB-DL

This group is often banned for the low quality Blu-ray releases but their WEB-DL are okay.

 ![image-20200823160627512](images/image-20200823160627512.png)

`\b-EVO\b`

 ![image-20200823160801588](images/image-20200823160801588.png)

`WEBDL`

 ![image-20200823162547299](images/image-20200823162547299.png)

------

------

### Dolby TrueHD/ATMOS

If you prefer TrueHD|Atmos audio tracks.



 ![image-20200823144556484](images/image-20200823144556484.png)



`truehd|atmos`

 ![image-20200823144701236](images/image-20200823144701236.png)

------

------

### DTS-HD/DTS:X

If you prefer DTS-HD/DTS:X audio tracks.

 ![image-20200823151557625](images/image-20200823151557625.png)

`dts.?(hd|es|x(?!\d))`

 ![image-20200823151639099](images/image-20200823151639099.png)

------

------

### Single Layer DV

Custom Format for Single Layer Dolby Vision releases.


 ![image-20200823152059999](images/image-20200823152059999.png)

`sl.?dv|single.?layer.?dovi`

 ![image-20200823152225653](images/image-20200823152225653.png)

`Remux`

 ![image-20200823152302737](images/image-20200823152302737.png)

------

------

### Special Edition

Custom format for several Special Editions

 ![image-20200904212829258](images/image-20200904212829258.png)

`extended|uncut|director|special|unrated|uncensored|\.cut[\.|-]`

 ![image-20200904212930373](images/image-20200904212930373.png)

------

------

