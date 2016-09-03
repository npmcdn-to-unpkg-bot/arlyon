from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

BASE_DIR = settings.BASE_DIR

# Basics


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Types(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Categories)
    image = models.FilePathField(
        path=BASE_DIR + "/website/static/icons/fashion/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types"


class Brands(models.Model):
    name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Brands"


class Room(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    brand = models.ForeignKey(Brands)

    class Meta:
        abstract = True

# Categories

# wardrobe


class Wardrobe(Item):
    type = models.ForeignKey(Types)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Wardrobe Items"

# library


class Library(Item):
    image = models.ImageField(upload_to='library/')
    genre = models.ForeignKey(Types)

    class Meta:
        abstract = True


class Book(Library):
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Books"


class Movie(Library):
    director = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Movies"


class Album(Library):
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Albums"


class Game(Library):
    platform = models.ForeignKey(Types, related_name="platform")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Games"

# technology


class Technology(Item):
    type = models.ForeignKey(Types)
    modelnumber = models.CharField(max_length=200)
    serialnumber = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technology Items"


class Furniture(Item):
    type = models.ForeignKey(Types)
    color = models.CharField(max_length=6)
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Furniture"
