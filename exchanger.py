import telebot
import os
from dotenv import load_dotenv
from module import exchanger_responser

load_dotenv()
token = '5144453861:AAFQ7mnec9IasqsjRzPyXIxm_c8GJyxCpFY'
exchanger_key = os.environ.get('EXCHANGE_RATE_API_KEY')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Я бот обменник валют. Введите валюту, курс который вам необходим:')

@bot.message_handler(content_types=['text'])
def show_currency(message):
    print(message.text)
    try:
        currency = exchanger_responser(f'https://v6.exchangerate-api.com/v6/{exchanger_key}/latest/{message.text}')
        bot.send_message(message.chat.id, currency)
    except NameError:
        bot.send_message(message.chat.id, 'Название валюты введено неправильно. Введите корректное название валюты (например: USD):')


bot.polling()
