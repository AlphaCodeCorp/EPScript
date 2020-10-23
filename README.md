# EPScript

Script to grab images from subreddit like <https://www.reddit.com/r/EarthPorn>

The rights to the images do not belong to you and are the property of the rightful owners.

## Script PowerShell

PS : This script grab images from subreddit EarthPorn only, change this link in the script to change of subreddit

PS bis : This script is the first version, I advise to use the one in python

To allow script to be executed follow this [documentation](<https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7>)

- Launch cmd in administrator
- Go to the location of the script
- Execute ```powershell.exe```

Now you can use the script

- Execute the commande ```.\EPScript.ps1 help``` to display the different commands
- Execute ```.\EPScript.ps1 X``` where ```x``` is the number of image to grab

  **Please note that the maximum of image is 100**

The script download image in a folder on your Desktop named ```imagesEarthPornReddit``` if you already have a folder with this name the script overwrites the images

## Script Python

The scipt expects at east 1 argument, the subreddit !

Execute ```\EP_Script_v2.py -h``` to display the different commands

The differentes arguments

|Argument|expects|Default value|Example|
|--------|:-----:|:-----------:|:------|
|-h --help|nothing|none|-h |
|-s --sub|subreddit|none|-s EarthPorn|
|-f --folder|The path destination folder|C:\users\usersname\Documents\Images_SubReddit_test|-f C:\Users\Dronai\Documents\|
|-n --number|The number of image to download|25|-n 50|

For example you can use ```.\EP_Script_v2.py -s EarthPorn -n 150```
