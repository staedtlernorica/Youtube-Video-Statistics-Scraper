import os
from datetime import date

default_save_path = f"{os.getenv('USERPROFILE')}/Desktop" 
today = str(date.today())
default_csv_name = f"Scraped Youtube { today}"