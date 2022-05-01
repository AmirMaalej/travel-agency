from rest_framework import serializers
from .models import Country, City


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for Country model
    """

    class Meta:
        model = Country
        fields = (
            'name',
            'continent'
        )


class CitySerializer(serializers.ModelSerializer):
    """
    Serializer for City model
    """

    class Meta:
        model = City
        fields = '__all__'

    def create(self, validated_data):
        city_name = validated_data.get("name")
        country = validated_data.get("country")

        created_cities = City.objects.filter(
            name__iexact=city_name,
            country=country
        )

        if not created_cities:
            new_city = City.objects.create(**validated_data)
            return new_city
        else:
            raise serializers.ValidationError("City already exists")
