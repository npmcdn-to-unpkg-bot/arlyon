from flipper.models import item, pricelog
from django.core.management.base import BaseCommand
import json
from urllib.request import urlopen
import urllib.parse
import time


class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):

        itemlist = item.objects.all()
        missing = []

        for i in itemlist:
            if pricelog.objects.filter(item=i).count() < 30:
                missing.append(i)

        print(missing)

        for t in missing:
            for u in pricelog.objects.filter(item=t):
                if pricelog.objects.filter(item=t).filter(date=u.date).count() > 1:
                    print("Deleting entry: "+str(u.date))
                    u.delete()
