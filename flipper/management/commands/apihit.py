from flipper.models import item, pricelog
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):

        url = "https://api.rsbuddy.com/grandExchange?a=guidePrice"

        for i in item.objects.all():
            url+=("&i="+str(i.itemid))

        print(url)
