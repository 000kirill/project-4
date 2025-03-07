from tools import download_image, make_request
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    start_date = os.environ["START_DAY"]
    end_date = os.environ["END_DAY"]
    api_key = os.environ["NASA_API_KEY"]
    directory = os.environ["DIRECTORY"]
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
            "api_key": api_key,
            "start_date": start_date,
            "end_date": end_date
        }
    nasa_images = make_request(url, payload)
    for i, nasa_image in enumerate(nasa_images):
        if nasa_image["media_type"] == "image":
            link = nasa_image["url"]
            extention = os.path.splitext(link)[1]
            path = os.path.join(directory, f"nasa{i}{extention}")
            download_image(link, path, directory)
        else:
            continue
        

if __name__ == "__main__":
    main()
