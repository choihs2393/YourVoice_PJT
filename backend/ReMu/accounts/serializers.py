from rest_framework import serializers
from accounts.models import User, Songs, WavFile
from djongo import models
import datetime
from rest_framework.fields import CharField, IntegerField

class SongsSerializer(serializers.Serializer):
    songid = CharField(max_length=200)

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid', 'username', 'password')
    def create(self, validated_data):
        now = datetime.datetime.now()
        user = User(
            userid=validated_data['userid'],
            username=validated_data['username'],
            joindate=now.strftime("%Y-%m-%d"),
            sang_songs=[],
            re_songs=[],
            pi_re_songs=[],
            pitch = 0
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TESTUSERSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid', 'username', 'password', 'sang_songs', 'pitch')
    def create(self, validated_data):
        now = datetime.datetime.now()
        user = User(
            userid=validated_data['userid'],
            username=validated_data['username'],
            joindate=now.strftime("%Y-%m-%d"),
            sang_songs=validated_data['sang_songs'],
            re_songs=[],
            pi_re_songs=[],
            pitch = validated_data['pitch']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    sang_songs = serializers.SerializerMethodField()
    re_songs = serializers.SerializerMethodField()
    pi_re_songs = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.sang_songs = validated_data.get('sang_songs', instance.sang_songs)
        instance.re_songs = validated_data.get('re_songs', instance.re_songs)
        instance.save()
        return instance
    def get_sang_songs(self, obj):
        ss = SongsSerializer(obj.sang_songs, many=True)
        return ss.data
    def get_re_songs(self, obj):
        rs = SongsSerializer(obj.re_songs, many=True)
        return rs.data
    def get_pi_re_songs(self, obj):
        rs = SongsSerializer(obj.pi_re_songs, many=True)
        return rs.data

class changeSangSongSerializer(serializers.ModelSerializer):
    sang_songs = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('userid', 'sang_songs', )
    def update(self, instance, validated_data):
        instance.sang_songs = validated_data.get('sang_songs', instance.sang_songs)
        instance.save()
        return instance
    def get_sang_songs(self, obj):
        ss = SongsSerializer(obj.sang_songs, many=True)
        return ss.data

class changeReSongSerializer(serializers.ModelSerializer):
    re_songs = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('userid', 're_songs', )
    def update(self, instance, validated_data):
        instance.re_songs = validated_data.get('re_songs', instance.re_songs)
        instance.save()
        return instance
    def get_re_songs(self, obj):
        ss = SongsSerializer(obj.re_songs, many=True)
        return ss.data

class changePiReSongSerializer(serializers.ModelSerializer):
    pi_re_songs = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('userid', 'pi_re_songs', )
    def update(self, instance, validated_data):
        instance.pi_re_songs = validated_data.get('pi_re_songs', instance.pi_re_songs)
        instance.save()
        return instance
    def get_pi_re_songs(self, obj):
        ss = SongsSerializer(obj.pi_re_songs, many=True)
        return ss.data

class changePitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid', 'pitch', )
    def update(self, instance, validated_data):
        instance.pitch = validated_data.get('pitch', instance.pitch)
        instance.save()
        return instance

class WavFileSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = WavFile
        fields = ('file', )