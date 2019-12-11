#!/bin/bash
# Reads a list of albums and downloads json tracks info for each album to a file
albums='albums.txt'
count=1
while read al; do
    file_in=$al
    file_out="alb_tracks_${count}.json"
    token='BQCa3HEoIUYVbM4I0wFhJ50wj8mU3akh07VFpN4zv5NtDW-miYORdRXT-PC-GEv4xfDEnOV4qKBVZf91hpbZQsFVDyrFRINGSGRh-vbh4r3eUCF21_panWRVY34tZDmvfAjyJlnXCh0LRr6geM_N7ukVTPYyZwc'
    curl -X "GET" "https://api.spotify.com/v1/albums/${al}/tracks?limit=50"\
     -H "Accept: application/json" -H "Content-Type: application/json"\
     -H "Authorization: Bearer ${token}" >> $file_out


    echo $count
    echo $file_in
    echo $file_out
    count=$((count+1))
done < $albums
