import os
import telegram
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['TELEGRAM_API_KEY']
bot = telegram.Bot(token=api_key)

channel_id = '-1001968826354'
#bot.send_message(text="Привет, канал!", chat_id=channel_id)
bot.send_document(chat_id=channel_id, document=open('images/spacex_0.png', 'rb'))

