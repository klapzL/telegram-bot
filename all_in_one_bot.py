import os
import telebot
import requests as rq
from dotenv import load_dotenv
from module import weather_responser
from module import exchanger_responser

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Weather Forecast', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Exchanger', callback_data=2))
    bot.send_message(message.chat.id, text="Какая функция бота нужна?", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
        weather_token = os.environ.get('OPENWEATHER_API_KEY')
        bot.send_message(call.message.chat.id, 'Введите название города:')
        @bot.message_handler(content_types=['text'])
        def show_weather(message):
            try:
                weather = weather_responser(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric&lang=ru')
                bot.send_message(message.chat.id, weather)
            except TypeError:
                bot.send_message(message.chat.id, 'Название города введено неправильно.')
    elif call.data == '2':
        exchanger_key = os.environ.get('EXCHANGE_RATE_API_KEY')
        bot.send_message(call.message.chat.id, 'Введите две валюты:')
        @bot.message_handler(content_types=['text'])
        def show_currency(message):
            val = message.text.split()
            try:
                currency = exchanger_responser(f'https://v6.exchangerate-api.com/v6/{exchanger_key}/latest/{val[0]}', val[1])
                bot.send_message(message.chat.id, currency)
            except NameError:
                bot.send_message(message.chat.id, 'Название валюты введено неправильно. Введите корректное название валюты (например: USD):')

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     keyboard = telebot.types.ReplyKeyboardMarkup(True)
#     keyboard.row('Weather Forecast', 'Exchanger')
#     bot.send_message(message.chat.id, 'привет!', reply_markup=keyboard)

bot.polling()
