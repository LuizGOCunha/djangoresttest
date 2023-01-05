from django.core.management.base import BaseCommand, CommandParser

from djangorest.models import DummyData

class Command(BaseCommand):
    help = "Deletes all object currently in the database, returning their"

    def handle(self, *args, **options):
        all_data = DummyData.objects.all()
        for data in all_data:
            print("deleting object ", data.id, data.number)
            data.delete()
            