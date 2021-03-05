from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response

from .models import Artists, Albums, Tracks
from accounts.models import User
from accounts.serializers import changePiReSongSerializer
from .serializers import ArtistsSerializer, AlbumsSerializer, TracksSerializer, TracksWAlbumSerializer, AlbumsWTracksSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import MM
import connectdb
from rest_framework.renderers import JSONRenderer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
changePiReSongSerializer

import pandas as pd

@api_view(['GET'])
@permission_classes([AllowAny])
def artist_follwer(request, Page):
    if(request.method == 'GET'):
        try:
            p = int(Page)
            ats = Artists.objects.all().order_by('-followers')[p*30:(p*30)+30]
            se = ArtistsSerializer(ats, many=True)
            return JsonResponse({'data' : se.data }, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/artist_follwer")
    return JsonResponse({'message': 'artist_follwer error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def artist_popularity(request, Page):
    if(request.method == 'GET'):
        try:
            p = int(Page)
            ats = Artists.objects.all().order_by('-popularity')[p*30:(p*30)+30]
            se = ArtistsSerializer(ats, many=True)
            return JsonResponse({'data' : se.data }, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/artist_popularity")
    return JsonResponse({'message': 'artist_popularity error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def artist_one(request, Artist_id):
    if(request.method == 'GET'):
        try:
            artist = Artists.objects.get(id=Artist_id)
            ser = ArtistsSerializer(artist)
            return JsonResponse({'data' : ser.data}, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/artist_one")
    return JsonResponse({'message': 'artist_one error'}, status=status.HTTP_404_NOT_FOUND) 
 

@api_view(['GET'])
@permission_classes([AllowAny])
def artists_album(request, Page, Artist_id):
    if(request.method == 'GET'):
        try:
            p = int(Page)
            ats = Albums.objects.filter(artists={'id':Artist_id}).order_by('-release_date')[p*30:(p*30)+30]
            se = AlbumsSerializer(ats, many=True)
            return JsonResponse({'data' : se.data }, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/artists_ablum")
    return JsonResponse({'message': 'artists_album error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def album_one(request, Album_id):
    if(request.method == 'GET'):
        try: 
            album = Albums.objects.get(id=Album_id)
            ser = AlbumsWTracksSerializer(album)
            return JsonResponse({'data' : ser.data }, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/album_one")
    return JsonResponse({'message': 'album_one error'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
@permission_classes([AllowAny])
def track_one(request, Track_id):
    if(request.method == 'GET'):
        try: 
            track = Tracks.objects.get(id=Track_id)
            ser = TracksWAlbumSerializer(track)
            return JsonResponse({'data' : ser.data}, status=status.HTTP_200_OK)
        except Exception as e:
            MM.send(e, "music/track_one") 
    return JsonResponse({'message': 'track_one error'}, status=status.HTTP_404_NOT_FOUND) 

    
@api_view(['GET'])
@permission_classes([AllowAny])
def track_popularity(request, Page):
    if(request.method == 'GET'):
        try: 
            p = int(Page)
            ats = Tracks.objects.all().order_by('-popularity')[p*15:(p*15)+15]
            se = TracksWAlbumSerializer(ats, many=True)
            return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/track_popularity")
    return JsonResponse({'message': 'track_popularity error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def track_cluster(request, Page, Cluster):
    if(request.method == 'GET'):
        try:
            p = int(Page)
            ats = Tracks.objects.filter(cluster=Cluster).order_by('-popularity')[p*15:(p*15)+15]
            se = TracksWAlbumSerializer(ats, many=True)
            return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/track_cluster")
    return JsonResponse({'message': 'track_cluster error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def track_search(request, Page, Query):
    if(request.method == 'GET'):
        try: 
            p = int(Page)
            ats = Tracks.objects.filter(name__istartswith = Query).order_by('name')[p*30:(p*30)+30]
            se = TracksWAlbumSerializer(ats, many=True)
            return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/track_search")
    return JsonResponse({'message': 'track_search error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def artist_search(request, Page, Query):
    if(request.method == 'GET'):
        try: 
            p = int(Page)
            ats = Artists.objects.filter(name__istartswith = Query).order_by('name')[p*30:(p*30)+30]
            se = ArtistsSerializer(ats, many=True)
            return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/artist_search")
    return JsonResponse({'message': 'artist_search error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, Page, Query):
    if(request.method == 'GET'):
        try: 
            p = int(Page)
            ats = Artists.objects.filter(name__istartswith = Query).order_by('name')[p*30:(p*30)+30]
            artistse = ArtistsSerializer(ats, many=True)

            ts = Tracks.objects.filter(name__istartswith = Query).order_by('name')[p*30:(p*30)+30]
            track_name_se = TracksWAlbumSerializer(ts, many=True)
            track_artist_se = connectdb.get_data_track({'artists': {'$elemMatch' : {'name': {'$regex': '^'+Query, '$options':'i'}}}}, p*30, (p*30)+30)

            alts = Albums.objects.filter(name__istartswith = Query).order_by('name')[p*30:(p*30)+30]
            album_name_se = AlbumsSerializer(alts, many=True)
            album_artist_se = connectdb.get_data_album({'artists': {'$elemMatch' : {'name': {'$regex': '^'+Query, '$options':'i'}}}}, p*30, (p*30)+30)
           
            data = {
                'artist': artistse.data, 
                'album' : {
                    'name' : album_name_se.data,
                    'artist' : album_artist_se
                }, 
                'track' : {
                    'name' : track_name_se.data,
                    'artist' : track_artist_se
                }
            }
            
            return JsonResponse({'data' : data}, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            MM.send(e, "music/search")
    return JsonResponse({'message': 'search error'}, status=status.HTTP_404_NOT_FOUND)

param_pitch = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string')
    }
)
@swagger_auto_schema(method='post', request_body=param_pitch)
@api_view(['POST'])
@permission_classes([AllowAny])
def pitch_recommend(request):
    if(request.method == 'POST'):
        try:
            user = None
            try:
                user = User.objects.get(userid=request.data['userid'])
                users = User.objects.filter(pitch__range=(user.pitch - 300, user.pitch))
                tlist = []
                tracks = {}
                for u in users:
                    if u.userid == request.data['userid']:
                        continue
                    for s in u.sang_songs:
                        try:
                            tracks[s['songid']] += 1
                        except:
                            tracks[s['songid']] = 1
                for t in tracks:
                    ps = True
                    for u in user.sang_songs:
                        if str(t) == u['songid']:
                            ps = False
                    if ps:
                        tlist.append(t)
                tlist = sorted(tlist, key=tracks.__getitem__, reverse=True)
                result = []
                count = 0
                for t in tlist:
                    track = Tracks.objects.get(id=t)
                    if track is not None:
                        ser = TracksWAlbumSerializer(track)
                        result.append(ser.data)
                        count += 1
                        if count >= 12:
                            break
                for req in result:
                    check = True
                    for song in user.pi_re_songs:
                        if req['id'] == song['songid']:
                            check = False
                            break
                    if check:
                        user.pi_re_songs.append({'songid' : req['id']})
                se = changePiReSongSerializer(user, data = request.data)
                if se.is_valid():
                    se.update(user, se.validated_data)
                return JsonResponse({'data': result}, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return JsonResponse({'message': 'pitch_recommend'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/pitch_recommend")
    return JsonResponse({'message': 'pitch_recommend'}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='post', request_body=param_pitch)
@api_view(['POST'])
@permission_classes([AllowAny])
def recommend(request):
    if(request.method == 'POST'):
        try:
            user = None
            try:
                user = User.objects.get(userid=request.data['userid'])
                results = connectdb.make_audio_feature(request.data['selectmusic'])
                data = []
                for result in results:
                    temp = []
                    for tid in result['data']:
                        track = Tracks.objects.get(id = tid)
                        if track is not None:
                            se = TracksWAlbumSerializer(track)
                            temp.append(se.data)
                    data.append({'cluster': result['cluster'], 'data':temp})
                return JsonResponse({'data': data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return JsonResponse({'message': 'recommend'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/recommend")
    return JsonResponse({'message': 'recommend'}, status=status.HTTP_404_NOT_FOUND)
