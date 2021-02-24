 # Youtube-Video-Info-Scraper (updated 23/02/2021)

This script will automatically scrape the statistics<sup>1</sup> of every video from a playlist/or every video uploaded by a channel. All the user has to do is provide a playlist/channel URL, and the script will output the collected statistics of all videos as a .csv file.

## Installation before using
1) Download the files from the `main` branch. 
2) Make sure these three packages are installed (in the global or virtual environment):
*  copy/paste all three commands in the second column into either the Windows cmd/virtual env. terminal, then hit enter to install package
  Packages | Install command 
   ------------ | -------------
   isodate | `pip install isodate`
   bs4 | `pip install bs4`
   googleapiclient | `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
3) supply your personal Youtube API key (free of charge) from Google
*  get your Youtube API key ([text](https://www.slickremix.com/docs/get-api-key-for-youtube/)/[video](https://www.youtube.com/watch?v=th5_9woFJmk) guide), and paste it into personal_api.py

Unless you

Now the script is ready to scrape playlists and channels. Go to the youtube-scraper folder, and open up `main.pyw` file, and the GUI should pop up.

## Usage
<a href="url"><img src="https://i.imgur.com/3Vnkxrs.png" align="left" height="100" width="525" ></a>

In my testing (not exhaustive as I'm only one person), the script is very resilient to errors (either by the user or by the program) and will not easily crash. If an incorrect URL is entered, or the Youtube servers doesn't play nice when scraping data (very unlikely), the program window will remain open, waiting for the correct URL<sup>2</sup> input.
```

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





The program should function correctly afterwards. Double click on "main.pyw" and a simple GUI box should pop up like this:

![GUI pic](https://i.imgur.com/TFC0kHl.png)

1. In the `Link` field, you can copy/paste the link of any channel/playlist, and the script will determine if the link leads to a channel/or playlist.

2. In the `Save CSV to` field, if you leave it blank, the CSV will be created on your desktop (i.e. I've set the default save path as `C:\Users\username\Desktop` in case one isn't enter/chosen)
      * if your default drive letter is different/don't have a Desktop folder for some reason/are on Linux or MacOS, then the program won't run at all.

3. In the `CSV name` field, if you leave it blank, the CSV will be named `Scraped Youtube dd/mm/yyyy.csv`.



## Footnote

 <sup>1</sup> statistics includes, in order, the video title, date uploaded, views, likes, dislikes, comments, video id, duration (in seconds).
 
 <sup>2</sup>
 
