import os
import argparse
import requests
from dotenv import load_dotenv
from urllib.parse import urlencode
from common_scripts import get_file_extension, create_folder


def fetch_nasa_apod(folder_path, nasa_token, count=5):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_token,
        'count': count,
    }
    response = requests.get(nasa_url, params=urlencode(payload))
    response.raise_for_status()

    for index, image_info in enumerate(response.json()):
        image_url = image_info['url']
        file_extension = get_file_extension(image_url)
        file_name = "nasa_{}{}".format(index, file_extension)
        file_path = folder_path / file_name
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        with open(file_path, 'wb') as file:
            file.write(image_response.content)

if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument('--count', help='How many pictures to download', default=5, type=int)
    args = parser.parse_args()

    folder_name = "images"
    folder_path = create_folder(folder_name)
    fetch_nasa_apod(folder_path, nasa_token, args.count)