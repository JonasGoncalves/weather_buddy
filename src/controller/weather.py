from core.weather import WeatherCore
from utils.response import Response

response = Response()


class WeatherController:
    def city_name(self, city_name):
        weather_core = WeatherCore(
            response=response
        )
        response_core = weather_core.city_name(city_name)
        return response_core

    def max_number(self, data):
        weather_core = WeatherCore(
            response=response
        )
        response_core = weather_core.max_number(data)
        return response_core


