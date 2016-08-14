from flipper.models import item, pricelog
from django.core.management.base import BaseCommand
import json
from urllib.request import urlopen
import urllib.parse
import time as tm
from datetime import datetime, timezone, timedelta, time
from django.utils import timezone as tz
import grequests


class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):

        # define variables

        currentdate = datetime.now(timezone.utc)
        print(currentdate)
        urls = []

        for i in item.objects.all()[:50]:
            pricelogs = pricelog.objects.filter(item=i)
            if pricelogs.count() > 0:
                print("count higher")
                logdate = pricelogs.order_by("-date").first().date
            else:
                print("count lower")
                logdate = currentdate - timedelta(days=10)

            if currentdate - logdate > timedelta(days=1):
                urls.append(
                    "https://api.rsbuddy.com/grandExchange?a=graph&start=1460803185&g=1440&i=" + str(i.itemid))

        print(urls)
        print("fetching "+str(len(urls))+" urls!")
        fetchgraph(urls)


def fetchgraph(urls):
    rs = (grequests.get(u) for u in urls)
    data = grequests.map(rs)
    for d in data:
        json = d.json()

def graphsave():


def fetchnow(urls):
    print("fdhskj")

def exception_handler(request, exception):
    print("Request failed")
