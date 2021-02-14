import PySimpleGUI as sg
import scrape_channel
import scrape_playlist


def scraper(user_input = {}):

    if user_input[1] != "":
        scrape_playlist.save_path = user_input[1]
    if user_input[2] != "":
        scrape_playlist.csv_name = user_input[2]

    if 'playlist' in user_input[0]:
       
        raw_url = user_input[0]
        pl_id = raw_url.replace("https://",'').replace("www.youtube.com/playlist?list=",'')
        scrape_playlist.playlist_id = pl_id
        scrape_playlist.main()

    else: 

        channel_url = user_input[0]
        scrape_channel.channel_link = channel_url
        scrape_channel.main()


#https://www.geeksforgeeks.org/user-input-in-pysimplegui/
layout = [ 
    [sg.Text('URL of Youtube channel/playlist to be scraped:')], 
    [sg.Text('Link', size =(10, 1)), sg.InputText()],
    [sg.Text("Save CSV to:", size =(10, 1)), sg.InputText(), sg.FolderBrowse()], 
    [sg.Text("CSV name:", size = (10,1)), sg.Input()], 
    [sg.Submit(), sg.Cancel("Exit")] 
] 

window = sg.Window('Youtube Channel/Playlist Scraper', layout) 

while True:      
      event, values = window.read()      
      if event == 'Exit'  or event == sg.WIN_CLOSED:      
        break # exit button clicked      
      if event == 'Submit' and (values[0] != ''):      
        scraper(values)
        print(values)
        
