# -*- encoding: utf-8 -*-
from selenium import webdriver
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from pymongo import MongoClient
import sys
from bson.objectid import ObjectId
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


client = MongoClient('mongodb://localhost:27017')
db = client.spotify

BASE_URL = "https://www.youtube.com/results?search_query="
BASE_URL_TJ = "https://www.youtube.com/channel/UCzv4mCu3YS_9WjAWSt9Xg9Q/search?query="
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

tracksCol = db.tracks


def crwal_youtube(NUM, driver, driver2):
    ts = tracksCol.find(no_cursor_timeout = True).skip(NUM*1000).limit(1000)
    print(NUM)
    idx = 0
    for track in ts:
        try:
            query = ""
            if track['artists'][0]['name'] is not None:
                query += track['artists'][0]['name'] + " "
            if track['name'] is not None:
                query += track['name']
            
            driver.get(BASE_URL + query)
            driver.implicitly_wait(5)
            bs = BeautifulSoup(driver.page_source, 'html.parser')
            ytd = bs.find('a',{"class":"yt-simple-endpoint style-scope ytd-video-renderer"})

            driver2.get(BASE_URL_TJ + query)
            driver2.implicitly_wait(5)
            tjbs = BeautifulSoup(driver2.page_source, 'html.parser')
            ytdtj = tjbs.find('a',{"class":"yt-simple-endpoint style-scope ytd-video-renderer"})
            li = []
            if isinstance(track['external_urls'], list):
                li.append({"spotify" :track['external_urls'][0]['spotify']})
            else:
                li.append({"spotify" :track['external_urls']['spotify']})
            if ytd is not None:
                li.append({"youtube" : ytd["href"]})
            if ytdtj is not None:
                li.append({"youtube_mr" : ytdtj["href"]})
            tracksCol.update_one({"_id": track["_id"]}, {"$set" : {"external_urls" : li}})
        except Exception as e :
            print(idx)
            print(track['_id'])
            print(e)
            #send(e, NUM)
        idx += 1
    #send(NUM, "data done")
    ts.close()
#220 260    230
#260 300    271
#300 340    311
#340 383    351

for i in range(0, 109):
    driver = webdriver.Chrome('/Users/KHR/Downloads/chromedriver', options=options)
    driver2 = webdriver.Chrome('/Users/KHR/Downloads/chromedriver', options=options)
    crwal_youtube(i, driver, driver2)
    driver.quit()
    driver2.quit()

"""
driver = webdriver.Chrome('/Users/KHR/Downloads/chromedriver', options=options)

tracksCol = db.tracks

NUM = 26


ts = tracksCol.find(no_cursor_timeout = True).skip(NUM*1000).limit(1000)
print(NUM)
idx = 0

for track in ts:
    try:
        query = ""
        if track['artists'][0]['name'] is not None:
            query += track['artists'][0]['name'] + " "
        if track['name'] is not None:
            query += track['name']
        if isinstance(track['external_urls'], list):
            continue
        driver.get(BASE_URL + query)
        driver.implicitly_wait(5)
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        ytd = bs.find('a',{"class":"yt-simple-endpoint style-scope ytd-video-renderer"})
        if ytd is not None:
            tracksCol.update_one({"_id": track["_id"]}, {"$set" : {"external_urls" : [{"spotify" :track['external_urls']['spotify']},{"youtube" : ytd["href"]}]}})
        else:
            tracksCol.update_one({"_id": track["_id"]}, {"$set" : {"external_urls" : [{"spotify" :track['external_urls']['spotify']}]}})
    except Exception as e :
        print(idx)
        print(track['_id'])
        print(e)
    idx += 1

"""
"""
for track in tracksCol.find({'artists' : {'$elemMatch' : {'name' : '개미'}}}):
    print(track)
"""

client.close()