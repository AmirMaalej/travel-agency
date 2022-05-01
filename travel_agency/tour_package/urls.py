"""urls for activities"""

from django.urls import path, include

from rest_framework import routers

from travel_agency.tour_package.views import DestinationTypeViewSet, DestinationViewSet, TourPackageViewSet, \
    TourDateViewSet

router = routers.DefaultRouter()
router.register(r'destination_types', DestinationTypeViewSet, basename='destination_type')
router.register(r'destinations', DestinationViewSet, basename='destination')
router.register(r'tour_dates', TourDateViewSet, basename='tour_date')
router.register(r'tour_packages', TourPackageViewSet, basename='tour_package')


urlpatterns = [
    path("", include(router.urls)),
]
