# Youtube-Video-Info-Scraper

This script will automatically scrape the statistics<sup>1</sup> of every video from any channel/playlist the user gives it. There a few steps to complete to get this script working:
* get your Youtube API key ([text](https://www.slickremix.com/docs/get-api-key-for-youtube/)/[video](https://www.youtube.com/watch?v=th5_9woFJmk) guide), and paste it into personal_api.py 
* make sure you have Python 3.6+ installed 
* copy/paste all the commands in the second column into the cmd:

   Packages | Install command
   ------------ | -------------
   isodate | `pip install isodate`
   PySimpleGUI | `pip install PySimpleGUI`
   requests | `pip install requests`
   bs4 | `pip install bs4`
   googleapiclient | `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`


The program should function correctly afterwards. Double click on "main.pyw" and a simple GUI box should pop up like this:

![GUI pic](https://i.imgur.com/TFC0kHl.png)

1. In the `Link` field, you can copy/paste the link of any channel/playlist, and the script will determine if the link leads to a channel/or playlist.

2. In the `Save CSV to` field, if you leave it blank, the CSV will be created on your desktop (i.e. I've set the default save path as `C:\Users\username\Desktop` in case one isn't enter/chosen)
      * if your default drive letter is different/don't have a Desktop folder for some reason/are on Linux or MacOS, then the program won't run at all.

3. In the `CSV name` field, if you leave it blank, the CSV will be named `Scraped Youtube dd/mm/yyyy.csv`.








 <sup>1</sup> statistics includes, in order, the video title, date uploaded, views, likes, dislikes, comments, video id, duration (in seconds).
