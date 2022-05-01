from travel_agency.tour_package.models import DestinationType

from django.core.management.base import BaseCommand

init_types = ['cultural', 'jungle excursion', 'adventure']


class Command(BaseCommand):
    help = 'Creates initial destination types'

    def handle(self, *args, **options):
        for destination_type in init_types:
            new_type = DestinationType.objects.create(
                choice=destination_type
            )
            new_type.save()
