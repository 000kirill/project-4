from tools import download_image, make_request
import os
from pathlib import Path
from dotenv import load_dotenv


def main():
    load_dotenv()
    launch_id = os.environ["LAUNCH_ID"]
    directory = os.environ["DIRECTORY"]
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = make_request(url, payload="")
    links = response["links"]["flickr"]['original']
    for i, link in enumerate(links):
        path = os.path.join(directory, f"spacex{i}.jpg")
        download_image(link, path, directory)


if __name__ == "__main__":
    main()
