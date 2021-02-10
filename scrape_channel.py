from googleapiclient.discovery import build

api_key = 'AIzaSyBT8wA9JslanCzQeKmqQoZShVVtMXBUApI'
youtube = build('youtube', 'v3', developerKey = api_key)




x = youtube.videos().list(
	part="snippet,statistics,contentDetails",
    id= "o1s8AJK6sSc").execute()

print(x)