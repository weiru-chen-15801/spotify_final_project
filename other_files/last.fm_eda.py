#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:19:23 2019

@author: weiruchen
"""
import pandas as pd

df = pd.read_csv('last.fm/lastfm_unique_tags.txt', sep="\t", names=["tag","freq"])


useful_freq = df[df['freq'] > 3000]
print(useful_freq)


import numpy as np
import matplotlib.pyplot as plt
 


fig, ax = plt.subplots()

# Example data
tags = list(useful_freq['tag'])[0:10]
y_pos = np.arange(len(tags))
freqs = list(useful_freq['freq'])[0:10]

ax.barh(y_pos, freqs)
ax.set_yticks(y_pos)
ax.set_yticklabels(tags)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of Occurrences')
ax.set_ylabel("Top Tags")
ax.set_title('Top 10 Tags Appearing Among All Songs')

plt.show()


