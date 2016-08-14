from flipper.models import item
from django.core.management.base import BaseCommand, CommandError
import json
from urllib.request import urlopen
import urllib.parse
from time import sleep

class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):

        itemobject = {}

        with open('D:/Documents/Programming/rscg/scripts/shop.json') as data_file:
            shop = json.load(data_file)
        with open('D:/Documents/Programming/rscg/scripts/price.json') as data_file:
            price = json.load(data_file)

        for obj in shop:
            print("["+obj+"] "+shop[obj]["name"])
            existingentries = item.objects.filter(itemid=obj)
            if existingentries.count() == 0:
                print("I need this")
                url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="+str(obj)
                try:
                    response = urlopen(url)
                    response=response.read()
                    if response == b'':
                        print("waiting")
                        sleep(60)
                        response = urlopen(url).read()
                    itemdata = json.loads(response.decode('utf-8'))
                    itemobject["id"] = obj
                    itemobject["name"] = shop[obj]["name"]
                    itemobject["members"] = price[obj]["members"]
                    itemobject["icon"] = itemdata["item"]["icon_large"]
                    itemobject["description"] = itemdata["item"]["description"]

                    q = item(itemid=itemobject["id"], name=itemobject["name"], members=itemobject["members"], icon=itemobject["icon"], description=itemobject["description"])
                    q.save()

                    shop[obj]["complete"] = True
                    with open('shop.json', 'w') as outfile:
                        json.dump(shop, outfile)
                except:
                    shop[obj]["complete"] = True
                    with open('shop.json', 'w') as outfile:
                        json.dump(shop, outfile)
                    print("error")
            else:
                print("Updating Membership")
                entry = existingentries.first()
                entry.members = price[obj]["members"]
                entry.save()

        print("complete!")
