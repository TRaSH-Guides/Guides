# Check if hardlinks are working

You've followed the guide step by step but still want to check if hardlinks are working, or someone on the Sonarr/Radarr support team asked you to check if your files are hardlinked  ?

For this you can use 2 options to check if you got working hardlinks.

Both ways requires you to login to your terminal with Putty or similar.

---

## The ls -al method

This is the easiest to check in my opinion.

In your terminal cd to your download location or type `ls -al /path/to/your/download/location/`

You will get a listing of all your files and on the left side you will see a couple of numbers, every files with a number above 1 are hardlinks.

![!Hardlinks check ls -al](images/hardlinks-ls-al.png)

- Red rectangle - Not Hardlinked
- Green rectangle - Hardlinks
- Blue rectangle - Folders/Directories you will need to go in to them to check if the files are hardlinked.

---

## The stat method

This way requires a bit more work.

In your terminal type: `stat /path/to/your/download/location/file.mkv`

and also type: `stat /path/to/your/media/location/file.mkv`

you then will get 2 results you can use to compare several things.

![!Hardlinks check stat](images/hardlinks-stat.png)

1. Links: Everything above 1 means it's a hardlink
1. Inode: if the numbers match you know the files are hardlinked
