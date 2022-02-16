from dotenv import load_dotenv
import os
import telebot
from module import url_responser

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)

data_dict = {'city': input('Введите название города: '), 'key': os.environ.get('OPENWEATHER_API_KEY')}
url = url_responser('https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=ru')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Я бот прогноза погоды. Введите название города:')

@bot.message_handler(content_types=['text'])
def show_weather(message):
    bot.send_message(message.chat.id, f'Вы написали: {message.text}')
    return url
# bot.polling()