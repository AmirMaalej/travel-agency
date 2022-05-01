from django.contrib import admin
from .models import DestinationType, Destination, TourPackage, TourDate


class DestinationTypeAdmin(admin.ModelAdmin):
    list_display = [
        'choice',
    ]


class DestinationAdmin(admin.ModelAdmin):
    list_display = [
        'get_city_name',
        'type',
        'danger_level'
    ]

    def get_city_name(self, obj):
        return obj.city.name


class TourDateAdmin(admin.ModelAdmin):
    list_display = [
        'tour_package',
        'date'
    ]


class TourPackageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'description',
        'get_destinations'
    ]


admin.site.register(DestinationType, DestinationTypeAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(TourDate, TourDateAdmin)
admin.site.register(TourPackage, TourPackageAdmin)
