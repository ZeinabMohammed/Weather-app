from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=917fe0498a0cf04f95e2814b27d764c8'
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()
	form = CityForm()
	cities = City.objects.all()
	weather_data =[]
	for city in cities:

		r = requests.get(url.format(city)).json()
		# print(r.text)
		city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

		weather_data.append(city_weather)
	print(weather_data)
	context={'weather_data':weather_data, 'form':form}
	print(city_weather)
	return render(request,'weather/weather.html', context)
