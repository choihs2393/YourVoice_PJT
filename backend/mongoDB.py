# -*- encoding: utf-8 -*-
"""
pip install pymongo
"""
from pymongo import MongoClient   #mongodb 모듈 지정
import datetime
import pprint
import json
import os
import sys
from bson.objectid import ObjectId  #objectid 모듈 지정
import requests
import json

def send(text, title):
    requests.post('https://meeting.ssafy.com/hooks/xjyuws5ywtratrtu8e8qx57k7c', 
        data=json.dumps({"attachments": [{
            "color": "#FF8000",
            "text": str(text),
            "author_name": "data",
            "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
            "title": str(title),
        }]}),
        headers={'Content-Type': 'application/json'}
    )
sys.stdout.reconfigure(encoding='utf-8')
def open_json(name):
    with open('./%s.json'%name,'r', -1, "utf-8") as f:
        dt=json.load(f)
    return dt

def open_file(name):
    with open(name, 'r', -1, "utf-8") as f:
        dt=json.load(f)
    return dt

def save_json(name,dt):
    with open('./%s.json'%name,'w', -1, "utf-8") as f:
        json.dump(dt,f)

#mongodb 연결객체 생성
# client = MongoClient()
# client = MongoClient('localhost', '27017')  #접속IP, 포트
#client = MongoClient('mongodb://root:sSLe2f46tf3EeLo3Eo9tj94cmEcVvERf3D3bBgVfcs@j3b302.p.ssafy.io:8022/admin')
client = MongoClient('mongodb://localhost:27017')
#데이터베이스 개체 가져오기
# db = client['------']
db = client.spotify
#컬렉션 개체 가져오기

"""
#아티스트 추가
artistsCol = db.artists

kpopArtists = open_json("data/artists/k-pop_artists_info")
for artist in kpopArtists:
    check = False
    for t in artist['genres']:
        if "k-pop" in t or "korean" in t:
            check = True
            break
    if not check:
        continue
    artistsCol.insert_one(artist)

#현재 aws에 아티스트만 추가함
"""

"""
#앨범 추가
albumsCol = db.albums
kpopAlbums = open_json("data/albums/k-pop_albums")
for albums in kpopAlbums:
    for album in kpopAlbums[albums]:
        albumsCol.insert_one(album)
        #print(album['name'])
"""

"""
#앨범 데이터 정제 for django
albumsCol = db.albums
DalbumsCol = db.music_albums
als = albumsCol.find(no_cursor_timeout = True)
for album in als:
    temp = {}
    
    if DalbumsCol.count_documents({'id' : album['id']}) != 0:
        continue
    temp['id'] = album['id']
    temp['album_type'] = album['album_type']
    temp['name'] = album['name']
    temp['release_date'] = album['release_date']
    temp['release_date_precision'] = album['release_date_precision']
    temp['total_tracks'] = album['total_tracks']
    temp['images'] = album['images']
    ate = []
    for ar in album['artists']:
        te = {}
        te['id'] = ar['id']
        te['name'] = ar['name']
        ate.append(te)
    temp['artists'] = ate
    try:
        temp['tracks'] = album['tracks']
    except:
        temp['tracks'] = []
        print(album['id'])
        
    DalbumsCol.insert_one(temp)
als.close()
"""
#db.users.count_documents({"email": email}) != 0:

"""
#트랙 추가
tracksCol = db.tracks
albumsCol = db.albums
dir_l=os.listdir(u'./data/tracks/')
for artist in dir_l:
    albums = open_file('./data/tracks/' + artist)
    for album in albums['albums']:
        tracks = []
        for track in albums['albums'][album]:
            tracks.append({'id' : track['id']})
            if tracksCol.count_documents({'id' : track['id']}) > 0:
                continue
            temp = {}
            temp['id'] = track['id']
            temp['artists'] = track['artists']
            temp['duration_ms'] = track['duration_ms']
            temp['external_urls'] = track['external_urls']
            temp['name'] = track['name']
            temp['preview_url'] = track['preview_url']
            temp['track_number'] = track['track_number']
            temp['album_id'] = album
            tracksCol.insert_one(temp)
        albumsCol.update_many({'id': album}, {'$set': {'tracks': tracks}})
"""

"""
#tarcks 복제
nts = db.ntracks
ts = db.tracks
tts = ts.find(no_cursor_timeout = True)

for t in tts:
    nts.insert_one(t)
tts.close()
"""


"""
#아티스트 데이터 정제 for django
artistsCol = db.artists
DartistsCol = db.music_artists
ars = artistsCol.find(no_cursor_timeout = True)
for artist in ars:
    if DartistsCol.count_documents({'id' : artist['id']}) != 0:
        continue
    temp = {}
    temp['id'] = artist['id']
    temp['followers'] = artist['followers']['total']
    temp['name'] = artist['name']
    temp['popularity'] = artist['popularity']
    li = []
    for gen in artist['genres']:
        te={}
        te['genre'] = gen
        li.append(te)
    temp['genres'] = li
    temp['images'] = artist['images']
    DartistsCol.insert_one(temp)
ars.close()
"""


"""
#트랙 데이터 정제
tracksCol = db.tracks
DtracksCol = db.music_tracks
for i in range(0, 109):
    ts = tracksCol.find(no_cursor_timeout = True).skip(i*1000).limit(1000)
    for track in ts:
        if DtracksCol.count_documents({'id' : track['id']}) >= 1:
            continue
        temp = {}
        temp['id'] = track['id']
        ate = []
        for ar in track['artists']:
            te = {}
            te['id'] = ar['id']
            te['name'] = ar['name']
            ate.append(te)
        temp['artists'] = ate
        you = None
        mr = None
        for ex in track['external_urls']:
            try:
                you = ex['youtube']
            except:
                pass
            try:
                mr = ex['youtube_mr']
            except:
                pass
        temp['youtube_urls'] = you
        temp['youtube_mr'] = mr
        temp['name'] = track['name']
        temp['duration_ms'] = track['duration_ms']
        temp['track_number'] = track['track_number']
        temp['preview_url'] = track['preview_url']
        try:
            temp['popularity'] = track['popularity']
        except:
            temp['popularity'] = None
        try:
            temp['album_id'] = track['album_id']
        except:
            temp['album_id'] = None
        #album_id = models.CharField(max_length=200)
        DtracksCol.insert_one(temp)
    ts.close()
    send(i, 'music_track')
send('done', 'music_track')
"""

tracksCol = db.tracks
DtracksCol = db.music_tracks
for i in range(0, 109):
    ts = tracksCol.find(no_cursor_timeout = True).skip(i*1000).limit(1000)
    for track in ts:
        mr = None
        for ex in track['external_urls']:
            try:
                mr = ex['youtube_mr']
            except:
                pass
        DtracksCol.update_one({'id': track['id']}, {'$set': {'youtube_mr': mr}})
    ts.close()

"""
tracksCol = db.tracks
idx = 0
for track in tracksCol.find().skip(2*1000).limit(1000):
    print(track['external_urls'])
    idx += 1
    print(idx)
"""

"""
idx = 0
tracksCol = db.tracks
DtracksCol = db.music_tracks
ts = tracksCol.find(no_cursor_timeout = True)
for track in ts:
    if 'album_id' in DtracksCol.find_one({'id': track['id']}):
        continue
    #print(idx)
    #print(track)
    #print(track['album_id'])
    DtracksCol.update_many({'id': track['id']}, {'$set': {'album_id': track['album_id']}})
    idx+=1
ts.close()
"""

"""
trackCol = db.tracks_af_clustered
DtracksCol = db.music_tracks
for i in range(0, 109):
    dts = trackCol.find(no_cursor_timeout = True).skip(i*1000).limit(1000)
    idx = 0
    for track in dts:
        #if 'cluster' in DtracksCol.find_one({'id': track['id']}):
        #    continue
        try:
            DtracksCol.update_many({'id': track['id']}, {'$set': {'cluster': track['cluster']}})
        except Exception as e:
            print(idx)
            print(track['id'])
            print(e)
        idx+= idx
    dts.close()
    if i%10 == 0:
        send(i, 'tracks_af_clustered')
send('done', 'tracks_af_clustered')
"""

"""
tracksCol = db.ntracks
DtracksCol = db.music_tracks
for i in range(0, 405):
    ts = tracksCol.find(no_cursor_timeout = True).skip(i*1000).limit(1000)
    for track in ts:
        mr = None
        for ex in track['external_urls']:
            try:
                mr = ex['youtube_mr']
            except:
                pass
        DtracksCol.update_many({'id': track['id']}, {'$set': {'youtube_mr': mr}})
    ts.close()
    send(i, 'music_track')
send('done', 'music_track')
"""

"""
idx=0
albumsCol = db.albums
DalbumsCol = db.music_albums
als = albumsCol.find(no_cursor_timeout = True)
for album in als:
    if 'tracks' in DalbumsCol.find_one({'id': album['id']}):
        continue
    try:
        trs = []
        for tr in album['tracks']:
            trs.append({'id':tr})
        DalbumsCol.update_many({'id': album['id']}, {'$set': {'tracks': trs}})
    except Exception as e:
        print(idx)
        print(album['id'])
        print(e)
    idx+= idx
als.close()
"""

"""
acuser = db.accounts_user
users = acuser.find()
for user in users:
    acuser.update_many({'userid': user['userid']}, {'$set': {'pi_re_songs': []}})
"""


"""
DartistsCol = db.music_artists
DalbumsCol = db.music_albums
DtrackCol = db.music_tracks

for i in range(0, 24):
    ats = DartistsCol.find({'$nor' : [{'genres': {'$elemMatch' : { 'genre' : {'$regex' : '^korean', '$options':'i'} }}}, {'genres': {'$elemMatch' : { 'genre' : {'$regex' : '^k-pop', '$options':'i'} }}}]}, no_cursor_timeout = True).limit(10)
    li = []
    for a in ats:
        als = DalbumsCol.find({'artists':{'$elemMatch': {'id' : a['id']}}})
        for album in als:
            for track in album['tracks']:
                DtrackCol.delete_many({'id' : track['id']})
            DalbumsCol.delete_many({'id' : album['id']})
        DartistsCol.delete_many({'id' : a['id']})
    ats.close()
"""

"""
DafCol = db.tracks_af_clustered
DtrackCol = db.music_tracks

for i in range(0, 398):
    afs = DafCol.find().skip(i*1000).limit(1000)
    for a in afs:
        track = DtrackCol.find_one({'id':a['id']})
        if track == None:
            DafCol.delete_many({'id':a['id']})

"""

"""
DartistsCol = db.music_artists
DtrackCol = db.music_tracks
DalbumsCol = db.music_albums
DafCol = db.tracks_af_clustered

for i in range(0, 395):
    tracks = DtrackCol.find().skip(i*1000).limit(1000)
    for track in tracks:
        temp = []

        for artist in track['artists']:
            temp.append({'id': artist['id']})
        if DartistsCol.count_documents({'$or': temp}) == 0:
            DalbumsCol.delete_many({'id' : track['album_id']})
            DtrackCol.delete_many({'id' : track['id']})
            DafCol.delete_many({'id' : track['id']})
    tracks.close()
"""


"""
DartistsCol = db.music_artists
DtrackCol = db.music_tracks
DalbumsCol = db.music_albums
albumsCol = db.albums
artistsCol = db.artists

idx = 0
for i in range(0, 395):
    tracks = DtrackCol.find().skip(i*1000).limit(1000)
    for track in tracks:
        if DalbumsCol.count_documents({'id': track['album_id']}) == 0:
            album = albumsCol.find_one({'id': track['album_id']})
            if album is not None:
                temp = {}
                temp['id'] = album['id']
                temp['album_type'] = album['album_type']
                temp['name'] = album['name']
                temp['release_date'] = album['release_date']
                temp['release_date_precision'] = album['release_date_precision']
                temp['total_tracks'] = album['total_tracks']
                temp['images'] = album['images']
                ate = []
                for ar in album['artists']:
                    te = {}
                    te['id'] = ar['id']
                    te['name'] = ar['name']
                    ate.append(te)
                temp['artists'] = ate
                trs = []
                for tr in album['tracks']:
                    trs.append({'id':tr})
                DalbumsCol.insert_one(temp)
        for artist in track['artists']:
            if DartistsCol.count_documents({'id': artist['id']}) == 0:
                artist = artistsCol.find_one({'id': artist['id']})
                if artist is not None:
                    temp = {}
                    temp['id'] = artist['id']
                    temp['followers'] = artist['followers']['total']
                    temp['name'] = artist['name']
                    temp['popularity'] = artist['popularity']
                    li = []
                    for gen in artist['genres']:
                        te={}
                        te['genre'] = gen
                        li.append(te)
                    temp['genres'] = li
                    temp['images'] = artist['images']
                    DartistsCol.insert_one(temp)
    idx+=1
    if idx%10 == 0:
        send(i, idx)
send('done', 'done')    

"""

"""
userdb = db.accounts_user
DtrackCol = db.music_tracks

users = userdb.find()

for user in users:
    sang_songs = []
    for songs in user['sang_songs']:
        if DtrackCol.count_documents({'id': songs['songid']}) >= 1:
            sang_songs.append(songs)
    userdb.update_one({'userid': user['userid']}, {'$set': {'sang_songs': sang_songs}})

    re_songs = []
    for songs in user['re_songs']:
        if DtrackCol.count_documents({'id': songs['songid']}) >= 1:
            re_songs.append(songs)
    userdb.update_one({'userid': user['userid']}, {'$set': {'re_songs': re_songs}})

    pi_re_songs = []
    for songs in user['pi_re_songs']:
        if DtrackCol.count_documents({'id': songs['songid']}) >= 1:
            pi_re_songs.append(songs)
    userdb.update_one({'userid': user['userid']}, {'$set': {'pi_re_songs': pi_re_songs}})
"""


#같은노래 external_url 같은거면 하나는 지우기

#제목에 못들어가는거 있으면 잘라내기
#k = re.sub('\*|\\|:|\?|"|<|>|\|', '', k)


#컬렉션 확인하기
#print(db.collection_names())


#데이터 삭제하기
# result = posts.delete_one()      #조건과 일치하는 데이터중 하나만 삭제
# result = posts.delete_many()     #조건과 일치하는 데이터 모두 삭제
# result = posts.delete_many({})   #모두 삭제 (조건지정x)


#접속 해제
client.close()