import requests
from pathlib import Path
from dotenv import load_dotenv
import os

def download_images(link, path, api_key=""):
    payload = {
        "api_key": api_key
    }
    load_dotenv()
    directory = os.environ.get("DIRECTORY")
    Path(directory).mkdir(parents=True, exist_ok=True)
    response = requests.get(link, payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def make_request(url, payload=""):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


