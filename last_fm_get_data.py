#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:13:33 2019

@author: weiruchen
"""

import pylast

username = ""
password_hash = pylast.md5("")

API_KEY = ""
API_SECRET = ""


network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

"""
artist = network.get_artist("System of a Down")
print(artist.get_name())


track = network.get_track("Iron Maiden", "The Nomad")
track.love()
track.add_tags(("awesome", "favorite"))

print(track.get_duration())
print(track.get_similar())
print(track.get_title())
print(track.get_top_tags())
"""

#import songs result data

songs_df = pd.read_csv("result.csv")
tracks = list(songs_df['track_name'])
artists = list(songs_df['artist_name'])
artist_tracks = list(zip(artists, tracks))

#unique tags threshold
threshold = 1000
unique_tags = []
with open("last.fm/lastfm_unique_tags.txt", 'r') as f:
    for line in f:
        tag_freq = line.split('\t')
        if int(tag_freq[1]) > threshold:
            unique_tags.append(tag_freq[0])
        else:
            break
  
print(unique_tags)


#get tags with weights (high frequency ones) from unique track
def get_tags_from_track(artist_name, track_name):
    try:
        track = network.get_track(artist_name, track_name)
        tags = track.get_top_tags()
        tags_with_weights = []
        for tag_item in tags:
            if str(tag_item.item) in unique_tags:
                tags_with_weights.append((str(tag_item.item), int(tag_item.weight)))
        return tags_with_weights
    except:
        return None
 

tracks_with_tags = []

for artist_track in artist_tracks:
    #turn tuple of artist_track into 'artist_name*,*track_name'
    tracks_with_tags.append({str(artist_track[0])+'*,*'+str(artist_track[1]): get_tags_from_track(artist_track[0],artist_track[1])})

with open('tracks_with_tags_from_sample_of_songs', 'w') as fout:
    json.dump(tracks_with_tags, fout)

    
