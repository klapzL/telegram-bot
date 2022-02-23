import telebot
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)
