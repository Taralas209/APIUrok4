import os
import requests
from urllib.parse import urlparse


def get_file_extension(image_url):
    parsed_url = urlparse(image_url)
    path, file_extension = os.path.splitext(parsed_url.path)
    return file_extension


def download_and_save_image(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)