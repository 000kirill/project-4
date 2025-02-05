import requests
from download_images import download_image


def main():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]['original']
    for i, link in enumerate(links):
        path = f'pictures/spacex{i}.jpeg'
        download_image(link, path)


if __name__ == 'main':
    main()