import os
import argparse
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from common_scripts import create_folder

if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']

    folder_name = "images"
    folder_path = create_folder(folder_name)

    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help='ID of the SpaceX launch.')
    parser.add_argument('--count', help='How many pictures to download', default=5, type=int)
    args = parser.parse_args()

    fetch_spacex_images(folder_path, args.launch_id)
    fetch_nasa_apod(folder_path, nasa_token, args.count)
    fetch_nasa_epic(folder_path, nasa_token)

