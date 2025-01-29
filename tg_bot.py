import telegram
import random
import os
import time
from dotenv import load_dotenv


load_dotenv()
delay = os.environ.get("TIME")
token = os.environ.get("TOKEN")
bot = telegram.Bot(token)
while True:
    for root, dirs, files in os.walk("pictures"):
        random.shuffle(files)
        for photo in files:
            bot.send_document(chat_id="@cosmicpicture1", document=open(f'pictures/{photo}', 'rb'))
            time.sleep(10)
    time.sleep(delay)