import requests as rq
import json

def url_responser(url):
    def inner(data_dict):
        nonlocal url
        response = rq.get(url.format_map(data_dict))
        dict_response = url(data_dict)
        weather = dict_response.get('weather')[0]
        return weather['description'].capitalize()

    return inner
