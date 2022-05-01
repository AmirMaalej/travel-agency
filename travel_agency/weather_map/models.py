from django.db import models


class Country(models.Model):
    name = models.CharField(
        help_text="Country name",
        max_length=256
    )
    continent = models.CharField(
        help_text="Continent name",
        max_length=256
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        help_text="City name",
        max_length=256
    )
    country = models.ForeignKey(
        'weather_map.Country',
        on_delete=models.CASCADE,
        related_name='countries',
        help_text="Countries"
    )
    latitude = models.DecimalField(help_text="Latitude of city",
                                   max_digits=9, decimal_places=6,
                                   blank=True, null=True),
    longitude = models.DecimalField(help_text="Longitude of city",
                                    max_digits=9, decimal_places=6,
                                    blank=True, null=True),
    temperature = models.DecimalField(help_text="Latest temperature recorded",
                                      max_digits=4, decimal_places=2,
                                      blank=True, null=True)
    temperature_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
