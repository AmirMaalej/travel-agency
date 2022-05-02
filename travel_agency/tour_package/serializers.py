from rest_framework import serializers
from .models import DestinationType, Destination, TourDate, TourPackage


class DestinationTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for DestinationType model
    """

    class Meta:
        model = DestinationType
        fields = (
            'choice',
        )


class DestinationSerializer(serializers.ModelSerializer):
    """
    Serializer for Destination model
    """

    class Meta:
        model = Destination
        fields = '__all__'


class TourDateSerializer(serializers.ModelSerializer):
    """
    Serializer for TourDate model
    """

    class Meta:
        model = TourDate
        fields = ['date']


class TourPackageSerializer(serializers.ModelSerializer):
    """
    Serializer for TourPackage model
    """
    tour_dates = serializers.SerializerMethodField()

    class Meta:
        model = TourPackage
        fields = ['name', 'price', 'description', 'capacity', 'available_places', 'destination', 'tour_dates']

    def get_tour_dates(self, instance):
        serializer = TourDateSerializer(instance.tourdate_set.all(), many=True)
        return serializer.data
