"""urls for activities"""

from django.urls import path, include
from rest_framework import routers
from travel_agency.weather_map.views import CityViewSet, CountryViewSet, \
    get_location_weather_details, get_capitals_by_continent


router = routers.DefaultRouter()
router.register(r'cities', CityViewSet, basename='city')
router.register(r'countries', CountryViewSet, basename='country')


urlpatterns = [
    path("", include(router.urls)),
    path("forcast/<str:city>", get_location_weather_details, name='weather-overview'),
    path("capitals/", get_capitals_by_continent, name='capitals-overview'),
]
