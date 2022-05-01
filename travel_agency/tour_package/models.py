from django.db import models
from django.utils.translation import gettext_lazy as _

from travel_agency.weather_map.models import City


class DestinationType(models.Model):
    choice = models.CharField(max_length=64)

    def __str__(self):
        return self.choice


class Destination(models.Model):

    class DangerLevel(models.TextChoices):
        NO_DANGER = 'ND', _('No Danger')
        MEDIUM_DANGER_SCORE = 'MD', _('Medium Danger Score')
        HIGH_DANGER_SCORE = 'HD', _('High Danger Score')
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE,
                             related_name='cities',
                             help_text="Cities")
    type = models.ForeignKey(DestinationType, on_delete=models.CASCADE)
    danger_level = models.CharField(
        max_length=2,
        choices=DangerLevel.choices,
        default=DangerLevel.NO_DANGER
    )

    def __str__(self):
        return f'destination {self.city.name}'


class TourPackage(models.Model):
    name = models.CharField(
        help_text="Package name",
        max_length=256
    )
    price = models.FloatField(
        help_text="Package price",
    )
    description = models.TextField(
        help_text="Package price",
        max_length=2048
    )
    capacity = models.PositiveSmallIntegerField(
        help_text="Maximum Capacity of travelers",
        blank=True, null=True
    )
    destination = models.ManyToManyField(Destination)

    def __str__(self):
        return self.name

    def get_destinations(self):
        return "\n".join([d.destinations for d in self.destination.all()])


class TourDate(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.date.strftime("%m/%d/%Y, %H:%M:%S")
