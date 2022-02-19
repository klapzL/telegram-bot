from dotenv import load_dotenv
import os
import telebot
from module import weather_responser

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')
weather_token = os.environ.get('OPENWEATHER_API_KEY')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Я бот прогноза погоды. Введите название города:')

@bot.message_handler(content_types=['text'])
def show_weather(message):
    try:
        weather = weather_responser(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric&lang=ru')
        bot.send_message(message.chat.id, weather)
    except TypeError:
        bot.send_message(message.chat.id, 'Название города введено неправильно.')

bot.polling()