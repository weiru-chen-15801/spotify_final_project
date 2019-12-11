#!/bin/bash
#reads a list of lists of track ids and downloads json files with audio features for each track list
playlists='nr_ids.txt'
count=1
while read pl; do
    file_in=$pl
    file_out="album_nr_${count}.json"
    token='BQDfWm733wJ2XcwjEAmADSL2KKvRf-2GgbZcsC0uqx6y-2uQ9d8JoQGtXgr7Ai0gLxPOumYP5Tcvw6DTC8BBT3g7LcRTPofrKfWOgm-rb_pXHWrL3HSshJXv1coSi4dH4gNDHfJ8-LS2IfkMqA8sWj5SjxUh_Oc'
    tracks=''

    while read line; do
        tracks+=$line
        tracks+="%2C"
    done < $file_in

    tracks=${tracks%???}

    curl -X "GET" "https://api.spotify.com/v1/audio-features?ids=${tracks}"\
    -H "Accept: application/json" -H "Content-Type: application/json"\
    -H "Authorization: Bearer ${token}" >> $file_out

    echo $count
    echo $file_in
    echo $file_out
    count=$((count+1))
done < $playlists
