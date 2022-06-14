from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from django.template import loader
# Create your views here.

def index(request):
    return render(request, 'index.html')


def weather(request):
    try:
        city = {'city': request.POST.get('cityname')}
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY =city['city']
        API_KEY = "f0665395dee59e656b8a205b0d1931d2"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            main['temp'] = round(main['temp'] - 272.15, 2)
            report = data['weather']
            main['report'] = report[0]['description']
            main['city'] = data['name']
            main['country'] = data['sys']['country']
            return render(request, 'index.html',main)
        else:
            return render(request, 'index.html')
    except:
        return render(request, 'index.html')

