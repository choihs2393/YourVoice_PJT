from pymongo import MongoClient
import tekore as tk
import time
import requests
import json

def send(text):
    requests.post('https://meeting.ssafy.com/hooks/xjyuws5ywtratrtu8e8qx57k7c', 
        data=json.dumps({"attachments": [{
            "color": "#FF8000",
            "text": str(text),
            "author_name": "data",
            "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
            "title": "data done",
        }]}),
        headers={'Content-Type': 'application/json'}
    )

def open_json(name):
    with open('./%s.json'%name,'r', -1, "utf-8") as f:
        dt=json.load(f)
    return dt

def save_json(name,dt):
    with open('./%s.json'%name,'w', -1, "utf-8") as f:
        json.dump(dt,f)


client = MongoClient('mongodb://localhost:27017')
db = client.spotify
#conf = ("a09fdcc51588442c985dbbe26c5b1989", "595137403fb84f3ea6d4f400229abc63", "https://localhost:8000/callback")
#token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
#spotify = tk.Spotify(token)


"""
print(ts[0])
t = Db.find(no_cursor_timeout = True)
print(t[t.count()-1])
"""


tracksCol = db.music_tracks
ts = tracksCol.find({},{'_id': False})
li = []
for t in ts:
    li.append(t)

save_json("data/music_tracks", {'data': li})


"""
datas = open_json('data/clustered_audio_feature')
af = db.tracks_af_clustered
for data in datas:
    af.insert_one(data)

"""
"""
for NUM in range(0, 109):
    tracksCol = db.tracks
    Db = db.tracks_af
    ts = tracksCol.find(no_cursor_timeout = True).skip(NUM*1000).limit(1000)
    for track in ts:
        temp = {}
        if Db.count_documents({'id' : track['id']}) == 0:
            try:
                te = spotify.track_audio_features(track['id'])
                temp['id'] = te.id
                temp['instrumentalness'] = te.instrumentalness
                temp['key'] = te.key
                temp['liveness'] = te.liveness
                temp['loudness'] = te.loudness
                temp['mode'] = te.mode
                temp['speechiness'] = te.speechiness
                temp['tempo'] = te.tempo
                temp['time_signature'] = te.time_signature
                temp['valence'] = te.valence
                temp['energy'] = te.energy
                temp['danceability'] = te.danceability
                temp['acousticness'] = te.acousticness
                Db.insert_one(temp)
            except Exception as e:
                print(track['id'])
                print(e)
            time.sleep(0.1)
    ts.close()
"""
"""
for NUM in range(0, 109):
    tracksCol = db.tracks
    ts = tracksCol.find(no_cursor_timeout = True).skip(NUM*1000).limit(1000)
    Db = db.tracks
    for track in ts:
        try:
            te = spotify.track(track['id'])
            Db.update_many({'id': track['id']}, {'$set': {'popularity': te.popularity}})
            time.sleep(0.1)
        except Exception as e:
            print(track['id'])
            print(e)
"""

"""
albumCol = db.albums
als = albumCol.find(no_cursor_timeout = True)
Db = db.albums

for album in als:
    try:
        print(album['tracks'])
        if 'tracks' in album:
            continue 
        te = spotify.album(album['id'])
        li=[]
        for tr in te.tracks.items:
            li.append(tr.id)
        Db.update_many({'id': album['id']}, {'$set': {'tracks': li}})
        time.sleep(0.1)
    except Exception as e:
        print(album['id'])
        print(e)
als.close()
"""


client.close()