#https://www.youtube.com/watch?v=th5_9woFJmk
from googleapiclient.discovery import build

api_key = 'AIzaSyBT8wA9JslanCzQeKmqQoZShVVtMXBUApI'
youtube = build('youtube', 'v3', developerKey = api_key)


eh = 'PLhyKYa0YJ_5Aq7g4bil7bnGi0A8gTsawu'

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#MANUAL ENTRY HERE, PROGRAM WILL DO THE REST
#----------------------------------------------------------------------------
#SO DONT HAVE TO CHANGE A BUNCH OF PLAYLIST ID VARIABLE
scrapedPlaylistId = eh 							#PLAYLIST TO BE SCRAPED

from datetime import date
today = str(date.today())
csvName = 'EH Playlist'+ ' ' + today +".csv"	#ZERO PUNCTUATION format

need_to_print = 1								#PRINT TO CSV
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


#take snippets from a playlist
def callYoutube(token='', desiredPlaylistId = ''):
	return youtube.playlistItems().list(
		part='snippet',
		playlistId = desiredPlaylistId,
		maxResults = 50,
		pageToken = token
		)

#calculate how many tokens will be needed/the amount of time to
#run the get token loop (right below)
def numTokensNeeded(desiredPlaylistId = ''):
	totalVidRequest = youtube.playlistItems().list(
			part='snippet',
			playlistId = desiredPlaylistId,
			)
	response = totalVidRequest.execute()

	#get total number of videos in the playlist
	numVidsInPlaylist = response['pageInfo']['totalResults']   
	numTokensNeeded = 0

	if numVidsInPlaylist%50 == 0:			#calculation formulas
		return numVidsInPlaylist/50 - 1
	else: 
		return divmod(numVidsInPlaylist, 50)[0] 
		#remember first 50 vids dont need/have nextPageToken


totalNumTokensNeeded = numTokensNeeded(scrapedPlaylistId)
i = tokens_used = 0
allNextToken = ['']

#run loop to get all nextPageToken, to crawl through the entire 
#playlist 50 vids at a time
#(totalNumTokensNeeded + 1) parameter is only for maxResults = 50
while len(allNextToken) != totalNumTokensNeeded + 1:
	extractNextToken = callYoutube(allNextToken[i], scrapedPlaylistId).execute()
	allNextToken.append(extractNextToken['nextPageToken'])
	i=i+1


#scrape items gotten with callYoutube function
def scrapePlayListItems(playListItemsDict={}):
	tempList = []
	o = 1

	for i in playListItemsDict["items"]:		
		vidId = i['snippet']['resourceId']['videoId']
#		print(o, vidId)	
		tempList.append(vidId)

		#can turn on to print video title, for easy track keeping
		# vidTitle = i['snippet']['title']
		# tempList.append((vidTitle, vidId))
		# print(o,(vidTitle, vidId))	
		o=o+1
	return tempList


#each element is a list containing 50 video ids
playlistIds = []

for token in allNextToken:
	youtubeDictObject = callYoutube(token,scrapedPlaylistId).execute()
	tempList = scrapePlayListItems(youtubeDictObject)
	playlistIds.append(tempList)


#turn [['a','b','c'], ['c','d']] into ['a,b,c', 'c,d']
# eg     3 strings    2 string          1 str   1 str
def oneLongString(vidIdsList=[]):

	idsList = vidIdsList
	tempString = ''

	for id in idsList:
		tempString = tempString + id +','

	#[:-1] b/c want to remove unwanted comma from last entry
	#or will cause error with nextPageToken
	return tempString[:-1]


stringedPlaylistIds = []

#apply oneLongString methods to each of the id list in playListIds
for i in playlistIds:
	stringedPlaylistIds.append(oneLongString(i))


def getYoutubeVideosStats(vidIds = ''):
	return youtube.videos().list(
    part="snippet,statistics,contentDetails",
    id= vidIds
    )

rawYoutubeStatsDict = []

for i in stringedPlaylistIds:
	x = getYoutubeVideosStats(i).execute() 
	rawYoutubeStatsDict.append(x)


def scrapeYoutubeVidStats(statDictObj = {}):

	tempDict = statDictObj
	tempList = []

	for i in tempDict['items']:
		
		vidId = i['id']

		playtime = i['contentDetails']['duration']	#need contentDetails in getYoutubeVideoStats
		import isodate
		vidDuration = isodate.parse_duration(playtime).total_seconds()
		#convert PT5M38S in actual seconds

		vidTitle = i['snippet']['title']
		vidDate = i['snippet']['publishedAt'][:10]		#[:10] only want upload dates, not hour			
		vidViews = i['statistics']['viewCount']
		vidLikes = i['statistics']['likeCount']
		vidDislikes = i['statistics']['dislikeCount']
		vidComments = i['statistics']['commentCount']


		tempList.append((vidTitle, vidDate, vidViews,
			vidLikes, vidDislikes, vidComments,vidId,vidDuration))

	return tempList


finalPlaylistStats = []

for i in rawYoutubeStatsDict:
	x = scrapeYoutubeVidStats(i)
	finalPlaylistStats.append(x)


#[title, date, views, likes, dislikes, comments] format
polishedPlaylistStatsInfo = []

#make finalPlaylistStats, [[a,b,c], [d,e,f], [g]] 
#into [a,b,c,d,e,f,g]
for i in finalPlaylistStats:
	for o in i:
		polishedPlaylistStatsInfo.append(o)

# #quality check
# for i in polishedPlaylistStatsInfo:
# 	print(polishedPlaylistStatsInfo.index(i)+1, i)

#https://stackoverflow.com/a/11196588/6030118
import os
path1 = os.getenv("USERPROFILE")
path2 = path1 + '\\Documents\\GitHub\\EH-Youtube\\'


if need_to_print == 1:
	import csv

	#newline='' helps prevent line skipping when printing entry
	#https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
	#-------------------------------------------------------------------------------------
	#encoding='UTF-8', or will run into UnicodeEncodeError, eg with EH episode
	#♫ Admiral Yi: Drums of War - Sean and Dean Kiner - Extra History Music
	#https://stackoverflow.com/questions/37490428/unicodeencodeerror-with-csv-writer
	with open(path2+csvName, 'w', newline='',encoding='UTF-8') as csvfile:
	    csvwriter = csv.writer(csvfile)
	    for currentRow in polishedPlaylistStatsInfo:
	        csvwriter.writerow(currentRow)
