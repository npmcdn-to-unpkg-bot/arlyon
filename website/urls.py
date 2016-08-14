from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='stuff'),
    url(r'^profile/', views.profile, name='account_profile'),
    url(r'^catalog/', views.catalog, name='stuff_catalog'),
    url(r'^rooms/', views.rooms, name='stuff_rooms'),
    url(r'^contact/', views.contact, name='stuff_contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
