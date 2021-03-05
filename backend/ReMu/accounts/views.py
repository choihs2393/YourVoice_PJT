from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import User, WavFile
from .serializers import UserSerializer, SignUpSerializer, changeSangSongSerializer, WavFileSerializer, changePitchSerializer, changeReSongSerializer, TESTUSERSerializer, changePiReSongSerializer
from music.models import Tracks
from music.serializers import TracksWAlbumSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from drf_yasg import openapi
import MM
from rest_framework.authtoken.models import Token
import datetime
import rest_framework_jwt
from django.http import HttpRequest
from rest_framework_jwt.views import ObtainJSONWebToken, obtain_jwt_token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import PitchTracking
import random
# Create your views here.

#@api_view(['POST'])
#@permission_classes((IsAuthenticated, )) #권한 체크
#@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
#def login(request):


@swagger_auto_schema(method='post', request_body=SignUpSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except User.DoesNotExist:
                if temp is None:
                    se = SignUpSerializer(data = request.data)
                    if se.is_valid():
                        se.save()
                        return JsonResponse(se.data, status=status.HTTP_201_CREATED)
                    else :
                        return JsonResponse({'message': 'input error'}, status=status.HTTP_400_BAD_REQUEST) 
            return JsonResponse({'message': 'already exist id'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/signup")
    return JsonResponse({'message': 'signup error'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
@permission_classes([AllowAny])
def id_check(request, Userid):
    if request.method == 'GET':
        try:
            temp = None
            try:
                if len(Userid) > 12:
                    return JsonResponse({'message': False}, status=status.HTTP_406_NOT_ACCEPTABLE)
                temp = User.objects.get(userid=Userid)
            except User.DoesNotExist:
                return JsonResponse({'message': True}, status=status.HTTP_201_CREATED)
            return JsonResponse({'message': False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/id_check")
    return JsonResponse({'message': 'id_check error'}, status=status.HTTP_404_NOT_FOUND)

    
param_login = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
)
@swagger_auto_schema(method='POST', request_body=param_login)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/login")
            if temp is not None:
                if temp.check_password(request.data['password']):
                    return JsonResponse({'message': 'success'}, status=status.HTTP_200_OK) 
                else :
                    return JsonResponse({'message': 'pwd error'}, status=status.HTTP_401_UNAUTHORIZED) 
        except Exception as e:
            MM.send(e, "account/login")
    return JsonResponse({'message': 'login error'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def get_pitch(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/get_pitch")
            if temp is not None:
                wase = WavFileSerializer(data={'file':request.data['file']})
                if wase.is_valid():
                    wase.save()
                pitch = PitchTracking.get_pitch(request.data['file'])
                temp.pitch = pitch
                se = changePitchSerializer(temp, data = {'userid':request.data['userid'], 'pitch' : temp.pitch})
                if se.is_valid():
                    se.update(temp, se.validated_data)
                    return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'get_pitch'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/get_pitch")
            return JsonResponse({'message': 'get_pitch error'}, status=status.HTTP_400_BAD_REQUEST) 
    return JsonResponse({'message': 'get_pitch error'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def get_pitch_file(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/get_pitch_file")
            if temp is not None:
                wase = WavFileSerializer(data={'file':request.data['file']})
                if wase.is_valid():
                    wase.save()
                pitch = PitchTracking.get_pitch_file(request.data['file'])
                temp.pitch = pitch
                se = changePitchSerializer(temp, data = {'userid':request.data['userid'], 'pitch' : temp.pitch})
                if se.is_valid():
                    se.update(temp, se.validated_data)
                    return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'get_pitch_file'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/get_pitch_file")
            return JsonResponse({'message': 'get_pitch_file error'}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'get_pitch_file error'}, status=status.HTTP_404_NOT_FOUND) 

param_add_songs = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'sang_songs': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'songid': openapi.Schema(type=openapi.TYPE_STRING, description='string')
                }
            ),description='array'),
    }   
)
@swagger_auto_schema(method='POST', request_body=param_add_songs)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def add_sang_song(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/add_sang_song")
            if temp is not None:
                for req in request.data['sang_songs']:
                    check = True
                    for song in temp.sang_songs:
                        if req['songid'] == song['songid']:
                            check = False
                            break
                    if check:
                        temp.sang_songs.append(req)
                se = changeSangSongSerializer(temp, data = request.data)
                if se.is_valid():
                    se.update(temp, se.validated_data)
                    return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'add_sang_song'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/add_sang_song")
    return JsonResponse({'message': 'add_sang_song error'}, status=status.HTTP_404_NOT_FOUND) 

param_delete_songs = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'songid': openapi.Schema(type=openapi.TYPE_STRING, description='string')
    }   
)
@swagger_auto_schema(method='POST', request_body=param_delete_songs)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def delete_sang_song(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/delete_sang_song")
            if temp is not None:
                idx = 0
                for song in temp.sang_songs:
                    if request.data['songid'] == song['songid']:
                        temp.sang_songs.pop(idx)
                        break
                    idx += 1
                se = changeSangSongSerializer(temp, data = request.data)
                if se.is_valid():
                    se.update(temp, se.validated_data)
                    return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'delete_sang_song'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/delete_sang_song")
    return JsonResponse({'message': 'delete_sang_song error'}, status=status.HTTP_404_NOT_FOUND) 

param_add_re_songs = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        're_songs': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'songid': openapi.Schema(type=openapi.TYPE_STRING, description='string')
                }
            ),description='array'),
    }   
)
@swagger_auto_schema(method='POST', request_body=param_add_re_songs)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def add_re_song(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/add_re_song")
            if temp is not None:
                for req in request.data['re_songs']:
                    check = True
                    for song in temp.re_songs:
                        if req['songid'] == song['songid']:
                            check = False
                            break
                    if check:
                        temp.re_songs.append(req)
                #temp.re_songs.extend(request.data['re_songs'])
                se = changeReSongSerializer(temp, data = request.data)
                if se.is_valid():
                    se.update(temp, se.validated_data)
                    return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'add_re_song'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/add_re_song")
    return JsonResponse({'message': 'add_re_song error'}, status=status.HTTP_404_NOT_FOUND) 

param_add_pi_re_songs = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'pi_re_songs': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'songid': openapi.Schema(type=openapi.TYPE_STRING, description='string')
                }
            ),description='array'),
    }   
)
@swagger_auto_schema(method='POST', request_body=param_add_pi_re_songs)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def add_pi_re_song(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/add_pi_re_song")
            if temp is not None:
                for req in request.data['pi_re_songs']:
                    check = True
                    for song in temp.pi_re_songs:
                        if req['songid'] == song['songid']:
                            check = False
                            break
                    if check:
                        temp.pi_re_songs.append(req)
                #temp.re_songs.extend(request.data['pi_re_songs'])
                se = changePiReSongSerializer(temp, data = request.data)
                if se.is_valid():
                    se.update(temp, se.validated_data)
                    return JsonResponse({'data' : se.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'add_pi_re_song'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            MM.send(e, "account/add_pi_re_song")
    return JsonResponse({'message': 'add_pi_re_song error'}, status=status.HTTP_404_NOT_FOUND) 

param_userid = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string')
    }
)
@swagger_auto_schema(method='POST', request_body=param_userid)
@api_view(['POST'])
#@permission_classes([AllowAny])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def get_user_info(request):
    if request.method == 'POST':
        try:
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/get_user_info")
            if temp is not None:
                se = UserSerializer(temp)
                return JsonResponse({'data':se.data}, status=status.HTTP_200_OK)
        except Exception as e:
            MM.send(e, "account/get_user_info")
    return JsonResponse({'message': 'get_user_info error'}, status=status.HTTP_404_NOT_FOUND) 

param_get = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'userid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'page': openapi.Schema(type=openapi.TYPE_STRING, description='string')
    }
)
@swagger_auto_schema(method='POST', request_body=param_get)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def get_user_sang_songs(request):
    if request.method == 'POST':
        try: 
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/get_user_sang_songs")
            if temp is not None:
                sang_songs = []
                p = int(request.data['page'])
                for song in temp.sang_songs[p*15:(p*15)+15]:
                    sang_songs.append(TracksWAlbumSerializer(Tracks.objects.get(id=song['songid'])).data)
                
                return JsonResponse({'data':sang_songs}, status=status.HTTP_200_OK)
        except Exception as e:
            MM.send(e, "account/get_user_sang_songs")
    return JsonResponse({'message': 'get_user_sang_songs error'}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='POST', request_body=param_get)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def get_user_re_songs(request):
    if request.method == 'POST':
        try: 
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/get_user_re_songs")
            if temp is not None:
                re_songs = []
                p = int(request.data['page'])
                for song in temp.re_songs[p*15:(p*15)+15]:
                    re_songs.append(TracksWAlbumSerializer(Tracks.objects.get(id=song['songid'])).data)
                return JsonResponse({'data':re_songs}, status=status.HTTP_200_OK)
        except Exception as e:
            MM.send(e, "account/get_user_re_songs")
    return JsonResponse({'message': 'get_user_re_songs error'}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='POST', request_body=param_get)
@api_view(['POST'])
@permission_classes((IsAuthenticated, )) #권한 체크
@authentication_classes((JSONWebTokenAuthentication,)) #JWT 토큰 확인
def get_user_pi_re_songs(request):
    if request.method == 'POST':
        try: 
            temp = None
            try:
                temp = User.objects.get(userid=request.data['userid'])
            except Exception as e:
                MM.send(e, "account/get_user_pi_re_songs")
            if temp is not None:
                pi_re_songs = []
                p = int(request.data['page'])
                for song in temp.pi_re_songs[p*15:(p*15)+15]:
                    pi_re_songs.append(TracksWAlbumSerializer(Tracks.objects.get(id=song['songid'])).data)
                return JsonResponse({'data':pi_re_songs}, status=status.HTTP_200_OK)
        except Exception as e:
            MM.send(e, "account/get_user_pi_re_songs")
    return JsonResponse({'message': 'get_user_pi_re_songs error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def TEST(request):
    data = {
        'userid': 'test0',
        'password': 'test0',
        'pitch': 100,
        'username': 'test0',
        'sang_songs': [
            {'songid': '5FGFoP6rmKZEKn4i95eRvQ'},
            {'songid': '19mOtiPH4ew4qPTGd9x1h5'},
            {'songid': '0xyyox4gBiaolgevqbpYV8'},
            {'songid': '7wAwTEA3TCHBSQCNTKLBon'},
            {'songid': '7BHijuU3OSoh4WnLfmZfU5'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test1',
        'password': 'test1',
        'pitch': 300,
        'username': 'test1',
        'sang_songs': [
            {'songid': '5b9KLFkFGQ8Jhcww3tjIvn'},
            {'songid': '1iMRYqTAIbxyjsdA2Tb8mP'},
            {'songid': '0iTMmwIo0FPhsUCJscI7Id'},
            {'songid': '7wAwTEA3TCHBSQCNTKLBon'},
            {'songid': '7BHijuU3OSoh4WnLfmZfU5'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test2',
        'password': 'test2',
        'pitch': 500,
        'username': 'test2',
        'sang_songs': [
            {'songid': '4B7Cb8abuoC7XiibUygi5K'},
            {'songid': '3O4ZjOswNySp5wcmglQhMj'},
            {'songid': '7AXJTnvVhuHmFsgrJozLnY'},
            {'songid': '58dwxhsVbmYv6VlYtVqUKx'},
            {'songid': '6MZx6uSwK1rRmycNYwrQNv'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test4',
        'password': 'test4',
        'pitch': 700,
        'username': 'test4',
        'sang_songs': [
            {'songid': '0afoCntatBcJGjz525RxBT'},
            {'songid': '2woXriAP3J52r5KlutnKzr'},
            {'songid': '7AXJTnvVhuHmFsgrJozLnY'},
            {'songid': '58dwxhsVbmYv6VlYtVqUKx'},
            {'songid': '7LSf4qEJhW07Ww9RPvFKsP'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test3',
        'password': 'test3',
        'pitch': 900,
        'username': 'test3',
        'sang_songs': [
            {'songid': '0afoCntatBcJGjz525RxBT'},
            {'songid': '2woXriAP3J52r5KlutnKzr'},
            {'songid': '7AXJTnvVhuHmFsgrJozLnY'},
            {'songid': '58dwxhsVbmYv6VlYtVqUKx'},
            {'songid': '7LSf4qEJhW07Ww9RPvFKsP'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test5',
        'password': 'test5',
        'pitch': 1100,
        'username': 'test5',
        'sang_songs': [
            {'songid': '3NxuezMdSLgt4OwHzBoUhL'},
            {'songid': '1YqGY2dW0a9ocyxaB5PtrR'},
            {'songid': '7AXJTnvVhuHmFsgrJozLnY'},
            {'songid': '58dwxhsVbmYv6VlYtVqUKx'},
            {'songid': '7LSf4qEJhW07Ww9RPvFKsP'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test6',
        'password': 'test6',
        'pitch': 1300,
        'username': 'test6',
        'sang_songs': [
            {'songid': '6tlMVCqZlmxfnjZt3OiHjE'},
            {'songid': '4Dr2hJ3EnVh2Aaot6fRwDO'},
            {'songid': '3y7ByLZ05tluscOTRgEJ9Y'},
            {'songid': '4as4XEOR03oGm1STUKl6pa'},
            {'songid': '2k3h2bJUBpddeXis6KZqbP'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()
    data = {
        'userid': 'test7',
        'password': 'test7',
        'pitch': 1500,
        'username': 'test7',
        'sang_songs': [
            {'songid': '0mQABqVHbNxxduxsC8Lz5q'},
            {'songid': '3GgqFQLN2OfpW8qm7tTKuu'},
            {'songid': '3ka75ywRax72WtCMd5Ynqw'},
            {'songid': '0GsRx0gPft6RmijIwMsKmG'},
            {'songid': '3QZeZgeeGlty1sHAxdfQ1w'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test8',
        'password': 'test8',
        'pitch': 1700,
        'username': 'test8',
        'sang_songs': [
            {'songid': '1wKOJ2fTflDiABy1EbFflM'},
            {'songid': '4E0DacxZNENaEeNgHWHq0X'},
            {'songid': '3ka75ywRax72WtCMd5Ynqw'},
            {'songid': '0GsRx0gPft6RmijIwMsKmG'},
            {'songid': '6tlMVCqZlmxfnjZt3OiHjE'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test9',
        'password': 'test9',
        'pitch': 1900,
        'username': 'test9',
        'sang_songs': [
            {'songid': '0dxVa6j7uoN8p8ytcHu4d4'},
            {'songid': '66XASSUmpMrdXfQiui2mYY'},
            {'songid': '5vKvdw2XJgR5ptQ0KWvFZL'},
            {'songid': '0GsRx0gPft6RmijIwMsKmG'},
            {'songid': '6tlMVCqZlmxfnjZt3OiHjE'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test10',
        'password': 'test10',
        'pitch': 2100,
        'username': 'test10',
        'sang_songs': [
            {'songid': '0dxVa6j7uoN8p8ytcHu4d4'},
            {'songid': '66XASSUmpMrdXfQiui2mYY'},
            {'songid': '6kwVyhHn28YMdgQkh3fLLe'},
            {'songid': '4mUoYd1F53Sml4JDdSoKIV'},
            {'songid': '65w0pdINTiQjWBaE4Rws9Y'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test11',
        'password': 'test11',
        'pitch': 2300,
        'username': 'test11',
        'sang_songs': [
            {'songid': '1uGFZ1dzoG3pS2lGYDTciP'},
            {'songid': '66XASSUmpMrdXfQiui2mYY'},
            {'songid': '2naxQzbpmYkz0dcAGriWQe'},
            {'songid': '3EFxv2pgoyWgmfcGJQ0EHE'},
            {'songid': '58KXhPGshGR40eOjWHNeWz'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()

    data = {
        'userid': 'test12',
        'password': 'test12',
        'pitch': 2500,
        'username': 'test12',
        'sang_songs': [
            {'songid': '0asaYh0r4NfgzgYLGcZ5Nm'},
            {'songid': '3DzTsH7OAt1cM5bq7KNgQz'},
            {'songid': '2naxQzbpmYkz0dcAGriWQe'},
            {'songid': '0eAGGoX6ocB8rBff6Gn9nN'},
            {'songid': '0ATt6kG9P0FuwGWtNgrE14'},
        ],
    }
    se = TESTUSERSerializer(data = data)
    if se.is_valid():
        se.save()
    return JsonResponse({'data':'data'}, status=status.HTTP_200_OK)