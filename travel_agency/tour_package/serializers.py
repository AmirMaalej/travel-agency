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
        fields = '__all__'


class TourPackageSerializer(serializers.ModelSerializer):
    """
    Serializer for TourPackage model
    """

    class Meta:
        model = TourPackage
        fields = '__all__'
