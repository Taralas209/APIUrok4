import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse, urlencode


def create_folder(folder_name):
    folder_path = Path(folder_name)
    if not folder_path.exists():
        folder_path.mkdir()
        print(f"Папка '{folder_name}' успешно создана.")
    else:
        print(f"Папка '{folder_name}' уже существует.")
    return folder_path

def fetch_nasa_epic(folder_path, nasa_token):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': nasa_token,
    }
    
    response = requests.get(epic_url, params=urlencode(payload))
    response.raise_for_status()

    for i, image_data in enumerate(response.json()):
        image_date = image_data['date']
        splitted_date = image_date.split()
        year, mounth, day = (splitted_date[0].split('-'))
        image_name = image_data['image']
        
        epic_archive_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{day}/png/{image_name}.png"
        payload = {
            'api_key': 'vBlYQAPas0Yh8uCldsXmYmZepKIOvsX6xJxm0x7Y',
        }
        archive_response = requests.get(epic_archive_url, params=urlencode(payload))
        archive_response.raise_for_status()

        file_name = "nasa_epic_{}_{}.png".format(splitted_date[0], i)
        file_path = folder_path / file_name
        with open(file_path, 'wb') as file:
            file.write(archive_response.content)

    
def fetch_nasa_apod(folder_path, nasa_token):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_token,
        'count': 5,
    }
    
    response = requests.get(nasa_url, params=urlencode(payload))
    response.raise_for_status()

    for i, response in enumerate(response.json()):
        image_url = response['url']
        file_extension = get_file_extension(image_url)
        file_name = "nasa_{}{}".format(i, file_extension)
        file_path = folder_path / file_name
        with open(file_path, 'wb') as file:
            file.write(requests.get(image_url).content)



def fetch_spacex_last_launch(folder_path):    
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(spacex_url)
    response.raise_for_status()

    images = response.json()['links']['flickr']['original']
    for i, image_url in enumerate(images):
        file_extension = get_file_extension(image_url)
        file_name = "spacex_{}{}".format(i, file_extension)
        file_path = folder_path / file_name
        with open(file_path, 'wb') as file:
            file.write(requests.get(image_url).content)


def get_file_extension(image_url):
    parsed_url = urlparse(image_url)
    path, file_extension = os.path.splitext(parsed_url.path)
    return file_extension


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']
    folder_name = "images"
    folder_path = create_folder(folder_name)
    fetch_spacex_last_launch(folder_path)
    fetch_nasa_apod(folder_path, nasa_token)
    fetch_nasa_epic(folder_path, nasa_token)

if __name__ == "__main__":
    main()




