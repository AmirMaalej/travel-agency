import requests
import environ
from django.db.models import Case, CharField, Value, When
from datetime import datetime
from dateutil import tz
from itertools import groupby
from operator import itemgetter

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City, Country
from .serializers import CitySerializer, CountrySerializer


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

API_KEY = env('API_KEY')

CURRENT_WEATHER_API = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}' \
                      '&exclude=minutely,hourly,daily,alerts&appid={}&units=metric'
FIVE_DAY_WEATHER_FORCAST_API = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}' \
                               '&exclude=current,minutely,hourly,alerts&appid={}&units=metric'
GET_COORDS_BY_NAME_API = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}'


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


@api_view(['GET'])
def get_capitals_by_continent(request):
    if 'continent' in request.query_params:
        continent = request.query_params['continent']
    else:
        continent = 'South America'
    capitals = City.objects.filter(country__continent=continent)
    for capital in capitals:
        lat, lon = get_coords_by_name(capital.name)

        get_forcast = CURRENT_WEATHER_API.format(lat, lon, API_KEY)
        forcast_details = requests.get(get_forcast).json()

        capital.temperature = forcast_details['current']['temp']
        capital.temperature_timestamp = unix_to_datetime_tz(forcast_details['current']['dt'])
        capital.save()

    cap_by_range = City.objects.filter(country__continent=continent).annotate(
        temp_group=Case(
            When(temperature__range=[-20.0, -0.01], then=Value('-20 - 0 °C')),
            When(temperature__range=[0.00, 25.99], then=Value('0 - 25 °C')),
            When(temperature__range=[26.0, 40.99], then=Value('26 - 40 °C')),
            When(temperature__range=[41.0, 55.99], then=Value('41 - 55 °C')),
            default=Value('Extreme Temperature group'),
            output_field=CharField(),
        )
    ).values('name', 'temperature', 'country__name', 'temp_group').order_by('temp_group')

    result = {
        k: [dict(name=v['name'], temperature=v['temperature'], country=v['country__name']) for v in vs]
        for k, vs in groupby(cap_by_range, itemgetter('temp_group'))
    }
    return Response(result)


@api_view(['GET'])
def get_location_weather_details(_, city):
    lat, lon = get_coords_by_name(city)
    get_forcast = FIVE_DAY_WEATHER_FORCAST_API.format(lat, lon, API_KEY)

    forcast_details = requests.get(get_forcast).json()

    data = {
        'lat': lat,
        'lon': lon,
    }
    daily = []
    for forecast in forcast_details['daily'][1:6]:
        dt = unix_to_date(forecast['dt'])
        temperature = forecast['temp']['day']
        condition = "{} ({})".format(
            forecast['weather'][0]['main'],
            forecast['weather'][0]['description']
        )
        daily.append({
            dt: {
                'temperature': temperature,
                'condition': condition,
            }
        })
    data['daily'] = daily

    return Response(data)


def unix_to_date(ts):
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')


def unix_to_datetime_tz(ts):
    return datetime.utcfromtimestamp(ts).replace(tzinfo=tz.tzutc())


def get_coords_by_name(location):
    get_cords = GET_COORDS_BY_NAME_API.format(location, API_KEY)
    city_details = requests.get(get_cords).json()
    lat = city_details[0]['lat']
    lon = city_details[0]['lon']

    return lat, lon
