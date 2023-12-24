import os
import requests 
import schedule
import time
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

bot_token = os.getenv("bot_token", "")
chat_id = os.getenv("chat_id", "")

#### root ####
def send_telegram_file(file_path):
  url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
  files = {'document': open(file_path, 'rb')}  
  data = {'chat_id' : chat_id}
  r= requests.post(url, files=files, data=data)
  return r.status_code

#### root ####
def send_telegram_message(message):
    bot_token = "bot_token"
    chat_id = "chat_id"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)


def get_next_image():
  with open('tempvar', 'r+') as f:
    page_num = int(f.read()) + 1
    f.seek(0)
    f.write(str(page_num))
    f.truncate()

  file_name = f'page{page_num}.png' 
  file_path = os.path.join('/config/Downloads/telepy/questions_images', file_name)
  send_telegram_file(file_path)

def theory():
  print("its theory practice time.. sending you something fun")
  get_next_image()
  get_next_image()

def get_words():
   
   pass
schedule.every().day.at("07:00").do(theory)


    
while True:

    # Get the current time
    current_time = datetime.now().time()

    # Extract hours and minutes
    hours = current_time.hour
    minutes = current_time.minute
    print(type(minutes))
    if minutes == 10:
       print("true")

    schedule.run_pending()
    time.sleep(1)