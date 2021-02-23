# Youtube-Video-Info-Scraper

- [ ] User pandas and convert youtube JSON objects to more readable df (for readability purposes)
   *https://stackoverflow.com/q/41168558/6030118
- [ x] Use get() function to get video stats (avoid premium vids/contents throwing keyError)
- [ ] present option to remove all incomplete entries (eg from premium vids)
- [ ] goes well with passing scrape object to a final print/clean up module; leave scraping_playlist only with scraping playlist
- [ x] Try to use urllib instead of requests in scrape_channel, so one less package installation



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


There are some limitations with the current script:
1. Only works on Python 3.6+
2. Only work on Windows 10 (possibly 8.1/8/7; have not been able to test)
3. Can only scrape publicly available videos; will not work on premium/paid videos
   * uncertain on how regionally locked videos will be affected
4. Can only scrape public playlists
5. Can only scrape channels with at least one uploaded video
6. The script is limited up to Google's daily [10,000 unit quota](https://developers.google.com/youtube/v3/getting-started#quota), i.e. if you scrape an obscene amount of videos, the script won't work until your next daily 10,000 quota. 
   * this truly is an obscene amount of scraping, easily equalling several thousands videos.

If the script crashes, it's because it has run into an error, either from these limitations, or the link is wrong. 





 <sup>1</sup> statistics includes, in order, the video title, date uploaded, views, likes, dislikes, comments, video id, duration (in seconds).
