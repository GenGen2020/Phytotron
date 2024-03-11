# booking/management/commands/init_facilities.py
from django.core.management.base import BaseCommand
from booking.models import Facility

class Command(BaseCommand):
    help = 'Initializes greenhouse zones and growth chambers'

    def handle(self, *args, **kwargs):
        for i in range(6):
            Facility.objects.create(facility_type='greenhouse', status='available')
        for i in range(29):
            Facility.objects.create(facility_type='chamber', status='available')
        self.stdout.write(self.style.SUCCESS('Successfully initialized facilities'))
