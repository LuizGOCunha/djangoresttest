from random import randint
import uuid

from django.core.management.base import BaseCommand, CommandParser

from djangorest.models import DummyData

class Command(BaseCommand):
    help = "Populates the database with a given number of model objects, default number is 100"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, default=100)

    def handle(self, *args, **options):
        count = options['count']
        for i in range(count):
            dummydata = DummyData.objects.create(id=uuid.uuid4(), number=randint(0,10000))
            print("Created ", dummydata.id, dummydata.number)
