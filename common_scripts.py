import os
import requests
from pathlib import Path
from urllib.parse import urlparse

def create_folder(folder_name):
    folder_path = Path(folder_name)
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Папка '{folder_name}' успешно создана.")
    return folder_path

def get_file_extension(image_url):
    parsed_url = urlparse(image_url)
    path, file_extension = os.path.splitext(parsed_url.path)
    return file_extension

def download_and_save_image(url, file_path, params=None):
    if params is not None:
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)

    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)