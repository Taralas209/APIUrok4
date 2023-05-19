import argparse
import requests
from common_scripts import get_file_extension, create_folder, download_and_save_image

def fetch_spacex_images(folder_path, launch_id):
    spacex_url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']

    for index, image_url in enumerate(images):
        file_extension = get_file_extension(image_url)
        file_name = "spacex_{}{}".format(index, file_extension)
        file_path = folder_path / file_name

        download_and_save_image(image_url, file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default="latest", help='ID of the SpaceX launch.')
    args = parser.parse_args()

    folder_name = "images"
    folder_path = create_folder(folder_name)
    fetch_spacex_images(folder_path, args.launch_id)


