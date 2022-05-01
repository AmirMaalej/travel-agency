from rest_framework import viewsets

from travel_agency.tour_package.models import DestinationType, Destination, TourPackage, TourDate
from travel_agency.tour_package.serializers import DestinationTypeSerializer, DestinationSerializer, \
    TourPackageSerializer, TourDateSerializer


class DestinationTypeViewSet(viewsets.ModelViewSet):
    queryset = DestinationType.objects.all()
    serializer_class = DestinationTypeSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class TourDateViewSet(viewsets.ModelViewSet):
    queryset = TourDate.objects.all()
    serializer_class = TourDateSerializer


class TourPackageViewSet(viewsets.ModelViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
