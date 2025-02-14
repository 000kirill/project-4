from tools import download_images
from tools import make_request
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("NASA_API_KEY")
    directory = os.environ.get("DIRECTORY")
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": api_key
    }
    response = make_request(url, payload)
    for i, epic_image in enumerate(response):
        date = epic_image["date"]
        image = epic_image["image"]

        date = date.split()[0]
        split = date.split("-")
        year = split[0]
        mounth = split[1]
        number = split[2]
        
        link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{number}/png/{image}.png"
        path = os.path.join(directory, f"epic{i}.jpg")
        download_images(link, path, api_key)


if __name__ == "__main__":
    main()