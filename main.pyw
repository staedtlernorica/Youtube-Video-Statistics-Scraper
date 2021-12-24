from tkinter import *
from tkinter import filedialog
import os
import csv
import scrape_channel as sc
import scrape_playlist as sp

import config
import parse_user_input as pui


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

    # user_inputs["url"] = url_input.get()
    user_input = url_input.get()

    scraped_info = []
    # if user_inputs['url'] != '':
    if user_inputs != '':    
        
        id_tuple = pui.main(user_input)
        
        if id_tuple[1] == 0:
            uploads_id = sc.get_uploads_id(id_tuple[0])
            scraped_info = sp.main(uploads_id)

        else:
            scraped_info = sp.main(id_tuple[0])

    progress_label['text'] = 'Waiting for save location.'
    ask_directory(scraped_info)
    progress_label['text'] = 'Saved file. Ready to scrape again.'


#close when press Esc 
#https://stackoverflow.com/a/28467330/6030118
import sys
def close_on_escape(event):
    window.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing


window = Tk()

window.title("Youtube Channel/Playlist Scraper")
window.geometry("525x100")
window.resizable(0,0)           #https://stackoverflow.com/a/51524693/6030118

my_label = Label(text="Enter URL or ID of the playlist/channel:", font = (None, 11))
my_label.place(x =65, y =5)

url_label = Label(text="URL:", font = (None, 11))
url_label.place(x = 5, y = 35)

status_label = Label(text="Status:", font = (None, 11))
status_label.place(x = 5, y = 70)

progress_label = Label(text="Waiting for user input.", font = (None, 11))
progress_label.place(x =65, y = 70)

user_inputs = {
    "url": "",
    "folder": "",
    "csv": ""
}

url_input = Entry(window, width=55, font = (None, 11))
url_input.place(x =68, y = 37)
url_input.focus_set()

submit_button = Button(text="Scrape & Save", command=get_user_input, font = (None, 11))
submit_button.place(x = 388, y =70, height = 25, width = 125)

window.bind('<Escape>', close_on_escape)


window.mainloop()


