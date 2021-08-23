from flask import Flask
from flask_restx import Api
from src.cache import cache

from src.resources.weather import weather_ns, WeatherCityName, WeatherMaxNumber

# configs
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
api = Api(app)

# namespaces
api.add_namespace(weather_ns)

# routes
weather_ns.add_resource(WeatherMaxNumber, '/?max=<max_number>')
weather_ns.add_resource(WeatherCityName, '/<city_name>')

if __name__ == '__main__':
    app.run(debug=True)
