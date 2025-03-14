from tools import download_image, make_request
import os
from pathlib import Path
from dotenv import load_dotenv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    args = parser.parse_args()
    load_dotenv()
    launch_id = os.environ["LAUNCH_ID"]
    directory = args.directory
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = make_request(url, payload="")
    links = response["links"]["flickr"]['original']
    for i, link in enumerate(links):
        path = os.path.join(directory, f"spacex{i}.jpg")
        download_image(link, path, directory)


if __name__ == "__main__":
    main()
