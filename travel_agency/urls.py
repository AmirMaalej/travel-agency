"""travel_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from travel_agency.tour_package.views import DestinationTypeViewSet, DestinationViewSet, TourPackageViewSet, \
    TourDateViewSet
from travel_agency.weather_map.views import CityViewSet, CountryViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet, basename='city')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'destination_types', DestinationTypeViewSet, basename='destination_type')
router.register(r'destinations', DestinationViewSet, basename='destination')
router.register(r'tour_dates', TourDateViewSet, basename='tour_date')
router.register(r'tour_packages', TourPackageViewSet, basename='tour_package')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather_map/', include('travel_agency.weather_map.urls')),
    path('tour_package/', include('travel_agency.tour_package.urls')),
    # path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
