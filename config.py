import os
from datetime import date


default_save_path = str(os.getenv('USERPROFILE')) + "\\Desktop" 
today = str(date.today())
default_csv_name = "Scraped Youtube " + today