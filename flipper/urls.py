from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='flipper'),
    url(r'^dashboard/$', views.dashboard, name='flipper_dash'),
    url(r'^dashboard/json$', views.dashboardjson, name='flipper_dash_json'),
    url(r'^dashboard/flipupdate$', views.dashboardupdate, name='flipper_dash_update'),
    url(r'^items/$', views.items, name='flipper_items'),
    url(r'^flips/$', views.flips, name='flipper_flips'),
    url(r'^items/json$', views.itemtable, name='flipper_items_json'),
    url(r'^flips/json$', views.fliptable, name='flipper_flips_json'),
    url(r'^items/(?P<item_id>[0-9]+)/$', views.iteminfo, name='flipper_iteminfo'),
    url(r'^items/(?P<item_id>[0-9]+)/newflip$', views.newflip, name='flipper_flips_new'),
    url(r'^items/(?P<item_id>[0-9]+)/newprice$', views.newprice, name='flipper_flips_new_price'),
    url(r'^items/(?P<item_id>[0-9]+)/prices/json$', views.itempricetable, name='flipper_iteminfo_prices_json'),
    url(r'^items/(?P<item_id>[0-9]+)/flips/json$', views.itemfliptable, name='flipper_iteminfo_flips_json'),
]
