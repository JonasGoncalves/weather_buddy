from flask_restx import Namespace, Resource
from flask import request
from controller.weather import WeatherController

weather_ns = Namespace('weather')


class WeatherCityName(Resource):
    def get(self, city_name):
        """
        Returns weather data by city name
        """

        return WeatherController().city_name(city_name)


class WeatherMaxNumber(Resource):
    def get(self):
        """
        Returns all the cached cities
        """
        max_number = request.args.to_dict()
        return WeatherController().max_number(max_number)



