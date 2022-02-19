import requests as rq
import json

def url_responser(url):
    respone = rq.get(url)
    dict_response = json.loads(respone.text)
    weather_descrs = dict_response.get('weather')[0]['description']
    # degree = dict_response.get('main')[0]['temp']
    return f'{weather_descrs.capitalize()}'
