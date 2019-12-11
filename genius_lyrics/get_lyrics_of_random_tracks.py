#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:43:00 2019

@author: weiruchen
"""

import json
import sys, requests
from bs4 import BeautifulSoup
import pandas as pd
import random

import time

#from constants import (
    #TOKEN
#)


client_id = ""
client_secret = ""
access_token = ""



defaults = {
    'request': {
        'token': access_token,
        'base_url': 'https://api.genius.com'
    },
    'message': {
        'search_fail': 'The lyrics for this song were not found!',
        'wrong_input': 'Wrong number of arguments.\n' \
                       'Use two parameters to perform a custom search ' \
                       'or none to get the song currently playing on Spotify.'
    }
}
    
"""
def get_current_song_info():
    # kudos to jooon at stackoverflow http://stackoverflow.com/a/33923095
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object('org.mpris.MediaPlayer2.spotify',
                                         '/org/mpris/MediaPlayer2')
    spotify_properties = dbus.Interface(spotify_bus,
                                        'org.freedesktop.DBus.Properties')
    metadata = spotify_properties.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    return {'artist': metadata['xesam:artist'][0], 'title': metadata['xesam:title']}
"""

def request_song_info(song_title, artist_name):
    base_url = defaults['request']['base_url']
    headers = {'Authorization': 'Bearer ' + defaults['request']['token']}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)

    return response

def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics

def main():
    #create pandas dataframe with title, artist, lyrics
    titles = []
    artists = []
    lyrics = []
    for item in random_artist_tracks:
        current_song_info = item
        curr_lyrics = get_lyrics(current_song_info)
        if curr_lyrics is not None:
            titles.append(current_song_info.get('title'))
            artists.append(current_song_info.get('artist'))
            lyrics.append(curr_lyrics) 
    df = pd.DataFrame({'Title': titles, 'Artist': artists, 'Lyrics': lyrics})
    #df.to_csv('random_tracks_with_lyrics.csv', index=False)
    df.to_csv('random_tracks_with_lyrics_larger.csv', index=False)
    


def write_lyrics_to_file (lyrics, song, artist):
    f = open('lyric-view.txt', 'w')
    f.write('{} by {}'.format(song, artist))
    f.write(lyrics)
    f.close()




# resample from random data

n = 300
with open('random_playlists.json') as json_file:
    data = json.load(json_file)
    random_data = random.sample(data, n)
    
playlists_artist_tracks = []
for playlist in random_data:
    artist_names = list(playlist.get("artist_name").values())
    track_names = list(playlist.get("track_name").values())
    artist_tracks = list(zip(artist_names, track_names))
    playlists_artist_tracks += list(artist_tracks)
    
random_artist_tracks = []

for pair in playlists_artist_tracks:
    random_artist_tracks.append({'title':pair[1],'artist':pair[0]})


"""
with open('candidates_with_tags.json') as json_file:
    data = json.load(json_file)


random_songs = list(data.keys())
random_artist_tracks = []

for song_info in random_songs:
    artist, track_name = song_info.split("*,*")
    random_artist_tracks.append({'title':track_name,'artist':artist})
"""

#print(random_artist_tracks[0])


def get_lyrics(current_song_info):
    # Get info about song currently playing on Spotify
    #current_song_info = {'title': "Look What You Made Me do", 'artist':"Taylor Swift"}
    #current_song_info = {'title': "Fake Love", 'artist':"BTS"}
    song_title = current_song_info['title']
    artist_name = current_song_info['artist']

    print('{} by {}'.format(song_title, artist_name))

    # Search for matches in request response
    response = request_song_info(song_title, artist_name)
    json = response.json()
    remote_song_info = None

    for hit in json['response']['hits']:
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break

    # Extract lyrics from URL if song was found
    if remote_song_info:
        song_url = remote_song_info['result']['url']
        lyrics = scrap_song_url(song_url)

        write_lyrics_to_file(lyrics, song_title, artist_name)

        #print(lyrics)
        return lyrics
    else:
        print(defaults['message']['search_fail'])
        return None
        
        
        



#if __name__ == '__main__':
    #main()
    
    
titles = []
artists = []
lyrics = []
for item in random_artist_tracks:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 




#random_artist_tracks.index({'title': "If I ever feel better", 'artist': 'Phoenix'})




"""
#0-2000


for item in random_artist_tracks[0:2000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 


"""


"""

for item in random_artist_tracks[2000:4000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 


"""

"""


#0-2000
for item in random_artist_tracks[4000:6000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""


"""
#0-2000
for item in random_artist_tracks[6000:8000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""

"""

#0-2000
for item in random_artist_tracks[8000:10000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""

"""
#0-2000
for item in random_artist_tracks[10000:12000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""

"""

#0-2000
for item in random_artist_tracks[12000:14000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""

"""
#0-2000
for item in random_artist_tracks[14000:16000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""

"""
#0-2000
for item in random_artist_tracks[16000:18000]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""


"""
#0-2000
for item in random_artist_tracks[18000:]:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 

"""




df = pd.DataFrame({'Title': titles, 'Artist': artists, 'Lyrics': lyrics})
#df.to_csv('random_tracks_with_lyrics.csv', index=False)
df.to_csv('random_tracks_with_lyrics.csv', index=False)


