from flask_restx import Namespace, Resource
from flask import request
from src.controller.weather import WeatherController

weather_ns = Namespace('weather')


class WeatherMaxNumber(Resource):
    def get(self):
        data = request.args.to_dict()
        return WeatherController().max_number(data)


class WeatherCityName(Resource):
    def get(self, city_name):
        """
        Returns weather data by city name
        """
        return WeatherController().city_name(city_name)
