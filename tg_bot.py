import telegram
import random
import os
import time
from dotenv import load_dotenv
import argparse


def collect_files(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            paths.append(os.path.join(directory, file_name))
    return paths


def send_images(directory, bot, chat_id, delay):
    while True:
        paths = collect_files(directory)
        random.shuffle(paths)
        for path in paths:
            while True:
                try:
                    with open(path, 'rb') as file:
                        bot.send_document(chat_id=chat_id, document=file)
                    break
                except (ConnectionError, telegram.error.TimedOut, telegram.error.NetworkError):
                    time.sleep(5)
                    continue
            time.sleep(delay)
        time.sleep(delay)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    parser.add_argument("--delay", type=int, help="Время задержки: ", default=14400)
    args = parser.parse_args()
    directory = args.directory
    delay = args.delay
    load_dotenv()
    token = os.environ["TG_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token)
    send_images(directory, bot, chat_id, delay)
    
        

if __name__ == "__main__":
    main()