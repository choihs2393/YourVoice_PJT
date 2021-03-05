from django.contrib import admin
#from rest_framework.routers import DefaultRouter
from music import views
from django.conf.urls import url 

#router = DefaultRouter(trailing_slash=False)
#router.register(r"^Artist/(?P<Artist_id>\d+)/$", views.artist_one, basename="Artists")
#router.register(r"^Album/(?P<Album_id>\d+)/$", views.album_one, basename="Albums")
#router.register(r"^Track/(?P<Track_id>\d+)/$", views.track_one, basename="Tracks")

#urlpatterns = router.urls
urlpatterns = [ 
    url(r'^artists/follwers/(?P<Page>\d*)/$', views.artist_follwer),
    url(r'^artists/popularity/(?P<Page>\d*)/$', views.artist_popularity),
    url(r'^artists/albums/(?P<Page>\d*)/(?P<Artist_id>.*)/$', views.artists_album),
    url(r'^artists/search/(?P<Page>\d*)/(?P<Query>.*)/$', views.artist_search),
    url(r'^artist/(?P<Artist_id>.*)/$', views.artist_one),
    url(r'^album/(?P<Album_id>.*)/$', views.album_one),
    url(r'^track/(?P<Track_id>.*)/$', views.track_one),
    url(r'^tracks/popularity/(?P<Page>\d*)/$', views.track_popularity),
    url(r'^tracks/cluster/(?P<Page>\d*)/(?P<Cluster>.*)/$', views.track_cluster),
    url(r'^tracks/search/(?P<Page>\d*)/(?P<Query>.*)/$', views.track_search),
    url(r'^search/(?P<Page>\d*)/(?P<Query>.*)/$', views.search),
    url(r'^pitch/recommend/$', views.pitch_recommend),
    url(r'^recommend/$', views.recommend),
]