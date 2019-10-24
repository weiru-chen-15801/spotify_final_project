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

artist = network.get_artist("System of a Down")
print(artist.get_name())


track = network.get_track("Iron Maiden", "The Nomad")
track.love()
track.add_tags(("awesome", "favorite"))

print(track.get_duration())
print(track.get_similar())
print(track.get_title())
print(track.get_top_tags())
