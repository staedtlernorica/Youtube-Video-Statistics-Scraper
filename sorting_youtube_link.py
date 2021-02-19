import scrape_channel as sc
import scrape_playlist as sp

#check if valid playlist or channel id
def check_valid_id(url):
	try: 
		sp.get_playlist_vid_id(playlist = url)
	except:
		pass

	#need return statement

def parsing_youtube_link(url):

	if "list=" not in url:
		return url

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