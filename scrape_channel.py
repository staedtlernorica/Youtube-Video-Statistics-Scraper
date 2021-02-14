import personal_api
from googleapiclient.discovery import build
api_key = personal_api.api_key
youtube = build('youtube', 'v3', developerKey = api_key)

channel_link = ""


#explnation for /c vs /channel vs /user and why need id
#https://redd.it/2vsyit
def get_channel_id(channel_link = ''):
    
    channel_url = channel_link.replace("https://",'').replace("featured",'')
    channel_videos_tab = f"https://{channel_url}/videos"

    import requests
    from bs4 import BeautifulSoup

    source = requests.get(channel_videos_tab).text
    soup = BeautifulSoup(source, "html.parser")
    a = soup.find('body').find('link')['href']
    channel_id = a.split('/')[-1]

    return channel_id


def main():
            
    channel_id = get_channel_id(channel_link)

    #https://stackoverflow.com/a/27872244/6030118
    #get channel's uploads playlist
    channel_info = youtube.channels().list(
    part ="contentDetails",
    id = channel_id).execute()

    uploads_id = channel_info["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    import scrape_playlist
    scrape_playlist.playlist_id = uploads_id
    scrape_playlist.main()

    
if __name__ == "__main__":
    if channel_link != '':
        main()
