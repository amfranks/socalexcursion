from django.shortcuts import render
import requests

# Create your views here.
from django.shortcuts import HttpResponse
from .models import Location

# from django.template import loader


def show_all_locations(request):
    locations = Location.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=63b2b15dd383ffdd72ca21f3cf842ad9'
    city = 'San Clemente'

    # request the API data and convert the JSON to Python data types
    response = requests.get(url.format(city)).json()
    
    city_weather = {
        'city' : city,
        'temperature' : response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
    }

    context = {'displayLocations': locations, 'pageTitle': 'Tourism', 'city_weather' : city_weather}

    # returns the index.html template
    return render(request, 'location/index.html', context)


def show_category_locations(request, categoryname):
    try:
        locations = Location.objects.filter(categoryid__name__iexact=categoryname)
        if locations.count() > 0:
            context = {'displayLocations': locations, 'categoryName': categoryname}
            return render(request, 'location/category.html', context)
        # else:
            # return HttpResponse(f'<h1>Unable to locate any items in our database of type {categoryname}</h1>')
    except:
        return HttpResponse(f'<h1>Unable to locate any locations of type {categoryname}</h1>')

def show_wishlist(request):
    # try:
        
    # except:

    return render(request, 'location/wishlist.html')