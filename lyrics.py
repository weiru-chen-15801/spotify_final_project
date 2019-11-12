# get lyrics from LyricsGenius APi

import lyricsgenius
genius = lyricsgenius.Genius("6i0gsOv7-g4U_0xYXez_MqIi0flfxRkbHUcHPZHnEM4M4dGIwuFS38z5Rw_AEwk7")
artist = genius.search_artist("Taylor Swift", max_songs=3, sort="title")
print("start here")
print(artist.songs)
print("end here")