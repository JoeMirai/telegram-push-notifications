import os,requests,schedule,time,csv,random
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

bot_token = os.getenv("bot_token", "")
chat_id = os.getenv("chat_id", "")
theory_bot_token = os.getenv("theory_bot_token", "")

#### root ####
def send_telegram_file(file_path):
  url = f"https://api.telegram.org/bot{theory_bot_token}/sendDocument"
  files = {'document': open(file_path, 'rb')}  
  data = {'chat_id' : chat_id}
  r= requests.post(url, files=files, data=data)
  return r.status_code

for page_num in range(7,25):
  file_name = f'page{page_num}.png' 
  file_path = os.path.join('/config/Downloads/telegram-push-notifications/questions_images', file_name)
  send_telegram_file(file_path)

