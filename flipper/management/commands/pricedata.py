from flipper.models import item, pricelog
from django.core.management.base import BaseCommand
import json
from urllib.request import urlopen
import urllib.parse
import time as tm
from datetime import datetime, timezone, timedelta, time
from django.utils import timezone as tz


class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):

        # define variables

        itemobject = {}
        itemlist = item.objects.order_by("itemid")
        noofitems = itemlist.count()
        bulk = []
        fail = []
        missing = []
        totallogs = pricelog.objects.all()
        currentdate = datetime.now(timezone.utc)
        loopstart = 220
        loopnow = 0
        loopend = 4000

# for each item

        for i in itemlist:

            if loopnow < loopstart:
                loopnow += 1
                continue

            if loopnow >= loopend:
                continue

            # get the price logs
            pricelogs = totallogs.filter(item=i)

            # if there is a date of the last entry, check for it. if not,
            # assign one.
            try:
                logdate = pricelogs.order_by("-date").first().date
            except:
                logdate = datetime(2014, 1, 1, 1, 1, 1)

            # if the data is over a day old or there is none, fetch new.
            # otherwise skip.
            print("[" + str(i.id) + "/" + str(noofitems) + ": " +
                  str(i.itemid) + "] Checking data for " + i.name)
            try:
                print(currentdate - logdate)
                if currentdate - logdate > timedelta(days=1):
                    print("Updating data.")
                else:
                    continue
            except:
                print("No data cached.")

            # now try and open the url, if it doesnt work, add it to the list
            # to manage at the end.

            url = "https://api.rsbuddy.com/grandExchange?a=graph&start=1460803185&g=1440&i=" + \
                str(i.itemid)
            try:
                response = urlopen(url)
                print("loaded url")
            except:
                print("failed url load")
                if i in missing:
                    continue
                else:
                    missing.append(i)


            response = response.read()
            itemdata = json.loads(response.decode('utf-8'))

            # for each entry in the data

            for entry in itemdata:

                # if the time of the entry is already in the database
                if pricelogs.filter(date=tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime(entry["ts"] / 1000))).count() > 0:
                    # skip the entry
                    print("Entry exists")
                    continue

                # if the entry is older than 5 years
                if datetime.now(timezone.utc).replace(tzinfo=None) - datetime.utcfromtimestamp(entry["ts"] / 1000) > timedelta(days=3000):
                    # skip the entry
                    print("Older than 1000 days")
                    continue

                # add the data to the data list. if the data is faulty, skip.
                try:
                    itemobject["date"] = tm.strftime(
                        "%Y-%m-%d %H:%M:%S", tm.localtime(entry["ts"] / 1000))
                    itemobject["pricelow"] = entry["buyingPrice"]
                    itemobject["pricehigh"] = entry["sellingPrice"]
                    itemobject["priceaverage"] = entry["overallPrice"]
                    itemobject["buyvolume"] = entry["buyingCompleted"]
                    itemobject["sellvolume"] = entry["sellingCompleted"]
                    itemobject["item"] = i
                    bulk.append(pricelog(date=itemobject["date"], pricelow=itemobject["pricelow"], pricehigh=itemobject["pricehigh"], priceaverage=itemobject[
                                "priceaverage"], buyvolume=itemobject["buyvolume"], sellvolume=itemobject["sellvolume"], item=i))
                except:
                    print("Data faulty.")
                    if i in missing:
                        continue
                    else:
                        missing.append(i)

            # add the entries to the database

            pricelog.objects.bulk_create(bulk)
            print("Updated " + str(len(bulk)) + " objects for item " + i.name)
            bulk = []

        print(missing)

        #do a manual check for all missing values

        for m in missing:
            url = "https://api.rsbuddy.com/grandExchange?a=guidePrice&i=" + \
                str(m.itemid)

            print("getting data for the "+str(m.name))

            try:
                response = urlopen(url)
                print("loading url")
            except:
                print("couldnt load url.")
                if m in fail:
                    continue
                else:
                    fail.append(m)

            response = response.read()

            itemdata = json.loads(response.decode('utf-8'))

            print(itemdata)

            itemobject["date"] = datetime.now()
            itemobject["pricelow"] = itemdata["buying"]
            itemobject["pricehigh"] = itemdata["selling"]
            itemobject["priceaverage"] = itemdata["overall"]
            itemobject["buyvolume"] = itemdata["buyingQuantity"]
            itemobject["sellvolume"] = itemdata["sellingQuantity"]
            itemobject["item"] = m.itemid

            if (itemdata["buying"] == 0) or (itemdata["selling"] == 0) or (itemdata["overall"] == 0):
                print("shit data")
            else:
                bulk.append(pricelog(date=itemobject["date"], pricelow=itemobject["pricelow"], pricehigh=itemobject["pricehigh"], priceaverage=itemobject["priceaverage"], buyvolume=itemobject["buyvolume"], sellvolume=itemobject["sellvolume"], item=m))
                print("saved data for "+m.name)

        print(bulk)
        pricelog.objects.bulk_create(bulk)
        print(fail)
        print("complete")
