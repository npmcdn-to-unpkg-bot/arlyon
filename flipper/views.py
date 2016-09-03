from .models import item, pricelog, flip
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from urllib.request import urlopen
import json
import math
import time as tm
from datetime import datetime, timezone, timedelta

# Create your views here.


def home(request):
    template = loader.get_template('flipper/home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def dashboard(request):
    # list current flips, bank value, total flipped

    allflips = flip.objects.filter(user_id=request.user.id)
    activeflips = allflips.filter(solddate=None)
    inactiveflips = allflips.exclude(solddate=None)
    averageprofit = 0

    # determine profit

    roi = 0
    profit = 0
    flipnumber = 0
    orders = []
    bank = []
    sales = []

    for f in inactiveflips:
        profit += f.profit() * f.number
        flipnumber += 1
        averageprofit = profit / flipnumber
        roi += (f.roi() - 1) / inactiveflips.count()

    for f in activeflips:
        if f.flipstatus() == 1:
            orders.append(f)
        elif f.flipstatus() == 2:
            bank.append(f)
        elif f.flipstatus() == 3:
            sales.append(f)

    # load the boring bits

    template = loader.get_template('dashboard.html')
    context = {
        'flipnumber': flipnumber,
        'averageprofit': averageprofit,
        'profit': profit,
        'orders': orders,
        'bank': bank,
        'sales': sales,
        'flips': activeflips,
        'averageroi': math.floor(roi * 1000) / 10,
    }
    return HttpResponse(template.render(context, request))


def dashboardjson(request):
    print("api call")
    allflips = flip.objects.filter(user_id=request.user.id)
    allflips_json = json.loads(serializers.serialize("json", allflips))

    for i in allflips_json:
        theitem = item.objects.filter(id=i["fields"]["item"]).first()
        theflip = allflips.filter(id=i['pk']).first()
        i["fields"]["item_id"] = theitem.itemid
        i["fields"]["item_name"] = theitem.name
        i["fields"]["flipstatus"] = theflip.flipstatus()

    return JsonResponse(allflips_json, safe=False)

def dashboardupdate(request):
    if request.is_ajax():
        if request.method == 'GET':
            flipid = request.GET.get("flip")
            sellprice = request.GET.get("sellprice")
            flipstatus = int(request.GET.get("flipstatus"))
            theflip = flip.objects.get(id=int(flipid))
            print(theflip, sellprice, flipstatus)
            if flipstatus == 1:
                print("status 1")
                theflip.purchasedate = datetime.now(timezone.utc)
            elif flipstatus == 2:
                print("status 2")
                theflip.sellprice = sellprice
                theflip.listeddate = datetime.now(timezone.utc)
            elif flipstatus == 3:
                print("status 3")
                theflip.solddate = datetime.now(timezone.utc)
            print('saving')
            theflip.save()
            return HttpResponse("updated flip")

def items(request):
    # show information for a specific item such as historical flow/high flips
    # and money earned
    items = item.objects.order_by("name").first()
    template = loader.get_template('items.html')
    # items.api()
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context, request))


def iteminfo(request, item_id):
    # show information for a specific item such as historical flow/high flips
    # and money earned

    currentdate = datetime.now(timezone.utc)

    # try and update the data with the latest

    try:
        logdate = pricelog.objects.filter(
            item__itemid=item_id).order_by("-date").first().date
        if currentdate - logdate > timedelta(hours=1):
            print("need to update")
            go = 1
        else:
            go = 0
    except:
        go = 0

    itemid = get_object_or_404(item, itemid=item_id)

    if go == 1:
        itemobject = {}

        url = "https://api.rsbuddy.com/grandExchange?a=guidePrice&i=" + \
            str(item_id)
        response = urlopen(url)
        response = response.read()
        itemdata = json.loads(response.decode('utf-8'))

        itemobject["date"] = datetime.now()
        itemobject["pricelow"] = itemdata["buying"]
        itemobject["pricehigh"] = itemdata["selling"]
        itemobject["priceaverage"] = itemdata["overall"]
        itemobject["buyvolume"] = itemdata["buyingQuantity"]
        itemobject["sellvolume"] = itemdata["sellingQuantity"]
        itemobject["item"] = itemid

        if (itemdata["buying"] == 0) or (itemdata["selling"] == 0) or (itemdata["overall"] == 0):
            print("shit data")
        else:
            q = pricelog(date=itemobject["date"], pricelow=itemobject["pricelow"], pricehigh=itemobject["pricehigh"], priceaverage=itemobject[
                         "priceaverage"], buyvolume=itemobject["buyvolume"], sellvolume=itemobject["sellvolume"], item=itemobject["item"])
            q.save()

    # build the graph data

    logs = pricelog.objects.filter(item=itemid).order_by("-date")[:30]
    flips = flip.objects.filter(item=itemid).filter(user_id=request.user.id).exclude(solddate=None)

    pricehigh = []
    pricelow = []
    priceaverage = []
    roi = []

    for s in logs:
        stime = tm.mktime(s.date.timetuple()) * 1000
        pricelow.append([stime, s.pricelow])
        pricehigh.append([stime, s.pricehigh])
        roi.append([stime, (s.roi() - 1) * 100])
        priceaverage.append([stime, s.priceaverage])

    template = loader.get_template('iteminfo.html')
    profit = itemid.profit()
    context = {
        'roi': roi,
        'priceaverage': priceaverage,
        'pricelow': pricelow,
        'pricehigh': pricehigh,
        'profit': profit,
        'flips': flips,
        'item': itemid,
    }
    return HttpResponse(template.render(context, request))


def flips(request):
    sold = flip.objects.exclude(solddate=None).filter(user_id=request.user.id).order_by("solddate")
    template = loader.get_template('flips.html')

    buydata = []
    selldata = []
    roi = []
    profit = []
    prevbuy = 0
    prevsell = 0

    for s in sold:
        stime = tm.mktime(s.solddate.timetuple()) * 1000
        cumulativebuy = s.buyprice * s.number + prevbuy
        cumulativesell = s.sellprice * s.number + prevsell
        buydata.append([stime, cumulativebuy])
        selldata.append([stime, cumulativesell])
        profit.append([stime, cumulativesell - cumulativebuy])
        roi.append([stime, s.roi() * 100 - 100])
        prevbuy = cumulativebuy
        prevsell = cumulativesell

    context = {
        'sold': sold,
        'roi': roi,
        'profit': profit,
        'buydata': buydata,
        'selldata': selldata,
    }
    return HttpResponse(template.render(context, request))


def newflip(request, item_id):
    buyvol = request.GET.get("buyvolume")
    buypri = request.GET.get("buyprice")
    if request.is_ajax():
        if request.method == 'GET':
            theitem = item.objects.filter(itemid=int(item_id))
            print(theitem.first(), buyvol, buypri)
            f = flip(item=theitem.first(), number=buyvol, user=request.user,
                     requestdate=datetime.now(timezone.utc), buyprice=buypri)
            f.save()
            return HttpResponse("%s bought %s %s at %sgp." % (request.user, theitem.first().name, buyvol, buypri))


def newprice(request, item_id):
    buypri = request.GET.get("buyingprice")
    sellpri = request.GET.get("sellingprice")
    if request.is_ajax():
        if request.method == 'GET':
            theitem = item.objects.filter(itemid=int(item_id))
            print(theitem.first(), sellpri, buypri)
            p = pricelog(item=theitem.first(), pricehigh=buypri, user=request.user,
                         date=datetime.now(timezone.utc), pricelow=sellpri)
            p.save()
            return HttpResponse("You can buy %s for %s and sell for %s" % (theitem.first().name, buypri, sellpri))


def itempricetable(request, item_id):
    print("api call")
    prices = pricelog.objects.filter(item__itemid=item_id)
    prices_json = json.loads(serializers.serialize("json", prices))

    for i in prices_json:
        try:
            i['fields']['roi'] = i['fields'][
                'pricelow'] / i['fields']['pricehigh']
        except:
            i['fields']['roi'] = 0
        prices_json[prices_json.index(i)] = i['fields']

    return JsonResponse(prices_json, safe=False)


def itemfliptable(request, item_id):
    print("api call")
    fliplist = flip.objects.exclude(solddate=None).filter(
        item__itemid=item_id).filter(user_id=request.user.id).order_by("solddate")
    flips_json = json.loads(serializers.serialize("json", fliplist))

    for f in flips_json:
        flips_json[flips_json.index(f)] = f['fields']

    for f in flips_json:
        f['profitea'] = f['sellprice'] - f['buyprice']
        f['profittot'] = f['profitea'] * f['number']
        f['roi'] = f['sellprice'] / f['buyprice'] * 100

    return JsonResponse(flips_json, safe=False)


def itemtable(request):
    print("api call")
    fliplist = flip.objects.exclude(solddate=None).filter(user_id=request.user.id).order_by("solddate")
    flips_json = json.loads(serializers.serialize("json", fliplist))

    for i in flips_json:
        flips_json[flips_json.index(i)] = i['fields']

    return JsonResponse(flips_json, safe=False)


def fliptable(request):
    print("api call")
    items = item.objects.all()
    fliplist = flip.objects.exclude(solddate=None).filter(user_id=request.user.id).order_by("solddate")
    flips_json = json.loads(serializers.serialize("json", fliplist))

    for f in flips_json:
        flips_json[flips_json.index(f)] = f['fields']

    for f in flips_json:
        theitem = items.filter(id=f['item']).first()
        f['profitea'] = f['sellprice'] - f['buyprice']
        f['profittot'] = f['profitea'] * f['number']
        f['roi'] = f['sellprice'] / f['buyprice'] * 100
        f['name'] = theitem.name
        f['item'] = theitem.itemid

    return JsonResponse(flips_json, safe=False)
