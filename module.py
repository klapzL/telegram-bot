import requests as rq
import json

def weather_responser(url):
    respone = rq.get(url)
    dict_response = json.loads(respone.text)
    weather_descrs = dict_response.get('weather')[0]['description'].capitalize()
    degree = dict_response.get('main')['temp']
    return f'{weather_descrs}, {degree}°C'

def exchanger_responser(url):
    resp = rq.get(url)
    dict_resp = json.loads(resp.text)
    currency = dict_resp.get('conversion_rates')
    n_str = ''
    for i, f in currency.items():
        n_str += f'{i} - {f}\n'
    return n_str
