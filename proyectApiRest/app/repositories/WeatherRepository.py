import requests

class WeatherRepository:
    def get_weatherData(self, city):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e0459fb77864e3363a6007e2d9424206&units=metric%27')
        data = response.json()
        print(data)
        return{
            "temp": data["main"]["temp"],
            "rain": "rain" in data["weather"][0]["description"] 
        }
        
         