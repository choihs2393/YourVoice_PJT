from django.contrib import admin
#from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import url 

#router = DefaultRouter(trailing_slash=False)
#router.register(r"^Artist/(?P<Artist_id>\d+)/$", views.artist_one, basename="Artists")
#router.register(r"^Album/(?P<Album_id>\d+)/$", views.album_one, basename="Albums")
#router.register(r"^Track/(?P<Track_id>\d+)/$", views.track_one, basename="Tracks")

#urlpatterns = router.urls
urlpatterns = [ 
    url('login/', views.login),
    url('signup/', views.signup),
    url(r'^get_pitch/$', views.get_pitch),
    url(r'^id_check/(?P<Userid>.*)/$', views.id_check),
    url(r'^add_sang_song/$', views.add_sang_song),
    url(r'^add_re_song/$', views.add_re_song),
    url(r'^add_pi_re_song/$', views.add_pi_re_song),
    url(r'^user_info/$', views.get_user_info),
    url(r'^delete_sang_song/$', views.delete_sang_song),
    url(r'^get_pitch_file/$', views.get_pitch_file),
    url(r'^get_user_sang_songs/$', views.get_user_sang_songs),
    url(r'^get_user_re_songs/$', views.get_user_re_songs),
    url(r'^get_user_pi_re_songs/$', views.get_user_pi_re_songs),
    #url(r'^TEST/$', views.TEST),
]