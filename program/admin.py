from django.contrib import admin
from .models import agency, kerbals, programs, missionstatuses, shiptypes, mods, ships, missions, colors, grandStatus, missionNodes, deltavMap
from django.conf import settings

class agencyFields(admin.ModelAdmin):
    fields = ['agency_name','agency_flag','agency_bio','agency_color']
    def save_model(self, request, obj, form, change):
        a = obj.agency_flag
        a = a[a.index('flags'):]
        obj.agency_flag = a
        obj.save()

class programFields(admin.ModelAdmin):
    fields = ['code','name','description','image']
    def save_model(self, request, obj, form, change):
        a = obj.image
        a = a[a.index('programs'):]
        obj.image = a
        obj.save()

class shiptypeFields(admin.ModelAdmin):
    fields = ['name','desc','color','image']
    def save_model(self, request, obj, form, change):
        a = obj.image
        a = a[a.index('shiptypes'):]
        obj.image = a
        obj.save()

admin.site.register(agency, agencyFields),
admin.site.register(kerbals),
admin.site.register(missionNodes),
admin.site.register(deltavMap),
admin.site.register(grandStatus),
admin.site.register(programs, programFields),
admin.site.register(missionstatuses),
admin.site.register(shiptypes, shiptypeFields),
admin.site.register(mods),
admin.site.register(ships),
admin.site.register(missions),
admin.site.register(colors),
