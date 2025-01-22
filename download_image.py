import requests
from pathlib import Path

def download_image(link, path, api_key=""):
    payload = {
        "api_key": api_key
    }
    Path("pictures").mkdir(parents=True, exist_ok=True)
    response = requests.get(link, payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def main():
    download_image()


if __name__ == 'main':
    main()