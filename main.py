#https://www.python-course.eu/tkinter_entry_widgets.php
import tkinter as tk

def show_entry_fields():
    file_path = e2.get()
    video_link = e3.get()
    playlist_link = e4.get()
    channel_link = e5.get()
    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    var.extend((
        file_path,
        video_link,
        playlist_link,
        channel_link))

var = []    

master = tk.Tk()
#maybe superfluous
# tk.Label(master, 
#          text="Scrape").grid(row=0)
tk.Label(master, 
         text="File Path").grid(row=1)
tk.Label(master, 
         text="Scrape Video").grid(row=2)
tk.Label(master, 
         text="Scrape Playlist").grid(row=3)
tk.Label(master, 
         text="Scrape Channel").grid(row=4)

#e1 = tk.Entry(master)
e2 = tk.Entry(master, width = '40')
e3 = tk.Entry(master, width = '40')
e4 = tk.Entry(master, width = '40')
e5 = tk.Entry(master, width = '40')


#e1.grid(row=0, column=1)
e2.grid(row=1, column=1, pady=5)
e3.grid(row=2, column=1, pady=5)
e4.grid(row=3, column=1, pady=5)
e5.grid(row=4, column=1, pady=5)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=10)


tk.Button(master, 
          text='Enter', command=show_entry_fields).grid(row=5, 
                                                       column=0, 
                                                       sticky=tk.E, 
                                                       pady=10)


tk.mainloop()


# var.append((
#     file_path,
#     video_link,
#     playlist_link,
#     channel_link))

a = [len(x) for x in var[1:]]
if a.count(0) != 2:
	print("something is wrong")



print(__name__)
import scrape_playlist

print(scrape_playlist.scrapedPlaylistId)
scrape_playlist.scrapedPlaylistId = 'tits'
print(scrape_playlist.scrapedPlaylistId)

   
#scrape_playlist.main()
