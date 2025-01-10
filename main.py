import requests
from pathlib import Path
from urllib.parse import urlparse
import os
import pprint

def download_image(link, path, api_key=""):
    payload = {
        "api_key": api_key
    }
    response = requests.get(link, payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch():
    Path("pictures").mkdir(parents=True, exist_ok=True)
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    links_list = response.json()["links"]["flickr"]['original']
    pprint.pprint(links_list)
    for i, link in enumerate(links_list):
        path = f'pictures/spacex{i}.jpeg'
        download_image(link, path)


def fetch_nasa_images(api_key):
    payload = {
        "api_key": api_key,
        "start_date": "2024-12-01",
        "end_date": "2024-12-29"
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    a_list = response.json()
    links_list = []
    for url in a_list:
        links_list.append(url["url"])
    for i, link in enumerate(links_list):
        extention = os.path.splitext(link)[1]
        path = f'pictures/nasa{i}{extention}'
        download_image(link, path)
        

def fetch_nasa_epic(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": api_key
    }
    
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for i in range(10):
        date = response.json()[i]["date"]
        image = response.json()[i]["image"]

        date = date.split()[0]
        split = date.split("-")
        year = split[0]
        mounth = split[1]
        number = split[2]
        
        link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{number}/png/{image}.png"
        path = f'pictures/epic{i}.png'
        download_image(link, path, api_key)
        

    
def main():
    api_key = "REM5wj8lR6iLveXgu5KW2ey8cEgug1DlOUSgeoMM"
    fetch_nasa_epic(api_key)
    # fetch_spacex_last_launch()
    # fetch_nasa_images(api_key)


if __name__ == "__main__":
    main()