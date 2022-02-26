import requests as rq
import json

def weather_responser(url):
    respone = rq.get(url)
    dict_response = json.loads(respone.text)
    weather_descrs = dict_response.get('weather')[0]['description'].capitalize()
    degree = dict_response.get('main')['temp']
    return f'{weather_descrs}, {degree}°C'

def exchanger_responser(url, val):
    resp = rq.get(url)
    dict_resp = json.loads(resp.text)
    currency = dict_resp.get('conversion_rates')
    return f'{round(currency.get(val), 2)} {val}'

# print(exchanger_responser('https://v6.exchangerate-api.com/v6/ba64cccfa622527fe9af0335/latest/USD', 'KGS'))
