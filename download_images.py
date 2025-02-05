import requests
from pathlib import Path
from dotenv import load_dotenv

def download_images(link, path, api_key=""):
    payload = {
        "api_key": api_key
    }
    Path("pictures").mkdir(parents=True, exist_ok=True)
    response = requests.get(link, payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def main():
    download_images()


if __name__ == 'main':
    main()