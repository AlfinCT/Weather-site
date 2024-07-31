import urllib
import json
import urllib.request
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=748acaaed7075639170606d44ab2388e').read()
        list_of_data = json.loads(source)
        temp_celsius = list_of_data['main']['temp']
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": f"{temp_celsius:.2f} °C",  # Display temperature in Celsius
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "icon": list_of_data['weather'][0]['icon'],
            "description": list_of_data['weather'][0]['description'],
            "city_name": str(list_of_data['name']),
            "wind_speed": str(list_of_data['wind']['speed'])+'kph',

        }
        print(data)
    else:
        data = {}
    return render(request, 'index.html', data)