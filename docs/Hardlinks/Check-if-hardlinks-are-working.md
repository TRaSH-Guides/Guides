# How to check if hardlinks are working

You've followed the guide step by step but still want to check if hardlinks are working, or someone on the Sonarr/Radarr support team asked you to check if your files are hardlinked?

You can use 3 options to check if you got working hardlinks.

_All methods require you to login to your terminal with PuTTY or similar software._

!!! warning

    You can't create hard links for directories :bangbang:

    You can't cross file systems :bangbang:

---

## Usenet

!!! note ""

    If you use Usenet these examples won't work because you make use of instant moves/atomic moves and not hardlinks.

    Still want to test if it works?

    Test an import of a 4k remux (or any other big file and you should notice it's almost instant) and not a slower and more I/O intensive copy + delete.

## Method 1: Using ls

This is the easiest to check in our opinion.

In your terminal `cd` to your download location and run `ls -al` or type `ls -al /path/to/your/download/location/`

You will get a listing of all your files and on the left side you will see a couple of numbers, every file with a number above 1 are hardlinks.

![!Hardlinks check ls -al](images/hardlinks-ls-al.png)

- Red rectangle - Not Hardlinked
- Green rectangle - Hardlinks
- Blue rectangle - Folders/Directories you will need to go into them to check if the files are hardlinked.

---

## Method 2: Using stat

This way requires a bit more work.

- In the terminal type: `stat /path/to/your/download/location/file.mkv`
- In the terminal type: `stat /path/to/your/media/location/file.mkv`

You will get 2 results you can use to compare several things.

![!Hardlinks check stat](images/hardlinks-stat.png)

1. Links: Everything above 1 means it's hardlinked
1. Inode: if the numbers match, you know the files are hardlinked

## Method 3: Using Inode copies

- In your terminal `cd` to your download location and run `ls -i file.mkv` or type `ls -i /path/to/your/download/location/file.mkv`

This will reveal the inode of your file on the left side of the file.

![!Hardlinks check ls -i](images/hardlinks-ls-i.png)

- In your terminal type: `find /mnt/user/data/ -inum ###` or `find . -inum ###` if you're in your root folder.

!!! note ""

    `###` = Your inode number on the left of the file you found.

![!hardlinks inode](images/hardlinks-inode.png)

It will list all files linked with the same inode number.
