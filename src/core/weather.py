from src.utils.apikey import API_KEY_WEATHER
from src.cache import cache
from src.utils.messages import *
import requests


class WeatherCore:
    def __init__(self, **dependencies):
        self.response = dependencies.get('response')

    def max_number(self, data):
        pass

    @cache.cached(timeout=300)
    def city_name(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_WEATHER}'
        response = requests.get(url).json()

        if response.get('cod') != 200:
            return self.response.not_found(CITY_NOT_FOUND)

        return self.response.success('Success', response)
