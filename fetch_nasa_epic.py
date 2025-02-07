import requests
from download_images import download_images
import os
from dotenv import load_dotenv


def main():
    api_key = os.environ.get("API_KEY")
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    for i, epic_image in enumerate(response.json()):
        date = epic_image["date"]
        image = epic_image["image"]

        date = date.split()[0]
        split = date.split("-")
        year = split[0]
        mounth = split[1]
        number = split[2]
        
        link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{number}/png/{image}.png"
        path = os.path.join("pictures", f"epic{i}.jpg")
        download_images(link, path, api_key)


if __name__ == "__main__":
    main()