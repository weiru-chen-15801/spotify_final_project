#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:17:06 2019

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


client_id = "amQOthO0c2NQYlsZmzS1BxLC78uFeq8v_aGeHqau5o2vQkHhvEQfQCw1V3zMnO7w"
client_secret = "UkLMfeQp6h1wrUXOuGYm2nnrLTYKiOQsDHBIiUZOBcYln9_6CcHeDBdhghLnVvXFiEFWqh1qDGdRGRBdscBsgg"
access_token = "Zg7xufM0f5VciOJ8fWqLjRONkj9ZwKbmfMwrStdbDL2ubfIWBv3PThjqP5Ad0EAc"



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
    data = {'q': str(song_title) + ' ' + str(artist_name)}
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






newly_released_artist_tracks = []
newly_released_df = pd.read_csv("raw_new_released_features.csv")
artists = list(newly_released_df['Artist'])
tracks = list(newly_released_df['track_name'])
for i in range(len(artists)):
    newly_released_artist_tracks.append({'title':tracks[i],'artist':artists[i]})


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
for item in newly_released_artist_tracks:
    current_song_info = item
    curr_lyrics = get_lyrics(current_song_info)
    time.sleep(1)
    
    if curr_lyrics is not None:
        titles.append(current_song_info.get('title'))
        artists.append(current_song_info.get('artist'))
        lyrics.append(curr_lyrics) 




#random_artist_tracks.index({'title': "If I ever feel better", 'artist': 'Phoenix'})









df = pd.DataFrame({'Title': titles, 'Artist': artists, 'Lyrics': lyrics})
#df.to_csv('random_tracks_with_lyrics.csv', index=False)
df.to_csv('new_released_with_lyrics.csv', index=False)


