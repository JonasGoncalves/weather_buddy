from utils.apikey import API_KEY_WEATHER
from cache import cache
from utils.messages import CITY_FOUND, CITY_NOT_FOUND, CACHE_EMPTY, CITY_CACHE_FOUND
import requests


class WeatherCore:
    def __init__(self, **dependencies):
        self.response = dependencies.get('response')

    @cache.memoize(timeout=300, args_to_ignore='self')
    def city_name(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_WEATHER}'
        response = requests.get(url).json()
        cache.set('city_name', response)
        if response.get('cod') != 200:
            return self.response.not_found(CITY_NOT_FOUND)

        return self.response.success(CITY_FOUND, response)

    def max_number(self, max_number=None):
        cached_keys = []
        response = []
        if max_number:
            max_number = int(max_number.get('max'))

        else:
            max_number = 5

        for city in cache.cache._cache:
            cached_keys.append(city)

        if not cached_keys:
            return self.response.not_found(CACHE_EMPTY)
        cached_keys.pop(0)
        cached_cities = cache.get_many(*cached_keys)
        if len(cached_cities) == 0:
            return self.response.not_found(CACHE_EMPTY)

        for i in range(len(cached_cities)):
            city = cached_cities[0]
            if city:
                city_data = city[0]
                if city_data['data'] is not None:
                    response.append(city)
                    cached_cities.pop(0)
                    max_number = max_number - 1
                else:
                    cached_cities.pop(0)
            else:
                cached_cities.pop(0)
            if max_number == 0:
                break

        if len(response) == 0:
            return self.response.not_found(CACHE_EMPTY)
        return self.response.success(CITY_CACHE_FOUND, response)
