from tools import download_images, make_request
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("NASA_API_KEY")
    directory = os.environ.get("DIRECTORY")
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
            "api_key": api_key,
            "start_date": "2024-12-01",
            "end_date": "2024-12-29"
        }
    nasa_images = make_request(url, payload)
    for i, nasa_image in enumerate(nasa_images):
        link = nasa_image["url"]
        extention = os.path.splitext(link)[1]
        path = os.path.join(directory, f"nasa{i}{extention}")
        download_images(link, path, directory)
        

if __name__ == "__main__":
    main()
