import os
import random
import telegram
import argparse
from dotenv import load_dotenv

def publish_image(api_key, channel_id, folder_name, image_name):
    if image_name is None:
        folder_path, folder_names, file_names = next(os.walk(folder_name))
        image_to_publish = random.choice(file_names)
    else:
        image_to_publish = image_name

    full_path_to_image = os.path.join(folder_name, image_to_publish)
    bot = telegram.Bot(token=api_key)
    with open(full_path_to_image, 'rb') as image_file:
        bot.send_document(chat_id=channel_id, document=image_file)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ['TELEGRAM_API_KEY']
    channel_id = os.environ['TELEGRAM_CHANNEL_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_name', help='Name of the folder containing images', default='images')
    parser.add_argument('--image_name', help='Name of the image to publish')
    args = parser.parse_args()

    publish_image(api_key, channel_id, args.folder_name, args.image_name)