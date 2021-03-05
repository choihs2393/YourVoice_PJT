from pymongo import MongoClient
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
import gc

#Artists = db.music_artists
#Albums = db.music_albums


def get_data_track(query, start, end):
    client = MongoClient('mongodb://localhost:27017')
    db = client.spotify
    
    Tracks = db.music_tracks
    Albums = db.music_albums

    cursor = Tracks.find(query, {'_id': False}).skip(start).limit(end)
    list_cur = list(cursor)
    for track in list_cur:
        try:
            track['album'] = Albums.find_one({'id': track['album_id']}, {'_id': False})
        except:
            track['album'] = None
    client.close()
    return list_cur

def get_data_album(query, start, end):
    client = MongoClient('mongodb://localhost:27017')
    db = client.spotify

    Albums = db.music_albums

    cursor = Albums.find(query, {'_id': False}).skip(start).limit(end)
    list_cur = list(cursor)
    client.close()
    return list_cur

def make_audio_feature(data):
    client = MongoClient('mongodb://localhost:27017')
    db = client.spotify

    Tracks = db.music_tracks
    AF = db.tracks_af_clustered
    cluster_features = [
        'acousticness',
        'danceability',
        'energy',
        'valence'
    ]

    ctemp = [{"valence": 0,"energy": 0,"danceability": 0,"acousticness": 0,}, 
            {"valence": 0,"energy": 0,"danceability": 0,"acousticness": 0,}, 
            {"valence": 0,"energy": 0,"danceability": 0,"acousticness": 0,}, 
            {"valence": 0,"energy": 0,"danceability": 0,"acousticness": 0,}, 
            {"valence": 0,"energy": 0,"danceability": 0,"acousticness": 0,}]
    clen = [0, 0, 0, 0, 0]
    for track in data:
        af = AF.find_one({'id': track['songid']}, {'_id': False})
        
        ctemp[af['cluster']]['valence'] += af['valence']
        ctemp[af['cluster']]['energy'] += af['energy']
        ctemp[af['cluster']]['danceability'] += af['danceability']
        ctemp[af['cluster']]['acousticness'] += af['acousticness']
        clen[af['cluster']]+=1

    result = []

    for i in range(0, 5):
        if clen[i] == 0:
            continue
        ctemp[i]['valence'] = ctemp[i]['valence']/clen[i]
        ctemp[i]['energy'] = ctemp[i]['energy']/clen[i]
        ctemp[i]['danceability'] = ctemp[i]['danceability']/clen[i]
        ctemp[i]['acousticness'] = ctemp[i]['acousticness']/clen[i]
    
        audio_feature_df = pd.DataFrame(columns=[
            "valence",
            "energy",
            "danceability",
            "acousticness"
        ])
        

        audio_feature = AF.find({'cluster': i}, {'_id': False})
        
        #idx = 1
        #for af in audio_feature:
        #    data_info = pd.DataFrame({
        #        "valence": af['valence'],
        #        "energy": af['energy'],
        #        "danceability": af['danceability'],
        #        "acousticness": af['acousticness'],
        #    }, index=[idx])
        #    idx+=1
        #    audio_feature_df = audio_feature_df.append(data_info, sort=True)
        #audio_feature_df = audio_feature_df.append(pd.DataFrame(ctemp[i], index=[0]), sort=True)

        afList = list(audio_feature)
        #afList.insert(0, ctemp[i])
        audio_feature_df = pd.DataFrame(afList)
        audio_feature_df = audio_feature_df[cluster_features]
        audio_feature_df.loc[:,['valence']] = audio_feature_df.loc[:,['valence']].astype('float32')
        audio_feature_df.loc[:,['energy']] = audio_feature_df.loc[:,['energy']].astype('float32')
        audio_feature_df.loc[:,['danceability']] = audio_feature_df.loc[:,['danceability']].astype('float32')
        audio_feature_df.loc[:,['acousticness']] = audio_feature_df.loc[:,['acousticness']].astype('float32')
        
        te = [ctemp[i]['acousticness'],ctemp[i]['danceability'],ctemp[i]['energy'],ctemp[i]['valence']]
        dists = euclidean_distances(audio_feature_df, pd.DataFrame(ctemp[i], index=[0]))
        
        six = [1, 1, 1, 1, 1, 1]
        li = []
        for dis in dists:
            for j in range(0, 6):
                if six[j] > dis[0]:
                    six[j] = dis[0]
                    break
            li.append(dis[0])
        
        re = []
        for val in six:
            re.append(afList[li.index(val)]['id'])

        result.append({'cluster' : i, 'data' : re})
        del audio_feature_df
        del dists
        gc.collect()
    
    client.close()
    return result
