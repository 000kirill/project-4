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
    args = parser.parse_args()
    load_dotenv()
    delay = os.getenv("TIME", default=14400)
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    directory = args.directory
    bot = telegram.Bot(token)
    while True:
        try:
            paths = collect_files(directory)
            random.shuffle(paths)
            for path in paths:
                with open(path, 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(10)
            time.sleep(delay)
        except requests.ConnectionError:
            time.sleep(5)


if __name__ == "__main__":
    main()