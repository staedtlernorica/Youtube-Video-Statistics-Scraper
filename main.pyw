import PySimpleGUI as sg
import scrape_channel
import scrape_playlist
import config


def scrape(user_input = {}):

    if user_input["-save_to-"] != "":
        scrape_playlist.save_path = user_input["-save_to-"]

    if user_input["-save_as-"] != "":
        scrape_playlist.csv_name = user_input["-save_as-"].replace(".csv",'')

    if 'playlist' in user_input["-yt_link-"]:
        raw_url = user_input["-yt_link-"]
        pl_id = raw_url.replace("https://",'').replace("www.youtube.com/playlist?list=",'')
        scrape_playlist.playlist_id = pl_id
        scrape_playlist.main()

    else: 
        channel_url = user_input["-yt_link-"]
        scrape_channel.channel_link = channel_url
        scrape_channel.main()


# #https://www.geeksforgeeks.org/user-input-in-pysimplegui/
# layout = [ 
#     [sg.Text('Enter the URL of Youtube channel/playlist to be scraped:')], 
#     [sg.Text('Link', size =(10, 1)), sg.InputText(key = "-yt_link-")],
#     [sg.Text("Save CSV to:", size =(10, 1)), sg.InputText(key = "-save_to-"), sg.FolderBrowse()], 
#     [sg.Text("CSV name:", size = (10,1)), sg.Input(key = "-save_as-")], 
#     [sg.Submit(), sg.Cancel("Exit")] 
# ] 

# window = sg.Window('Youtube Channel/Playlist Scraper', layout) 

# while True:      
#       event, values = window.read()      
#       if event == 'Exit'  or event == sg.WIN_CLOSED:      
#         break # exit button clicked      

#       #only worry about name bc save path and save name has default values
#       if event == 'Submit' and (values["-yt_link-"] != ''):      
#         scrape(values)

#         #reset path/file name after scraping, o/w remembers 
#         #from last input, even if input fields are cleared
#         scrape_playlist.save_path = config.default_save_path    
#         scrape_playlist.csv_name = config.default_csv_name







from tkinter import *
from tkinter import filedialog
import os

window = Tk()







window.title("Youtube Channel/Playlist Scraper")
window.geometry("570x100")
#window.minsize(width=575, height=175)
window.resizable(0,0)           #https://stackoverflow.com/a/51524693/6030118

my_label = Label(text="Enter the URL:")
my_label.place(x = 100, y =20)

url_label = Label(text="URL:")
url_label.place(x = 20, y = 50)

# folder_label = Label(text="Save CSV as:")
# folder_label.place(x = 20, y = 80)

# csv_label = Label(text="CSV name:")
# csv_label.place(x = 20, y = 110)





user_inputs = {
    "url": "",
    "folder": "",
    "csv": ""
}




import csv

def ask_directory(x):
    currdir = os.getcwd()
    #tempdir = filedialog.askdirectory(parent=window, initialdir=currdir, title='Please select a directory')
    
    tempdir = filedialog.asksaveasfile(
        initialfile = config.default_csv_name,
        defaultextension=".csv",
        parent=window, 
        initialdir=currdir, 
        title='Save as:',
        filetypes = (("Comma Separated Values ","*.csv"),("all files","*.*")),
        confirmoverwrite=False, 
        mode = "w")


    with open(tempdir.name, 'w', newline='',encoding='UTF-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for currentRow in x:
            csvwriter.writerow(currentRow)

    #print(tempdir)

    # if tempdir != None:
    #     print(tempdir)
    #     folder_path.insert(0,f"{str(tempdir)}")

    return tempdir



#https://stackoverflow.com/a/15495560/6030118
def get_user_input():

    user_inputs["url"] = user_url.get()
    # user_inputs["folder"] = folder_path.get()
    # user_inputs["csv"] = csv_name.get()
    print(user_inputs)

    if user_inputs['url'] != '':
        scrape_playlist.playlist_id = user_inputs['url']
        scraped_info = scrape_playlist.main()

        [print(i) for i in scraped_info]


    ask_directory(scraped_info)


    # file = filedialog.asksaveasfile(mode='w', defaultextension=".csv")

    # if file:
    #     file.write(scraped_info)
    #     file.close()


    #user_inputs["folder"] = ask_directory()



user_url = Entry(window, width=60)
user_url.place(x = 100, y = 50)

# folder_path = Entry(window,width=60)
# folder_path.place(x = 100, y = 80)

# csv_name = Entry(window, width=60)
# csv_name.place(x = 100, y = 110)


# browse_dir_button = Button(text="Save As", command=ask_directory)
# browse_dir_button.place(x = 100, y =110, height = 25, width = 83)


submit_button = Button(text="Scrape", command=get_user_input)
submit_button.place(x = 470, y =48, height = 25, width = 83)

# exit_button = Button(text="Exit", command=window.destroy)
# exit_button.place(x = 390, y = 125, height = 25, width = 70)




window.mainloop()





print(user_inputs)



