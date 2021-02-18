import scrape_channel
import scrape_playlist

#urls = "https://www.youtube.com/playlist?list=PLhyKYa0asdYJ_5DTz_FAbdQyXo9TZdx1hTWf"

def parsing_youtube_link(url):

	#print(url)

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


	#scrape_playlist.playlist_id = id_only



	# try:
	# 	x = scrape_playlist.get_playlist_vid_id(playlist = id_only)
	# 	print(x)
	# 	scrape_playlist.main()
		
	# except:
	# 	pass















#parsing_youtube_link(urls)

# x = parsing_youtube_link(urls)
# print(x)

# scrape_playlist.get_playlist_vid_id(playlist = x)


# scrape_playlist.playlist_id = parsing_youtube_link(urls)
# scrape_playlist.main()