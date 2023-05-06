import os
from pathlib import Path
from urllib.parse import urlparse

def create_folder(folder_name):
    folder_path = Path(folder_name)
    if not folder_path.exists():
        folder_path.mkdir()
        print(f"Папка '{folder_name}' успешно создана.")
    else:
        print(f"Папка '{folder_name}' уже существует.")
    return folder_path

def get_file_extension(image_url):
    parsed_url = urlparse(image_url)
    path, file_extension = os.path.splitext(parsed_url.path)
    return file_extension