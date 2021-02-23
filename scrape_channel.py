import personal_api
from googleapiclient.discovery import build
api_key = personal_api.api_key
youtube = build('youtube', 'v3', developerKey = api_key)


def get_uploads_id(channel_id = ""):

    #https://stackoverflow.com/a/27872244/6030118
    #get channel's uploads playlist
    channel_info = youtube.channels().list(
    part ="contentDetails",
    id = channel_id).execute()

    uploads_id = channel_info["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    return uploads_id