import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/User/Desktop/All Desktop Folder/importants Screenshots/Problem SS/"
destination_dir = "C:/Users/User/Desktop/All Desktop Folder/Backup Files and Folder"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder Copied To: {dest_dir}")
    except FileExistsError:
        print(f"Folder Already Exists in: {dest}")
        
        
schedule.every().days.at("10:58").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)     

         
    