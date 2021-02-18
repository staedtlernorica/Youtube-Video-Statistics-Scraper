# import personal_api
# from googleapiclient.discovery import build
# api_key = personal_api.api_key
# youtube = build('youtube', 'v3', developerKey = api_key)

# playlist_id = ''  

# #channel  UCDkN-3e82Pf_xWMUH4iEV1A
# #uplodads UUDkN-3e82Pf_xWMUH4iEV1A

# def get_playlist_vid_id(token='', playlist = '', target = "snippet"):

#     return youtube.playlistItems().list(
#         part= target,
#         playlistId = playlist,
#         maxResults = 50,
#         pageToken = token
#         ).execute()




# def get_vid_ids_from_json(json_dict={}):
#     temp_list = []

#     for vid in json_dict["items"]:        
#         vid_id = vid['contentDetails']['videoId']
#         temp_list.append(vid_id)

#     return ','.join(temp_list)


# def get_vids_json(vidIds = ''):
#     return youtube.videos().list(
#     part="snippet,statistics,contentDetails",
#     id= vidIds
#     ).execute()


# import isodate
# def get_stats_from_vids_json(statDictObj = {}):

#     temp_list = []

#     for i in statDictObj['items']:
       
#         vidId = i['id']
#         #need contentDetails in scrape_yt_vids_dict
#         playtime = i['contentDetails']['duration']  
#         #convert PT5M38S in actual seconds
#         vidDuration = isodate.parse_duration(playtime).total_seconds()
#         vidTitle = i['snippet']['title']
#         #[:10] only want upload dates, not hour 
#         vidDate = i['snippet']['publishedAt'][:10]             
#         vidViews = i['statistics']['viewCount']
#         vidLikes = i['statistics']['likeCount']
#         vidDislikes = i['statistics']['dislikeCount']
#         vidComments = i['statistics']['commentCount']


#         temp_list.append((vidTitle, vidDate, vidViews,
#             vidLikes, vidDislikes, vidComments,vidId,vidDuration))

#     return temp_list


# def main():
#     print('this is the playlist id', playlist_id)
#     keep_running = True
#     next_token = ''
#     final_playlist_stats = []
#     while keep_running == True:


#         json_vid_id = get_playlist_vid_id(token = next_token, playlist = playlist_id, target = "contentDetails")
#         next_token = json_vid_id.get('nextPageToken', '')

#         vid_ids = get_vid_ids_from_json(json_vid_id)
#         vid_stats = get_vids_json(vid_ids)

#         x = get_stats_from_vids_json(vid_stats)
#         final_playlist_stats.extend(x)

#         if next_token == '':
#             keep_running = False

#     #print(final_playlist_stats)

#     return final_playlist_stats


# if __name__ == "__main__":
#     if playlist_id != '':
#         main()













import personal_api
from googleapiclient.discovery import build
api_key = personal_api.api_key
youtube = build('youtube', 'v3', developerKey = api_key)


playlist_id = ''  


def get_playlist_vid_id(token='', playlist = '', target = "snippet"):

    return youtube.playlistItems().list(
        part= target,
        playlistId = playlist,
        maxResults = 50,
        pageToken = token
        ).execute()


def get_vid_ids_from_json(json_dict={}):
    temp_list = []

    for vid in json_dict["items"]:        
        vid_id = vid['contentDetails']['videoId']
        temp_list.append(vid_id)

    return ','.join(temp_list)


def get_vids_json(vidIds = ''):
    return youtube.videos().list(
    part="snippet,statistics,contentDetails",
    id= vidIds
    ).execute()


import isodate
def get_stats_from_vids_json(statDictObj = {}):

    temp_list = []

    for i in statDictObj['items']:
        
        vidId = i['id']
        #need contentDetails in scrape_yt_vids_dict
        playtime = i['contentDetails']['duration']  
        #convert PT5M38S in actual seconds
        vidDuration = isodate.parse_duration(playtime).total_seconds()
        vidTitle = i['snippet']['title']
        #[:10] only want upload dates, not hour 
        vidDate = i['snippet']['publishedAt'][:10]              
        vidViews = i['statistics']['viewCount']
        vidLikes = i['statistics']['likeCount']
        vidDislikes = i['statistics']['dislikeCount']
        vidComments = i['statistics']['commentCount']


        temp_list.append((vidTitle, vidDate, vidViews,
            vidLikes, vidDislikes, vidComments,vidId,vidDuration))

    return temp_list


def main():
    keep_running = True
    next_token = ''
    final_playlist_stats = []
    while keep_running == True:

        json_vid_id = get_playlist_vid_id(next_token, playlist_id, "contentDetails")
        next_token = json_vid_id.get('nextPageToken', '')

        vid_ids = get_vid_ids_from_json(json_vid_id)
        vid_stats = get_vids_json(vid_ids)

        x = get_stats_from_vids_json(vid_stats)
        final_playlist_stats.extend(x)

        if next_token == '':
            keep_running = False

    return final_playlist_stats



if __name__ == "__main__":
    if (playlist_id) != '':
        main()