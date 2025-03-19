from tools import download_image, make_request
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    parser.add_argument("--api_key", type=str, help=" NASA api key: ", default="REM5wj8lR6iLveXgu5KW2ey8cEgug1DlOUSgeoMM")
    parser.add_argument("--start_date", type=str, help="Дата начала отсчета: ", default="2024-12-01")
    parser.add_argument("--end_date", type=str, help=" Дата конца отсчета: ", default="2024-12-29")
    args = parser.parse_args()
    directory = args.directory
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
            "api_key": args.api_key,
            "start_date": args.start_date,
            "end_date": args.end_date
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
