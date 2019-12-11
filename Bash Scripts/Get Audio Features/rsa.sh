#!/bin/bash
#reads a txt file containing track ids for a single playlist  and returns a json file containing the audio features for the songs on that playlist
file_in='track_ids_97.txt'
file_out='playlist_97.json'
token='BQCEcta_M58GXINHTKvYeHqMXBDf-1MprB-8utHwUjEqhyF4z_1dcsH4744ye2G9N3fovAiEZV783dSkgR_PlwhYaHL-wcfS156uUg7bLJ-bw74W65SJwtfgVsPpgu3BkB0FxbMNnwK0rzIljk0wUo9HHV61OOg'
tracks=''

while read line; do
    tracks+=$line
    tracks+="%2C"
done < $file_in

tracks=${tracks%???}

curl -X "GET" "https://api.spotify.com/v1/audio-features?ids=${tracks}"\
 -H "Accept: application/json" -H "Content-Type: application/json"\
  -H "Authorization: Bearer ${token}" >> $file_out

echo $tracks
