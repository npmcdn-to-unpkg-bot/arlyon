from django.contrib import admin
from .models import item, pricelog, flip

# Register your models here.

admin.site.register(item)
admin.site.register(pricelog)
admin.site.register(flip)
