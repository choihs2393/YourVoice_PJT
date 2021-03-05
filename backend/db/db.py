from pymongo import MongoClient
import tekore as tk
import time
import requests
import json



def open_json(name):
    with open('./%s.json'%name,'r', -1, "utf-8") as f:
        dt=json.load(f)
    return dt
client = MongoClient('mongodb://localhost:27017')
db = client.spotify


datas = open_json('tracks_af_clustered')
af = db.tracks_af_clustered
for data in datas['data']:
    af.insert_one(data)

datas = open_json('music_tracks')
af = db.music_tracks
for data in datas['data']:
    af.insert_one(data)

datas = open_json('music_albums')
af = db.music_albums
for data in datas['data']:
    af.insert_one(data)

datas = open_json('music_artists')
af = db.music_artists
for data in datas['data']:
    af.insert_one(data)