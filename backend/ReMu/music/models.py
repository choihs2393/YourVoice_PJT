from djongo import models
from django.contrib.postgres.fields import JSONField
from django import forms

# Create your models here.
class Arts(models.Model):
    id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    class Meta:
        abstract = True    
        
class ArtsForm(forms.ModelForm):
    class Meta:
        model = Arts
        fields = (
            'id', 'name'
        )

class Genre(models.Model):
    genre = models.CharField(max_length=200)
    class Meta:
        abstract = True
    
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = (
            'genre', 
        )

class Image(models.Model):
    height = models.IntegerField(default=0)
    url = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    class Meta:
        abstract = True
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            'height', 'url', 'width'
        )

class Trs(models.Model):
    id = models.CharField(max_length=200)
    class Meta:
        abstract = True
        
class TrsForm(forms.ModelForm):
    class Meta:
        model = Trs
        fields = (
            'id', 
        )

class Artists(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    followers = models.CharField(max_length=20)
    genres = models.ArrayField(
        model_container=Genre
    )
    images = models.ArrayField(
        model_container=Image
    )
    name = models.CharField(max_length=200)
    popularity = models.IntegerField(default=0)

class Albums(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    album_type = models.CharField(max_length=200)
    artists = models.ArrayField(
        model_container=Arts
    )
    images = models.ArrayField(
        model_container=Image
    )
    name = models.CharField(max_length=200)
    release_date = models.CharField(max_length=11)
    release_date_precision = models.CharField(max_length=200)
    total_tracks = models.IntegerField(default=0)
    tracks = models.ArrayField(
        model_container=Trs
    )

class Tracks(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    artists = models.ArrayField(
        model_container=Arts,
        model_form_class=ArtsForm
    )
    youtube_urls = models.CharField(max_length=200)
    youtube_mr = models.CharField(max_length=200)
    duration_ms  = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    track_number  = models.IntegerField(default=0)
    preview_url = models.CharField(max_length=200)
    album_id = models.CharField(max_length=200)
    popularity = models.IntegerField(default=0)
    cluster = models.IntegerField(default=0)
    objects = models.DjongoManager()
    

class TrackAb(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    youtube_urls = models.CharField(max_length=200)
    youtube_mr = models.CharField(max_length=200)
    duration_ms  = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    track_number  = models.IntegerField(default=0)
    preview_url = models.CharField(max_length=200)
    album_id = models.CharField(max_length=200)
    popularity = models.IntegerField(default=0)
    cluster = models.IntegerField(default=0)
    class Meta:
        abstract = True
    def __str__(self):
        return self.name

class TracksWAlbum(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    artists = models.ArrayField(
        model_container=Arts,
        model_form_class=ArtsForm
    )
    youtube_urls = models.CharField(max_length=200)
    youtube_mr = models.CharField(max_length=200)
    duration_ms  = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    track_number  = models.IntegerField(default=0)
    preview_url = models.CharField(max_length=200)
    popularity = models.IntegerField(default=0)
    cluster = models.IntegerField(default=0)
    album = Albums
    class Meta:
        managed = False

class AlbumsWTracks(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    album_type = models.CharField(max_length=200)
    artists = models.ArrayField(
        model_container=Arts,
        model_form_class=ArtsForm
    )
    images = models.ArrayField(
        model_container=Image
    )
    name = models.CharField(max_length=200)
    release_date = models.CharField(max_length=11)
    release_date_precision = models.CharField(max_length=200)
    total_tracks = models.IntegerField(default=0)
    trackslist = models.ArrayField(
        model_container=Tracks
    )
    class Meta:
        managed = False