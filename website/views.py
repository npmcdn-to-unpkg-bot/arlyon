from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Wardrobe, Technology, Movie, Album, Game, Book
from itertools import chain

def landing(request):
    template = loader.get_template('catalog/landing.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('catalog/contact.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def rooms(request):
    if request.user.is_authenticated():
        template = loader.get_template('catalog/rooms.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/accounts/login')

def catalog(request):
    if request.user.is_authenticated():
        template = loader.get_template('catalog/catalog.html')
        wardrobe = Wardrobe.objects.filter(user=request.user)
        albums = Album.objects.filter(user=request.user)
        games = Game.objects.filter(user=request.user)
        books = Book.objects.filter(user=request.user)
        movies = Movie.objects.filter(user=request.user)
        library = list(chain(albums, games, books, movies))
        technology = Technology.objects.filter(user=request.user)
        context = {
            "wardrobe": wardrobe,
            "library": library,
            "movies": movies,
            "books": books,
            "games": games,
            "albums": albums,
            "technology": technology,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/accounts/login')
