import argparse
import requests
from common_scripts import get_file_extension, create_folder

def fetch_spacex_images(folder_path, launch_id):
    spacex_url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']

    for i, image_url in enumerate(images):
        file_extension = get_file_extension(image_url)
        file_name = "spacex_{}{}".format(i, file_extension)
        file_path = folder_path / file_name
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        with open(file_path, 'wb') as file:
            file.write(image_response.content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default="latest", help='ID of the SpaceX launch.')
    args = parser.parse_args()

    folder_name = "images"
    folder_path = create_folder(folder_name)
    fetch_spacex_images(folder_path, args.launch_id)


