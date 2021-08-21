from flask_restx import Namespace, Resource

weather_ns = Namespace('weather')

weather_fields = weather_ns.model('WeatherFields', {

})


class WeatherMaxNumber(Resource):
    def get(self):
        pass


class WeatherCityName(Resource):
    def get(self):
        pass
