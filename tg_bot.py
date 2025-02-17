import telegram
import random
import os
import time
from dotenv import load_dotenv


def main():
    load_dotenv()
    delay = os.environ.get("TIME")
    token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")
    directory = os.environ.get("DIRECTORY")
    bot = telegram.Bot(token)
    while True:
        for root, dirs, files in os.walk("pictures"):
            random.shuffle(files)
            
            for photo in files:
                path = os.path.join(directory, photo)
                with open(path, 'wb') as file:
                    bot.send_document(chat_id=chat_id, document=file )
                time.sleep(10)
        time.sleep(delay)


if __name__ == "__main__":
    main()