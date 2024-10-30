from app.repositories.WeatherRepository import WeatherRepository

class WeatherService:
    def __init__(self):
        self._repo = WeatherRepository()
        
    def kelvin_a_celsius(self, k):
        return k - 273.15
        
    def fahrenheit_a_celsius(self, f):
        return (f - 32) / 1.8 
        
    def get_message(self, city):
        data = self._repo.get_weatherData(city)
        celsius_temp = self.kelvin_a_celsius(data['temp'])
        print (celsius_temp)
        if celsius_temp > 27:
            return "Esta para el chapu en la yapla"
        elif data['rain']:
            return "Esta para quedarse a tomar mate en la casona"
        else: 
            return "Un dia normal capo"
        
        
