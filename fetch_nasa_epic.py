import requests
from download_image import download_image


def main():
    api_key = "REM5wj8lR6iLveXgu5KW2ey8cEgug1DlOUSgeoMM"
    url = "https://api.nasa.gov/EPIC/api/natural"
    payload = {
        "api_key": api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    for i, epic_image in enumerate(response.json()):
        date = epic_image["date"]
        image = epic_image["image"]

        date = date.split()[0]
        split = date.split("-")
        year = split[0]
        mounth = split[1]
        number = split[2]
        
        link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{number}/png/{image}.png"
        path = f'pictures/epic{i}.png'
        download_image(link, path, api_key)

if __name__ == 'main':
    main()