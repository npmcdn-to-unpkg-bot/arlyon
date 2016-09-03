from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='kml'),
    url(r'^setup/$', views.setup, name='kml_setup'),
    url(r'^setup/continue$', views.setupcomplete, name='kml_setup_complete'),
    url(r'^import/mods$', views.importmods, name='kml_import_mods'),
    url(r'^agency/$', views.agencypage, name='kml_agency'),
    url(r'^missions/$', views.missionlist, name='kml_mission'),
    url(r'^missions/new/$', views.missionnew, name='kml_mission_new'),
    url(r'^missions/(?P<mission_id>[0-9]+)/$', views.missioninfo, name='kml_mission_info'),
    url(r'^kerbals/$', views.kerballist, name='kml_kerbal'),
    url(r'^programs/$', views.programlist, name='kml_program'),
    url(r'^contracts/$', views.index, name='kml_contract'),
    url(r'^ships/$', views.shiplist, name='kml_ship'),
    url(r'^ships/(?P<ship_id>[0-9]+)/$', views.shipinfo, name='kml_ship_info'),
    url(r'^mods/$', views.modlist, name='kml_mod'),
    url(r'^mods/(?P<mod_id>[0-9]+)/$', views.modinfo, name='kml_mod_info'),
    url(r'^settings/$', views.settingspage, name='kml_settings'),
    url(r'^new/$', views.new, name='kml_new'),
]
