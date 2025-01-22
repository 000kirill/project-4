import telegram
import random
import os
import time


bot = telegram.Bot(token='7516140299:AAGlBSDDZ8AtRBU-jbLK4V0D9Paj9kKlg40')
bot.send_document(chat_id="@cosmicpicture1", document=open('pictures/nasa1.jpg', 'rb'))
for root, dirs, files in os.walk("pictures"):
    random.shuffle(files)
    print(files)
    for photo in files:
        bot.send_document(chat_id="@cosmicpicture1", document=open(f'pictures/{photo}', 'rb'))
        time.sleep(10)