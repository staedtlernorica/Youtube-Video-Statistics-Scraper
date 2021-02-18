from tkinter import *
from tkinter import filedialog
import os
import csv
import scrape_playlist
import scrape_channel
import config
import sorting_youtube_link as syl



def ask_directory(x):

    currdir = os.getcwd()
    tempdir = filedialog.asksaveasfile(
        initialfile = config.default_csv_name,
        defaultextension=".csv",
        parent=window, 
        initialdir=config.default_save_path, 
        title='Save as:',
        filetypes = (("Comma Separated Values ","*.csv"),("all files","*.*")),
        confirmoverwrite=True)

    if tempdir != None:
        with open(tempdir.name, 'w', newline='',encoding='UTF-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            [csvwriter.writerow(currentRow) for currentRow in x]



#https://stackoverflow.com/a/15495560/6030118
def get_user_input():

    user_inputs["url"] = user_url.get()

    parsed_link = ''
    scraped_info = []
    if user_inputs['url'] != '':
        
        parsed_link = syl.parsing_youtube_link(user_inputs['url'])

        if user_inputs['url'] == parsed_link:
            scrape_channel.channel_link = user_inputs['url']
            #print(scrape_channel.channel_link)
            uploads_id = scrape_channel.main()
            print(uploads_id)
            scrape_playlist.playlist_id = uploads_id
            scraped_info = scrape_playlist.main()


        else:
            scrape_playlist.playlist_id = parsed_link
            scraped_info = scrape_playlist.main()

    ask_directory(scraped_info)



window = Tk()


window.title("Youtube Channel/Playlist Scraper")
window.geometry("570x100")
window.resizable(0,0)           #https://stackoverflow.com/a/51524693/6030118

my_label = Label(text="Enter the URL:")
my_label.place(x = 100, y =20)

url_label = Label(text="URL:")
url_label.place(x = 20, y = 50)


user_inputs = {
    "url": "",
    "folder": "",
    "csv": ""
}

user_url = Entry(window, width=60)
user_url.place(x = 100, y = 50)

submit_button = Button(text="Scrape", command=get_user_input)
submit_button.place(x = 470, y =48, height = 25, width = 83)

window.mainloop()





