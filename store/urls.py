from django.conf.urls import url

from . import views

# app-name = 'store'

urlpatterns = [
    #/store/
    url(r'^$', views.listing, name='listing'),
    #/store/album_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #/store/search/
    url(r'^search/$', views.search, name='search'),
]