from tools import download_image
from tools import make_request
import os
from dotenv import load_dotenv
from datetime import datetime


def main():
    load_dotenv()
    
    api_key = os.environ["NASA_API_KEY"]
    directory = os.environ["DIRECTORY"]
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": api_key
    }
    response = make_request(url, payload)
    for i, epic_image in enumerate(response):
        date = epic_image["date"]
        image = epic_image["image"]
        
        date = datetime.fromisoformat(date)
        year = date.year
        month = date.strftime("%m")
        day = date.strftime("%d")
        
        link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png"
        path = os.path.join(directory, f"epic{i}.jpg")
        download_image(link, path, directory, payload)


if __name__ == "__main__":
    main()