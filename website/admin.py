from django.contrib import admin
from .models import Categories, Types, Brands, Wardrobe, Movie, Album, Game, Book, Technology, Room, Furniture

# Register your models here.

myModels = [Categories, Types, Brands, Wardrobe, Movie, Album, Game, Book, Technology, Room, Furniture]

admin.site.register(myModels)
