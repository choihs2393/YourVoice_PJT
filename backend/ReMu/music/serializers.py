from rest_framework import serializers
from music.models import Artists, Albums, Tracks, Arts, Genre, Image, Trs, TracksWAlbum, AlbumsWTracks
from djongo import models
from rest_framework.fields import CharField, IntegerField

class ArtsSerializer(serializers.Serializer):
    id = CharField(max_length=200)
    name = CharField(max_length=200)

class GenreSerializer(serializers.Serializer):
    genre = CharField(max_length=200)
        
class ImageSerializer(serializers.Serializer):
    height = IntegerField(default=0)
    url = CharField(max_length=200)
    width = IntegerField(default=0)

class TrsSerializer(serializers.Serializer):
    id = CharField(max_length=200)

class ArtistsSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    class Meta:
        model = Artists
        fields = '__all__'

    def get_genres(self, obj):
        genres_serializer = GenreSerializer(obj.genres, many=True)
        return genres_serializer.data
    def get_images(self, obj):
        images_serializer = ImageSerializer(obj.images, many=True)
        return images_serializer.data

class AlbumsSerializer(serializers.ModelSerializer):
    artists = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    tracks = serializers.SerializerMethodField()
    class Meta:
        model = Albums
        fields = '__all__'

    def get_images(self, obj):
        images_serializer = ImageSerializer(obj.images, many=True)
        return images_serializer.data
    def get_artists(self, obj):
        artists_serializer = ArtsSerializer(obj.artists, many=True)
        return artists_serializer.data
    def get_tracks(self, obj):
        tracks_serializer = TrsSerializer(obj.tracks, many=True)
        return tracks_serializer.data

class TracksSerializer(serializers.ModelSerializer):
    artists = serializers.SerializerMethodField()
    class Meta:
        model = Tracks
        fields = '__all__'

    def get_artists(self, obj):
        artists_serializer = ArtsSerializer(obj.artists, many=True)
        return artists_serializer.data

class TracksWAlbumSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()
    artists = serializers.SerializerMethodField()
    class Meta:
        model = TracksWAlbum
        fields = '__all__'

    def get_album(self, obj):
        album = Albums.objects.get(id=obj.album_id)
        if album is not None:
            als = AlbumsSerializer(instance = Albums.objects.get(id=obj.album_id))
            return als.data
        else:
            return {}
    def get_artists(self, obj):
        artists_serializer = ArtsSerializer(obj.artists, many=True)
        return artists_serializer.data

class AlbumsWTracksSerializer(serializers.ModelSerializer):
    trackslist = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    artists = serializers.SerializerMethodField()
    class Meta:
        model = AlbumsWTracks
        fields = '__all__'

    def get_trackslist(self, obj):
        li = []
        for tid in obj.tracks:
            try:
                track = Tracks.objects.get(id=tid['id'])
                if track is not None:
                    li.append(track)
            except Tracks.DoesNotExist:
                continue
        trs = TracksSerializer(li, many=True)
        return trs.data
    def get_images(self, obj):
        images_serializer = ImageSerializer(obj.images, many=True)
        return images_serializer.data
    def get_artists(self, obj):
        artists_serializer = ArtsSerializer(obj.artists, many=True)
        return artists_serializer.data