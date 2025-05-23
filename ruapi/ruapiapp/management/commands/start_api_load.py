from ruapiapp.models import Person
from django.core.management.base import BaseCommand
from ruapiapp.utils import load_persons


class Command(BaseCommand):
    help = 'clear db and load new 1000 users'

    def handle(self, *args, **kwargs):
        Person.objects.all().delete()
        load_persons(1000)
