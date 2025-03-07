import telegram
import random
import os
import time
from dotenv import load_dotenv


def collect_files(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        random.shuffle(files)
        for file_name in files:
            paths.append(os.path.join(directory, file_name))
    return paths

def main():
    load_dotenv()
    delay = os.getenv("TIME", default=14400)
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    directory = os.getenv("DIRECTORY", default="images")
    bot = telegram.Bot(token)
    while True:
        for path in collect_files(directory):
            with open(path, 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file )
            time.sleep(10)
        time.sleep(delay)


if __name__ == "__main__":
    main()