#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
pip install spotipy
pip install tables
pip install pandas
"""
import os
import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import re
from pymongo import MongoClient
from bson.objectid import ObjectId

class MySpotify(object):
    """This class was to download data from Spotify API.
    The download process should be: 
        artist=artist_genre -> album=album_artists(artist) -> songs=songs_albums(album)
    
    """
    def __init__(self, genre='k-pop'):
        self.authenticate()
        self.genre=genre
        
        
    def authenticate(self):
        auth=open_json('auth')
        my_id = auth['my_id']
        secret_key = auth['secret_key']
        client_credentials_manager = SpotifyClientCredentials(client_id = my_id, client_secret = secret_key)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=5000)
                
        
    def artist_genre(self):
        """Download all artists info from a genre """
        
        artist=[]
        at=self.sp.search(q='genre:'+self.genre,limit=50,type='artist')['artists']
        total = at['total']
        if(total >= 2000):
            total = 1950
        if total>50:
            for i in range(0, total,50):
                artist+=self.sp.search(q='genre:'+self.genre,limit=50,type='artist',offset=i)['artists']['items']
        save_json("data/artists/{}_artists_info".format(self.genre), artist)
        
        """
        print("Download {}'s artists info".format(self.genre))
        """
        print()
                
        return artist
    
    
    def album_artists(self, artist):
        """Download all albums info from artists """
        """artist=open_json("data/artists/{}_artists_info".format(self.genre))"""
        album={}
        
        for i in artist:
            name=i['name']
            check = False
            for t in i['genres']:
                if "k-pop" in t or "korean" in t:
                    check = True
                    print(t)
                    break
            if not check:
                continue
            album[name]=[]
            ab=self.sp.artist_albums(i['id'], limit=50)
            total = ab['total']
            if(total >= 2000):
                total = 1950
            if total > 50:
                for j in range(0,total,50):
                    album[name]+=self.sp.artist_albums(i['id'], limit=50,offset=j)['items']
            else:
                album[name]+=self.sp.artist_albums(i['id'], limit=50)['items']
            """
            print("Download {}'s albums info".format(name))
            """
        save_json("data/albums/{}_albums".format(self.genre),album)
        
        return album


    def songs_albums(self, album):  
        """Download all songs info from albums """
        """
        album=open_json("data/albums/{}_albums_info".format(self.genre))
        """
        songs={}
        
        for k,v in album.items():
            list_dir=os.listdir('./data/tracks/')
            k = k.replace('/','_')
            k = re.sub('\*|\\|:|\?|"|<|>|\|', ' ', k)

            if "{}_tracks_info.json".format(k) not in list_dir:
                songs['artist']=k
                songs['albums']={}
                
                for i in v:        
                    songs['albums'][i['id']]=self.sp.album_tracks(i['id'])['items']
                save_json("data/tracks/{}_tracks_info".format(k), songs)
                """
                print("Download {}'s tracks info".format(k))
                """
                
        return songs
    
    
    def songs_albums_add_popularity(self):
        list_dir=os.listdir('./data/tracks/')
        
        for fl in list_dir:
            try:
                album=open_json("data/tracks/{}".format(fl[:-5]))
            except:
                pass
            for ak,av in album['albums'].items():
                for tr in av:
                    try:
                        tr['popularity']=self.sp.track(tr['id'])['popularity']
                    except Exception as e:
                        print("songs_albums_add_popularity")
                        """
                        print(e,album['artist'])
                        """
            """
            print("Add track popularity to {}'s songs".format(album['artist']))
            """
            save_json("data/tracks/{}".format(fl[:-5]),album)
    
    
    def audio_feature(self, artist):
        """Download audio features of all tracks of one artist
        
        :artist(string)
        
        """
                
        albums=open_json('data/tracks/{}_tracks_info'.format(artist))['albums']
        Analysis=pd.DataFrame()
        for k,v in albums.items():
            audios=[]
            track_name=[]
            for i in v:
                audios.append(i['id'])
                track_name.append(i['name'])
            analysis=pd.DataFrame(self.sp.audio_features(audios))
            analysis['track_name']=track_name
            analysis['album']=self.sp.album(k)['name']
            analysis['release_date']=self.sp.album(k)['release_date']
            analysis['album_id']=k
            analysis['artist']=artist
            Analysis=Analysis.append(analysis)
            
        Analysis=Analysis.drop_duplicates('id')
        Analysis=Analysis[~Analysis.analysis_url.isnull()]
        
        if 0 in Analysis.columns:
            del Analysis[0]
        
        # drop similar songs, highly possible the same songs
        Analysis=Analysis.drop_duplicates(['acousticness','liveness',          
                  'instrumentalness','speechiness', 
                   'danceability','energy','valence', 'key'])
        """
        print("Extract tracks analysis of artist {}".format(artist))
        """
        Analysis.to_json("./data/analysis/{}_tracks_analysis.json".format(artist), orient='table')
        
    def audio_feature_all(self):
        """Download audio features of all tracks of all artists of one genre
        
        """
        dir_l=os.listdir(u'./data/tracks/')
        for artist in dir_l:
            if artist[:-17]+'_tracks_analysis.json' not in os.listdir('./data/analysis/'):
                try:
                    self.audio_feature(artist[:-17])
                except Exception as e:
                    print("errer in audio feature")
                    """
                    print("Artist {} has something wrong:{}".format(artist,e))
                    """

    def audio_analysis(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.spotify
        tracksCol = db.tracks
        #여기 수정해가면서 돌리면 됩니다.
        t = tracksCol.find(no_cursor_timeout = True).skip(0*1000).limit(1000)
        client.close()
        for track in t:
            if track['id'] + '_detail_analysis.json' not in os.listdir('./data/detail_analysis/'):
                try:
                    save_json("data/detail_analysis/{}_detail_analysis.json".format(track['id']), self.sp.audio_analysis(track['id']))
                except Exception as e:
                    print("errer in audio_analysis")
        
        
        

def update_data(genre='k-pop'):
    spf=MySpotify(genre)  
    #upate artists info 
    #artist=spf.artist_genre()
    #update albums info of artists
    artist=open_json('data/artists/k-pop_artists_info')
    album=spf.album_artists(artist)
    #update songs info of albums
    spf.songs_albums(album)


def save_json(name,dt):
    with open('./%s.json'%name,'w', -1, "utf-8") as f:
        json.dump(dt,f)


def open_json(name):
    with open('./%s.json'%name,'r', -1, "utf-8") as f:
        dt=json.load(f)
    return dt


if __name__=="__main__":
    update_data()
    #spotf=MySpotify()
    #spotf.audio_feature_all()
    #spotf.audio_analysis()
    
    pass