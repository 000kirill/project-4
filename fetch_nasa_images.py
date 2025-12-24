from tools import download_image, make_request
import os
import argparse
from dotenv import load_dotenv


def download_nasa_images(nasa_images, directory):
    for i, nasa_image in enumerate(nasa_images):
        if nasa_image["media_type"] == "image":
            link = nasa_image["url"]
            extension = os.path.splitext(link)[1]
            path = os.path.join(directory, f"nasa{i}{extension}")
            download_image(link, path, directory)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    parser.add_argument("--start_date", type=str, help="Дата начала отсчета: ", default="2024-12-01")
    parser.add_argument("--end_date", type=str, help="Дата конца отсчета: ", default="2024-12-29")
    args = parser.parse_args()
    directory = args.directory
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
            "api_key": api_key,
            "start_date": args.start_date,
            "end_date": args.end_date
        }
    nasa_images = make_request(url, payload)
    download_nasa_images(nasa_images, directory)
        

if __name__ == "__main__":
    main()
