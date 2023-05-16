import os
import time
import random
import telegram
import argparse
from dotenv import load_dotenv

def publish_images_at_intervals(api_key, channel_id, hours_interval, folder_name):
    bot = telegram.Bot(token=api_key)
    while True:
        folder_path, folder_names, file_names = next(os.walk(folder_name))
        random.shuffle(file_names)

        for image_to_publish in file_names:
            full_path_to_image = os.path.join(folder_name, image_to_publish)
            with open(full_path_to_image, 'rb') as image_file:
                bot.send_document(chat_id=channel_id, document=image_file)

            time.sleep(hours_interval * 60 * 60)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ['TELEGRAM_API_KEY']
    channel_id = os.environ['TELEGRAM_CHANNEL_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('--hours_interval', help='Frequency of publication in hours', default=4, type=int)
    parser.add_argument('--folder_name', help='Name of the folder containing images', default='images')
    args = parser.parse_args()

    publish_images_at_intervals(api_key, channel_id, args.hours_interval, args.folder_name)