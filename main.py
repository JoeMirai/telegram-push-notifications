import os,requests,schedule,time,csv,random
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

bot_token = os.getenv("bot_token", "")
chat_id = os.getenv("chat_id", "")
theory_bot_token = os.getenv("theory_bot_token", "")

current_index = 0

#### root ####
def send_telegram_file(file_path):
  url = f"https://api.telegram.org/bot{theory_bot_token}/sendDocument"
  files = {'document': open(file_path, 'rb')}  
  data = {'chat_id' : chat_id}
  r= requests.post(url, files=files, data=data)
  return r.status_code

#### root ####
def send_telegram_message(message):
    
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
  file_path = os.path.join('/config/Downloads/telegram-push-notifications/questions_images', file_name)
  send_telegram_file(file_path)

def theory():
  print("its theory practice time.. sending you something fun")
  get_next_image()
  get_next_image()



def get_dict_word():
    global current_index
    
    # Open the text file
    with open('dict.txt', 'r', encoding='utf-8') as file:
        # Read the lines from the file
        lines = file.read().splitlines()
        
        # If the list is empty, return None
        if not lines:
            return None
        
        # Initialize variables to store the current entry
        entry = []
        
        # Iterate through lines until a blank line is encountered
        while current_index < len(lines) and lines[current_index].strip():
            entry.append(lines[current_index].strip())
            current_index += 1
        
        # Join the lines to form the complete entry
        chosen_entry = '^$'.join(entry)
        
        # Skip the blank line for the next function call
        current_index += 1
        
        return chosen_entry





schedule.every().day.at("08:00").do(theory)

    
while True:

    # Get the current time
    current_time = datetime.now().time()

    # Extract hours and minutes
    hours = current_time.hour
    minutes = current_time.minute
    # Check if the current time is between 8 am and 9 pm
    if 6 <= hours < 19:
        if minutes == 15 or minutes == 45: 
          dict_word = get_dict_word()
          send_telegram_message(dict_word)
          print(f"{hours}:{minutes} a word {dict_word} has been sent")
          time.sleep(60)
    
    schedule.run_pending()
    time.sleep(30)
    
    
    
    
    
