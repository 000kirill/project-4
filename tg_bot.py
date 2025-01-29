import telegram
import random
import os
import time
from dotenv import load_dotenv


load_dotenv()
delay = os.environ.get("TIME")
token = os.environ.get("TOKEN")
chat_id = os.environ.get("CHAT_ID")
bot = telegram.Bot(token)
while True:
    for root, dirs, files in os.walk("pictures"):
        random.shuffle(files)
        for photo in files:
            bot.send_document(chat_id=chat_id, document=open(f'pictures/{photo}', 'rb'))
            time.sleep(10)
    time.sleep(delay)