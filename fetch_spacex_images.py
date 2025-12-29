from tools import download_image, make_request
import os 
import argparse


def download_spacex_images(response, directory):
    links = response["links"]["flickr"]['original']
    for i, link in enumerate(links):
        path = os.path.join(directory, f"spacex{i}.jpg")
        download_image(link, path, directory)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, help="Название папки: ", default="pictures")
    parser.add_argument("--launch_id", type=str, help="launch id: ", default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    directory = args.directory
    
    url = f"https://api.spacexdata.com/v5/launches/{args.launch_id}"
    response = make_request(url)
    download_spacex_images(response, directory)


if __name__ == "__main__":
    main()
