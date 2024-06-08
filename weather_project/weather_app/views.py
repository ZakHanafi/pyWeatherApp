import datetime
import requests

from django.shortcuts import render



# Create your views here.
def index(request):
    API_KEY = open("API_KEY", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
  #  forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely, hourly,alerts&appid={}"

    if requests.method == "POST":
        city1 = request.POST['city1']
        city2 = request.get('city2', None)
        weather_data1,  = fetch_weather_and_forecast(city1, API_KEY, current_weather_url)


        if city2:
             weather_data2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url)
        else:
            weather_data2 = None, None

        context = {
            "weather_data1" : weather_data1,
           
            "weather_data2" : weather_data2,
            

        }

        return render(request, "weather_app/index.hmtl", context)
    else:
        return render(request, "weather_app/index.hmtl")
    

def fetch_weather_and_forecast(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']


    weather_data = {


        "city": city,
        "temperature": round(response['main']['temp'] - 273.15, 2), 
        "description": response['weather'][0]['description'], 
        "icon" : response['weather'][0]['icon']

    }

 
    return weather_data
