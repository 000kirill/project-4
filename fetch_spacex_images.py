from tools import download_images, make_request
import os
from pathlib import Path
from dotenv import load_dotenv


def main():
    load_dotenv()
    directory = os.environ.get("DIRECTORY")
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = make_request(url, payload="")
    links = response["links"]["flickr"]['original']
    for i, link in enumerate(links):
        path = os.path.join(directory, f"spacex{i}.jpg")
        download_images(link, path, directory)


if __name__ == "__main__":
    main()
