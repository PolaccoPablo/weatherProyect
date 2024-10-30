from flask import Blueprint, request 
from app.services.WeatherService import WeatherService

weather_bp = Blueprint ('weather', __name__)

#Endpoint 
@weather_bp.route('/weather', methods=['GET']) # esto se invoca de afuera
def get_weather():
    city = request.args.get('city')
    _weather_service = WeatherService()
    message = _weather_service.get_message(city) # aca se invoca la logica de negocio del service
    return {"message": message}