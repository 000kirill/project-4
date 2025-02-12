import requests
from download_images import download_images
import os
from pathlib import Path


def main():
    directory = os.environ.get("DIRECTORY")
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]['original']
    for i, link in enumerate(links):
        path = os.path.join(directory, f"spacex{i}.jpg")
        download_images(link, path)


if __name__ == "__main__":
    main()