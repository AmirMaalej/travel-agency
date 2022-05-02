"""urls for activities"""

from django.urls import path, include

from rest_framework import routers

from travel_agency.tour_package.views import DestinationTypeViewSet, DestinationViewSet, TourPackageViewSet, \
    TourDateViewSet, get_tour_package_by_date_and_danger, book_tour_package

router = routers.DefaultRouter()
router.register(r'destination_types', DestinationTypeViewSet, basename='destination_type')
router.register(r'destinations', DestinationViewSet, basename='destination')
router.register(r'tour_dates', TourDateViewSet, basename='tour_date')
router.register(r'tour_packages', TourPackageViewSet, basename='tour_package')


urlpatterns = [
    path("", include(router.urls)),
    path("book_tour_package/<int:tour_package_id>&<int:travelers_number>", book_tour_package,
         name='book-tour-package'),
    path("tour_package_filter/<str:danger_score>&<str:start_date>&<str:end_date>", get_tour_package_by_date_and_danger,
         name='tour-package-filter'),
]
