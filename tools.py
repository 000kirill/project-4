import requests
from pathlib import Path
from dotenv import load_dotenv
import os

def download_image(link, path, directory, payload=None):
    
    Path(directory).mkdir(parents=True, exist_ok=True)
    response = requests.get(link, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def make_request(url, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()