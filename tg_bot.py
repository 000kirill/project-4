import telegram
import random
import os
import time
from dotenv import load_dotenv
import argparse
import requests


def collect_files(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            paths.append(os.path.join(directory, file_name))
    return paths

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    parser.add_argument("--delay", type=int, help="Время задержки: ", default=14400)
    args = parser.parse_args()
    directory = args.directory
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token)
    while True:
        paths = collect_files(directory)
        random.shuffle(paths)
        for path in paths:
            try:
                with open(path, 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
            except requests.ConnectionError:
                time.sleep(5)
            time.sleep(10)
        time.sleep(args.delay)
        

if __name__ == "__main__":
    main()