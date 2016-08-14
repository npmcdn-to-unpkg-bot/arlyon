from flipper.models import item
from django.core.management.base import BaseCommand, CommandError
import json
from urllib.request import urlopen
import urllib.parse
from time import sleep

class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):
        for row in item.objects.all():
            if item.objects.filter(itemid=row.itemid).count() > 1:
                print("Deleting itemid: "+str(row.itemid))
                row.delete()
