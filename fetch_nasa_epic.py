import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlencode
from common_scripts import download_and_save_image


def fetch_nasa_epic(folder_path, nasa_token):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': nasa_token,
    }

    response = requests.get(epic_url, params=urlencode(payload))
    response.raise_for_status()

    for index, image_info in enumerate(response.json()):
        image_date = image_info['date']
        splitted_date = image_date.split()
        year, mounth, day = (splitted_date[0].split('-'))
        image_name = image_info['image']

        epic_archive_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{day}/png/{image_name}.png"
        file_name = "nasa_epic_{}_{}.png".format(splitted_date[0], index)
        file_path = folder_path / file_name

        download_and_save_image(epic_archive_url, file_path, params=payload)

if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']

    folder_name = "images"
    folder_path = Path(folder_name)
    folder_path.mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic(folder_path, nasa_token)