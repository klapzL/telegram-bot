import requests as rq
import json
import os

def url_responser(url):
    response = rq.get(url)
    dict_response = json.loads(response.text)
    weather = dict_response.get('weather')[0]
    return weather['description'].capitalize()

key = os.environ.get('OPENWEATHER_API_KEY')
print(url_responser('https://api.openweathermap.org/data/2.5/weather?q=London&appid={key}&units=metric&lang=ru'))