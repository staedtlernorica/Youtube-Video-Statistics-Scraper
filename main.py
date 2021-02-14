import PySimpleGUI as sg
import scrape_channel
import scrape_playlist
import config


def scrape(user_input = {}):

    if user_input["-save_to-"] != "":
        scrape_playlist.save_path = user_input["-save_to-"]

    if user_input["-save_as-"] != "":
        scrape_playlist.csv_name = user_input["-save_as-"]

    if 'playlist' in user_input["-yt_link-"]:
        raw_url = user_input["-yt_link-"]
        pl_id = raw_url.replace("https://",'').replace("www.youtube.com/playlist?list=",'')
        scrape_playlist.playlist_id = pl_id
        scrape_playlist.main()

    else: 
        channel_url = user_input["-yt_link-"]
        scrape_channel.channel_link = channel_url
        scrape_channel.main()


#https://www.geeksforgeeks.org/user-input-in-pysimplegui/
layout = [ 
    [sg.Text('URL of Youtube channel/playlist to be scraped:')], 
    [sg.Text('Link', size =(10, 1)), sg.InputText(key = "-yt_link-")],
    [sg.Text("Save CSV to:", size =(10, 1)), sg.InputText(key = "-save_to-"), sg.FolderBrowse()], 
    [sg.Text("CSV name:", size = (10,1)), sg.Input(key = "-save_as-")], 
    [sg.Submit(), sg.Cancel("Exit")] 
] 

window = sg.Window('Youtube Channel/Playlist Scraper', layout) 

while True:      
      event, values = window.read()      
      if event == 'Exit'  or event == sg.WIN_CLOSED:      
        break # exit button clicked      

      #only worry about name bc save path and save name has default values
      if event == 'Submit' and (values["-yt_link-"] != ''):      
        scrape(values)

        #reset path/file name, o/w remembers from last input, even
        #if input field are cleared
        scrape_playlist.save_path = config.default_save_path    
        scrape_playlist.csv_name = config.default_csv_name

