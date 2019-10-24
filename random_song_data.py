#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 01:58:11 2019

@author: weiruchen
"""

import pandas as pd
import numpy as np
import json

playlists = []
random_indices = np.random.choice([i for i in range(1000)], size = 10)

# load data into pandas dataframe
for idx in random_indices:
    songs_df = pd.read_csv("songs/songs{}.csv".format(idx))

    # get playlists into dictionaries and store in a list

    id_nums = set(songs_df['pid'].tolist())
    songs_df = songs_df.groupby("pid")

    for id in id_nums:
        playlist = songs_df.get_group(id)
        playlists.append(playlist.to_dict())

# store the list of dictionaries into json file
with open('random_playlists', 'w') as fout:
    json.dump(playlists, fout)
