from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='stuff'),
    url(r'^catalog/', views.catalog, name='stuff_catalog'),
    url(r'^rooms/', views.rooms, name='stuff_rooms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
