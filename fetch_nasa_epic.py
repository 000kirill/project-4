from tools import download_image
from tools import make_request
import os
from datetime import datetime
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    parser.add_argument("--api_key", type=str, help=" NASA api key: ", default="REM5wj8lR6iLveXgu5KW2ey8cEgug1DlOUSgeoMM")
    args = parser.parse_args()
    directory = args.directory
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": args.api_key
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