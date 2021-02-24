 # Youtube-Video-Info-Scraper (updated 23/02/2021)

This script will automatically scrape the statistics<sup>1</sup> of every video from a playlist/or every video uploaded by a channel. All the user has to do is provide a playlist/channel URL, and the script will output the collected statistics of all videos as a .csv file.

## Installation before using
This readme assumes that you are at least Python beginner who can write/edit .py files. 

1) Download the files from the `main` branch. 
2) Make sure these three packages are installed (in the global or virtual environment):
*  copy/paste all three commands in the second column into either the Windows cmd/virtual env. terminal, then hit enter to install package
  Packages | Install command 
   ------------ | -------------
   isodate | `pip install isodate`
   bs4 | `pip install bs4`
   googleapiclient | `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
3) supply your personal Youtube API key (free of charge) from Google
*  get your Youtube API key ([text](https://www.slickremix.com/docs/get-api-key-for-youtube/)/[video](https://www.youtube.com/watch?v=th5_9woFJmk) guide)
*  follow the direction in personal_api.py and paste your API key


Now the script is ready to scrape playlists and channels. Doubble click on `main.pyw`, and the GUI should pop up.

## Usage
<a href="url"><img src="https://i.imgur.com/3Vnkxrs.png" align="left" height="125" width="525" ></a>


To scrape any playlist or channel, simply copy/paste (or type) the appropriate<sup>2</sup> Youtube URL into the entry box, then click the `Scrape & Save` button. Once the statistics are scraped, a Save As dialog box will pop up, asking the user where to save the .csv file. <sup>3</sup>. Once the .csv is saved, the script is ready to scrape another channel/playlist, repeating the same steps.

If the playlist or channel has a lot of videos, the Save As dialog box might take a second (or several) to pop up, as it has to wait for the script to finish scraping the videos for statistics. In my testing, the script is very resilient to errors and will not easily crash or hang.  


## Limitations
There are some current limitations outside my control:

1. Only tested on Windows 10 (will possibly work 8.1/8/7; unsure for Mac/Linux)
2. Can only scrape free and publicly available videos; will not work on premium/paid videos
   * uncertain on how regionally locked videos will be affected
3. Can only scrape public playlists
4. Can only scrape channels with at least one uploaded video
5. The amount of videos the script can scrape is limited by Google's daily [10,000 unit quota](https://developers.google.com/youtube/v3/getting-started#quota), i.e. exceed this quota, the script won't work until your next daily 10,000 quota. 
   * keep in mind this is truly an obscene amount of scraping, easily equalling a thousand videos, maybe even more.


## TODO

- [ ] User pandas and convert youtube JSON objects to more readable df (for readability purposes)
   *[low priority](https://stackoverflow.com/q/41168558/6030118)
- [x] Use get() function to get video stats (avoid premium vids/contents throwing keyError)
  - [ ] present option to remove all incomplete entries (eg from premium vids)
  - [ ] goes well with passing scrape object to a final print/clean up module; leave scraping_playlist only with scraping playlist
- [ ] implement a settings.txt, allow the user to set default_save_path and default_csv_name that persists after script is closed
- [ ] implement Windows duplicate naming, so if xxx.csv already exist, the new save file will be xxx (1).csv, xxx (2).csv 
- [ ] manually crawl through HTML string and remove bs4 installation, one less package install
- [ ] even more status update bar to update user on process




The program should function correctly afterwards. Double click on "main.pyw" and a simple GUI box should pop up like this:

![GUI pic](https://i.imgur.com/TFC0kHl.png)

1. In the `Link` field, you can copy/paste the link of any channel/playlist, and the script will determine if the link leads to a channel/or playlist.

2. In the `Save CSV to` field, if you leave it blank, the CSV will be created on your desktop (i.e. I've set the default save path as `C:\Users\username\Desktop` in case one isn't enter/chosen)
      * if your default drive letter is different/don't have a Desktop folder for some reason/are on Linux or MacOS, then the program won't run at all.

3. In the `CSV name` field, if you leave it blank, the CSV will be named `Scraped Youtube dd/mm/yyyy.csv`.



## Footnote

 <sup>1</sup> statistics includes, in order, the video title, date uploaded, views, likes, dislikes, comments, video id, duration (in seconds).
 
 <sup>2</sup>
 
 <sup>3</sup>
