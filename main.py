import PySimpleGUI as sg
import scrape_channel
import scrape_playlist


def scraper(user_input = {}):

    scrape_playlist.save_path = user_input["Browse"]

    if 'playlist' in user_input[0]:
       
        raw_url = user_input[0]
        pl_id = raw_url.lstrip("https://").lstrip("www.youtube.com/playlist?list=")
        scrape_playlist.playlist_id = pl_id
        scrape_playlist.main()

    else: 

        channel_url = user_input[0]
        scrape_channel.channel_link = channel_url
        scrape_channel.main()

    # if values[1] != values['Browse']:
    # print('File save path don\'t match')
    # file_save_path = values['Browse']


#https://www.geeksforgeeks.org/user-input-in-pysimplegui/
layout = [ 
    [sg.Text('URL of Youtube channel/playlist to be scraped:')], 
    [sg.Text('Link', size =(10, 1)), sg.InputText()],
    [sg.Text("Save CSV to:"), sg.Input(), sg.FolderBrowse()],  
    [sg.Submit(), sg.Cancel("Exit")] 
] 

window = sg.Window('Youtube Channel/Playlist Scraper', layout) 
#event, values = window.read() 
#window.close() 

input_dict = {}
while True:      
      event, values = window.read()      
      if event == 'Exit'  or event == sg.WIN_CLOSED:      
        break # exit button clicked      
      if event == 'Submit' and (values[0] != '' and values[1] != ''):      
        scraper(values)
        # print(values)
        input_dict = values

values = input_dict
# The input data looks like a simple list  
# when automatic numbered 
# print(event)  
# print(values[0])
# print(values[1])



