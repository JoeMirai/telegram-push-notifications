import os,requests,schedule,time,csv,random
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
    # Open the CSV file
    with open('dict.csv', 'r') as file:
        # Read the CSV file into a dictionary
        reader = csv.DictReader(file)
        words_data = list(reader)

        # Choose a random word and update its repetitiveness value
        selected_word = random.choice(words_data)
        selected_word['repetitiveness'] = str(int(selected_word['repetitiveness']) + 1)

    # Write the updated data back to the CSV file
    with open('dict.csv', 'w', newline='') as file:
        # Write the header
        fieldnames = ['word', 'repetitiveness']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Write the updated data
        writer.writerows(words_data)
    
    return selected_word['word'], int(selected_word['repetitiveness'])






schedule.every().day.at("07:00").do(theory)


    
while True:

    # Get the current time
    current_time = datetime.now().time()

    # Extract hours and minutes
    hours = current_time.hour
    minutes = current_time.minute
    # Check if the current time is between 8 am and 9 pm
    if 6 <= hours < 19:
        if minutes == 30: 
          dict_word = get_dict_word()
          send_telegram_message(dict_word)
          print(f"a word {dict_word} has been sent")
          time.sleep(60)
    
    schedule.run_pending()
    time.sleep(30)
