from flask import Flask
from flask_restx import Api
from src.resources.weather import weather_ns, WeatherCityName, WeatherMaxNumber

# configs
app = Flask(__name__)
api = Api(app)

# namespaces
api.add_namespace(weather_ns)
# routes
weather_ns.add_resource(WeatherMaxNumber, '/weather?max=<max_number>')
weather_ns.add_resource(WeatherCityName, '/weather/<city_name>')

if __name__ == '__main__':
    app.run(debug=True)
