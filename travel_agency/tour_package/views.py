from datetime import datetime
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from travel_agency.tour_package.models import DestinationType, Destination, TourPackage, TourDate
from travel_agency.tour_package.serializers import DestinationTypeSerializer, DestinationSerializer, \
    TourPackageSerializer, TourDateSerializer


class DestinationTypeViewSet(viewsets.ModelViewSet):
    queryset = DestinationType.objects.all()
    serializer_class = DestinationTypeSerializer
    permission_classes = [IsAuthenticated]


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]


class TourDateViewSet(viewsets.ModelViewSet):
    queryset = TourDate.objects.all()
    serializer_class = TourDateSerializer
    permission_classes = [IsAuthenticated]


class TourPackageViewSet(viewsets.ModelViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def book_tour_package(_, tour_package_id, travelers_number):
    # minimum implementation just for testing
    try:
        tour_package = TourPackage.objects.get(id=tour_package_id)

        if tour_package.available_places - travelers_number >= 0:
            tour_package.available_places -= travelers_number
            tour_package.save()

            serializer = TourPackageSerializer(tour_package)
            return Response(serializer.data)
        return Response(f'There are only {tour_package.available_places} places left')

    except TourPackage.DoesNotExist:
        return Response('Tour package not found')


@api_view(['GET'])
def get_tour_package_by_date_and_danger(_, danger_score, start_date, end_date):
    if danger_score not in [d.value for d in Destination.DangerLevel]:
        return Response('Error: Danger score is invalid')
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return Response('Error: Dates are invalid')
    if start_date > end_date:
        return Response('Error: Start date cannot be later than End date')
    if start_date <= datetime.today():
        return Response('Error: Start date should be in the future')

    tour_packages = TourPackage.objects.filter(destination__danger_level=danger_score,
                                               tourdate__date__range=[start_date, end_date],
                                               available_places__gt=0).distinct()

    serializer = TourPackageSerializer(tour_packages, many=True)

    return Response(serializer.data)
