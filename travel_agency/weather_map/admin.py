from django.contrib import admin

from .models import City, Country


class CityAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'temperature',
        'temperature_timestamp',
        'get_country_name'
    ]

    def get_country_name(self, obj):
        return obj.country.name


class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'continent'
    ]


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
