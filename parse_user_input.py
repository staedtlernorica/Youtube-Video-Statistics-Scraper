import personal_api
from googleapiclient.discovery import build
api_key = personal_api.api_key
youtube = build('youtube', 'v3', developerKey = api_key)


def check_channel_id(url):
    request = youtube.channels().list(
        part="id",
        id=url
    )
    response = request.execute()
    found_channel = response.get('pageInfo')
    found_channel = found_channel.get("totalResults")
    
    if found_channel == 1:
        return True
    return False


#return == 1 if id leads to channel/playlist
#on assumption that id will lead to one AND
#ONLY ONE channel/playlist
#could change to return != 0 if yt breaks
def check_playlist_id(url):
    request = youtube.playlists().list(
        part="id",
        id=url
    )
    response = request.execute()
    found_playlist = response.get('pageInfo')
    found_playlist = found_playlist.get("totalResults")
    
    if found_playlist == 1:
        return True
    return False


#explnation for /c vs /channel vs /user and why need id
#https://redd.it/2vsyit
def get_channel_id(channel_link):
    
    channel_url = channel_link.replace("https://",'').replace("featured",'')
    channel_videos_tab = f"https://{channel_url}/videos"

    # import requests
    # from bs4 import BeautifulSoup

    # source = requests.get(channel_videos_tab).text
    # soup = BeautifulSoup(source, "html.parser")
    # a = soup.find('body').find('link')['href']
    # channel_id = a.split('/')[-1]

    from urllib import request
    from bs4 import BeautifulSoup

    re = request.urlopen(channel_videos_tab)
    re = re.read().decode('utf-8')
    soup = BeautifulSoup(re, "html.parser")
    a = soup.find('body').find('link')['href']
    channel_id = a.split('/')[-1]

    return channel_id


def get_playlist_id(url):

    link = url.replace('https://','')
    link = link.replace("www.youtube.com",'')
    link = link.replace("/featured",'')
    link = link.split("=")
    
    id_only = ""
    for i in link:
        id_part = ''
        if "list" in i:
            index = link.index(i)
            id_part = link[index + 1]
            id_part = id_part.split("&")
            id_only = id_part[0]
            break

    return id_only


def main(user_input):

    #return user_input if it's a valid ch/pl id,
    #else parse it the correct id from user_input
    #0 = channel
    #1 = playlist
    if check_channel_id(user_input):
        return (user_input, 0)
    elif check_playlist_id(user_input):
        return (user_input, 1)
    elif "list=" not in user_input:
        return (get_channel_id(user_input), 0)
    else:
        return (get_playlist_id(user_input), 1)

