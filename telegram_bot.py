import os
import random
import telegram
import argparse
from dotenv import load_dotenv

def publish_image(api_key, channel_id, folder_name, image_name):
    full_path_to_image = os.path.join(folder_name, image_name)
    bot = telegram.Bot(token=api_key)
    with open(full_path_to_image, 'rb') as image_file:
        bot.send_document(chat_id=channel_id, document=image_file)

def get_random_image_name(folder_name):
    folder_path, folder_names, file_names = next(os.walk(folder_name))
    return random.choice(file_names)

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ['TELEGRAM_API_KEY']
    channel_id = os.environ['TELEGRAM_CHANNEL_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_name', help='Name of the folder containing images', default='images')
    parser.add_argument('--image_name', help='Name of the image to publish')
    args = parser.parse_args()

    if args.image_name is None:
        args.image_name = get_random_image_name(args.folder_name)

    publish_image(api_key, channel_id, args.folder_name, args.image_name)