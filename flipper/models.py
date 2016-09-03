from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import json
import urllib

# Create your models here.

BASE_DIR = settings.BASE_DIR
osbuddy = 'https://api.rsbuddy.com/grandExchange?a=guidePrice&i='


def osapi(item):
    osbuddy = 'https://api.rsbuddy.com/grandExchange?a=guidePrice&i=' + \
        str(item)
    jsonlist = urllib.request.urlopen(osbuddy)
    jsonlist = jsonlist.read().decode('utf-8')
    apiinfo = json.loads(jsonlist)
    return apiinfo


class item(models.Model):
    itemid = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    members = models.CharField(max_length=5)
    description = models.CharField(max_length=500)
    buylimit = models.IntegerField(default=0, blank=True, null=True)
    highalch = models.IntegerField(default=0, blank=True, null=True)

    def api(self):
        return osapi(self.itemid)

    def profit(self):
        profit = 0
        for i in flip.objects.filter(item=self.id):
            profit += i.totalprofit()

        return profit

    def __str__(self):
        return("[" + str(self.itemid) + "] " + self.name)

    class Meta:
        verbose_name_plural = "Items"


class pricelog(models.Model):
    date = models.DateTimeField()
    pricelow = models.IntegerField(default=0)
    pricehigh = models.IntegerField(default=0)
    priceaverage = models.IntegerField(default=0, blank=True, null=True)
    buyvolume = models.IntegerField(default=0, blank=True, null=True)
    sellvolume = models.IntegerField(default=0, blank=True, null=True)
    item = models.ForeignKey(item)
    user = models.ForeignKey(User, blank=True, null=True)

    def source(self):
        if self.priceaverage is None:
            return 0
        else:
            return 1

    def roi(self):
        try:
            return self.pricelow / self.pricehigh
        except:
            return 0

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name_plural = "Price Logs"


class flip(models.Model):
    item = models.ForeignKey(item)
    number = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    # buying
    requestdate = models.DateTimeField()
    buyprice = models.IntegerField(default=0)
    # in bank
    purchasedate = models.DateTimeField(null=True, blank=True)
    # selling
    listeddate = models.DateTimeField(null=True, blank=True)
    sellprice = models.IntegerField(default=0)
    # sold
    solddate = models.DateTimeField(null=True, blank=True)

    def profit(self):
        "Returns the profit amount per item."
        if self.flipstatus() < 3:
            return 0
        else:
            return int(self.sellprice - self.buyprice)

    def roi(self):
        return self.sellprice / self.buyprice

    def totalprofit(self):
        "Returns the profit amount overall."
        if self.flipstatus() != 4:
            return 0
        else:
            return int(self.number * (self.sellprice - self.buyprice))

    def flipstatus(self):
        "Returns the status of the flip (buy/bank/sell/sold)"
        if self.solddate is not None:
            return 4
        if self.listeddate is not None:
            return 3
        if self.purchasedate is not None:
            return 2
        if self.requestdate is not None:
            return 1

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name_plural = "Flips"
